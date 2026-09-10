import os
import json
import logging
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import config
import api_client
from sanitizer import sanitize_text

logger = logging.getLogger("pipeline.summary_table_generator")

class SummaryTableGenerator:
    def __init__(self):
        self.processed_dir = config.DATA_PROCESSED_DIR
        self.output_dir = config.OUTPUT_DIR
        self.cache_file = os.path.join(config.DATA_INTERIM_DIR, "summary_cache.json")
        self.cache_lock = threading.Lock()
        self.cache = self._load_cache()
        self.dirty_count = 0

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load summary cache: {e}")
        return {}

    def _save_cache(self, force=False):
        with self.cache_lock:
            if not force and self.dirty_count < 20:
                return
            try:
                with open(self.cache_file, "w", encoding="utf-8") as f:
                    json.dump(self.cache, f, indent=2, ensure_ascii=False)
                self.dirty_count = 0
            except Exception as e:
                logger.error(f"Failed to save summary cache: {e}")

    def _build_url(self, post):
        url_fonte = post.get("url") or post.get("url_fonte")
        if url_fonte:
            return url_fonte
            
        topic_id = str(post.get("thread_id") or post.get("topic_id") or post["id"].split("_")[0])
        slug = post.get("slug", "post") or "post"
        game = post.get("game") or post.get("jogo", "")
        source = post.get("platform") or post.get("fonte", "")
        section = post.get("community") or post.get("seccao", "")
        
        # Build direct link dynamically based on game, source and section
        if game == "EVE Online":
            if "reddit" in (source or "").lower():
                return f"https://www.reddit.com/r/Eve/comments/{topic_id}"
            else:
                return f"https://forums.eveonline.com/t/{slug}/{topic_id}"
        elif game == "World of Warcraft":
            if "reddit" in (source or "").lower():
                return f"https://www.reddit.com/r/wow/comments/{topic_id}"
            elif "mmo-champion" in (section or "").lower() or "mmo-champion" in (source or "").lower():
                return f"https://www.mmo-champion.com/threads/{topic_id}"
            else:
                return f"https://forums.blizzard.com/pt/wow/t/{slug}/{topic_id}"
        return f"https://www.example.com/posts/{topic_id}"

    def generate_single_summary(self, post):
        post_id = str(post.get("post_id") or post["id"])
        
        # Check cache
        with self.cache_lock:
            if post_id in self.cache:
                entry = self.cache[post_id]
                return {
                    "post_id": post_id,
                    "resumo": entry.get("resumo", ""),
                    "tema": entry.get("tema", ""),
                    "url": entry.get("url") or self._build_url(post)
                }

        logger.info(f"Generating summary and theme for post {post_id}...")
        body = post.get("text") or post.get("corpo", "")
        
        system_prompt = (
            "És um assistente netnográfico especializado em resumos científicos.\n"
            "Deves ler o corpo do post e extrair:\n"
            "1. Um resumo curto em português de Portugal (estritamente máximo de 50 palavras).\n"
            "2. Um resumo do tema (estritamente máximo de 8 palavras).\n\n"
            "Responde ESTRITAMENTE em formato JSON com a seguinte estrutura:\n"
            "{\n"
            "  \"resumo\": \"O resumo do post aqui...\",\n"
            "  \"tema\": \"O tema aqui...\"\n"
            "}"
        )
        
        user_prompt = f"Corpo do Post:\n{sanitize_text(body)}\n"
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        try:
            # SummaryTableGenerator: deepseek-v4-flash, non-thinking mode
            content, _ = api_client.call_llm(
                model=config.MODEL_FLASH,
                messages=messages,
                thinking_enabled=False,
                temperature=0.1
            )
            
            json_match = re.search(r"\{.*\}", content, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group(0))
            else:
                result = json.loads(content)
                
            resumo = result.get("resumo", "").strip()
            tema = result.get("tema", "").strip()
            
            # Clean up if the model exceeded word counts slightly
            resumo_words = resumo.split()
            if len(resumo_words) > 50:
                resumo = " ".join(resumo_words[:47]) + "..."
                
            tema_words = tema.split()
            if len(tema_words) > 8:
                tema = " ".join(tema_words[:7]) + "..."
                
            url = self._build_url(post)
            with self.cache_lock:
                self.cache[post_id] = {"resumo": resumo, "tema": tema, "url": url}
                self.dirty_count += 1
            self._save_cache()
            return {
                "post_id": post_id,
                "resumo": resumo,
                "tema": tema,
                "url": url
            }
        except Exception as e:
            logger.error(f"Failed to generate summary for post {post_id}: {e}")
            # Fallback
            words = (post.get("text") or post.get("corpo", "")).split()
            fallback_summary = " ".join(words[:45]) + "..." if len(words) > 45 else " ".join(words)
            title = post.get("title") or post.get("titulo", "Automação e Bots")
            title_words = title.split()
            fallback_theme = " ".join(title_words[:7]) + "..." if len(title_words) > 7 else title
            url = self._build_url(post)
            with self.cache_lock:
                self.cache[post_id] = {"resumo": fallback_summary, "tema": fallback_theme, "url": url}
                self.dirty_count += 1
            self._save_cache()
            return {
                "post_id": post_id,
                "resumo": fallback_summary,
                "tema": fallback_theme,
                "url": url
            }

    def run(self):
        logger.info("SummaryTableGenerator starting processing...")
        
        anon_file = os.path.join(self.processed_dir, "anonymized_posts.json")
        if not os.path.exists(anon_file):
            logger.error(f"Anonymized posts file not found: {anon_file}")
            return False
            
        with open(anon_file, "r", encoding="utf-8") as f:
            posts = json.load(f)
            
        if not posts:
            logger.warning("No posts available to summarize.")
            return False
            
        # Load netnography coding results to cross-reference classifications
        netno_file = os.path.join(config.DATA_ANALYSIS_DIR, "netnography_results.jsonl")
        netno_map = {}
        if os.path.exists(netno_file):
            try:
                with open(netno_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            d = json.loads(line)
                            pid = str(d.get("post_id") or d.get("id"))
                            netno_map[pid] = d
            except Exception as e:
                logger.error(f"Error loading netnography results for summary table: {e}")
            
        # Filter posts to only include those in the active netnography corpus
        if netno_map:
            posts = [p for p in posts if str(p.get("post_id") or p.get("id")) in netno_map]

        table_rows = []
        num_workers = min(config.MAX_WORKERS, len(posts)) if posts else 1
        
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_post = {executor.submit(self.generate_single_summary, post): post for post in posts}
            for future in as_completed(future_to_post):
                post = future_to_post[future]
                try:
                    row_data = future.result()
                    pid = str(row_data["post_id"])
                    
                    # Attach DART-NET coding attributes if present
                    if pid in netno_map:
                        nc = netno_map[pid]
                        row_data["game"] = nc.get("game") or nc.get("jogo", post.get("game", "N/A"))
                        row_data["ai_type"] = nc.get("ai_type", "A2")
                        row_data["interaction_type"] = nc.get("interaction_type", "I4")
                        row_data["value_type"] = nc.get("value_type", "VC4")
                        dart_scores = f"{nc.get('dart', {}).get('dialogue', {}).get('score', 0)}/{nc.get('dart', {}).get('access', {}).get('score', 0)}/{nc.get('dart', {}).get('risk', {}).get('score', 0)}/{nc.get('dart', {}).get('transparency', {}).get('score', 0)}"
                        row_data["dart_scores"] = dart_scores
                        row_data["human_review"] = "⚠️ Sim" if nc.get("human_review_required", False) else "Não"
                    else:
                        row_data["game"] = post.get("game") or post.get("jogo", "N/A")
                        row_data["ai_type"] = "-"
                        row_data["interaction_type"] = "-"
                        row_data["value_type"] = "-"
                        row_data["dart_scores"] = "-/-/-/-"
                        row_data["human_review"] = "-"
                        
                    table_rows.append(row_data)
                except Exception as e:
                    logger.error(f"Failed thread summary execution for post {post.get('id')}: {e}")
                    
        # Ensure all summary cache updates are flushed to disk
        self._save_cache(force=True)

        # Sort rows to align with original posts order
        posts_id_order = [str(p.get("post_id") or p.get("id")) for p in posts]
        table_rows.sort(key=lambda x: posts_id_order.index(str(x["post_id"])) if str(x["post_id"]) in posts_id_order else 999999)
        
        # Write Markdown Table
        output_file = os.path.join(self.output_dir, "tabela_resumos.md")
        
        markdown_lines = [
            "# Tabela de Resumos Netnográficos e Codificação DART-NET\n",
            "Tabela de dados compilando os posts do corpus, classificações DART-NET (A1-A6, I1-I6, VC1-VC4, DART 0-5), sinalizações para revisão humana e links de acesso direto.\n",
            "| ID do Post | Jogo | Tipo IA | Interação | Valor | DART (D/A/R/T) | Rev. Humana | Resumo do Tema (Máx. 8 palavras) | Resumo do Post (Máx. 50 palavras) | Link Web Direto |",
            "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
        ]
        
        for row in table_rows:
            link_markdown = f"[Aceder ao Post]({row['url']})"
            markdown_lines.append(
                f"| `{row['post_id']}` | {row['game']} | `{row['ai_type']}` | `{row['interaction_type']}` | `{row['value_type']}` | `{row['dart_scores']}` | {row['human_review']} | {row['tema']} | {row['resumo']} | {link_markdown} |"
            )
            
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("\n".join(markdown_lines) + "\n")
            logger.info(f"SummaryTableGenerator complete. Markdown table saved to {output_file}.")
            return True
        except Exception as e:
            logger.error(f"Failed to write summary table file: {e}")
            return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generator = SummaryTableGenerator()
    generator.run()
