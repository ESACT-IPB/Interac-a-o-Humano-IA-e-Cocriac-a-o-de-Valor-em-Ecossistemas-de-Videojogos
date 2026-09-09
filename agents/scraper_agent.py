import os
import json
import time
import re
import logging
import config

logger = logging.getLogger("pipeline.scraper_agent")

def strip_html_tags(text):
    """HTML tag stripping using regular expressions."""
    if not text:
        return ""
    # Strip HTML tags
    clean = re.sub(r"<[^>]+>", "", text)
    # Decode basic HTML entities
    clean = clean.replace("&quot;", '"').replace("&amp;", '&').replace("&lt;", '<').replace("&gt;", '>').replace("&nbsp;", ' ')
    return clean.strip()

class ScraperAgent:
    def __init__(self):
        self.raw_dir = config.DATA_RAW_DIR
        self.interim_dir = config.DATA_INTERIM_DIR
        self.corpus_file = os.path.join(config.BASE_DIR, "data", "target_corpus_303.json")
        self.target_topic_ids = set()
        self.target_urls = set()
        
        if os.path.exists(self.corpus_file):
            try:
                with open(self.corpus_file, "r", encoding="utf-8") as f:
                    corpus = json.load(f)
                    for item in corpus:
                        tid = str(item.get("topic_id") or "").strip()
                        if tid and tid != "None":
                            self.target_topic_ids.add(tid)
                        u = item.get("canonical_url", "").strip()
                        if u:
                            self.target_urls.add(u)
                logger.info(f"Loaded target corpus: {len(self.target_topic_ids)} topic IDs, {len(self.target_urls)} canonical URLs.")
            except Exception as e:
                logger.error(f"Error loading target corpus: {e}")
        
    def run(self):
        logger.info(f"ScraperAgent starting with temporal boundary >= {config.POST_MIN_DATE}...")
        
        # Look for JSON files in the raw folder
        raw_files = [f for f in os.listdir(self.raw_dir) if f.endswith(".json")]
        if not raw_files:
            logger.warning("No raw JSON topic files found to scrape.")
            return []
            
        logger.info(f"Found {len(raw_files)} raw topic files. Beginning extraction...")
        
        normalized_posts = []
        skipped_pre_2024 = 0
        skipped_short = 0
        skipped_non_target = 0

        for file_name in raw_files:
            file_path = os.path.join(self.raw_dir, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    topic = json.load(f)
            except Exception as e:
                logger.error(f"Error reading file {file_path}: {e}")
                continue
                
            topic_id = str(topic.get("id") or topic.get("topic_id") or "")
            title = topic.get("title", "Sem Título")
            slug = topic.get("slug", "")
            game = topic.get("jogo", "Desconhecido")
            source = topic.get("fonte", "Desconhecido")
            section = topic.get("seccao", "Geral")
            url_fonte = topic.get("url_fonte") or topic.get("canonical_url") or ""
            
            # Check if topic belongs to target corpus
            is_target = False
            if self.target_topic_ids:
                if topic_id in self.target_topic_ids:
                    is_target = True
                elif any(tid in file_name for tid in self.target_topic_ids):
                    is_target = True
                elif url_fonte and any(tu in url_fonte or url_fonte in tu for tu in self.target_urls):
                    is_target = True
            else:
                is_target = True

            if not is_target:
                skipped_non_target += 1
                continue
            
            posts = topic.get("post_stream", {}).get("posts", [])
            for post in posts:
                post_stream_id = post.get("id")
                post_id = f"{topic_id}_{post_stream_id}"
                
                # STRICT TEMPORAL FILTER: created_at >= POST_MIN_DATE (2024-01-01)
                post_created_at = post.get("created_at") or ""
                if post_created_at < config.POST_MIN_DATE:
                    skipped_pre_2024 += 1
                    continue
                
                cooked_content = post.get("cooked", "")
                clean_body = strip_html_tags(cooked_content)
                
                if len(clean_body) < config.MIN_BODY_LENGTH:
                    skipped_short += 1
                    continue
                    
                # Determine platform
                platform = "Discourse"
                if "reddit" in (url_fonte or "").lower() or "reddit" in (source or "").lower():
                    platform = "Reddit"
                elif "steam" in (url_fonte or "").lower() or "steam" in (source or "").lower():
                    platform = "Steam Community"
                elif "mmo-champion" in (url_fonte or "").lower():
                    platform = "vBulletin"

                # Check discovery keywords triggered (Stage 1)
                full_searchable = f"{title} {clean_body}".lower()
                keywords_triggered = [
                    kw for kw in config.DISCOVERY_KEYWORDS
                    if kw.lower() in full_searchable
                ]

                # Normalize schema carrying over Discourse metadata and DART-NET requirements
                normalized_post = {
                    # Core DART-NET fields (Section 4 & 13)
                    "platform": platform,
                    "game": game,
                    "community": section or source,
                    "thread_id": str(topic_id),
                    "post_id": str(post_id),
                    "parent_post_id": str(post.get("reply_to_post_number") or ""),
                    "timestamp": post.get("created_at") or time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "author_id": post.get("username", "Anónimo"),
                    "title": title,
                    "text": clean_body,
                    "replies": post.get("reply_count", 0),
                    "conversation_structure": {
                        "post_number": post.get("post_number", 1),
                        "reply_to_post_number": post.get("reply_to_post_number")
                    },
                    "url": url_fonte,
                    "collection_date": time.strftime("%Y-%m-%d"),
                    "keywords_triggered": keywords_triggered,
                    
                    # Backward-compatibility alias keys
                    "id": str(post_id),
                    "topic_id": topic_id,
                    "slug": slug,
                    "jogo": game,
                    "fonte": source,
                    "titulo": title,
                    "corpo": clean_body,
                    "autor": post.get("username", "Anónimo"),
                    "seccao": section,
                    "url_fonte": url_fonte,
                    "likes": post.get("like_count", 0),
                    "trust_level": post.get("trust_level", 0),
                    "edits": post.get("version", 1)
                }
                normalized_posts.append(normalized_post)
                logger.info(f"Post {post_id} normalized successfully (keywords: {len(keywords_triggered)}).")

            
        logger.info(
            f"Extraction metrics: {len(normalized_posts)} posts retained (>= {config.POST_MIN_DATE}). "
            f"Filtered out: {skipped_pre_2024} pre-2024 posts, {skipped_short} short posts (< {config.MIN_BODY_LENGTH} chars), "
            f"{skipped_non_target} non-target topic files."
        )

        # Write to interim directory
        output_file = os.path.join(self.interim_dir, "scraped_posts.json")
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(normalized_posts, f, indent=2, ensure_ascii=False)
            logger.info(f"ScraperAgent complete. Saved {len(normalized_posts)} posts to {output_file}.")
        except Exception as e:
            logger.error(f"Failed to write scraped posts: {e}")
            raise e
            
        return normalized_posts

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = ScraperAgent()
    agent.run()
