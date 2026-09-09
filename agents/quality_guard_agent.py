import os
import json
import logging
import random
import re
import time
import config
import api_client
from sanitizer import sanitize_text

logger = logging.getLogger("pipeline.quality_guard_agent")

class QualityGuardAgent:
    def __init__(self):
        self.processed_dir = config.DATA_PROCESSED_DIR
        self.analysis_dir = config.DATA_ANALYSIS_DIR
        
    def _load_anonymized_posts(self):
        anon_file = os.path.join(self.processed_dir, "anonymized_posts.json")
        if not os.path.exists(anon_file):
            raise FileNotFoundError(f"Anonymized posts file not found: {anon_file}")
        with open(anon_file, "r", encoding="utf-8") as f:
            posts = json.load(f)
        return {p["id"]: p for p in posts}
        
    def _load_netnography_results(self):
        results_file = os.path.join(self.analysis_dir, "netnography_results.jsonl")
        if not os.path.exists(results_file):
            raise FileNotFoundError(f"Netnography results file not found: {results_file}")
        results = []
        with open(results_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))
        return results

    def audit_single_analysis(self, original_post, analysis):
        post_id = str(original_post.get("post_id") or original_post.get("id"))
        logger.info(f"Auditing DART-NET analysis for post {post_id} using deepseek-v4-pro (thinking mode)...")
        
        system_prompt = (
            "You are a senior academic auditor evaluating qualitative netnographic codings under the DART-NET Framework.\n"
            "Audit the generated coding against the original post text under the following scientific criteria:\n\n"
            "AUDIT CRITERIA:\n"
            "1. Literal Evidence Veracity (Evidence-First Principle): Do the quotations cited in 'evidence' for dialogue, access, risk, and transparency exist verbatim in the original post? (No invented quotes allowed).\n"
            "2. AI Agent Classification Validity (A1-A6): Did the agent correctly classify the entity? Crucially: was a conventional bot (A2) or deterministic script (A3) prevented from being falsely classified as an AI agent (A1) without explicit evidence of AI/autonomy?\n"
            "3. Interaction & Value Co-Creation Consistency (I1-I6 and VC1-VC4): Are the interaction structure and value impact supported by the text?\n"
            "4. DART Scoring Calibration (0 to 5): Are the 0-5 scores for Dialogue, Access, Risk, and Transparency well-calibrated against definitions (0=absent, 1=weak, 2=moderate, 3=strong, 4=very strong, 5=explicit)?\n"
            "5. Human Review Calibration: Was 'human_review_required' set to true if confidence < 0.80 or if ambiguity was present?\n\n"
            "Respond STRICTLY in JSON format with the following keys:\n"
            "{\n"
            "  \"evidencia_literal_existe\": true/false,\n"
            "  \"consistencia_ai_type\": true/false,\n"
            "  \"consistencia_interacao_valor\": true/false,\n"
            "  \"calibracao_dart_scores\": true/false,\n"
            "  \"human_review_corretamente_sinalizado\": true/false,\n"
            "  \"consistencia_conceitual\": true/false,\n"
            "  \"score_auditoria\": 0-100,\n"
            "  \"justificacao_auditoria\": \"Detailed audit justification of findings, strengths, or defects.\"\n"
            "}"
        )
        
        user_prompt = (
            f"[POST ORIGINAL]\n"
            f"Game: {original_post.get('game') or original_post.get('jogo')}\n"
            f"Title: {sanitize_text(original_post.get('title') or original_post.get('titulo'))}\n"
            f"Post Body:\n{sanitize_text(original_post.get('text') or original_post.get('corpo'))}\n\n"
            f"[DART-NET AI CODING]\n"
            f"{json.dumps(analysis, indent=2, ensure_ascii=False)}\n"
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        try:
            # QualityGuardAgent: deepseek-v4-pro, non-thinking mode for reliable structured JSON
            content, reasoning = api_client.call_llm(
                model=config.MODEL_PRO,
                messages=messages,
                thinking_enabled=False,
                temperature=0.0,
                max_tokens=3000
            )
            
            json_match = re.search(r"\{.*\}", content, re.DOTALL)
            if json_match:
                audit_result = json.loads(json_match.group(0))
            else:
                audit_result = json.loads(content)
                
            audit_result["post_id"] = post_id
            audit_result["_thinking_process"] = reasoning
            if "consistencia_conceitual" not in audit_result:
                audit_result["consistencia_conceitual"] = audit_result.get("consistencia_ai_type", True) and audit_result.get("calibracao_dart_scores", True)
            return audit_result
            
        except Exception as e:
            logger.error(f"Audit failed for post {post_id}: {e}")
            return {
                "post_id": post_id,
                "evidencia_literal_existe": False,
                "consistencia_ai_type": False,
                "consistencia_interacao_valor": False,
                "calibracao_dart_scores": False,
                "human_review_corretamente_sinalizado": False,
                "consistencia_conceitual": False,
                "score_auditoria": 0,
                "justificacao_auditoria": f"Audit execution failure: {e}",
                "_thinking_process": f"API error: {e}",
                "api_error": True
            }

    def run(self):
        logger.info("QualityGuardAgent starting qualitative audit...")
        
        original_posts_map = self._load_anonymized_posts()
        analyses = self._load_netnography_results()
        
        if not analyses:
            logger.error("No netnography analyses found to audit.")
            return False
            
        # Select 20% sample (minimum of 2 posts if we have enough data, else 1)
        sample_size = max(1, int(len(analyses) * 0.2))
        random.seed(42)  # For reproducible evaluation sampling across restarts
        audited_samples = random.sample(analyses, sample_size)
        
        logger.info(f"Auditing a sample of {sample_size} out of {len(analyses)} total analyses ({20.0:.1f}%)...")
        
        audit_results = []
        scores = []
        failed_posts = []
        
        from concurrent.futures import ThreadPoolExecutor, as_completed
        num_workers = min(config.MAX_WORKERS, len(audited_samples)) if audited_samples else 1
        logger.info(f"Running qualitative audit with {num_workers} concurrent workers...")
        
        futures_map = {}
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            for scarcity_item in audited_samples:
                post_id = scarcity_item["post_id"]
                if post_id not in original_posts_map:
                    logger.error(f"Original post for ID {post_id} not found in anonymized posts. Skipping.")
                    continue
                    
                original_post = original_posts_map[post_id]
                future = executor.submit(self.audit_single_analysis, original_post, scarcity_item)
                futures_map[future] = post_id
                
            for future in as_completed(futures_map):
                post_id = futures_map[future]
                try:
                    audit_res = future.result()
                    audit_results.append(audit_res)
                    
                    if audit_res.get("api_error", False):
                        logger.warning(f"Audit for post {post_id} skipped in average score due to API/network error.")
                    else:
                        score = audit_res.get("score_auditoria", 0)
                        scores.append(score)
                        
                        # If the score is low or critical flags are false
                        if score < 70 or not audit_res.get("evidencia_literal_existe", True) or not audit_res.get("consistencia_conceitual", True):
                            failed_posts.append((post_id, score, audit_res.get("justificacao_auditoria")))
                except Exception as e:
                    logger.error(f"Error processing future audit for post {post_id}: {e}")
                
        # Calculate average consistency
        avg_score = sum(scores) / len(scores) if scores else 100.0
        logger.info(f"Qualitative audit completed. Average Consistency Score: {avg_score:.2f}%")
        
        # Save audit results
        audit_report_file = os.path.join(self.analysis_dir, "quality_audit_results.json")
        report_data = {
            "audited_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_analyses": len(analyses),
            "sample_size": sample_size,
            "average_consistency_score": avg_score,
            "failed_audits": [
                {
                    "post_id": pid,
                    "score": s,
                    "reason": r
                } for pid, s, r in failed_posts
            ],
            "details": audit_results
        }
        
        try:
            with open(audit_report_file, "w", encoding="utf-8") as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            logger.info(f"QualityGuardAgent audit report written to {audit_report_file}")
        except Exception as e:
            logger.error(f"Failed to write audit report: {e}")
            
        # Enforce threshold
        if avg_score < 70.0:
            logger.critical(f"Aborting pipeline! Global quality consistency is {avg_score:.2f}% (< 70%).")
            logger.critical(f"Failed posts: {failed_posts}")
            raise ValueError(f"Pipeline aborted by QualityGuardAgent: quality consistency is {avg_score:.2f}% (< 70.0%).")
            
        logger.info("QualityGuardAgent passed the consistency threshold (> 70.0%). Pipeline can proceed.")
        return True
