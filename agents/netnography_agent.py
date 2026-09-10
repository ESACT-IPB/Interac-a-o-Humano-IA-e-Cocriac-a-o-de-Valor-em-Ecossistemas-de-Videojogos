import os
import json
import logging
import threading
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import config
import api_client
from sanitizer import sanitize_text

logger = logging.getLogger("pipeline.netnography_agent")

def extract_and_repair_json(text):
    """Extracts and repairs JSON output from LLM responses, handling code blocks, trailing commas, and formatting."""
    if not text:
        raise ValueError("Empty response from LLM")
    
    cleaned = text.strip()
    if "```" in cleaned:
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", cleaned, re.DOTALL)
        if match:
            cleaned = match.group(1).strip()
        else:
            cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
            cleaned = re.sub(r"```$", "", cleaned).strip()

    start_idx = cleaned.find("{")
    end_idx = cleaned.rfind("}")
    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        cleaned = cleaned[start_idx:end_idx + 1]

    # Attempt 1: Standard load
    try:
        return json.loads(cleaned)
    except Exception:
        pass

    # Attempt 2: Trailing commas removal
    try:
        repaired = re.sub(r",\s*([\]}])", r"\1", cleaned)
        return json.loads(repaired)
    except Exception:
        pass

    # Attempt 3: Line-by-line sanitize
    try:
        lines = [line.rstrip() for line in cleaned.splitlines()]
        repaired = "\n".join(lines)
        repaired = re.sub(r",\s*([\]}])", r"\1", repaired)
        return json.loads(repaired)
    except Exception as e:
        raise ValueError(f"Failed to parse JSON: {e} | Snippet: {cleaned[:120]}")

STATIC_DART_INSTRUCTIONS = """
You are an AI research agent responsible for screening, classifying and coding online community data for a scientific study investigating human–AI agent interactions and value co-creation in video game ecosystems (Framework: DART-NET).

Your task is to produce a TRACEABLE, AUDITABLE and REPRODUCIBLE research dataset.
You are not the final scientific decision-maker: your classifications are recommendations that must remain open to human validation.

1. CENTRAL ANALYTICAL UNIT:
The central analytical unit is the human–AI interaction, not simply the presence of the word "AI".

2. DEFINITION OF AI AGENT & AI TYPE TAXONOMY:
An AI agent is a computational system capable of performing tasks, making decisions or taking actions with some degree of autonomy on behalf of, or in interaction with, a human player.
Do NOT automatically classify every bot, script or automation tool as an AI agent. Distinguish carefully between:
- A1 — AI Agent: Evidence suggests the system uses AI and possesses some degree of autonomy.
- A2 — Conventional Bot: Automated software is present, but there is insufficient evidence that it is AI-based.
- A3 — Script / Automation: A deterministic script, macro or automation mechanism with no evidence of AI.
- A4 — AI-Assisted Human: AI assists a human player, but the human remains the primary decision-maker.
- A5 — Discussion About AI: The post discusses AI but does not describe an actual AI agent interaction.
- A6 — Irrelevant: The content is unrelated to the research question.
RULE: When evidence is insufficient, do not infer that a bot is an AI agent. Preserve ambiguity.

3. INTERACTION CLASSIFICATION (I1–I6):
- I1 — Human → AI Agent: A human player communicates with, instructs or interacts directly with an AI agent.
- I2 — AI Agent → Human: The AI agent produces an action, recommendation, response or outcome affecting the human player.
- I3 — Human ↔ AI Agent: Bidirectional interaction exists. (Primary category for human–AI co-creation analysis).
- I4 — Human → Human about AI: Humans discuss AI agents but do not directly interact with them.
- I5 — Human → AI-mediated environment: The AI influences the game environment in which humans operate.
- I6 — No meaningful interaction: AI is mentioned but no relevant interaction is identified.

4. VALUE CO-CREATION (VC1–VC4):
- VC1 — Value co-creation: The human and AI agent jointly contribute to an outcome perceived as valuable.
- VC2 — Potential value co-creation: Evidence suggests collaborative value creation, but evidence is incomplete.
- VC3 — Value co-destruction: The interaction produces harm, loss, frustration, unfairness or negative value.
- VC4 — No evidence of value creation/destruction: No meaningful value consequence can be identified.
RULE: Never assume that the existence of an AI agent constitutes value co-creation.

5. DART CODING (0 to 5 for each dimension independently):
- D — Dialogue: Communication, interaction, feedback, negotiation, instructions, responses, conversational exchange, mutual influence.
- A — Access: AI changes or facilitates access to information, resources, capabilities, game functions, knowledge, decision-making.
- R — Risk Assessment: Cheating, unfair advantage, economic risks, security, privacy, dependence, manipulation, loss of control, ecosystem disruption.
- T — Transparency: Disclosure of AI use, explainability, visibility of AI behavior, understanding how the system works, opacity, trust, accountability.
Scale for each DART dimension:
  0 = absent
  1 = weak
  2 = moderate
  3 = strong
  4 = very strong
  5 = explicit and central
For each dimension, provide: "score" (integer 0-5), "evidence" (direct quotation from post text, max 40 words, or "" if absent), and "confidence" (0.0 to 1.0).

6. EVIDENCE-FIRST PRINCIPLE:
Never assign a classification without identifying the literal evidence from the text. Never invent quotations.

7. CONFIDENCE CALIBRATION & HUMAN REVIEW:
Assign confidence (0.0 to 1.0) to classifications:
0.90–1.00 = Very high | 0.80–0.89 = High | 0.60–0.79 = Moderate | 0.40–0.59 = Low | 0.00–0.39 = Very low.
FLAG FOR HUMAN REVIEW (human_review_required = true) WHEN:
- Any confidence is below 0.80;
- AI vs conventional bot is unclear;
- Interaction type or DART dimension is ambiguous;
- Text contains sarcasm or irony, or context is missing.

8. OUTPUT FORMAT:
Respond STRICTLY with a single valid JSON object following this exact schema:
{
  "platform": "Discourse / Reddit / etc.",
  "game": "Game name",
  "community": "Community/Section name",
  "thread_id": "Thread ID",
  "post_id": "Post ID",
  "parent_post_id": "Parent post ID or empty string",
  "timestamp": "ISO timestamp",
  "author_id": "Author identifier",
  "title": "Topic title",
  "text": "Post text excerpt",
  "ai_type": "A1" | "A2" | "A3" | "A4" | "A5" | "A6",
  "ai_type_confidence": 0.0 to 1.0,
  "interaction_type": "I1" | "I2" | "I3" | "I4" | "I5" | "I6",
  "interaction_confidence": 0.0 to 1.0,
  "value_type": "VC1" | "VC2" | "VC3" | "VC4",
  "value_confidence": 0.0 to 1.0,
  "dart": {
    "dialogue": {
      "score": 0,
      "evidence": "Literal quote or empty string",
      "confidence": 0.0 to 1.0
    },
    "access": {
      "score": 0,
      "evidence": "Literal quote or empty string",
      "confidence": 0.0 to 1.0
    },
    "risk": {
      "score": 0,
      "evidence": "Literal quote or empty string",
      "confidence": 0.0 to 1.0
    },
    "transparency": {
      "score": 0,
      "evidence": "Literal quote or empty string",
      "confidence": 0.0 to 1.0
    }
  },
  "relevance": "RELEVANT" | "POSSIBLY RELEVANT" | "IRRELEVANT",
  "relevance_confidence": 0.0 to 1.0,
  "human_review_required": true | false,
  "classification_notes": "Reasoning supporting ai_type, interaction, and value classifications."
}
"""

class NetnographyAgent:
    def __init__(self, state_update_callback=None):
        self.processed_dir = config.DATA_PROCESSED_DIR
        self.analysis_dir = config.DATA_ANALYSIS_DIR
        self.output_jsonl = os.path.join(self.analysis_dir, "netnography_results.jsonl")
        self.write_lock = threading.Lock()
        self.state_callback = state_update_callback
        
    def _get_already_processed_ids(self):
        processed_ids = set()
        if os.path.exists(self.output_jsonl):
            try:
                with open(self.output_jsonl, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            try:
                                data = json.loads(line)
                                pid = data.get("post_id") or data.get("id")
                                if pid:
                                    processed_ids.add(str(pid))
                            except Exception:
                                pass
            except Exception as e:
                logger.error(f"Error reading processed JSONL: {e}")
        return processed_ids

    def analyze_single_post(self, post):
        post_id = str(post.get("post_id") or post.get("id"))
        game = post.get("game") or post.get("jogo", "Unknown")
        platform = post.get("platform", "Discourse")
        community = post.get("community") or post.get("seccao", "General")
        thread_id = str(post.get("thread_id") or post.get("topic_id", ""))
        parent_post_id = str(post.get("parent_post_id") or "")
        author_id = post.get("author_id") or post.get("autor", "Author_Unknown")
        timestamp = post.get("timestamp", "")
        title = post.get("title") or post.get("titulo", "")
        text = post.get("text") or post.get("corpo", "")
        
        logger.info(f"Analyzing post {post_id} under DART-NET Framework...")
        
        sanitized_post_text = sanitize_text(text)
        if len(sanitized_post_text) > 8000:
            prompt_text = sanitized_post_text[:8000] + "\n...[text truncated for analysis]..."
        else:
            prompt_text = sanitized_post_text
        
        user_content = (
            f"PLATFORM: {platform}\n"
            f"GAME: {game}\n"
            f"COMMUNITY: {community}\n"
            f"THREAD ID: {thread_id}\n"
            f"POST ID: {post_id}\n"
            f"PARENT POST ID: {parent_post_id}\n"
            f"TIMESTAMP: {timestamp}\n"
            f"AUTHOR ID: {author_id}\n"
            f"TITLE: {sanitize_text(title)}\n"
            f"POST TEXT:\n{prompt_text}\n\n"
            f"QUANTITATIVE METADATA:\n"
            f"- Likes: {post.get('likes', 0)}\n"
            f"- Author Trust Level: {post.get('trust_level', 0)}\n"
            f"- Edit Count: {post.get('edits', 1)}\n"
        )
        
        messages = [
            {"role": "system", "content": STATIC_DART_INSTRUCTIONS},
            {"role": "user", "content": user_content}
        ]
        
        try:
            # NetnographyAgent: deepseek-v4-flash, non-thinking mode for reliable structured JSON
            content, reasoning = api_client.call_llm(
                model=config.MODEL_FLASH,
                messages=messages,
                thinking_enabled=False,
                temperature=0.0,
                max_tokens=4000
            )
            
            # Parse the JSON output with robust repair
            parsed_json = extract_and_repair_json(content)
                
            # Guarantee Section 13 schema integrity
            parsed_json["platform"] = platform
            parsed_json["game"] = game
            parsed_json["community"] = community
            parsed_json["thread_id"] = thread_id
            parsed_json["post_id"] = post_id
            parsed_json["parent_post_id"] = parent_post_id
            parsed_json["timestamp"] = timestamp
            parsed_json["author_id"] = author_id
            parsed_json["title"] = title
            parsed_json["text"] = text
            
            # Default values if missing
            parsed_json["ai_type"] = parsed_json.get("ai_type", "A2")
            parsed_json["ai_type_confidence"] = float(parsed_json.get("ai_type_confidence", 0.75))
            parsed_json["interaction_type"] = parsed_json.get("interaction_type", "I4")
            parsed_json["interaction_confidence"] = float(parsed_json.get("interaction_confidence", 0.75))
            parsed_json["value_type"] = parsed_json.get("value_type", "VC4")
            parsed_json["value_confidence"] = float(parsed_json.get("value_confidence", 0.75))
            
            # Normalize DART dimensions
            if "dart" not in parsed_json or not isinstance(parsed_json["dart"], dict):
                parsed_json["dart"] = {}
                
            for dim in ["dialogue", "access", "risk", "transparency"]:
                if dim not in parsed_json["dart"] or not isinstance(parsed_json["dart"][dim], dict):
                    parsed_json["dart"][dim] = {"score": 0, "evidence": "", "confidence": 0.8}
                else:
                    d_obj = parsed_json["dart"][dim]
                    d_obj["score"] = int(d_obj.get("score", 0))
                    d_obj["evidence"] = str(d_obj.get("evidence") or "")
                    d_obj["confidence"] = float(d_obj.get("confidence", 0.8))
                    
            parsed_json["relevance"] = parsed_json.get("relevance", post.get("relevance", "RELEVANT"))
            parsed_json["relevance_confidence"] = float(parsed_json.get("relevance_confidence", post.get("relevance_confidence", 0.90)))
            
            # Evaluate Human Review Flag (Section 11)
            # Flag if confidence < 0.80 in any classification or explicitly marked
            confidences = [
                parsed_json["ai_type_confidence"],
                parsed_json["interaction_confidence"],
                parsed_json["value_confidence"],
                parsed_json["relevance_confidence"],
                parsed_json["dart"]["dialogue"]["confidence"],
                parsed_json["dart"]["access"]["confidence"],
                parsed_json["dart"]["risk"]["confidence"],
                parsed_json["dart"]["transparency"]["confidence"]
            ]
            min_conf = min(confidences) if confidences else 1.0
            
            human_review_required = bool(
                parsed_json.get("human_review_required", False) or
                (min_conf < config.CONFIDENCE_HIGH) or
                (parsed_json["ai_type"] in ["A2", "A3"] and "ai" in text.lower() and "agent" in text.lower()) # Ambiguity check
            )
            parsed_json["human_review_required"] = human_review_required
            
            if "classification_notes" not in parsed_json:
                parsed_json["classification_notes"] = f"Min confidence: {min_conf:.2f}. Human review: {human_review_required}."
                
            # Maintain backward-compatibility alias keys for legacy reporters/tables
            parsed_json["id"] = post_id
            parsed_json["jogo"] = game
            parsed_json["likes"] = post.get("likes", 0)
            parsed_json["trust_level"] = post.get("trust_level", 0)
            parsed_json["edits"] = post.get("edits", 1)
            parsed_json["_thinking_process"] = reasoning
            
            # Mapping to legacy keys
            # Dominant dimension by max score
            scores = {dim: parsed_json["dart"][dim]["score"] for dim in ["dialogue", "access", "risk", "transparency"]}
            max_dim = max(scores, key=scores.get) if any(scores.values()) else "risk"
            parsed_json["dimensao_dominante"] = max_dim
            parsed_json["score_risco_percebido"] = max(1, parsed_json["dart"]["risk"]["score"])
            parsed_json["fundamentacao_risco"] = parsed_json["dart"]["risk"]["evidence"] or parsed_json.get("classification_notes", "")
            
            # Map value_type to legacy tipologia_cocriacao
            vc_map = {
                "VC1": "simetrica",
                "VC2": "assimetrica",
                "VC3": "parasitaria",
                "VC4": "assimetrica"
            }
            parsed_json["tipologia_cocriacao"] = vc_map.get(parsed_json["value_type"], "parasitaria")
            
            # Backward-compatible DART dict format for old scripts
            for dim in ["dialogue", "access", "risk", "transparency"]:
                legacy_dim_name = {"dialogue": "dialogo", "access": "acesso", "risk": "risco", "transparency": "transparencia"}[dim]
                parsed_json[legacy_dim_name] = {
                    "presente": parsed_json["dart"][dim]["score"] > 0,
                    "evidencia_literal": parsed_json["dart"][dim]["evidence"],
                    "interpretacao_teorica": f"Score {parsed_json['dart'][dim]['score']}/5 (conf {parsed_json['dart'][dim]['confidence']:.2f})",
                    "contexto_jogo": f"{game} {community}"
                }
                
            logger.info(f"Post {post_id} analyzed. AI Type: {parsed_json['ai_type']}, Interaction: {parsed_json['interaction_type']}, Value: {parsed_json['value_type']}, Human Review: {human_review_required}")
            return parsed_json
            
        except Exception as e:
            logger.error(f"Error executing DART-NET analysis on post {post_id}: {e}")
            return {
                "platform": platform,
                "game": game,
                "community": community,
                "thread_id": thread_id,
                "post_id": post_id,
                "parent_post_id": parent_post_id,
                "timestamp": timestamp,
                "author_id": author_id,
                "title": title,
                "text": text,
                "ai_type": "A6",
                "ai_type_confidence": 0.30,
                "interaction_type": "I6",
                "interaction_confidence": 0.30,
                "value_type": "VC4",
                "value_confidence": 0.30,
                "dart": {
                    "dialogue": {"score": 0, "evidence": "", "confidence": 0.30},
                    "access": {"score": 0, "evidence": "", "confidence": 0.30},
                    "risk": {"score": 0, "evidence": "", "confidence": 0.30},
                    "transparency": {"score": 0, "evidence": "", "confidence": 0.30}
                },
                "relevance": "POSSIBLY RELEVANT",
                "relevance_confidence": 0.30,
                "human_review_required": True,
                "classification_notes": f"Processing error encountered: {e}",
                "id": post_id,
                "jogo": game,
                "dimensao_dominante": "risk",
                "score_risco_percebido": 1,
                "fundamentacao_risco": f"Erro: {e}",
                "tipologia_cocriacao": "parasitaria",
                "_thinking_process": f"Erro: {e}"
            }


    def run(self):
        logger.info("NetnographyAgent starting execution...")
        
        processed_file = os.path.join(self.processed_dir, "anonymized_posts.json")
        if not os.path.exists(processed_file):
            logger.error(f"Anonymized posts file not found at {processed_file}. Please run previous agents first.")
            return []
            
        try:
            with open(processed_file, "r", encoding="utf-8") as f:
                posts = json.load(f)
        except Exception as e:
            logger.error(f"Failed to read anonymized posts: {e}")
            return []
            
        already_processed = self._get_already_processed_ids()
        posts_to_process = [p for p in posts if p["id"] not in already_processed]
        
        logger.info(f"Resume Status: {len(already_processed)} posts already analyzed, {len(posts_to_process)} posts remaining to analyze.")
        
        if not posts_to_process:
            logger.info("All posts are already analyzed. Nothing to do.")
            # Read and return existing results
            results = []
            if os.path.exists(self.output_jsonl):
                with open(self.output_jsonl, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            results.append(json.loads(line))
            return results
            
        results = []
        batch = []
        batch_size = 10
        
        # Process remaining posts in parallel
        num_workers = min(config.MAX_WORKERS, len(posts_to_process)) if posts_to_process else 1
        logger.info(f"Running DART analysis with {num_workers} threads...")
        
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_post = {executor.submit(self.analyze_single_post, post): post for post in posts_to_process}
            
            for index, future in enumerate(as_completed(future_to_post)):
                post = future_to_post[future]
                try:
                    analysis_result = future.result()
                    results.append(analysis_result)
                    batch.append(analysis_result)
                except Exception as e:
                    logger.error(f"Future execution failed for post {post.get('id')}: {e}")
                    
                # Incrementally save in batches of 10
                if len(batch) >= batch_size or (index + 1) == len(posts_to_process):
                    with self.write_lock:
                        try:
                            # Append to file
                            with open(self.output_jsonl, "a", encoding="utf-8") as f:
                                for res in batch:
                                    f.write(json.dumps(res, ensure_ascii=False) + "\n")
                            logger.info(f"Saved batch of {len(batch)} analyses to {self.output_jsonl}")
                        except Exception as e:
                            logger.error(f"Failed to write analysis batch: {e}")
                            
                    # Update progress state via callback if set
                    if self.state_callback:
                        progress_pct = int(((len(already_processed) + index + 1) / len(posts)) * 100)
                        self.state_callback(
                            last_post_id=post["id"],
                            progress_pct=progress_pct,
                            remaining_count=len(posts_to_process) - (index + 1)
                        )
                    batch = []
                    
        # Load all results from file (both old and new) to return full dataset
        all_results = []
        if os.path.exists(self.output_jsonl):
            try:
                with open(self.output_jsonl, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            all_results.append(json.loads(line))
            except Exception as e:
                logger.error(f"Error loading final list of results: {e}")
                
        return all_results

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = NetnographyAgent()
    agent.run()
