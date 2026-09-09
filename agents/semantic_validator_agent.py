import os
import json
import logging
import threading
import re
import time
import config
import api_client
from sanitizer import sanitize_text

logger = logging.getLogger("pipeline.semantic_validator_agent")

class SemanticValidatorAgent:
    def __init__(self):
        self.interim_dir = config.DATA_INTERIM_DIR
        self.cache_file = os.path.join(self.interim_dir, "validation_cache.json")
        self.cache_lock = threading.Lock()
        self.cache = self._load_cache()
        
        self.dirty_count = 0

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load validation cache: {e}")
        return {}
        
    def _save_cache(self, force=False):
        with self.cache_lock:
            if not force and self.dirty_count < 25:
                return
            try:
                with open(self.cache_file, "w", encoding="utf-8") as f:
                    json.dump(self.cache, f, indent=2, ensure_ascii=False)
                self.dirty_count = 0
            except Exception as e:
                logger.error(f"Failed to save validation cache: {e}")
                
    def check_post_relevance(self, post):
        post_id = post.get("post_id") or post["id"]
        
        # Check cache first
        with self.cache_lock:
            if post_id in self.cache:
                entry = self.cache[post_id]
                logger.info(f"Post {post_id} found in validation cache.")
                if isinstance(entry, bool):
                    rel = "RELEVANT" if entry else "IRRELEVANT"
                    return rel, 0.90, "From historical validation cache"
                elif isinstance(entry, dict):
                    return entry.get("relevance", "RELEVANT"), entry.get("relevance_confidence", 0.9), entry.get("justification", "")
                return "RELEVANT", 0.90, ""
                
        # Cache miss, query LLM
        title = post.get("title") or post.get("titulo", "")
        body = post.get("text") or post.get("corpo", "")
        game = post.get("game") or post.get("jogo", "")
        keywords = post.get("keywords_triggered", [])
        
        system_prompt = (
            "You are an AI research agent conducting netnographic data screening for DART-NET.\n"
            "RESEARCH OBJECTIVE: Identify online community discussions containing evidence of human-AI agent interaction, "
            "use of AI agents/bots/automation within game ecosystems, AI-mediated gameplay, perceptions of AI, "
            "or value creation/destruction associated with AI.\n"
            "NOTE: The central analytical unit is the human-AI interaction or automation impact, not simply the presence of the word 'AI'.\n\n"
            "SCREENING CATEGORIES:\n"
            "- RELEVANT: Post contains evidence directly related to an AI agent, bots, automation, player-AI interaction, consequences, perceptions, or value co-creation.\n"
            "- POSSIBLY RELEVANT: Evidence is ambiguous or implicit (e.g. describes adaptive behavior, emergent bot dynamics, or unclear automation).\n"
            "- IRRELEVANT: Content is completely unrelated to AI, bots, automation, or game ecosystems.\n\n"
            "Respond STRICTLY in JSON format with the following keys:\n"
            "{\n"
            "  \"relevance\": \"RELEVANT\" | \"POSSIBLY RELEVANT\" | \"IRRELEVANT\",\n"
            "  \"relevance_confidence\": 0.0 to 1.0,\n"
            "  \"justification\": \"Brief explanation (max 35 words) in Portuguese or English.\"\n"
            "}"
        )
        
        user_prompt = (
            f"Game: {game}\n"
            f"Title: {sanitize_text(title)}\n"
            f"Keywords Triggered: {', '.join(keywords) if keywords else 'None'}\n"
            f"Post Body:\n{sanitize_text(body)}\n"
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        try:
            # SemanticValidatorAgent: deepseek-v4-flash, non-thinking
            response_content, _ = api_client.call_llm(
                model=config.MODEL_FLASH,
                messages=messages,
                thinking_enabled=False,
                temperature=0.0
            )
            
            # Find the JSON block inside the response
            json_match = re.search(r"\{.*\}", response_content, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group(0))
            else:
                result = json.loads(response_content)
                
            raw_rel = str(result.get("relevance", "RELEVANT")).upper()
            if "POSSIB" in raw_rel:
                relevance = "POSSIBLY RELEVANT"
            elif "IRREL" in raw_rel or raw_rel == "FALSE":
                relevance = "IRRELEVANT"
            else:
                relevance = "RELEVANT"
                
            confidence = float(result.get("relevance_confidence", 0.85))
            justification = result.get("justification", "Sem justificação.")
            
            # Save to cache
            with self.cache_lock:
                self.cache[post_id] = {
                    "relevance": relevance,
                    "relevance_confidence": confidence,
                    "justification": justification,
                    "checked_at": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                self.dirty_count += 1
            self._save_cache()
            
            logger.info(f"Post {post_id} evaluated: relevance={relevance} (conf={confidence:.2f}). Justification: {justification}")
            return relevance, confidence, justification
            
        except Exception as e:
            logger.error(f"Error evaluating post {post_id}: {e}. Defaulting to POSSIBLY RELEVANT for safety.")
            return "POSSIBLY RELEVANT", 0.50, f"Error checking post: {e}"

    def run(self, posts):
        logger.info("SemanticValidatorAgent starting DART-NET verification...")
        
        valid_posts = []
        num_workers = min(config.MAX_WORKERS, len(posts)) if posts else 1
        logger.info(f"Running semantic validation with {num_workers} concurrent workers...")
        
        from concurrent.futures import ThreadPoolExecutor, as_completed
        futures_map = {}
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            for post in posts:
                future = executor.submit(self.check_post_relevance, post)
                futures_map[future] = post
                
            for future in as_completed(futures_map):
                post = futures_map[future]
                try:
                    relevance, confidence, justification = future.result()
                    # Keep both RELEVANT and POSSIBLY RELEVANT posts as per DART-NET guideline
                    if relevance in ["RELEVANT", "POSSIBLY RELEVANT"]:
                        post["relevance"] = relevance
                        post["relevance_confidence"] = confidence
                        post["relevance_justification"] = justification
                        post["validacao_justificacao"] = justification
                        valid_posts.append(post)
                    else:
                        logger.info(f"Post {post.get('id')} excluded as IRRELEVANT: {justification}")
                except Exception as e:
                    logger.error(f"Error processing future for post {post.get('id')}: {e}")
                    
        # Sort back to preserve order efficiently
        post_indices = {(p.get('id') or p.get('post_id')): i for i, p in enumerate(posts)}
        valid_posts.sort(key=lambda x: post_indices.get(x.get('id') or x.get('post_id'), 999999))
        
        # Ensure all cache updates are flushed to disk
        self._save_cache(force=True)

        # Save validated posts
        output_file = os.path.join(self.interim_dir, "validated_posts.json")
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(valid_posts, f, indent=2, ensure_ascii=False)
            logger.info(f"SemanticValidatorAgent complete. Saved {len(valid_posts)} valid posts to {output_file}.")
        except Exception as e:
            logger.error(f"Failed to write validated posts: {e}")
            
        return valid_posts
