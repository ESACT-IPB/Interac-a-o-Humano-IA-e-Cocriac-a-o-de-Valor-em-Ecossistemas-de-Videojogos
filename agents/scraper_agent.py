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
        
    def run(self):
        logger.info("ScraperAgent starting...")
        
        # Look for JSON files in the raw folder
        raw_files = [f for f in os.listdir(self.raw_dir) if f.endswith(".json")]
        if not raw_files:
            logger.warning("No raw JSON topic files found to scrape.")
            return []
            
        logger.info(f"Found {len(raw_files)} raw topic files. Beginning extraction...")
        
        normalized_posts = []
        for file_name in raw_files:
            file_path = os.path.join(self.raw_dir, file_name)
            logger.info(f"Loading raw topic file: {file_path}")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    topic = json.load(f)
            except Exception as e:
                logger.error(f"Error reading file {file_path}: {e}")
                continue
                
            topic_id = topic.get("id")
            title = topic.get("title", "Sem Título")
            slug = topic.get("slug", "")
            game = topic.get("jogo", "Desconhecido")
            source = topic.get("fonte", "Desconhecido")
            section = topic.get("seccao", "Geral")
            url_fonte = topic.get("url_fonte", "")
            
            posts = topic.get("post_stream", {}).get("posts", [])
            for post in posts:
                post_stream_id = post.get("id")
                post_id = f"{topic_id}_{post_stream_id}"
                
                logger.info(f"Processing post {post_id}... (Simulating {config.IO_DELAY_SECONDS}s I/O delay)")
                time.sleep(config.IO_DELAY_SECONDS)
                
                cooked_content = post.get("cooked", "")
                clean_body = strip_html_tags(cooked_content)
                
                if len(clean_body) < config.MIN_BODY_LENGTH:
                    logger.warning(f"Post {post_id} filtered out: body length is {len(clean_body)} (< {config.MIN_BODY_LENGTH} chars).")
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
