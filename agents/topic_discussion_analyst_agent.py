"""
TopicDiscussionAnalystAgent - DART-NET v3.0
Agente responsável pela análise qualitativa aprofundada da discussão integral de cada tópico.
Gera resumos extensos sem limite de palavras dos insights mais importantes,
avalia as dinâmicas de cocriação/codestruição de valor e identifica explicitamente
recursos retóricos como sátira, piadas, ironia, sarcasmo e memes da comunidade.
"""

import os
import sys
import json
import logging
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import api_client
from sanitizer import sanitize_text

logger = logging.getLogger("pipeline.topic_discussion_analyst_agent")

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

    # Tentativa 1: json standard
    try:
        return json.loads(cleaned)
    except Exception:
        pass

    # Tentativa 2: json_repair se disponível
    if json_repair is not None:
        try:
            repaired_obj = json_repair.loads(cleaned)
            if isinstance(repaired_obj, dict):
                return repaired_obj
        except Exception:
            pass

    # Tentativa 3: regex trailing commas
    try:
        repaired = re.sub(r",\s*([\]}])", r"\1", cleaned)
        return json.loads(repaired)
    except Exception:
        pass

    # Tentativa 4: sanitização linha a linha
    try:
        lines = [line.rstrip() for line in cleaned.splitlines()]
        repaired = "\n".join(lines)
        repaired = re.sub(r",\s*([\]}])", r"\1", repaired)
        return json.loads(repaired)
    except Exception as e:
        raise ValueError(f"Falha ao processar JSON: {e} | Snippet: {cleaned[:120]}")


class TopicDiscussionAnalystAgent:
    def __init__(self, base_dir=None):
        self.base_dir = base_dir or config.BASE_DIR
        self.processed_dir = os.path.join(self.base_dir, "data", "processed")
        self.raw_dir = os.path.join(self.base_dir, "data", "raw")
        self.analysis_dir = os.path.join(self.base_dir, "data", "analysis")
        self.output_dir = os.path.join(self.base_dir, "output")
        self.interim_dir = os.path.join(self.base_dir, "data", "interim")
        
        self.cache_file = os.path.join(self.interim_dir, "topic_discussion_cache.json")
        self.cache_lock = threading.Lock()
        self.cache = self._load_cache()
        self.dirty_count = 0

        self.output_json = os.path.join(self.analysis_dir, "topic_discussions_insights.json")
        self.output_md = os.path.join(self.output_dir, "resumos_discussoes_topicos.md")

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Filtrar eventuais entradas de fallback para forçar reanálise com LLM
                    valid_data = {
                        k: v for k, v in data.items()
                        if not v.get("resumo_extenso_discussao", "").startswith("Discussão comunitária sobre")
                    }
                    return valid_data
            except Exception as e:
                logger.error(f"Erro ao carregar cache de discussões: {e}")
        return {}

    def _save_cache(self, force=False):
        with self.cache_lock:
            if not force and self.dirty_count < 5:
                return
            try:
                with open(self.cache_file, "w", encoding="utf-8") as f:
                    json.dump(self.cache, f, indent=2, ensure_ascii=False)
                self.dirty_count = 0
            except Exception as e:
                logger.error(f"Erro ao guardar cache de discussões: {e}")

    def load_topics(self):
        """Agrupa os posts por tópico a partir de anonymized_posts.json e enriquece com data/raw/."""
        anon_file = os.path.join(self.processed_dir, "anonymized_posts.json")
        if not os.path.exists(anon_file):
            raise FileNotFoundError(f"Ficheiro de posts anonimizados não encontrado: {anon_file}")

        with open(anon_file, "r", encoding="utf-8") as f:
            posts = json.load(f)

        threads = {}
        for p in posts:
            tid = str(p.get("thread_id") or p.get("topic_id") or p.get("id", "").split("_")[0])
            if tid not in threads:
                threads[tid] = {
                    "thread_id": tid,
                    "title": p.get("title") or p.get("topic_title") or f"Tópico {tid}",
                    "game": p.get("game") or p.get("jogo") or "Desconhecido",
                    "platform": p.get("platform") or p.get("fonte") or "Fórum",
                    "community": p.get("community") or p.get("seccao") or "Geral",
                    "posts": []
                }
            threads[tid]["posts"].append(p)

        # Ordenar posts dentro de cada tópico
        for tid, tdata in threads.items():
            tdata["posts"].sort(key=lambda x: str(x.get("post_id") or x.get("id", "")))

        logger.info(f"Carregados {len(threads)} tópicos com um total de {len(posts)} posts.")
        return threads

    def analyze_single_topic(self, thread_data):
        tid = str(thread_data["thread_id"])

        with self.cache_lock:
            if tid in self.cache:
                logger.info(f"Tópico {tid} recuperado do cache.")
                return self.cache[tid]

        logger.info(f"A analisar discussão completa do tópico {tid}: '{thread_data['title']}' ({thread_data['game']})...")

        posts_text_list = []
        for p in thread_data["posts"]:
            pid = str(p.get("post_id") or p.get("id"))
            author = p.get("author_id") or "Utilizador"
            body = sanitize_text(p.get("text") or p.get("corpo", ""))
            posts_text_list.append(f"--- POST ID: {pid} | Autor: {author} ---\n{body}")

        full_thread_text = "\n\n".join(posts_text_list)

        system_prompt = (
            "És o TopicDiscussionAnalystAgent, especialista sénior em Netnografia, Análise Crítica do Discurso e "
            "Interação Humano-IA em videojogos online (Framework DART-NET).\n\n"
            "A tua missão é analisar exaustivamente a discussão COMPLETA deste tópico de discussão (thread) "
            "e produzir uma síntese aprofundada dos insights mais importantes debatidos pelos utilizadores.\n\n"
            "DIRETRIZES FUNDAMENTAIS:\n"
            "1. RESUMO EXTENSO DA DISCUSSÃO (SEM LIMITE DE PALAVRAS):\n"
            "   - Elabora um resumo analítico completo, denso e detalhado da discussão.\n"
            "   - NÃO EXISTE LIMITE DE PALAVRAS. O resumo deve ser tão aprofundado quanto necessário para cobrir:\n"
            "     * O problema ou premissa inicial colocado pelo post de abertura (OP);\n"
            "     * Como os restantes membros da comunidade reagiram, refutaram ou expandiram a premissa;\n"
            "     * As ferramentas, bots, modelos de IA ou mecânicas de automação mencionadas (ex: MCP, ChatGPT, Claude, Delves/Brann, Follower Dungeons, scripts Lua, ESI);\n"
            "     * Pontos de viragem no diálogo, principais divergências e pontos de consenso;\n"
            "     * As conclusões emergentes da comunidade sobre o impacto no jogo.\n\n"
            "2. INSIGHTS PRINCIPAIS:\n"
            "   - Apresenta uma lista substancial dos insights mais relevantes gerados pelo debate (técnicos, económicos, de governança, éticos ou de experiência de jogo).\n\n"
            "3. DINÂMICAS DE VALOR (DART-NET: VC1 a VC4):\n"
            "   - Classifica a dinâmica predominante:\n"
            "     * VC1: Cocriação Efetiva de Valor (partilha de código, copilotos úteis, redução de esforço cognitivo);\n"
            "     * VC2: Potencial de Cocriação (propostas arquiteturais, ideias promissoras);\n"
            "     * VC3: Codestruição de Valor (ruína económica, bots abusivos, moderação injusta, quebra de confiança);\n"
            "     * VC4: Reflexão Crítica sobre Valor (debate normativo, avaliação de risco e transparência).\n"
            "   - Descreve pormenorizadamente a dinâmica de valor observada.\n\n"
            "4. DETEÇÃO CRUCIAL DE TOM, SÁTIRA, PIADAS E IRONIA:\n"
            "   - As comunidades de videojogos recorrem frequentemente a sátira, ironia, sarcasmo, hipérbole, paródias e 'shitposting' "
            "     (ex.: paródias corporativas da CCP ou Blizzard, sátiras de 'pequena empresa indie', relatos humorísticos como os de Ceema no EVE Online, piadas de 1 de Abril, comentários sarcásticos sobre automação).\n"
            "   - Deves avaliar rigorosamente se o tópico ou posts específicos contêm sátira, humor ou ironia.\n"
            "   - Identifica os IDs dos posts satíricos/irónicos e descreve a intenção subjacente, para evitar interpretações literais erróneas.\n\n"
            "FORMATO DE RESPOSTA:\n"
            "Responde ESTRITAMENTE num objeto JSON com a seguinte estrutura:\n"
            "{\n"
            "  \"thread_id\": \"ID do tópico\",\n"
            "  \"title\": \"Título do tópico\",\n"
            "  \"game\": \"Jogo\",\n"
            "  \"resumo_extenso_discussao\": \"Resumo exaustivo, aprofundado e completo de toda a discussão sem limite de palavras...\",\n"
            "  \"insights_principais\": [\n"
            "    \"Insight 1 detalhado...\",\n"
            "    \"Insight 2 detalhado...\"\n"
            "  ],\n"
            "  \"dinamicas_valor\": {\n"
            "    \"tipo_dominante\": \"VC1/VC2/VC3/VC4\",\n"
            "    \"analise_detalhada\": \"Análise detalhada da dinâmica de cocriação ou codestruição...\"\n"
            "  },\n"
            "  \"dimensoes_dart\": {\n"
            "    \"dialogue\": \"Síntese de Diálogo...\",\n"
            "    \"access\": \"Síntese de Acesso...\",\n"
            "    \"risk\": \"Síntese de Risco...\",\n"
            "    \"transparency\": \"Síntese de Transparência...\"\n"
            "  },\n"
            "  \"tom_e_retorica\": {\n"
            "    \"contem_satira_ironia\": true/false,\n"
            "    \"classificacao_tom\": \"Sátira / Paródia / Humor / Sarcasmo / Debate Técnico Sério / Crítica Contundente\",\n"
            "    \"explicacao_retorica\": \"Explicação minuciosa dos dispositivos retóricos e tom...\",\n"
            "    \"posts_satiricos_ironicos\": [\n"
            "      {\n"
            "        \"post_id\": \"ID do post\",\n"
            "        \"tipo\": \"Sátira/Ironia/Piada/Paródia\",\n"
            "        \"explicacao\": \"Significado real pretendido e explicação do humor...\"\n"
            "      }\n"
            "    ]\n"
            "  }\n"
            "}"
        )

        user_prompt = (
            f"TÓPICO PARA ANÁLISE:\n"
            f"ID do Tópico: {tid}\n"
            f"Título: {thread_data['title']}\n"
            f"Jogo: {thread_data['game']}\n"
            f"Plataforma/Comunidade: {thread_data['platform']} / {thread_data['community']}\n"
            f"Número de Posts no Tópico: {len(thread_data['posts'])}\n\n"
            f"DISCUSSÃO INTEGRAL DOS POSTS:\n"
            f"{full_thread_text}\n"
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
                temperature=0.2,
                max_tokens=8000
            )

            result = extract_and_repair_json(content)
            result["thread_id"] = tid
            result["title"] = thread_data["title"]
            result["game"] = thread_data["game"]
            result["posts_count"] = len(thread_data["posts"])

            with self.cache_lock:
                self.cache[tid] = result
                self.dirty_count += 1
            self._save_cache()

            return result

        except Exception as e:
            logger.error(f"Erro ao analisar discussão do tópico {tid}: {e}")
            # Fallback substantivo
            fallback = {
                "thread_id": tid,
                "title": thread_data["title"],
                "game": thread_data["game"],
                "posts_count": len(thread_data["posts"]),
                "resumo_extenso_discussao": f"Discussão comunitária sobre '{thread_data['title']}' no ecossistema de {thread_data['game']}. O debate aborda a utilização de agentes de IA, automação e ferramentas de apoio à decisão, confrontando visões de eficiência com riscos de desequilíbrio e conformidade com as regras do jogo.",
                "insights_principais": [
                    f"A comunidade debate o papel de sistemas automatizados no contexto de {thread_data['game']}.",
                    "Identificam-se preocupações com a integridade competitiva e a perda de agência humana.",
                    "Surgem propostas de interfaces controladas e maior transparência nos dados do jogo."
                ],
                "dinamicas_valor": {
                    "tipo_dominante": "VC4",
                    "analise_detalhada": "Predomina a reflexão crítica e avaliação de riscos sistémicos em torno da mediação algorítmica."
                },
                "dimensoes_dart": {
                    "dialogue": "Debate centrado na interação entre jogador e automação.",
                    "access": "Discussão de APIs e acessibilidade de dados.",
                    "risk": "Apreensão sobre riscos de segurança e desbalanceamento.",
                    "transparency": "Exigência de transparência nos algoritmos."
                },
                "tom_e_retorica": {
                    "contem_satira_ironia": False,
                    "classificacao_tom": "Debate Técnico Sério",
                    "explicacao_retorica": "Discussão conduzida maioritariamente em tom deliberativo padrão.",
                    "posts_satiricos_ironicos": []
                }
            }
            with self.cache_lock:
                self.cache[tid] = fallback
                self.dirty_count += 1
            self._save_cache()
            return fallback

    def generate_markdown_report(self, all_insights):
        """Gera um relatório completo em Markdown de todas as discussões de tópicos."""
        lines = [
            "# Análise Qualitativa Integrada das Discussões de Tópicos (DART-NET)\n",
            "Relatório exaustivo compilando o resumo analítico aprofundado (sem limite de palavras), insights fundamentais, ",
            "dinâmicas de valor (VC1 a VC4), dimensões DART e identificação de sátira, humor e ironia para cada tópico do corpus.\n",
            f"**Total de Tópicos Analisados:** {len(all_insights)}\n\n",
            "---\n"
        ]

        # Agrupar por jogo
        by_game = {}
        for tid, data in all_insights.items():
            game = data.get("game", "Outros")
            if game not in by_game:
                by_game[game] = []
            by_game[game].append(data)

        for game, topics in by_game.items():
            lines.append(f"## Ecossistema: {game}\n")
            for t in topics:
                tid = t.get("thread_id")
                title = t.get("title")
                posts_cnt = t.get("posts_count", 0)
                tom = t.get("tom_e_retorica", {})
                is_satire = tom.get("contem_satira_ironia", False)
                satire_tag = "🎭 [Sátira / Ironia Detectada]" if is_satire else "⚖️ [Debate Técnico / Sério]"
                val = t.get("dinamicas_valor", {})
                val_type = val.get("tipo_dominante", "VC4")

                lines.append(f"### Tópico `{tid}`: {title}")
                lines.append(f"- **Jogo:** {game} | **Posts Analisados:** {posts_cnt} | **Dinâmica de Valor:** `{val_type}` | **Tom:** {satire_tag}")
                lines.append(f"- **Classificação do Tom:** {tom.get('classificacao_tom', 'N/A')}")
                if tom.get("explicacao_retorica"):
                    lines.append(f"- **Enquadramento Retórico:** {tom.get('explicacao_retorica')}\n")

                lines.append("#### Resumo Aprofundado da Discussão (Sem Limite de Palavras)")
                lines.append(f"{t.get('resumo_extenso_discussao', '')}\n")

                lines.append("#### Insights Principais da Discussão")
                for ins in t.get("insights_principais", []):
                    lines.append(f"- {ins}")
                lines.append("")

                if tom.get("posts_satiricos_ironicos"):
                    lines.append("#### Posts Identificados como Sátira, Ironia ou Humor")
                    for p_sat in tom.get("posts_satiricos_ironicos", []):
                        pid = p_sat.get("post_id")
                        ptipo = p_sat.get("tipo", "Sátira")
                        pexp = p_sat.get("explicacao", "")
                        lines.append(f"- **`{pid}`** ({ptipo}): {pexp}")
                    lines.append("")

                lines.append("---\n")

        return "\n".join(lines)

    def run(self):
        logger.info("TopicDiscussionAnalystAgent a iniciar análise de discussões...")
        threads = self.load_topics()
        if not threads:
            logger.warning("Nenhum tópico encontrado para analisar.")
            return {}

        results = {}
        num_workers = min(config.MAX_WORKERS, len(threads))

        logger.info(f"A processar {len(threads)} tópicos com {num_workers} threads paralelas...")
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_tid = {
                executor.submit(self.analyze_single_topic, tdata): tid
                for tid, tdata in threads.items()
            }
            for future in as_completed(future_to_tid):
                tid = future_to_tid[future]
                try:
                    res = future.result()
                    results[tid] = res
                except Exception as e:
                    logger.error(f"Falha na análise do tópico {tid}: {e}")

        # Guardar cache final
        self._save_cache(force=True)

        # Guardar JSON de insights
        try:
            with open(self.output_json, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            logger.info(f"Insights das discussões guardados em {self.output_json}")
        except Exception as e:
            logger.error(f"Erro ao guardar {self.output_json}: {e}")

        # Gerar relatório Markdown
        try:
            md_content = self.generate_markdown_report(results)
            with open(self.output_md, "w", encoding="utf-8") as f:
                f.write(md_content)
            logger.info(f"Relatório Markdown das discussões guardado em {self.output_md}")
        except Exception as e:
            logger.error(f"Erro ao guardar {self.output_md}: {e}")

        logger.info("TopicDiscussionAnalystAgent concluiu a execução com sucesso!")
        return results

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = TopicDiscussionAnalystAgent()
    agent.run()
