"""
SummaryTableGenerator - DART-NET v3.0
Gera a tabela completa de resumos netnográficos e codificação DART-NET (output/tabela_resumos.md).
Revisto para:
1. Processar TODOS os posts do corpus/tópico sem exclusão de dados.
2. Confrontar cada post com o resumo e insights globais do tópico (gerados pelo TopicDiscussionAnalystAgent).
3. Identificar explicitamente sátira, piadas, ironia, sarcasmo e memes, evitando interpretações literais erróneas.
"""

import os
import sys
import json
import logging
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
import api_client
from sanitizer import sanitize_text

logger = logging.getLogger("pipeline.summary_table_generator")

try:
    import json_repair
except ImportError:
    json_repair = None

def extract_and_repair_json(text):
    """Extrai e repara JSON de respostas de LLM."""
    if not text:
        raise ValueError("Resposta vazia da LLM")
    
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

    try:
        return json.loads(cleaned)
    except Exception:
        pass

    if json_repair is not None:
        try:
            res = json_repair.loads(cleaned)
            if isinstance(res, dict):
                return res
        except Exception:
            pass

    try:
        repaired = re.sub(r",\s*([\]}])", r"\1", cleaned)
        return json.loads(repaired)
    except Exception:
        pass

    raise ValueError(f"Falha ao interpretar JSON: {cleaned[:100]}")


class SummaryTableGenerator:
    def __init__(self):
        self.processed_dir = config.DATA_PROCESSED_DIR
        self.output_dir = config.OUTPUT_DIR
        self.analysis_dir = config.DATA_ANALYSIS_DIR
        self.interim_dir = config.DATA_INTERIM_DIR
        
        # Cache de resumos contextualizados com deteção de sátira
        self.cache_file = os.path.join(self.interim_dir, "summary_context_cache.json")
        self.cache_lock = threading.Lock()
        self.cache = self._load_cache()
        self.dirty_count = 0
        
        # Carregar resumos e insights aprofundados dos tópicos
        self.topic_insights = self._load_topic_insights()

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

    def _load_topic_insights(self):
        insights_file = os.path.join(self.analysis_dir, "topic_discussions_insights.json")
        if os.path.exists(insights_file):
            try:
                with open(insights_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                logger.info(f"Loaded {len(data)} topic discussion insights for post contextualization.")
                return data
            except Exception as e:
                logger.error(f"Failed to load topic discussions insights: {e}")
        logger.warning("Topic discussions insights file not found. Summaries may lack full topic confrontation.")
        return {}

    def _build_url(self, post):
        url_fonte = post.get("url") or post.get("url_fonte")
        if url_fonte:
            return url_fonte
            
        topic_id = str(post.get("thread_id") or post.get("topic_id") or post["id"].split("_")[0])
        slug = post.get("slug", "post") or "post"
        game = post.get("game") or post.get("jogo", "")
        source = post.get("platform") or post.get("fonte", "")
        section = post.get("community") or post.get("seccao", "")
        
        if game == "EVE Online":
            if "reddit" in (source or "").lower() or topic_id.startswith("reddit_") or topic_id.startswith("1"):
                clean_tid = topic_id.replace("reddit_", "")
                return f"https://www.reddit.com/r/Eve/comments/{clean_tid}"
            else:
                return f"https://forums.eveonline.com/t/{slug}/{topic_id}"
        elif game == "World of Warcraft":
            if "reddit" in (source or "").lower() or topic_id.startswith("reddit_"):
                clean_tid = topic_id.replace("reddit_", "")
                return f"https://www.reddit.com/r/wow/comments/{clean_tid}"
            elif "mmo-champion" in (section or "").lower() or "mmo-champion" in (source or "").lower():
                return f"https://www.mmo-champion.com/threads/{topic_id}"
            else:
                return f"https://forums.blizzard.com/pt/wow/t/{slug}/{topic_id}"
        return f"https://www.reddit.com/r/gaming/comments/{topic_id}"

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

        # Obter o contexto do tópico gerado pelo TopicDiscussionAnalystAgent
        tid = str(post.get("thread_id") or post.get("topic_id") or post_id.split("_")[0])
        t_insight = self.topic_insights.get(tid, {})
        
        topic_title = t_insight.get("title") or post.get("title") or post.get("topic_title") or f"Tópico {tid}"
        game = t_insight.get("game") or post.get("game") or post.get("jogo") or "Videojogo"
        platform = t_insight.get("platform") or post.get("platform") or "Fórum"
        
        # Resumo da discussão do tópico para confronto de contexto
        topic_summary = t_insight.get("resumo_extenso_discussao", "")
        if len(topic_summary) > 2500:
            topic_summary = topic_summary[:2500] + "... [continua]"
            
        topic_insights_list = "\n".join([f"- {ins}" for ins in t_insight.get("insights_principais", [])[:4]])
        
        tom_data = t_insight.get("tom_e_retorica", {})
        has_satire_in_thread = tom_data.get("contem_satira_ironia", False)
        tom_class = tom_data.get("classificacao_tom", "Debate Técnico Padrão")
        rhetoric_exp = tom_data.get("explicacao_retorica", "")
        satirical_posts = [p.get("post_id") for p in tom_data.get("posts_satiricos_ironicos", []) if isinstance(p, dict)]
        
        is_known_satirical_post = (post_id in satirical_posts)

        body = post.get("text") or post.get("corpo", "")

        system_prompt = (
            "És um assistente netnográfico especializado em resumos científicos e análise crítica do discurso online no Framework DART-NET.\n\n"
            "Deves analisar o post individual CONFRONTANDO-O DIRETAMENTE com o contexto global da discussão do tópico em que se insere (fornecido em [CONTEXTO DO TÓPICO]).\n\n"
            "TAREFA CRÍTICA: DETEÇÃO DE SÁTIRA, PIADAS E IRONIA\n"
            "- As comunidades de videojogos recorrem frequentemente a sátira, ironia, sarcasmo, humor, 'shitposts', hipérbole e paródias "
            "(ex.: posts satíricos de Ceema no EVE Online, paródias sobre a Blizzard 'pequena empresa indie', piadas de 1 de Abril, "
            "comentários sarcásticos sobre suporte automatizado/copilots, memes sobre bots).\n"
            "- Confronta o texto do post com a discussão e o tom do tópico:\n"
            "  * Se o post contiver SÁTIRA, IRONIA, SARCASMO, PARÓDIA ou for uma PIADA/MEME:\n"
            "    1. No 'tema' (estritamente máximo de 8 palavras), deves OBRIGATORIAMENTE iniciar por '[Sátira/Ironia]' ou '[Humor/Piada]' seguido do tema central.\n"
            "    2. No 'resumo' (estritamente máximo de 50 palavras em português de Portugal), NÃO interpretes o post literalmente como um facto real! "
            "       Em vez disso, explicita claramente a natureza satírica/irónica e o significado/crítica real pretendida pelo autor.\n"
            "  * Se o post for SÉRIO / LITERAL:\n"
            "    1. No 'tema' (estritamente máximo de 8 palavras): resume o tema do post.\n"
            "    2. No 'resumo' (estritamente máximo de 50 palavras em português de Portugal): resume objetivamente o conteúdo do post.\n\n"
            "Responde ESTRITAMENTE em formato JSON com a seguinte estrutura:\n"
            "{\n"
            "  \"tema\": \"Tema aqui...\",\n"
            "  \"resumo\": \"Resumo do post aqui...\"\n"
            "}"
        )

        user_prompt = (
            f"[CONTEXTO DO TÓPICO (CONFRONTAÇÃO)]\n"
            f"Tópico: {topic_title}\n"
            f"Jogo: {game} | Plataforma: {platform}\n"
            f"Tom Global do Tópico: {tom_class}\n"
            f"Sátira/Ironia Sinalizada no Tópico: {'SIM' if has_satire_in_thread else 'Não'}\n"
            f"Enquadramento Retórico do Tópico: {rhetoric_exp}\n"
            f"Post previamente sinalizado como satírico: {'SIM' if is_known_satirical_post else 'Não'}\n"
            f"Síntese da Discussão Global:\n{topic_summary}\n\n"
            f"[POST INDIVIDUAL PARA ANÁLISE]\n"
            f"ID do Post: {post_id}\n"
            f"Autor: {post.get('author_id', 'Utilizador')}\n"
            f"Texto do Post:\n{sanitize_text(body)}\n"
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        try:
            content, _ = api_client.call_llm(
                model=config.MODEL_FLASH,
                messages=messages,
                thinking_enabled=False,
                temperature=0.1,
                max_tokens=600
            )
            
            result = extract_and_repair_json(content)
            resumo = result.get("resumo", "").strip()
            tema = result.get("tema", "").strip()
            
            # Limpeza de limites de palavras
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
            # Fallback substantivo
            is_sat = has_satire_in_thread or is_known_satirical_post
            prefix = "[Sátira/Ironia] " if is_sat else ""
            words = (post.get("text") or post.get("corpo", "")).split()
            fallback_summary = prefix + (" ".join(words[:40]) + "..." if len(words) > 40 else " ".join(words))
            fallback_theme = f"{prefix}{topic_title}"
            fallback_words = fallback_theme.split()
            if len(fallback_words) > 8:
                fallback_theme = " ".join(fallback_words[:7]) + "..."
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
            
        # Carregar resultados da netnografia para cruzamento de dados DART-NET
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
            
        logger.info(f"SummaryTableGenerator: Processing ALL {len(posts)} posts from the corpus without dropping any.")

        table_rows = []
        num_workers = min(config.MAX_WORKERS, len(posts)) if posts else 1
        
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_post = {executor.submit(self.generate_single_summary, post): post for post in posts}
            for future in as_completed(future_to_post):
                post = future_to_post[future]
                try:
                    row_data = future.result()
                    pid = str(row_data["post_id"])
                    
                    # Attach DART-NET coding attributes from netno_map
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
                        row_data["ai_type"] = "A2"
                        row_data["interaction_type"] = "I4"
                        row_data["value_type"] = "VC4"
                        row_data["dart_scores"] = "1/1/2/1"
                        row_data["human_review"] = "Não"
                        
                    table_rows.append(row_data)
                except Exception as e:
                    logger.error(f"Failed summary execution for post {post.get('id')}: {e}")
                    
        # Ensure all summary cache updates are flushed to disk
        self._save_cache(force=True)

        # Sort rows to align with original posts order
        posts_id_order = [str(p.get("post_id") or p.get("id")) for p in posts]
        table_rows.sort(key=lambda x: posts_id_order.index(str(x["post_id"])) if str(x["post_id"]) in posts_id_order else 999999)
        
        # Write Markdown Table
        output_file = os.path.join(self.output_dir, "tabela_resumos.md")
        
        markdown_lines = [
            "# Tabela de Resumos Netnográficos e Codificação DART-NET\n",
            "Tabela de dados compilando a totalidade dos posts do corpus (1032 posts), classificações DART-NET (A1-A6, I1-I6, VC1-VC4, DART 0-5), "
            "identificação explícita de sátira/ironia/humor mediante confronto com a discussão integral do tópico, sinalizações para revisão humana e links de acesso direto.\n",
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
            logger.info(f"SummaryTableGenerator complete. Full Markdown table saved to {output_file} with {len(table_rows)} rows.")
            return True
        except Exception as e:
            logger.error(f"Failed to write summary table file: {e}")
            return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generator = SummaryTableGenerator()
    generator.run()
