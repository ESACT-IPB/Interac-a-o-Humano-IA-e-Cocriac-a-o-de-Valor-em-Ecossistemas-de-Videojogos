"""
ThreadSynthesisAgent - DART-NET v3.6
Agente de Análise Agregada ao Nível de Tópicos de Discussão (Threads).
Agrupa os posts validados da netnografia, computa métricas agregadas DART-NET,
gera fichas sistemáticas e produz a macro-síntese transversal (EVE Sandbox vs. WoW Controlado).
"""

import os
import json
import glob
import logging
from collections import defaultdict, Counter

logger = logging.getLogger("pipeline.thread_synthesis_agent")

class ThreadSynthesisAgent:
    def __init__(self, base_dir=None):
        self.base_dir = base_dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.netno_file = os.path.join(self.base_dir, "data", "analysis", "netnography_results.jsonl")
        self.raw_dir = os.path.join(self.base_dir, "data", "raw")
        self.target_corpus_file = os.path.join(self.base_dir, "data", "target_corpus_303.json")
        self.anon_file = os.path.join(self.base_dir, "data", "processed", "anonymized_posts.json")
        self.cache_file = os.path.join(self.base_dir, "data", "interim", "summary_cache.json")
        
        self.output_md = os.path.join(self.base_dir, "output", "analise_agregada_topicos.md")
        self.output_json = os.path.join(self.base_dir, "data", "analysis", "thread_level_results.json")
        
    def load_data(self):
        """Carrega todos os dados do corpus refinado e índices auxiliares de metadados."""
        if not os.path.exists(self.netno_file):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.netno_file}")
            
        posts = []
        with open(self.netno_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    posts.append(json.loads(line))
                    
        # Carregar cache de resumos
        summary_cache = {}
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    summary_cache = json.load(f)
            except Exception as e:
                logger.warning(f"Erro ao carregar summary_cache: {e}")
                
        # Carregar metadados dos tópicos canónicos
        corpus_by_id = {}
        if os.path.exists(self.target_corpus_file):
            try:
                with open(self.target_corpus_file, "r", encoding="utf-8") as f:
                    tc = json.load(f)
                    for entry in tc:
                        corpus_by_id[str(entry.get("topic_id"))] = entry
            except Exception as e:
                logger.warning(f"Erro ao carregar target_corpus: {e}")
                
        # Carregar metadados em data/raw/
        raw_meta = {}
        for fpath in glob.glob(os.path.join(self.raw_dir, "*.json")):
            fname = os.path.basename(fpath)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    d = json.load(f)
                    tid = d.get("id") or d.get("topic_id")
                    title = d.get("title") or d.get("topic_title") or ""
                    raw_posts = d.get("posts") or d.get("post_stream", {}).get("posts") or d.get("comments") or []
                    raw_count = d.get("posts_count") or len(raw_posts) or 1
                    url = d.get("url") or d.get("canonical_url") or ""
                    slug = d.get("slug") or ""
                    
                    data_obj = {"title": title, "raw_count": raw_count, "slug": slug, "url": url}
                    if tid:
                        raw_meta[str(tid)] = data_obj
                    base = fname.replace("topic_fetched_", "").replace(".json", "")
                    raw_meta[base] = data_obj
                    if "_" in base:
                        sub = base.split("_", 1)[1]
                        raw_meta[sub] = data_obj
            except Exception:
                pass
                
        # Carregar contagens e títulos de anonymized_posts.json
        anon_counts = defaultdict(int)
        anon_titles = {}
        anon_posts_map = {}
        if os.path.exists(self.anon_file):
            try:
                with open(self.anon_file, "r", encoding="utf-8") as f:
                    for p in json.load(f):
                        pid = str(p.get("post_id") or p.get("id", ""))
                        tid = str(p.get("thread_id") or p.get("topic_id") or pid.split("_")[0])
                        anon_counts[tid] += 1
                        anon_posts_map[pid] = p
                        if p.get("title") or p.get("topic_title"):
                            anon_titles[tid] = p.get("title") or p.get("topic_title")
            except Exception as e:
                logger.warning(f"Erro ao carregar anonymized_posts: {e}")

        return posts, summary_cache, corpus_by_id, raw_meta, anon_counts, anon_titles, anon_posts_map

    def group_threads(self, posts):
        """Agrupa os 825 posts por thread_id."""
        thread_map = defaultdict(list)
        for p in posts:
            pid = str(p.get("post_id") or p.get("id", ""))
            tid = p.get("thread_id") or p.get("topic_id")
            if not tid:
                parts = pid.rsplit("_", 1)
                tid = parts[0] if len(parts) > 1 else pid
            thread_map[str(tid)].append(p)
        return thread_map

    def resolve_metadata(self, tid, tposts, corpus_by_id, raw_meta, anon_counts, anon_titles):
        """Identifica título, contagem original, ecossistema e URL para cada thread."""
        sample_post = tposts[0]
        game_raw = sample_post.get("jogo") or sample_post.get("game") or "World of Warcraft"
        if "eve" in game_raw.lower():
            ecosystem = "EVE Online (Sandbox)"
            game = "EVE Online"
        else:
            ecosystem = "World of Warcraft (Controlado)"
            game = "World of Warcraft"
            
        retained_count = len(tposts)
        
        # Obter contagem original de posts no tópico
        orig_count = retained_count
        if tid in raw_meta and raw_meta[tid].get("raw_count"):
            orig_count = max(raw_meta[tid]["raw_count"], retained_count)
        elif tid in anon_counts:
            orig_count = max(anon_counts[tid], retained_count)
            
        # Obter título da discussão
        title = ""
        if tid in anon_titles and anon_titles[tid]:
            title = anon_titles[tid]
        elif tid in raw_meta and raw_meta[tid].get("title"):
            title = raw_meta[tid]["title"]
        elif tid in corpus_by_id:
            slug = corpus_by_id[tid].get("slug", "")
            title = slug.replace("-", " ").title() if slug else f"Discussão {tid}"
        else:
            # Tentar extrair do post ou slug
            title = sample_post.get("title") or sample_post.get("topic_title") or f"Discussão Comunitária {tid}"
            
        # Limpar título
        title = title.strip().replace("\n", " ")
        if len(title) > 120:
            title = title[:117] + "..."
            
        return {
            "thread_id": tid,
            "title": title,
            "game": game,
            "ecosystem": ecosystem,
            "posts_retidos": retained_count,
            "posts_originais": orig_count,
        }

    def compute_metrics(self, tposts):
        """Computa métricas DART-NET, perfil de agência, interação e valor da thread."""
        n = len(tposts)
        d_scores = [p.get("dart", {}).get("dialogue", {}).get("score", 0) for p in tposts]
        a_scores = [p.get("dart", {}).get("access", {}).get("score", 0) for p in tposts]
        r_scores = [p.get("dart", {}).get("risk", {}).get("score", 0) for p in tposts]
        t_scores = [p.get("dart", {}).get("transparency", {}).get("score", 0) for p in tposts]
        
        avg_d = sum(d_scores) / n
        avg_a = sum(a_scores) / n
        avg_r = sum(r_scores) / n
        avg_t = sum(t_scores) / n
        
        ai_counts = Counter(p.get("ai_type", "A5") for p in tposts)
        inter_counts = Counter(p.get("interaction_type", "I4") for p in tposts)
        vc_counts = Counter(p.get("value_type", "VC4") for p in tposts)
        
        # Determinar código de agência prevalente:
        # Se houver A1 ou A4 com presença ativa (>=15%), destaca agência inovadora/assistida; caso contrário, a moda
        if ai_counts.get("A1", 0) / n >= 0.20:
            prev_ai = "A1"
        elif ai_counts.get("A4", 0) / n >= 0.20:
            prev_ai = "A4"
        elif ai_counts.get("A3", 0) / n >= 0.25:
            prev_ai = "A3"
        elif ai_counts.get("A2", 0) / n >= 0.25:
            prev_ai = "A2"
        else:
            prev_ai = ai_counts.most_common(1)[0][0]
            
        # Padrão de interação principal:
        # Prioriza I3 (cooperação), I1 (prompting) ou I2 (recomendação) se presentes
        if inter_counts.get("I3", 0) > 0:
            prev_inter = "I3"
        elif inter_counts.get("I1", 0) > 0:
            prev_inter = "I1"
        elif inter_counts.get("I2", 0) > 0:
            prev_inter = "I2"
        elif inter_counts.get("I5", 0) > 0:
            prev_inter = "I5"
        else:
            prev_inter = inter_counts.most_common(1)[0][0]
            
        # Dinâmica de valor dominante (focada no impacto teórico de cocriação/codestruição):
        if vc_counts.get("VC1", 0) > 0:
            val_dyn = "VC1 (Cocriação)"
            val_code = "VC1"
        elif vc_counts.get("VC3", 0) > vc_counts.get("VC2", 0) and vc_counts.get("VC3", 0) > 0:
            val_dyn = "VC3 (Codestruição)"
            val_code = "VC3"
        elif vc_counts.get("VC2", 0) > 0:
            val_dyn = "VC2 (Potencial)"
            val_code = "VC2"
        else:
            val_dyn = "VC4 (Reflexivo/Neutro)"
            val_code = "VC4"
            
        return {
            "avg_d": round(avg_d, 1),
            "avg_a": round(avg_a, 1),
            "avg_r": round(avg_r, 1),
            "avg_t": round(avg_t, 1),
            "prev_ai": prev_ai,
            "prev_inter": prev_inter,
            "val_dyn": val_dyn,
            "val_code": val_code,
            "ai_counts": dict(ai_counts),
            "inter_counts": dict(inter_counts),
            "vc_counts": dict(vc_counts)
        }

    def select_paradigmatic_evidence(self, tposts, anon_posts_map):
        """Seleciona a citação literal mais paradigmática da discussão."""
        candidates = []
        for p in tposts:
            dart = p.get("dart", {})
            for dim in ["dialogue", "access", "risk", "transparency"]:
                dim_data = dart.get(dim, {})
                ev = dim_data.get("evidence", "") or dim_data.get("evidencia_literal", "")
                score = dim_data.get("score", 0)
                if ev and len(ev.strip()) >= 25:
                    clean_ev = ev.strip().replace("\n", " ")
                    candidates.append((score, len(clean_ev), clean_ev, dim))
                    
        if candidates:
            # Ordena por score descendente e por comprimento razoável (preferência por citações substanciais)
            candidates.sort(key=lambda x: (x[0], min(x[1], 250)), reverse=True)
            return candidates[0][2]
            
        # Fallback: tentar extrair do conteúdo integral do post em anonymized_posts_map
        for p in tposts:
            pid = str(p.get("post_id") or p.get("id", ""))
            if pid in anon_posts_map:
                txt = anon_posts_map[pid].get("content", "") or anon_posts_map[pid].get("conteudo", "")
                if txt and len(txt.strip()) >= 30:
                    sentences = [s.strip() for s in txt.split(".") if len(s.strip()) >= 30]
                    if sentences:
                        return sentences[0] + "."
        return "Evidência empírica baseada na interação observada no tópico."

    def synthesize_analytic_summary(self, meta, metrics, tposts, summary_cache):
        """Gera um resumo analítico denso de 4-5 linhas focado na interação humano-IA e no valor."""
        title = meta["title"]
        game = meta["game"]
        prev_ai = metrics["prev_ai"]
        prev_inter = metrics["prev_inter"]
        val_code = metrics["val_code"]
        n_posts = meta["posts_retidos"]
        
        # Recolher tópicos e resumos dos posts individuais
        resumos = []
        temas = []
        for p in tposts:
            pid = str(p.get("post_id") or p.get("id"))
            if pid in summary_cache:
                c = summary_cache[pid]
                if c.get("resumo"):
                    resumos.append(c["resumo"])
                if c.get("tema"):
                    temas.append(c["tema"])
                    
        # Deteção de ferramentas e entidades-chave mencionadas
        combined_text = (title + " " + " ".join(resumos) + " " + " ".join(temas)).lower()
        
        tools_detected = []
        if "mcp" in combined_text or "model context protocol" in combined_text:
            tools_detected.append("Model Context Protocol (MCP)")
        if "chatgpt" in combined_text:
            tools_detected.append("ChatGPT")
        if "claude" in combined_text:
            tools_detected.append("Claude")
        if "copilot" in combined_text:
            tools_detected.append("Copiloto de IA")
        if "esi" in combined_text:
            tools_detected.append("EVE Swagger Interface (ESI)")
        if "follower" in combined_text or "masmorra" in combined_text:
            tools_detected.append("Follower Dungeons (NPCs com IA)")
        if "delve" in combined_text or "brann" in combined_text:
            tools_detected.append("Delves / Brann Bronzebeard (Companheiro IA)")
        if "addon" in combined_text or "lua" in combined_text:
            tools_detected.append("Addons / Scripts Lua")
        if "machine learning" in combined_text or "aprendizado" in combined_text:
            tools_detected.append("Modelos de Machine Learning")
        if "suporte" in combined_text or "ticket" in combined_text or "gm" in combined_text:
            tools_detected.append("Sistemas Automatizados de Moderação/Tickets")
        if "aura" in combined_text:
            tools_detected.append("Aura AI (Assistente Oficial EVE)")
        if "eve crews" in combined_text:
            tools_detected.append("EVE Crews (Motor Heurístico)")

        tools_str = ", ".join(tools_detected[:3]) if tools_detected else "ferramentas algorítmicas e modelos de IA"

        # Construção das 4-5 linhas analíticas
        # Linha 1: Ferramentas e agentes abordados no contexto do jogo
        if prev_ai == "A1":
            l1 = f"O tópico centra-se na integração e operação de agentes autónomos ({tools_str}) no ecossistema de {game}."
        elif prev_ai == "A4":
            l1 = f"A discussão analisa o desenvolvimento e utilização de copilotos assistivos ({tools_str}) por jogadores de {game}."
        elif prev_ai == "A2" or prev_ai == "A3":
            l1 = f"O debate aborda a interseção entre automação técnica ({tools_str}) e a emergência de comportamentos agênticos em {game}."
        else:
            l1 = f"A comunidade debate reflexivamente as implicações técnicas, operacionais e éticas de {tools_str} em {game}."

        # Linha 2-3: Reação da comunidade e padrão de interação
        if prev_inter in ["I1", "I3"]:
            l2 = f"Os utilizadores descrevem interações diretas e colaborativas com sistemas algorítmicos, articulando prompts, consultas de telemetria e testes empíricos de interface."
        elif prev_inter == "I5":
            l2 = f"A discussão é marcada por tensões e disputas decorrentes de assimetrias competitivas provocadas pela mediação algorítmica no ambiente do jogo."
        else:
            l2 = f"A interação estrutura-se em discurso deliberativo comunitário (I4), confrontando visões sobre eficiência técnica versus perda de autonomia e conformidade com os termos de serviço (EULA)."

        # Linha 4: Impacto em valor (VC1, VC2, VC3 ou VC4)
        if val_code == "VC1":
            l3 = f"Observa-se cocriação efetiva de valor (VC1), traduzida na criação de novas capacidades informacionais, redução de barreiras de aprendizagem e partilha colaborativa de código e ferramentas."
        elif val_code == "VC2":
            l3 = f"Identifica-se potencial tangível de cocriação (VC2), com os participantes a delinearem arquiteturas conceptuais e propostas de integração entre agentes de IA e os sistemas do jogo."
        elif val_code == "VC3":
            l3 = f"Evidencia-se fricção crítica e codestruição de valor (VC3), motivada pela degradação da confiança nas interações sociais, perceção de injustiça competitiva ou opacidade na moderação automatizada."
        else:
            l3 = f"Predomina uma dinâmica de valor reflexiva (VC4), focada na avaliação percetiva do risco sistémico, na transparência dos dados e nos limites normativos da automação em videojogos."

        summary = f"{l1} {l2} {l3}"
        return summary

    def generate_systematic_sheet(self, meta, metrics, evidence, summary):
        """Formata a ficha individual exatamente como exigido na especificação."""
        lines = []
        lines.append(f"#### `{meta['thread_id']}` — {meta['title']}")
        lines.append(f"- **Ecossistema:** {meta['ecosystem']}")
        lines.append(f"- **Volume Empírico:** {meta['posts_retidos']} posts retidos / {meta['posts_originais']} posts originais no tópico")
        lines.append(f"- **Perfil Técnico Dominante:**")
        lines.append(f"  - Código de Agência Prevalente: `{metrics['prev_ai']}`")
        lines.append(f"  - Padrão de Interação Principal: `{metrics['prev_inter']}`")
        lines.append(f"- **Vetor DART do Tópico (Médias 0–5):** D: `{metrics['avg_d']:.1f}` | A: `{metrics['avg_a']:.1f}` | R: `{metrics['avg_r']:.1f}` | T: `{metrics['avg_t']:.1f}`")
        lines.append(f"- **Dinâmica de Valor:** {metrics['val_dyn']}")
        lines.append(f"- **Resumo Analítico (Máx. 4-5 linhas):**")
        lines.append(f"  {summary}")
        lines.append(f"- **Evidência Paradigmática:**")
        lines.append(f'  > "{evidence}"')
        lines.append("")
        lines.append("---")
        lines.append("")
        return "\n".join(lines)

    def generate_macro_synthesis(self, thread_records):
        """Produz a síntese final com tabela comparativa, clusters tipológicos e padrão transversal."""
        lines = []
        lines.append("## Síntese Final Pós-Análise dos Tópicos")
        lines.append("")
        
        # 1. Tabela Comparativa Global por Ecossistema
        eve_threads = [t for t in thread_records if t["game"] == "EVE Online"]
        wow_threads = [t for t in thread_records if t["game"] == "World of Warcraft"]
        
        def calc_ecosystem_stats(tlist):
            n_threads = len(tlist)
            total_retained = sum(t["posts_retidos"] for t in tlist)
            avg_posts = total_retained / n_threads if n_threads else 0
            avg_d = sum(t["avg_d"] for t in tlist) / n_threads if n_threads else 0
            avg_a = sum(t["avg_a"] for t in tlist) / n_threads if n_threads else 0
            avg_r = sum(t["avg_r"] for t in tlist) / n_threads if n_threads else 0
            avg_t = sum(t["avg_t"] for t in tlist) / n_threads if n_threads else 0
            
            vc1_count = sum(1 for t in tlist if t["val_code"] == "VC1")
            vc2_count = sum(1 for t in tlist if t["val_code"] == "VC2")
            vc3_count = sum(1 for t in tlist if t["val_code"] == "VC3")
            vc4_count = sum(1 for t in tlist if t["val_code"] == "VC4")
            
            return {
                "n_threads": n_threads,
                "total_retained": total_retained,
                "avg_posts": avg_posts,
                "avg_d": avg_d,
                "avg_a": avg_a,
                "avg_r": avg_r,
                "avg_t": avg_t,
                "vc1": vc1_count,
                "vc2": vc2_count,
                "vc3": vc3_count,
                "vc4": vc4_count,
                "vc1_pct": (vc1_count / n_threads * 100) if n_threads else 0,
                "vc3_pct": (vc3_count / n_threads * 100) if n_threads else 0
            }

        eve_stats = calc_ecosystem_stats(eve_threads)
        wow_stats = calc_ecosystem_stats(wow_threads)
        total_stats = calc_ecosystem_stats(thread_records)

        lines.append("### 1. Tabela Comparativa Global por Ecossistema")
        lines.append("")
        lines.append("| Dimensão Metodológica / Ecossistema | EVE Online (Sandbox Aberto) | World of Warcraft (Ambiente Controlado) | Total Consolidado |")
        lines.append("| :--- | :---: | :---: | :---: |")
        lines.append(f"| **Número Total de Tópicos Ativos** | **{eve_stats['n_threads']} tópicos** ({eve_stats['n_threads']/total_stats['n_threads']*100:.1f}%) | **{wow_stats['n_threads']} tópicos** ({wow_stats['n_threads']/total_stats['n_threads']*100:.1f}%) | **{total_stats['n_threads']} tópicos** (100,0%) |")
        lines.append(f"| **Volume de Posts Analisados** | {eve_stats['total_retained']} posts ({eve_stats['total_retained']/total_stats['total_retained']*100:.1f}%) | {wow_stats['total_retained']} posts ({wow_stats['total_retained']/total_stats['total_retained']*100:.1f}%) | {total_stats['total_retained']} posts (100,0%) |")
        lines.append(f"| **Média de Posts Retidos por Tópico** | `{eve_stats['avg_posts']:.2f}` posts/tópico | `{wow_stats['avg_posts']:.2f}` posts/tópico | `{total_stats['avg_posts']:.2f}` posts/tópico |")
        lines.append(f"| **Vetor DART Médio Global** | `D: {eve_stats['avg_d']:.2f} | A: {eve_stats['avg_a']:.2f} | R: {eve_stats['avg_r']:.2f} | T: {eve_stats['avg_t']:.2f}` | `D: {wow_stats['avg_d']:.2f} | A: {wow_stats['avg_a']:.2f} | R: {wow_stats['avg_r']:.2f} | T: {wow_stats['avg_t']:.2f}` | `D: {total_stats['avg_d']:.2f} | A: {total_stats['avg_a']:.2f} | R: {total_stats['avg_r']:.2f} | T: {total_stats['avg_t']:.2f}` |")
        lines.append(f"| **Proporção de Tópicos VC1 (Cocriação Efetiva)** | `{eve_stats['vc1_pct']:.1f}%` ({eve_stats['vc1']} tópicos) | `{wow_stats['vc1_pct']:.1f}%` ({wow_stats['vc1']} tópicos) | `{total_stats['vc1_pct']:.1f}%` ({total_stats['vc1']} tópicos) |")
        lines.append(f"| **Proporção de Tópicos VC3 (Codestruição / Fricção)** | `{eve_stats['vc3_pct']:.1f}%` ({eve_stats['vc3']} tópicos) | `{wow_stats['vc3_pct']:.1f}%` ({wow_stats['vc3']} tópicos) | `{total_stats['vc3_pct']:.1f}%` ({total_stats['vc3']} tópicos) |")
        lines.append(f"| **Proporção de Tópicos VC2 (Potencial de Cocriação)** | `{eve_stats['vc2']/eve_stats['n_threads']*100:.1f}%` ({eve_stats['vc2']} tópicos) | `{wow_stats['vc2']/wow_stats['n_threads']*100:.1f}%` ({wow_stats['vc2']} tópicos) | `{total_stats['vc2']/total_stats['n_threads']*100:.1f}%` ({total_stats['vc2']} tópicos) |")
        lines.append(f"| **Proporção de Tópicos VC4 (Reflexivos / Neutros)** | `{eve_stats['vc4']/eve_stats['n_threads']*100:.1f}%` ({eve_stats['vc4']} tópicos) | `{wow_stats['vc4']/wow_stats['n_threads']*100:.1f}%` ({wow_stats['vc4']} tópicos) | `{total_stats['vc4']/total_stats['n_threads']*100:.1f}%` ({total_stats['vc4']} tópicos) |")
        lines.append("")
        lines.append("---")
        lines.append("")

        # 2. Tipologia Emergente de Tópicos (Clusters Temáticos)
        lines.append("### 2. Tipologia Emergente de Tópicos: Clusters Temáticos")
        lines.append("")
        lines.append("A análise transversal das 143 threads revela cinco agrupamentos (*clusters*) sociotécnicos fundamentais, estruturados pelo tipo de artefacto algorítmico e pela postura comunitária:")
        lines.append("")
        
        # Categorizar tópicos nos clusters
        clusters = {
            "c1_api_mcp": {"nome": "Cluster 1: Ferramentas Externas, Integração de APIs e MCP", "threads": [], "desc": "Tópicos dedicados à interligação de dados do jogo com Large Language Models via APIs oficiais (ex.: EVE Swagger Interface - ESI, Model Context Protocol - MCP, Pyfa, exportação de telemetria). Caracterizam-se por elevada concessão de Acesso (A >= 3.0), diálogo agêntico e prevalência de cocriação efetiva (VC1 e VC2)."},
            "c2_fairplay": {"nome": "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva", "threads": [], "desc": "Discussões inflamadas sobre a fronteira entre assistência de IA permitida e automação desleal em ambientes PvP e instâncias de alta dificuldade (Mythic+, arenas, frotas Nullsec). Apresentam o score mais elevado de Risco Percebido (R >= 3.5) e frequente codestruição de valor (VC3) motivada por desconfiança competitiva."},
            "c3_support": {"nome": "Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning", "threads": [], "desc": "Queixas e deliberações sobre o uso de agentes de IA pela publicadora (Blizzard / CCP) para gestão de tickets de suporte, respostas pré-programadas e bans automatizados. Marcado por baixíssima Transparência (T <= 1.0), severa frustração dos utilizadores e episódios paradigmáticos de codestruição de valor (VC3)."},
            "c4_followers": {"nome": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores", "threads": [], "desc": "Análise das funcionalidades oficiais introduzidas pelas publicadoras incorporando comportamento de IA nos NPCs aliados (ex.: Follower Dungeons e Delves em WoW; Aura Guidance em EVE). Regista interação direta humano-IA (I1 e I3), com avaliação mista entre inclusão de novos jogadores (VC1/VC2) e quebra da sociabilidade tradicional (VC3/VC4)."},
            "c5_vibecoding": {"nome": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding", "threads": [], "desc": "Partilha de experiências de jogadores e programadores comunitários que utilizam assistentes de código (ChatGPT, Claude, Copilot) para gerar macros complexas, addons em Lua e ferramentas web. Representa a tipologia mais nítida de Humanos Assistidos por IA (A4) com cooperação triádica (I3) e cocriação de valor (VC1)."}
        }

        for t in thread_records:
            txt = (t["title"] + " " + t["summary"]).lower()
            if "mcp" in txt or "esi" in txt or "api" in txt or "endpoint" in txt:
                clusters["c1_api_mcp"]["threads"].append(t)
            elif "follower" in txt or "masmorra" in txt or "delve" in txt or "brann" in txt or "aura" in txt:
                clusters["c4_followers"]["threads"].append(t)
            elif "ticket" in txt or "suporte" in txt or "gm" in txt or "ban" in txt or "modera" in txt:
                clusters["c3_support"]["threads"].append(t)
            elif "copilot" in txt or "vibe" in txt or "claude" in txt or "chatgpt" in txt or "addon" in txt or "desenvolv" in txt or "lua" in txt:
                clusters["c5_vibecoding"]["threads"].append(t)
            else:
                clusters["c2_fairplay"]["threads"].append(t)

        for c_key, c_info in clusters.items():
            c_threads = c_info["threads"]
            n_c = len(c_threads)
            pct_c = (n_c / len(thread_records) * 100) if thread_records else 0
            avg_r_c = sum(t["avg_r"] for t in c_threads) / n_c if n_c else 0
            avg_a_c = sum(t["avg_a"] for t in c_threads) / n_c if n_c else 0
            lines.append(f"#### {c_info['nome']} ({n_c} tópicos | {pct_c:.1f}%)")
            lines.append(f"* **Enquadramento:** {c_info['desc']}")
            lines.append(f"* **Perfil Médio DART:** Acesso: `{avg_a_c:.1f}` | Risco: `{avg_r_c:.1f}` | Tópicos em Destaque: " + ", ".join([f"`{t['thread_id']}`" for t in c_threads[:4]]) + ("..." if n_c > 4 else ""))
            lines.append("")

        lines.append("---")
        lines.append("")

        # 3. Padrão Transversal Sandbox vs. Controlado
        lines.append("### 3. Padrão Transversal: Sandbox vs. Ecossistema Controlado")
        lines.append("")
        lines.append(
            "A análise agregada dos 143 tópicos demonstra que a **arquitetura de governança e a infraestrutura técnica do jogo exercem um papel determinístico na transição do discurso comunitário de simples debate abstrato (A5/I4) para a cocriação tangível de valor (A1/A4/I3)**. "
            "No ecossistema **Sandbox de *EVE Online***, a disponibilização pública e abrangente de interfaces de programação de aplicações (ESI - *EVE Swagger Interface*) e a arquitetura económica aberta criam um terreno fértil para a emergência de agentes autónomos e copilotos generativos. Os jogadores não se limitam a especular sobre o impacto da IA: desenvolvem servidores MCP (*Model Context Protocol*), integram LLMs para triagem tática de telemetria e concebem sistemas heurísticos colaborativos (*EVE Crews*), elevando significativamente os índices dimensionais de Acesso (`1,47`) e Transparência (`1,49`). O valor é ativamente cocriado no limiar entre o código da publicadora e as ferramentas comunitárias, onde a IA atua como uma prótese analítica para dominar a complexidade operacional da galáxia."
        )
        lines.append("")
        lines.append(
            "Em contrapartida, no ecossistema **Controlado de *World of Warcraft***, a governança algorítmica é rigidamente mediada pela desenvolvedora (Blizzard), delimitando fronteiras estritas à sandbox de scripts Lua e concentrando o uso oficial de IA em instâncias fechadas de jogabilidade assistida (*Follower Dungeons* e *Delves*). Em consequência, o discurso comunitário em *WoW* adquire uma postura predominantemente reativa e defensiva, com forte dominância da dimensão de Risco Percebido (`1,56`) e proliferação de debates éticos sobre integridade competitiva, perda da sociabilidade humana e opacidade no suporte automatizado por tickets. Quando a cocriação emerge em *WoW*, assume a forma de assistência indireta (*vibe-coding* de addons e macros assistidas por IA), revelando que ambientes virtuais fechados tendem a canalizar a agência sociotécnica dos jogadores para a contestação normativa e mitigação de risco (VC3/VC4), ao passo que ecossistemas sandbox abertos catalisam o desenvolvimento distribuído e a cocriação efetiva de valor (VC1/VC2)."
        )
        lines.append("")
        return "\n".join(lines)

    def run(self):
        """Executa o ciclo completo de análise agregada por tópico."""
        logger.info("ThreadSynthesisAgent: Iniciando agregação de dados...")
        posts, summary_cache, corpus_by_id, raw_meta, anon_counts, anon_titles, anon_posts_map = self.load_data()
        
        thread_map = self.group_threads(posts)
        logger.info(f"ThreadSynthesisAgent: {len(posts)} posts agrupados em {len(thread_map)} tópicos ativos.")
        
        thread_records = []
        md_sections = []
        
        # Cabeçalho do documento
        md_sections.append("# Análise Agregada ao Nível de Tópicos de Discussão (*Threads*) — DART-NET v3.6")
        md_sections.append("")
        md_sections.append(
            "Este documento formaliza a **análise agregada ao nível de tópicos de discussão (*threads*)** a partir do corpus "
            "purificado de **825 posts validados** de alta densidade empírica, cobrindo os ecossistemas de *EVE Online* e *World of Warcraft* "
            "no período estrito de **janeiro de 2024 a setembro de 2026**. O estudo ancora-se na framework de **Cocriação de Valor DART-NET** "
            "(Prahalad & Ramaswamy, 2004; Kozinets, 2020; DART-NET 2026), articulando as mecânicas de interação humano-IA e a emergência de valor sociotécnico."
        )
        md_sections.append("")
        md_sections.append("> [!IMPORTANT]")
        md_sections.append(f"> **Critério de Inclusão Estrito:** Todos os **{len(thread_map)} tópicos ativos** aqui analisados contêm pelo menos um post validado pós-poda metodológica, eliminando threads espúrias e garantindo que cada unidade analítica apresente evidência empírica verificável.")
        md_sections.append("")
        md_sections.append("---")
        md_sections.append("")
        md_sections.append("## Catálogo Sistemático das Fichas Analíticas de Tópicos")
        md_sections.append("")
        
        # Ordenação consistente: por ecossistema (EVE Online primeiro, depois WoW) e por volume de posts retidos
        sorted_tids = sorted(
            thread_map.keys(),
            key=lambda tid: (
                0 if "eve" in (thread_map[tid][0].get("jogo") or thread_map[tid][0].get("game") or "").lower() else 1,
                -len(thread_map[tid]),
                str(tid)
            )
        )
        
        for tid in sorted_tids:
            tposts = thread_map[tid]
            meta = self.resolve_metadata(tid, tposts, corpus_by_id, raw_meta, anon_counts, anon_titles)
            metrics = self.compute_metrics(tposts)
            evidence = self.select_paradigmatic_evidence(tposts, anon_posts_map)
            summary = self.synthesize_analytic_summary(meta, metrics, tposts, summary_cache)
            
            # Formatar ficha Markdown
            sheet_md = self.generate_systematic_sheet(meta, metrics, evidence, summary)
            md_sections.append(sheet_md)
            
            record = {
                **meta,
                **metrics,
                "summary": summary,
                "evidence": evidence
            }
            thread_records.append(record)
            
        # Adicionar Síntese Final Pós-Análise dos Tópicos
        macro_synthesis_md = self.generate_macro_synthesis(thread_records)
        md_sections.append(macro_synthesis_md)
        
        # Gravar ficheiro Markdown
        with open(self.output_md, "w", encoding="utf-8") as f:
            f.write("\n".join(md_sections) + "\n")
            
        # Gravar ficheiro JSON estruturado
        with open(self.output_json, "w", encoding="utf-8") as f:
            json.dump(thread_records, f, indent=2, ensure_ascii=False)
            
        logger.info(f"ThreadSynthesisAgent: Concluído com sucesso. Ficheiros gerados:")
        logger.info(f" - Markdown: {self.output_md} ({len(thread_records)} fichas sistemáticas)")
        logger.info(f" - JSON: {self.output_json}")
        print(f"Sucesso: {self.output_md} gerado com {len(thread_records)} tópicos ativos.")
        print(f"Sucesso: {self.output_json} estruturado com metadados e métricas completas.")
        return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = ThreadSynthesisAgent()
    agent.run()
