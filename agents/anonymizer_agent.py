import os
import json
import re
import time
import logging
import config

logger = logging.getLogger("pipeline.anonymizer_agent")

class AnonymizerAgent:
    def __init__(self):
        self.interim_dir = config.DATA_INTERIM_DIR
        self.processed_dir = config.DATA_PROCESSED_DIR
        self.map_file = os.path.join(self.interim_dir, "author_token_map.json")
        self.author_map = self._load_author_map()
        
    def _load_author_map(self):
        if os.path.exists(self.map_file):
            try:
                with open(self.map_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load author token map: {e}")
        return {}
        
    def _save_author_map(self):
        try:
            with open(self.map_file, "w", encoding="utf-8") as f:
                json.dump(self.author_map, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Failed to save author token map: {e}")
            
    def _get_next_player_id(self):
        existing_nums = []
        for pid in self.author_map.values():
            if pid.startswith("Player_"):
                try:
                    num = int(pid.split("_")[1])
                    existing_nums.append(num)
                except ValueError:
                    pass
        next_num = max(existing_nums) + 1 if existing_nums else 1
        return f"Player_{next_num:03d}"
        
    def _get_or_create_synthetic_id(self, real_username):
        if not real_username:
            return "Player_Anonymous"
        
        # Strip prefixes like u/ or @ if they were passed
        clean_name = real_username.strip()
        if clean_name.lower().startswith("u/"):
            clean_name = clean_name[2:]
        elif clean_name.startswith("@"):
            clean_name = clean_name[1:]
            
        if clean_name not in self.author_map:
            synthetic_id = self._get_next_player_id()
            self.author_map[clean_name] = synthetic_id
            logger.info(f"Mapped user '{clean_name}' to synthetic '{synthetic_id}'")
        return self.author_map[clean_name]

    def anonymize_text(self, text):
        if not text:
            return ""
            
        # 1. Anonymize Emails
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        text = re.sub(email_pattern, "[EMAIL_ANONYMIZED]", text)
        
        # 2. Anonymize URLs
        url_pattern = r'https?://[a-zA-Z0-9./?=&_%+-]+'
        text = re.sub(url_pattern, "[URL_ANONYMIZED]", text)
        
        # 3. Keep User Mentions (u/username or @username) original as per user requirement
        pass
            
        # 4. Anonymize Numeric IDs (sequences of 4+ digits representing internal IDs or codes)
        numeric_id_pattern = r'\b\d{4,}\b'
        text = re.sub(numeric_id_pattern, "[ID_ANONYMIZED]", text)
        
        return text

    def run(self, posts=None):
        logger.info("AnonymizerAgent starting sanitization...")
        
        if posts is None:
            validated_file = os.path.join(self.interim_dir, "validated_posts.json")
            if not os.path.exists(validated_file):
                logger.error(f"Validated posts file not found at {validated_file}. Aborting anonymizer.")
                return []
                
            try:
                with open(validated_file, "r", encoding="utf-8") as f:
                    posts = json.load(f)
            except Exception as e:
                logger.error(f"Failed to read validated posts: {e}")
                return []
            
        anonymized_posts = []
        for post in posts:
            # Determine pseudonymized author id
            real_author = post.get("author_id") or post.get("autor", "Anónimo")
            synthetic_author = self._get_or_create_synthetic_id(real_author)
            
            # Sanitization of private PII (emails/private links) while preserving original text
            raw_text = post.get("text") or post.get("corpo", "")
            sanitized_text = self.anonymize_text(raw_text)
            title = post.get("title") or post.get("titulo", "")
            
            # Construct processed post complying with DART-NET Layer 2
            anon_post = {
                # Core DART-NET fields
                "platform": post.get("platform", "Discourse"),
                "game": post.get("game") or post.get("jogo", "Desconhecido"),
                "community": post.get("community") or post.get("seccao", "Geral"),
                "thread_id": str(post.get("thread_id") or post.get("topic_id", "")),
                "post_id": str(post.get("post_id") or post["id"]),
                "parent_post_id": str(post.get("parent_post_id") or ""),
                "timestamp": post.get("timestamp") or "",
                "author_id": synthetic_author,
                "title": title,
                "text": sanitized_text,
                "replies": post.get("replies", 0),
                "conversation_structure": post.get("conversation_structure", {}),
                "url": post.get("url") or post.get("url_fonte", ""),
                "collection_date": post.get("collection_date", time.strftime("%Y-%m-%d")),
                "keywords_triggered": post.get("keywords_triggered", []),
                "relevance": post.get("relevance", "RELEVANT"),
                "relevance_confidence": post.get("relevance_confidence", 0.90),
                "relevance_justification": post.get("relevance_justification") or post.get("validacao_justificacao", ""),
                
                # Backward-compatibility alias keys
                "id": str(post.get("post_id") or post["id"]),
                "topic_id": post.get("topic_id"),
                "slug": post.get("slug", ""),
                "jogo": post.get("game") or post.get("jogo", ""),
                "fonte": post.get("fonte", ""),
                "titulo": title,
                "corpo": sanitized_text,
                "autor": synthetic_author,
                "seccao": post.get("seccao", ""),
                "url_fonte": post.get("url") or post.get("url_fonte", ""),
                "likes": post.get("likes", 0),
                "trust_level": post.get("trust_level", 0),
                "edits": post.get("edits", 1),
                "validacao_justificacao": post.get("relevance_justification") or post.get("validacao_justificacao", "")
            }
            anonymized_posts.append(anon_post)
            
        # Save map and final anonymized data
        self._save_author_map()
        
        processed_file = os.path.join(self.processed_dir, "anonymized_posts.json")
        existing_anon_posts = []
        if os.path.exists(processed_file):
            try:
                with open(processed_file, "r", encoding="utf-8") as f:
                    existing_anon_posts = json.load(f)
            except Exception:
                pass
                
        # Merge by unique ID: newly anonymized posts take precedence over older records
        merged_map = {}
        for p in existing_anon_posts:
            pid = str(p.get("post_id") or p.get("id"))
            # Normalize legacy fields if missing
            if "game" not in p:
                p["game"] = p.get("jogo", "Desconhecido")
            if "platform" not in p:
                src = (p.get("fonte", "") + p.get("url_fonte", "")).lower()
                if "reddit" in src:
                    p["platform"] = "Reddit"
                elif "steam" in src:
                    p["platform"] = "Steam Community"
                else:
                    p["platform"] = "Discourse"
            if "title" not in p:
                p["title"] = p.get("titulo", "")
            if "text" not in p:
                p["text"] = p.get("corpo", "")
            if "author_id" not in p:
                p["author_id"] = p.get("autor", "Player_Anonymous")
            if "relevance" not in p:
                p["relevance"] = "RELEVANT"
            if "relevance_confidence" not in p:
                p["relevance_confidence"] = 0.90
            merged_map[pid] = p

        for p in anonymized_posts:
            pid = str(p.get("post_id") or p.get("id"))
            merged_map[pid] = p

        merged_posts = list(merged_map.values())
                
        try:
            with open(processed_file, "w", encoding="utf-8") as f:
                json.dump(merged_posts, f, indent=2, ensure_ascii=False)
            logger.info(f"AnonymizerAgent saved {len(merged_posts)} total merged anonymized posts to {processed_file}.")
        except Exception as e:
            logger.error(f"Failed to save anonymized posts: {e}")
            raise e
            
        # DART-NET Section 14: Preservation of 3 Layers (RAW DATA / AI CODING / HUMAN VALIDATION)
        # Raw and interim data are preserved intact to guarantee scientific auditability and reproducibility.
        logger.info("DART-NET Layer 1 (RAW DATA) and Layer 2 (AI CODING) preserved without destructive deletion.")
        logger.info("AnonymizerAgent execution complete.")
        return anonymized_posts

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = AnonymizerAgent()
    agent.run()
