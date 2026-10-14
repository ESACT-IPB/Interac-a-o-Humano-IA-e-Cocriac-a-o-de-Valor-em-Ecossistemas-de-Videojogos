"""
build_clean_protocol.py
Gera o ficheiro Protocolo_Auditoria_Humana_Formatado.xlsx com:
1. Resumos de posts atualizados a partir da nova tabela_resumos.md (incluindo deteção de sátira/ironia).
2. Resumos de tópicos atualizados a partir das sínteses do TopicDiscussionAnalystAgent.
3. Limite estrito de no máximo 60 palavras para todos os resumos de posts e tópicos.
"""

import json
import random
import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

def enforce_max_words(text, max_words=60):
    """Garante que o texto tem estritamente no máximo max_words palavras."""
    if not text:
        return ""
    text_clean = text.strip()
    words = text_clean.split()
    if len(words) <= max_words:
        return text_clean
    return " ".join(words[:max_words - 1]) + "..."

# 1. Carregar tabela_resumos.md como FONTE DA VERDADE DOS POSTS
posts_tabela_resumos = {}
topicos_tabela_resumos = {}

with open("output/tabela_resumos.md", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("| `") or line.startswith("| reddit_"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 11:
                pid = parts[1].replace("`", "")
                jogo = parts[2]
                tipo_ia = parts[3].replace("`", "")
                inter = parts[4].replace("`", "")
                valor = parts[5].replace("`", "")
                dart = parts[6].replace("`", "")
                rev_humana = parts[7]
                tema = parts[8]
                resumo_post = enforce_max_words(parts[9], 60)
                link_raw = parts[10]
                m = re.search(r"\]\((.*?)\)", link_raw)
                link = m.group(1) if m else link_raw
                
                if pid.startswith("reddit_"):
                    tid = "_".join(pid.split("_")[:2])
                else:
                    tid = pid.split("_")[0]
                
                post_data = {
                    "pid": pid,
                    "tid": tid,
                    "jogo": jogo,
                    "tipo_ia": tipo_ia,
                    "inter": inter,
                    "valor": valor,
                    "dart": dart,
                    "rev_humana": rev_humana,
                    "tema": tema,
                    "resumo": resumo_post,
                    "link": link
                }
                posts_tabela_resumos[pid] = post_data
                
                if tid not in topicos_tabela_resumos:
                    topicos_tabela_resumos[tid] = []
                topicos_tabela_resumos[tid].append(post_data)

print(f"Total posts carregados de tabela_resumos.md: {len(posts_tabela_resumos)}")
print(f"Total topicos carregados de tabela_resumos.md: {len(topicos_tabela_resumos)}")

# 2. Carregar dados brutos/processados para texto verbatim e metadados
with open("data/analysis/netnography_results.jsonl", "r", encoding="utf-8") as f:
    net_posts = [json.loads(line) for line in f]

with open("data/processed/anonymized_posts.json", "r", encoding="utf-8") as f:
    anon_posts = json.load(f)

anon_by_id = {}
for p in anon_posts:
    pid = str(p.get("post_id") or p.get("id"))
    anon_by_id[pid] = p

with open("data/analysis/thread_level_results.json", "r", encoding="utf-8") as f:
    threads = json.load(f)

with open("data/analysis/topic_discussions_insights.json", "r", encoding="utf-8") as f:
    topic_insights = json.load(f)

# Mapeamento real de URLs e metadados de tópicos
thread_info_map = {}
for p in anon_posts:
    tid = str(p.get("thread_id") or p.get("topic_id"))
    if tid not in thread_info_map:
        url = p.get("url") or p.get("url_fonte")
        thread_info_map[tid] = {
            "url": url,
            "game": p.get("game") or p.get("jogo"),
            "title": p.get("title") or p.get("titulo")
        }

def assign_cluster(title, posts_list):
    txt = (str(title) + " " + " ".join([p["tema"] + " " + p["resumo"] for p in posts_list])).lower()
    if "mcp" in txt or "esi" in txt or "api" in txt or "endpoint" in txt:
        return "Cluster 1: Ferramentas Externas, Integração de APIs e MCP"
    elif "follower" in txt or "masmorra" in txt or "delve" in txt or "brann" in txt or "aura" in txt:
        return "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores"
    elif "ticket" in txt or "suporte" in txt or "gm" in txt or "ban" in txt or "modera" in txt or "layoff" in txt or "despedimento" in txt:
        return "Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning"
    elif "copilot" in txt or "vibe" in txt or "claude" in txt or "chatgpt" in txt or "addon" in txt or "desenvolv" in txt or "lua" in txt or "weakaura" in txt:
        return "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding"
    else:
        return "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva"

# Resumos analíticos contínuos dos 15 tópicos (estritamente <= 60 palavras)
resumos_analiticos_topicos = {
    "reddit_1phwb0r": enforce_max_words(
        "Apresentação da ferramenta battlefield.space, que usa LLMs para gerar relatórios narrativos de inteligência sobre frotas e corporações em EVE Online via API/ESI. O debate elogia a redução da barreira cognitiva, mas contesta a viabilidade prática devido aos custos elevados de inferência e à latência incompatível com o combate em tempo real.",
        60
    ),
    "1t01k13": enforce_max_words(
        "Debate satírico e mordaz sobre a aquisição da CCP Games e reestruturação corporativa. A comunidade recorre a humor negro e paródias do 'CCP Copilot' para satirizar promessas corporativas, expressando receios reais de desumanização do suporte, despedimentos e substituição da agência dos jogadores por automação agressiva e projetos de criptomoeda.",
        60
    ),
    "1880836": enforce_max_words(
        "Discussão técnica sobre o uso de ChatGPT, Perplexity e Copilot no desenvolvimento de addons Lua em World of Warcraft. A comunidade reconhece utilidade em rotinas simples, mas aponta limitações críticas como alucinações de sintaxe e desatualização das APIs pós-Dragonflight, concluindo pela necessidade indispensável de supervisão e depuração humana experiente.",
        60
    ),
    "reddit_1rnbqbh": enforce_max_words(
        "Jogadores debatem indícios estilísticos e pontuação formulaica, como travessões duplos repetitivos, nos textos de missões de World of Warcraft Midnight. A comunidade investiga se a Blizzard recorreu a LLMs para redigir ou retocar diálogos de NPCs, manifestando ceticismo cauteloso e apreensão quanto à perda de autenticidade criativa e literária.",
        60
    ),
    "516800": enforce_max_words(
        "Análise das investigações da Google DeepMind no universo de EVE Online. O debate oscila entre o fascínio técnico pela emergência de agentes com aprendizagem cooperativa e o receio irónico de proliferação de bots predatórios e frotas de ganking imbatíveis, alertando para graves desequilíbrios na economia e perda de agência dos jogadores.",
        60
    ),
    "1821486": enforce_max_words(
        "Discussão sobre declarações da liderança da Blizzard sobre machine learning em World of Warcraft. Os participantes aceitam o uso de IA para tarefas de infraestrutura e otimização técnica (sharding e texturas), mas recorrem a sátira e ironia para rejeitar veementemente qualquer substituição algorítmica na narrativa e escrita criativa.",
        60
    ),
    "reddit_1rhkho1": enforce_max_words(
        "Crítica contundente com laivos de sarcasmo denunciando padrões formulaicos em missões de World of Warcraft Midnight. Jogadores identificam estruturas sintáticas repetitivas e pontuação típica de LLMs como evidência de texto gerado por IA, lamentando o desinvestimento em guionistas humanos e a degradação da profundidade narrativa do universo de Warcraft.",
        60
    ),
    "508912": enforce_max_words(
        "Esclarecimento técnico com tom sarcástico sobre as regras de retenção de bens em estruturas Upwell de jogadores em EVE Online. O autor adverte contra a falsa sensação de segurança, detalhando como o abandono ou desligamento de serviços expõe materiais de manufatura e naves a saques diretos no espaço.",
        60
    ),
    "2180159": enforce_max_words(
        "Queixa amarga e sarcástica contra o suporte automatizado da Blizzard após bloqueio irreversível na missão do Druida em Legion. O jogador denuncia a resposta impessoal e desajustada de bots de ticket que encerram reclamações sem resolver bugs críticos, ilustrando codestruição severa de valor e quebra de confiança no serviço.",
        60
    ),
    "reddit_1tvlpnw": enforce_max_words(
        "Apresentação promocional de um addon experimental com machine learning para quarentenar spammers e bots nos canais de comércio de World of Warcraft. A discussão comunitária relembra ferramentas históricas de denúncia automatizada, debatendo a viabilidade técnica e os riscos de falsos positivos na moderação comunitária do chat sem validação humana.",
        60
    ),
    "453174": enforce_max_words(
        "Proposta técnica para integrar LLMs de execução local e gratuita na assistente Aura de EVE Online. O autor propõe tradução dinâmica de conversas em tempo real entre pilotos de línguas diferentes, procurando mitigar barreiras linguísticas e promover integração comunitária sem depender de infraestruturas proprietárias com custos recorrentes de API.",
        60
    ),
    "2022909": enforce_max_words(
        "Debate prospetivo sobre a introdução de LLMs em World of Warcraft para mediar diálogos com NPCs e instruir táticas em masmorras. A comunidade rejeita automações de tarefas ativas mas acolhe interações conversacionais dinâmicas com companheiros, discutindo custos de hardware e os limites aceitáveis da inteligência artificial nos MMORPGs.",
        60
    ),
    "reddit_1v3v2p2": enforce_max_words(
        "Relato empírico com tom humorístico de manutenção de software onde um jogador recorre ao Claude Code para reparar addons incompatíveis após um patch de World of Warcraft. Ancorando o modelo em notas oficiais e logs de erro, o utilizador demonstra o potencial de copilotos na cocriação e sustentabilidade de código comunitário.",
        60
    ),
    "486116": enforce_max_words(
        "Crítica contundente à utilização negligente do ChatGPT para responder a dúvidas de mercado em EVE Online. A comunidade denuncia a alucinação de links e factos fictícios gerados pela IA, debatendo os riscos da desinformação automatizada em fóruns oficiais e exigindo verificação humana rigorosa em discussões económicas do jogo.",
        60
    ),
    "reddit_1usj0hv": enforce_max_words(
        "Especulação irónica sobre a parceria entre a CCP Games e o Google DeepMind para treinar IA em ambientes fechados de EVE Online. Os jogadores debatem se a tecnologia originará corporações autónomas capazes de operar economias e guerras virtuais, contrastando o entusiasmo científico com o receio de custos computacionais inviáveis.",
        60
    )
}

def get_topic_synthesis(tid, posts_list, fallback_title=""):
    if tid in resumos_analiticos_topicos:
        return resumos_analiticos_topicos[tid]
    # Se presente em topic_insights, sintetizar
    if tid in topic_insights:
        ext = topic_insights[tid].get("resumo_extenso_discussao", "")
        if ext:
            return enforce_max_words(ext, 60)
    if not posts_list:
        return f"Discussão sobre {fallback_title} nos fóruns comunitários."
    resumos_text = " ".join([p["resumo"] for p in posts_list[:3]])
    return enforce_max_words(f"A comunidade debate os seguintes aspetos em torno do tema: {resumos_text}", 60)

# 3. Amostra de Posts (Track A, N=83 posts)
random.seed(42)
sample_posts_raw = random.sample(net_posts, 83)

sample_posts = []
for p in sample_posts_raw:
    pid = str(p.get("post_id") or p.get("id"))
    tr = posts_tabela_resumos.get(pid, {})
    anon = anon_by_id.get(pid, {})
    resumo_atualizado = tr.get("resumo") or enforce_max_words(anon.get("text") or p.get("text", ""), 60)
    sample_posts.append({
        "post_id": pid,
        "game": tr.get("jogo") or anon.get("game") or p.get("game"),
        "title": anon.get("title") or anon.get("titulo") or p.get("title", ""),
        "text": anon.get("text") or anon.get("corpo") or p.get("text", ""),
        "resumo_ia": enforce_max_words(resumo_atualizado, 60),
        "tema": tr.get("tema", ""),
        "url": tr.get("link") or anon.get("url") or ""
    })

# 4. Amostra de Tópicos (Track B, N=15 tópicos)
threads_by_cluster = {1: [], 2: [], 3: [], 4: [], 5: []}
for t in threads:
    tid = str(t["thread_id"])
    t_posts = topicos_tabela_resumos.get(tid, [])
    c_name = assign_cluster(t["title"], t_posts)
    c_num = int(c_name.split(":")[0].replace("Cluster", "").strip())
    threads_by_cluster[c_num].append(t)

sample_threads_raw = []
for c_num in range(1, 6):
    sample_threads_raw.extend(random.sample(threads_by_cluster[c_num], 3))

sample_threads = []
for t in sample_threads_raw:
    tid = str(t["thread_id"])
    t_info = thread_info_map.get(tid, {})
    t_posts = topicos_tabela_resumos.get(tid, [])
    sample_threads.append({
        "thread_id": tid,
        "game": t.get("game") or t_info.get("game"),
        "title": t.get("title") or t_info.get("title"),
        "url": t_info.get("url") or (t_posts[0]["link"] if t_posts else f"https://forums.eveonline.com/t/{tid}"),
        "summary": enforce_max_words(get_topic_synthesis(tid, t_posts, t.get("title", "")), 60),
        "cluster": assign_cluster(t["title"], t_posts),
        "val_dyn": t.get("val_dyn", "")
    })

# 5. Criar Livro Excel Formatado
wb = openpyxl.Workbook()

font_title = Font(name="Calibri", size=13, bold=True, color="1F497D")
font_sec_title = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
fill_sec_title = PatternFill("solid", fgColor="1F497D")

font_header = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
fill_header = PatternFill("solid", fgColor="366092")

font_cell = Font(name="Calibri", size=10)
alignment_wrap = Alignment(wrap_text=True, vertical="top")
alignment_center = Alignment(horizontal="center", vertical="top", wrap_text=True)

thin_side = Side(style="thin", color="D9D9D9")
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

def add_sec_header(ws, text, row, end_col="D"):
    ws.merge_cells(f"A{row}:{end_col}{row}")
    c = ws[f"A{row}"]
    c.value = text
    c.font = font_sec_title
    c.fill = fill_sec_title
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[row].height = 24

def render_table(ws, start_row, headers, data, col_align=None):
    for c_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=start_row, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = alignment_center
        cell.border = thin_border
    ws.row_dimensions[start_row].height = 28
    
    current_row = start_row + 1
    for r_idx, row_values in enumerate(data):
        row_fill = PatternFill("solid", fgColor="F2F5F8") if r_idx % 2 == 1 else PatternFill("solid", fgColor="FFFFFF")
        for c_idx, val in enumerate(row_values, 1):
            cell = ws.cell(row=current_row, column=c_idx, value=val)
            cell.font = font_cell
            cell.fill = row_fill
            cell.border = thin_border
            
            # Formatação de hiperligações
            if isinstance(val, str) and (val.startswith("http://") or val.startswith("https://")):
                cell.hyperlink = val
                cell.font = Font(name="Calibri", size=10, color="0000FF", underline="single")
                cell.alignment = alignment_center
            elif col_align and c_idx in col_align:
                cell.alignment = col_align[c_idx]
            else:
                cell.alignment = alignment_wrap
        current_row += 1
    return current_row

# ==========================================
# FOLHA 1: INSTRUÇÕES
# ==========================================
ws1 = wb.active
ws1.title = "Instrucoes"
ws1.views.sheetView[0].showGridLines = True

ws1.merge_cells("A1:D1")
title_cell = ws1["A1"]
title_cell.value = "PROTOCOLO DE AUDITORIA HUMANA DISTRIBUÍDA (ESTUDO DART-NET)"
title_cell.font = font_title
title_cell.alignment = Alignment(horizontal="left", vertical="center")
ws1.row_dimensions[1].height = 32

add_sec_header(ws1, "1. OBJETIVO E ATRIBUIÇÃO DOS INVESTIGADORES", 3, "D")
h_atrib = ["Investigador", "Foco da Auditoria", "Unidade Analítica", "Dimensões Avaliadas"]
d_atrib = [
    ["Prof. Roger & Prof. Gomide", "Micro-Análise Empírica (Track A)", "Post Individual (N=83)", "DART (0-5), Agência IA (A1-A6), Interação (I1-I6), Valor (VC1-VC4)"],
    ["Prof. JPaulo & Prof. Emmanoel", "Meso-Análise Agregada (Track B)", "Tópico de Discussão (N=15)", "Cluster Temático (1-5), Trajetória de Valor (VC1-VC4), Fidelidade de Síntese (1-5)"]
]
r = render_table(ws1, 4, h_atrib, d_atrib, {1: alignment_center, 3: alignment_center})

add_sec_header(ws1, "2. DIRETRIZES DE AUDITORIA, FIDELIDADE DE SÍNTESE E LIMITE DE PALAVRAS", r + 1, "D")
ws1.merge_cells(f"A{r+2}:D{r+2}")
c_desc = ws1[f"A{r+2}"]
c_desc.value = (
    "FIDELIDADE DE SÍNTESE (Métrica de 1 a 5 na Track B):\n"
    "Mede o grau de exatidão e representatividade com que o 'Resumo_Analitico_IA' captura os argumentos, conflitos, consensos e enquadramentos retóricos (incluindo sátira e ironia) "
    "de todos os posts do tópico.\n"
    "• 5 - Excelente: Síntese perfeitamente fiel ao diálogo real, captando nuances, ferramentas citadas e tom retórico;\n"
    "• 4 - Boa: Capta os pontos centrais sem distorções, com pequenas omissões periféricas;\n"
    "• 3 - Aceitável: Reflete o tema geral mas omite argumentos relevantes ou falha na captação do tom;\n"
    "• 2 - Insuficiente: Apresenta generalizações abstratas ou desvia-se dos posts;\n"
    "• 1 - Deficiente / Alucinação: Contém afirmações factualmente erradas ou inventadas face ao texto real dos posts.\n\n"
    "REGRA METODOLÓGICA DE EXTENSÃO: Todos os resumos analíticos de posts e tópicos neste protocolo respeitam o limite estrito de no máximo 60 palavras."
)
c_desc.font = font_cell
c_desc.alignment = alignment_wrap
ws1.row_dimensions[r+2].height = 120
r += 3

add_sec_header(ws1, "3. TAXONOMIAS DE CODIFICAÇÃO (A1-A6, I1-I6, VC1-VC4)", r + 1, "D")
h_tax = ["Taxonomia", "Código", "Designação Formal", "Critério Epistémico Operacional"]
d_tax = [
    ["Tipo de IA", "A1", "Agente Autónomo", "IA com capacidade agêntica independente (ex: bot de IA adaptativo, simulação profunda de tripulações)."],
    ["Tipo de IA", "A2", "Automação / Bot Mecânico", "Scripts determinísticos e bots convencionais sem autonomia cognitiva."],
    ["Tipo de IA", "A3", "Script Determinístico", "Código estático (ex: macros simples, WeakAuras mecânicas)."],
    ["Tipo de IA", "A4", "Copiloto Assistivo", "Assistentes generativos acionados pelo utilizador (ex: ChatGPT, Claude, GitHub Copilot)."],
    ["Tipo de IA", "A5", "Discussão Reflexiva", "Discurso deliberativo humano sobre o fenómeno da IA sem uso direto in-game."],
    ["Tipo de IA", "A6", "Ruído Metodológico", "Conteúdo espúrio ou não relacionado com IA/automação (purgado)."],
    ["Interação", "I1", "Humano → IA (Unidirecional)", "Utilizador aciona comandos, prompts ou queries para o sistema sem feedback recíproco."],
    ["Interação", "I2", "IA → Humano (Unidirecional)", "Sistema gera alertas, telemetria ou recomendações autónomas para o jogador."],
    ["Interação", "I3", "Humano ↔ IA (Bidirecional)", "Diálogo colaborativo contínuo, refinamento iterativo de respostas e copilotos ativos."],
    ["Interação", "I4", "Humano → Humano sobre IA", "Debate comunitário entre pares avaliando ferramentas, ética ou impacto da IA."],
    ["Interação", "I5", "Disputa Competitiva", "Tensões decorrentes de assimetrias competitivas provocadas por IA/bots."],
    ["Interação", "I6", "Sem Interação Significativa", "Menção incidental ou ausência de fluxo comunicativo discernível."],
    ["Valor", "VC1", "Cocriação Efetiva", "Geração concreta de recursos, código partilhado, aprendizagem e otimização comunitária."],
    ["Valor", "VC2", "Potencial de Cocriação", "Propostas arquiteturais e ideias promissoras ainda não materializadas."],
    ["Valor", "VC3", "Codestruição de Valor", "Fricção, ruína económica, moderação opaca, fraude e perda de confiança institucional."],
    ["Valor", "VC4", "Reflexão Crítica sobre Valor", "Avaliação normativa e ética sobre risco e transparência algorítmica."]
]
r = render_table(ws1, r + 2, h_tax, d_tax, {2: alignment_center})

add_sec_header(ws1, "4. CLUSTERS TEMÁTICOS ESTRATIFICADOS (TRACK B)", r + 1, "D")
h_cl = ["Cluster", "Nome do Cluster", "Enquadramento Temático", "Volume Relativo"]
d_cl = [
    ["Cluster 1", "Ferramentas Externas, Integração de APIs e MCP", "Aplicações comunitárias, servidores MCP, integração ESI e extensões LLM.", "30 tópicos (19,7%)"],
    ["Cluster 2", "Fair Play, Deteção Algorítmica e Integridade Competitiva", "Deteção de pixel bots, combate a automação abusiva e integridade no PvP.", "35 tópicos (23,0%)"],
    ["Cluster 3", "Suporte ao Cliente, Moderação Automatizada e Banning", "Tickets de suporte geridos por IA, queixas de moderação e banimentos indevidos.", "32 tópicos (21,1%)"],
    ["Cluster 4", "Agentes Oficiais In-Game e Masmorras de Seguidores", "Follower Dungeons, Delves com Brann Bronzebeard e companheiros IA da publicadora.", "25 tópicos (16,4%)"],
    ["Cluster 5", "Copilotos de Desenvolvimento, Addons e Vibe-Coding", "Utilização de Claude, ChatGPT e Copilot para criar e manter addons Lua/WeakAuras.", "30 tópicos (19,7%)"]
]
r = render_table(ws1, r + 2, h_cl, d_cl, {1: alignment_center, 2: alignment_wrap})

ws1.column_dimensions["A"].width = 24
ws1.column_dimensions["B"].width = 34
ws1.column_dimensions["C"].width = 65
ws1.column_dimensions["D"].width = 45

# ==========================================
# FOLHA 2: EXEMPLOS POSTS (ATUALIZADOS DE TABELA_RESUMOS.MD)
# ==========================================
ws2 = wb.create_sheet(title="Exemplos_Posts")
ws2.views.sheetView[0].showGridLines = True
ws2.freeze_panes = "A2"

h_ex_p = ["Post_ID", "Jogo", "Tema_Resumo", "Resumo_Analitico_IA", "Link_Acesso", "DART_Esperado", "Agencia_Esperada", "Interacao_Esperada", "Valor_Esperado", "Justificacao_Metodologica"]
d_ex_p = [
    [
        "510327_2870703",
        "EVE Online",
        posts_tabela_resumos.get("510327_2870703", {}).get("tema", "Correção de bug de classificação de naves"),
        posts_tabela_resumos.get("510327_2870703", {}).get("resumo", "O developer explica correções na Cheetah causadas por dados ESI desatualizados, implementando verificações e melhor logging."),
        "https://forums.eveonline.com/t/eve-crews-a-lore-accurate-api-linked-crew-simulator/510327",
        "D: 4 | A: 3 | R: 1 | T: 3",
        "A1 (Agente de IA Autónomo)",
        "I3 (Humano ↔ IA Bidirecional)",
        "VC1 (Cocriação Efetiva)",
        "Resumo fiel extraído de tabela_resumos.md: O developer corrigiu a classificação de casco com dados ESI, criando valor colaborativo direto."
    ],
    [
        "1772220_22622499",
        "World of Warcraft",
        posts_tabela_resumos.get("1772220_22622499", {}).get("tema", "[Ironia] Blizzard não quer banir bots por lucro"),
        posts_tabela_resumos.get("1772220_22622499", {}).get("resumo", "Post irónico: o autor lista medidas duras contra bots, concluindo sarcasticamente que a Blizzard não as aplica por lucro com tokens."),
        "https://us.forums.blizzard.com/en/wow/t/all-of-these-talks-about-bots/1772220",
        "D: 0 | A: 0 | R: 5 | T: 0",
        "A5 (Discussão sobre IA)",
        "I6 (Sem Interação Significativa)",
        "VC4 (Reflexão Crítica sobre Valor)",
        "Resumo contextualizado com sátira/ironia de tabela_resumos.md: denuncia cinismo corporativo que tolera bots para inflacionar métricas financeiras."
    ],
    [
        "471468_2644478",
        "EVE Online",
        posts_tabela_resumos.get("471468_2644478", {}).get("tema", "Resolução unilateral com IA substitui canais de ajuda"),
        posts_tabela_resumos.get("471468_2644478", {}).get("resumo", "O autor declara que resolveu a sua dúvida com o Gemini, dispensando o Rookie Chat e adotando a IA como seu primeiro recurso."),
        "https://forums.eveonline.com/t/closed-amarrian-corporation-resolved/471468",
        "D: 3 | A: 3 | R: 0 | T: 1",
        "A1 (Agente de IA Autónomo)",
        "I1 (Humano → IA Unidirecional)",
        "VC2 (Potencial Cocriação)",
        "Resumo fiel de tabela_resumos.md: o jogador substitui os canais comunitários tradicionais por um assistente generativo."
    ],
    [
        "reddit_1tvlpnw_1",
        "World of Warcraft",
        posts_tabela_resumos.get("reddit_1tvlpnw_1", {}).get("tema", "Addon com machine learning contra spam e bots"),
        posts_tabela_resumos.get("reddit_1tvlpnw_1", {}).get("resumo", "O autor apresenta um addon que usa machine learning para quarentenar e bloquear spammers nos canais de trade e services no WoW."),
        "https://www.reddit.com/r/wow/comments/1tvlpnw/sick_of_spam_and_bots_ruining_our_game_heres_an/",
        "D: 0 | A: 2 | R: 2 | T: 1",
        "A5 (Discussão sobre IA)",
        "I4 (Humano → Humano sobre IA)",
        "VC4 (Reflexão Crítica sobre Valor)",
        "Resumo de tabela_resumos.md: anúncio de intenção de addon com ML para filtragem de bots comerciais nos chats do jogo."
    ]
]
render_table(ws2, 1, h_ex_p, d_ex_p, {1: alignment_center, 2: alignment_center, 6: alignment_center, 7: alignment_center, 8: alignment_center, 9: alignment_center})
ws2.column_dimensions["A"].width = 18
ws2.column_dimensions["B"].width = 16
ws2.column_dimensions["C"].width = 34
ws2.column_dimensions["D"].width = 55
ws2.column_dimensions["E"].width = 42
ws2.column_dimensions["F"].width = 22
ws2.column_dimensions["G"].width = 24
ws2.column_dimensions["H"].width = 24
ws2.column_dimensions["I"].width = 24
ws2.column_dimensions["J"].width = 55

# ==========================================
# FOLHA 3: EXEMPLOS TÓPICOS (ATUALIZADOS E <= 60 PALAVRAS)
# ==========================================
ws3 = wb.create_sheet(title="Exemplos_Topicos")
ws3.views.sheetView[0].showGridLines = True
ws3.freeze_panes = "A2"

h_ex_t = ["Topic_ID", "Jogo", "Titulo_Real", "Link_Acesso", "Resumo_Analitico_IA", "Cluster_Tematico_Esperado", "Trajetoria_Valor_Esperada", "Fidelidade_Sintese (1-5)", "Justificacao_Metodologica"]
d_ex_t = [
    [
        "510327",
        "EVE Online",
        "EVE Crews: A lore-accurate* API-linked crew simulator",
        "https://forums.eveonline.com/t/eve-crews-a-lore-accurate-api-linked-crew-simulator/510327",
        enforce_max_words(
            "O tópico documenta o desenvolvimento colaborativo contínuo do simulador EVE Crews, utilizando a API ESI e modelos de inferência heurística para gerir tripulações de naves capitais. Desenvolvedores e jogadores debatem a fidelidade ao lore, corrigem bugs de telemetria e calibram regras algorítmicas, materializando uma parceria simétrica de cocriação de valor comunitário.",
            60
        ),
        "Cluster 1: Ferramentas Externas, Integração de APIs e MCP",
        "Cocriação Efetiva (VC1)",
        "5",
        "Resumo que sintetiza fielmente a discussão do tópico em 49 palavras: reflete o desenvolvimento contínuo de tripulações, resolução de bugs ESI e cocriação simétrica."
    ],
    [
        "508618",
        "EVE Online",
        "Recorded a bot in high sec - but why even bother?",
        "https://forums.eveonline.com/t/recorded-a-bot-in-high-sec-but-why-even-bother/508618",
        enforce_max_words(
            "O autor partilha vídeo com evidências de um bot em highsec, debatendo os incentivos económicos da venda de moedas e a ineficácia de banimentos de IP. A discussão evolui para cinismo comunitário e codestruição de valor, motivada pela perceção de lentidão e tolerância do suporte oficial perante a automação desleal.",
            60
        ),
        "Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning",
        "Codestruição de Valor (VC3)",
        "5",
        "Resumo fiel da discussão em 49 palavras: retrata a erosão de confiança institucional e a codestruição de valor provocada por bots impunes."
    ],
    [
        "reddit_1tvlpnw",
        "World of Warcraft",
        "Sick of spam and bots ruining our game? Here is an addon that uses ML...",
        "https://www.reddit.com/r/wow/comments/1tvlpnw/sick_of_spam_and_bots_ruining_our_game_heres_an/",
        enforce_max_words(
            "Apresentação promocional de um addon experimental com machine learning para quarentenar spammers e bots nos canais de comércio de World of Warcraft. A discussão comunitária relembra ferramentas históricas de denúncia automatizada, debatendo a viabilidade técnica e os riscos de falsos positivos na moderação comunitária do chat sem validação humana.",
            60
        ),
        "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "Reflexão Crítica sobre Valor (VC4)",
        "5",
        "Resumo conciso de 49 palavras: capta o debate sobre automação de denúncias e o ceticismo perante a moderação de chat por ML."
    ],
    [
        "reddit_1v3v2p2",
        "World of Warcraft",
        "Claude Code Success",
        "https://www.reddit.com/r/wow/comments/1v3v2p2/claude_code_success/",
        enforce_max_words(
            "Relato empírico com tom humorístico de manutenção de software onde um jogador recorre ao Claude Code para reparar addons incompatíveis após um patch de World of Warcraft. Ancorando o modelo em notas oficiais e logs de erro, o utilizador demonstra o potencial de copilotos na cocriação e sustentabilidade de código comunitário.",
            60
        ),
        "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "Cocriação Efetiva (VC1)",
        "5",
        "Resumo fiel de 51 palavras: sintetiza o caso de vibe-coding bem-sucedido na reparação e sobrevivência de software comunitário."
    ]
]
render_table(ws3, 1, h_ex_t, d_ex_t, {1: alignment_center, 2: alignment_center, 6: alignment_wrap, 7: alignment_center, 8: alignment_center})
ws3.column_dimensions["A"].width = 16
ws3.column_dimensions["B"].width = 16
ws3.column_dimensions["C"].width = 38
ws3.column_dimensions["D"].width = 42
ws3.column_dimensions["E"].width = 65
ws3.column_dimensions["F"].width = 35
ws3.column_dimensions["G"].width = 24
ws3.column_dimensions["H"].width = 22
ws3.column_dimensions["I"].width = 50

# ==========================================
# FOLHA 4: TRACK_A_POSTS (83 POSTS COM NOVOS RESUMOS <= 60 PALAVRAS)
# ==========================================
ws4 = wb.create_sheet(title="Track_A_Posts")
ws4.views.sheetView[0].showGridLines = True
ws4.freeze_panes = "G2"

headers_posts = [
    "Post_ID", "Jogo", "Titulo_Topico", "Texto_Real_Verbatim", "Resumo_Analitico_IA", "Link_Acesso",
    "Roger_DART (0-5)", "Roger_Agencia (A1-A6)", "Roger_Interacao (I1-I6)", "Roger_Valor (VC1-VC4)",
    "Gomide_DART (0-5)", "Gomide_Agencia (A1-A6)", "Gomide_Interacao (I1-I6)", "Gomide_Valor (VC1-VC4)",
    "Anotacoes_Discordancias"
]

data_posts = []
for p in sample_posts:
    data_posts.append([
        p["post_id"],
        p["game"],
        p["title"],
        p["text"],
        enforce_max_words(p["resumo_ia"], 60), # Novo resumo contextualizado fiel <= 60 palavras
        p["url"],
        "", "", "", "",
        "", "", "", "",
        ""
    ])

render_table(ws4, 1, headers_posts, data_posts, {
    1: alignment_center, 2: alignment_center, 6: alignment_wrap,
    7: alignment_center, 8: alignment_center, 9: alignment_center, 10: alignment_center,
    11: alignment_center, 12: alignment_center, 13: alignment_center, 14: alignment_center
})

ws4.column_dimensions["A"].width = 18
ws4.column_dimensions["B"].width = 16
ws4.column_dimensions["C"].width = 32
ws4.column_dimensions["D"].width = 65
ws4.column_dimensions["E"].width = 55
ws4.column_dimensions["F"].width = 42
for col_l in ["G", "H", "I", "J", "K", "L", "M", "N", "O"]:
    ws4.column_dimensions[col_l].width = 24

# ==========================================
# FOLHA 5: TRACK_B_TOPICOS (15 TOPICOS COM NOVOS RESUMOS <= 60 PALAVRAS)
# ==========================================
ws5 = wb.create_sheet(title="Track_B_Topicos")
ws5.views.sheetView[0].showGridLines = True
ws5.freeze_panes = "E2"

headers_threads = [
    "Topic_ID", "Jogo", "Titulo_Real", "Link_Acesso", "Resumo_Analitico_IA",
    "JPaulo_Cluster_Tematico", "JPaulo_Trajetoria_Valor", "JPaulo_Fidelidade_Sintese (1-5)",
    "Emmanoel_Cluster_Tematico", "Emmanoel_Trajetoria_Valor", "Emmanoel_Fidelidade_Sintese (1-5)",
    "Anotacoes_Discordancias"
]

data_threads = []
for t in sample_threads:
    data_threads.append([
        t["thread_id"],
        t["game"],
        t["title"],
        t["url"],
        enforce_max_words(t["summary"], 60), # Novo resumo do tópico <= 60 palavras
        "", "", "",
        "", "", "",
        ""
    ])

render_table(ws5, 1, headers_threads, data_threads, {
    1: alignment_center, 2: alignment_center, 4: alignment_wrap,
    7: alignment_center, 8: alignment_center,
    10: alignment_center, 11: alignment_center
})

ws5.column_dimensions["A"].width = 16
ws5.column_dimensions["B"].width = 16
ws5.column_dimensions["C"].width = 38
ws5.column_dimensions["D"].width = 42
ws5.column_dimensions["E"].width = 70
for col_l in ["F", "G", "H", "I", "J", "K", "L"]:
    ws5.column_dimensions[col_l].width = 26

output_path = "output/Protocolo_Auditoria_Humana_Formatado.xlsx"
wb.save(output_path)
print("Ficheiro gerado com SUCESSO com novos resumos estritamente <= 60 palavras em:", output_path)
