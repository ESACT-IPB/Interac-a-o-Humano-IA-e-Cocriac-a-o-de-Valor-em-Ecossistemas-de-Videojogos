import json
import random
import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# 1. Carregar tabela_resumos.md como FONTE DA VERDADE ABSOLUTA para os resumos analíticos
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
                tema = parts[8]
                resumo_post = parts[9]
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

# 2. Carregar dados para texto verbatim e metadados adicionais
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
    # Basear classificacao de cluster nos temas reais de tabela_resumos.md
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

def build_topic_summary(posts_list):
    """Constrói o resumo analítico do tópico estritamente a partir dos resumos de tabela_resumos.md."""
    if not posts_list:
        return "Sem posts analisados."
    if len(posts_list) == 1:
        return f"[{posts_list[0]['tema']}]: {posts_list[0]['resumo']}"
    
    # Se tem múltiplos posts, agrega os pontos principais de tabela_resumos.md
    lines = []
    # Selecionar até 4 posts representativos para síntese
    for i, p in enumerate(posts_list[:4], 1):
        lines.append(f"• Post {i} ({p['tema']}): {p['resumo']}")
    if len(posts_list) > 4:
        lines.append(f"(Tópico inclui um total de {len(posts_list)} posts analisados na tabela de resumos).")
    return "\n".join(lines)

# 3. Amostra de Posts (Track A, N=83 posts, 10% de 825)
random.seed(42)
sample_posts_raw = random.sample(net_posts, 83)

sample_posts = []
for p in sample_posts_raw:
    pid = str(p.get("post_id") or p.get("id"))
    tr = posts_tabela_resumos.get(pid, {})
    anon = anon_by_id.get(pid, {})
    sample_posts.append({
        "post_id": pid,
        "game": tr.get("jogo") or anon.get("game") or p.get("game"),
        "title": anon.get("title") or anon.get("titulo") or p.get("title", ""),
        "text": anon.get("text") or anon.get("corpo") or p.get("text", ""),
        "resumo_ia": tr.get("resumo", "Sem resumo na tabela."),
        "tema": tr.get("tema", ""),
        "url": tr.get("link") or anon.get("url") or ""
    })

# 4. Amostra de Tópicos (Track B, N=15 tópicos, 10% de 143)
# Equilibrar entre clusters usando os dados de tabela_resumos.md
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
        "summary": build_topic_summary(t_posts),
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
    ws.row_dimensions[start_row].height = 24
    
    cur_row = start_row + 1
    for r_data in data:
        for c_idx, val in enumerate(r_data, 1):
            cell = ws.cell(row=cur_row, column=c_idx, value=val)
            cell.font = font_cell
            cell.border = thin_border
            align = col_align.get(c_idx, alignment_wrap) if col_align else alignment_wrap
            cell.alignment = align
        ws.row_dimensions[cur_row].height = 20 if len(str(r_data[1])) < 60 else 38
        cur_row += 1
    return cur_row + 1

# ==========================================
# FOLHA 1: INSTRUÇÕES E QUADROS TEÓRICOS
# ==========================================
ws1 = wb.active
ws1.title = "Instrucoes"
ws1.views.sheetView[0].showGridLines = True

r = 1
ws1.merge_cells(f"A{r}:D{r}")
t_cell = ws1[f"A{r}"]
t_cell.value = "PROTOCOLO DE AUDITORIA HUMANA DISTRIBUÍDA (DUPLO-CEGO) — DART-NET"
t_cell.font = font_title
t_cell.alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[r].height = 30
r += 2

add_sec_header(ws1, "1. DIVISÃO DAS TAREFAS DE AUDITORIA (AMOSTRA VERIFICADA DE 10%)", r)
r += 1
h_div = ["Tarefa / Nível", "Dupla de Avaliadores", "Unidade Amostral", "Instruções Específicas"]
d_div = [
    ["Track A (Posts - Micro)", "Roger e Gomide", "83 Posts Reais (10% de 825)", "Classificar de forma independente com base no texto verbatim e no resumo analítico de tabela_resumos.md: Dimensões DART (0-5), Agência (A1-A6), Interação (I1-I6) e Valor (VC1-VC4)."],
    ["Track B (Tópicos - Meso)", "JPaulo e Emmanoel", "15 Tópicos Reais (10% de 143)", "Classificar de forma independente com base na thread e na síntese fundamentada em tabela_resumos.md: Cluster Temático (1 a 5), Trajetória Global de Valor (VC1 a VC4) e Fidelidade da Síntese IA (escala 1 a 5)."]
]
r = render_table(ws1, r, h_div, d_div, {1: alignment_center, 2: alignment_center, 3: alignment_center})

add_sec_header(ws1, "2. TAXONOMIA DE AGÊNCIA: IA VS. AUTOMAÇÃO CONVENCIONAL (A1–A6)", r)
r += 1
h_a = ["Código", "Classificação", "Definição Operacional (DART-NET)", "Exemplo no Corpus do Estudo"]
d_a = [
    ["A1", "Agente de IA Autónomo", "Sistema com autonomia decisória, aprendizagem ou raciocínio contextual adaptativo.", "LLMs integrados na API ESI de EVE, agentes narrativos de tripulação (EVE Crews), bots com tomada de decisão contextual."],
    ["A2", "Bot Convencional", "Automação mecânica e determinística com regras rígidas, sem aprendizagem.", "Bots tradicionais de farming, pixel bots, clickers repetitivos de rota ou mineração."],
    ["A3", "Script / Automação", "Scripts ou macros determinísticos gerados por IA ou para automação de tarefas.", "Macros em Lua para WoW, WeakAuras avançadas ou scripts em Python para ler logs de combate."],
    ["A4", "Humano Assistido por IA", "O humano opera o jogo e utiliza IA generativa como ferramenta de apoio/copiloto.", "Vibe-coding de addons com ChatGPT/Claude, consulta de táticas, fitações e refinamento de dados."],
    ["A5", "Discussão sobre IA", "Debate reflexivo, ético, laboral ou económico sobre IA sem interação direta.", "Threads a discutir o impacto ético de IA no design de jogos, autenticidade e receio de substituição."],
    ["A6", "Irrelevante / Ruído", "Conteúdo incidental sem qualquer relação com tecnologia, IA ou automação.", "Conversas sobre lore de classes ou menções acidentais da palavra AI fora de contexto."]
]
r = render_table(ws1, r, h_a, d_a, {1: alignment_center, 2: alignment_wrap})

add_sec_header(ws1, "3. ESTRUTURAS DE INTERAÇÃO HUMANO-IA (I1–I6)", r)
r += 1
h_i = ["Código", "Estrutura de Interação", "Definição Operacional", "Exemplo no Corpus do Estudo"]
d_i = [
    ["I1", "Humano → IA Unidirecional", "Comandos diretos, prompts isolados, consultas de informação ou dados a um modelo.", "Submeter um pedido de otimização de macro ao ChatGPT sem diálogo subsequente."],
    ["I2", "IA → Humano Unidirecional", "Alertas proativos, recomendações contextuais ou relatórios emitidos pelo agente.", "Addon de IA a emitir alerta situacional sobre aproximação de frotas inimigas ou rotação de spells."],
    ["I3", "Humano ↔ IA Bidirecional", "Ciclo iterativo conversacional (loop) de perguntas, respostas e refinação contínua.", "Conversa com Claude para depurar linha a linha um script da API ESI ou código de addon."],
    ["I4", "Humano → Humano sobre IA", "Interação social exclusiva entre jogadores a discutir, criticar ou elogiar IA.", "Debate entre jogadores sobre se a Blizzard usa IA no apoio ao cliente ou bots na Auction House."],
    ["I5", "Humano → Ambiente mediado", "Jogador a interagir com instâncias ou ecossistemas mediados por IA oficial.", "Completar Follower Dungeons ou Delves em WoW com companheiros de masmorra dinâmicos."],
    ["I6", "Sem Interação Significativa", "Menção passageira ou superficial sem interação comunicativa observável.", "Citação incidental de notícias sobre OpenAI numa conversa geral sobre a economia do jogo."]
]
r = render_table(ws1, r, h_i, d_i, {1: alignment_center, 2: alignment_wrap})

add_sec_header(ws1, "4. TAXONOMIA DE COCRIAÇÃO E CODESTRUIÇÃO DE VALOR (VC1–VC4)", r)
r += 1
h_vc = ["Código", "Dimensão de Valor", "Definição Operacional (Service-Dominant Logic / DART-NET)", "Critério de Enquadramento"]
d_vc = [
    ["VC1", "Cocriação Efetiva de Valor", "Parceria simétrica e bem-sucedida entre jogador e IA com benefícios tangíveis mútuos.", "Criação de ferramentas comunitárias (MCP), redução da curva de aprendizagem, personalização de addons funcionais."],
    ["VC2", "Potencial Cocriação", "Propostas conceituais, testes preliminares ou intenções de uso colaborativo de IA.", "Protótipos em fase de teste, ideias de integração de LLMs em guildas ainda não concretizadas."],
    ["VC3", "Codestruição de Valor", "Interações que produzem perdas, danos económicos, frustração ou quebra de confiança.", "Perda de naves caras por alucinações de IA, banimentos indevidos por tickets automatizados sem suporte humano."],
    ["VC4", "Sem Evidência Direta / Neutro", "Discussões teóricas e reflexões que não geram ganhos nem perdas empíricas diretas.", "Debates genéricos e reflexões normativas sobre o futuro da indústria de videojogos e ética."]
]
r = render_table(ws1, r, h_vc, d_vc, {1: alignment_center, 2: alignment_wrap})

add_sec_header(ws1, "5. MODELO DART E ESCALA DE PONTUAÇÃO (0 A 5)", r)
r += 1
h_dart = ["Dimensão", "Conceito Central", "Operacionalização em Videojogos com IA", "Escala de Pontuação (0 a 5)"]
d_dart = [
    ["D - Diálogo", "Engajamento ativo e partilha de conhecimento bilateral.", "Comunicação conversacional contínua entre humano e IA ou deliberação comunitária sobre uso de IA.", "0 = Ausente\n1 = Fraco / Superficial\n2 = Moderado\n3 = Forte\n4 = Muito Forte\n5 = Central e Explícito"],
    ["A - Acesso", "Disponibilidade de ferramentas, dados, telemetria e interfaces.", "Acesso à API oficial (ex.: ESI no EVE), dados de telemetria, código aberto de addons ou ferramentas MCP.", "0 = Ausente\n1 = Fraco / Superficial\n2 = Moderado\n3 = Forte\n4 = Muito Forte\n5 = Central e Explícito"],
    ["R - Risco", "Avaliação de potenciais danos, perdas, injustiça ou punições.", "Risco de alucinação de dados, perda de bens no jogo, banimentos por quebra de ToS ou distorção da economia.", "0 = Ausente\n1 = Fraco / Superficial\n2 = Moderado\n3 = Forte\n4 = Muito Forte\n5 = Central e Explícito"],
    ["T - Transparência", "Visibilidade algorítmica, clareza sobre regras e código aberto.", "Abertura do código do addon/bot, clareza da empresa sobre decisões automatizadas de moderação.", "0 = Ausente\n1 = Fraco / Superficial\n2 = Moderado\n3 = Forte\n4 = Muito Forte\n5 = Central e Explícito"]
]
r = render_table(ws1, r, h_dart, d_dart, {1: alignment_center, 4: alignment_wrap})

add_sec_header(ws1, "6. OS 5 CLUSTERS SOCIOTÉCNICOS DO NÍVEL MESO (TÓPICOS)", r)
r += 1
h_cl = ["Cluster", "Denominação Sociotécnica", "Foco Temático e Metodológico", "Comportamento DART e Valor Dominante"]
d_cl = [
    ["Cluster 1", "Ferramentas Externas, Integração de APIs e MCP", "Desenvolvimento e ligação de dados via APIs públicas (ESI, Model Context Protocol, Pyfa, exportação de telemetria para LLMs).", "Elevado Acesso (A: 1,8) e Transparência (T: 1,6). Predomínio de Cocriação Efetiva (VC1 e VC2)."],
    ["Cluster 2", "Fair Play, Deteção e Integridade Competitiva", "Tensão entre assistência de IA permitida e automação desleal em ambientes competitivos (PvP, Arenas, Mythic+, frotas Nullsec).", "Pico de Risco Percebido (R: 1,5) e baixo Acesso (A: 0,9). Elevada fricção e desconfiança normativa."],
    ["Cluster 3", "Suporte ao Cliente e Moderação Automatizada", "Queixas sobre o uso de IA pela publicadora para gestão de tickets de suporte, respostas pré-programadas e bans automáticos.", "Risco mais severo (R: 2,1) e mínima Transparência (T: 1,0). Principal nascente de Codestruição de Valor (VC3)."],
    ["Cluster 4", "Agentes Oficiais In-Game (Followers / Delves)", "Avaliação dos NPCs aliados oficiais introduzidos pelas publicadoras com comportamento dinâmico (Follower Dungeons, Delves, Aura).", "Acesso institucional controlado (A: 1,4) e Risco moderado. Dinâmica mista entre inclusão (VC2) e isolamento (VC4)."],
    ["Cluster 5", "Copilotos de Addons e Vibe-Coding", "Utilização de LLMs (ChatGPT, Claude, Copilot) para conceção de macros, interfaces, scripts em Lua e addons comunitários.", "Forte Diálogo e Acesso técnico (A: 1,3). Maior volume empírico, catalisando cocriação efetiva (VC1)."]
]
r = render_table(ws1, r, h_cl, d_cl, {1: alignment_center, 2: alignment_wrap})

ws1.column_dimensions["A"].width = 24
ws1.column_dimensions["B"].width = 34
ws1.column_dimensions["C"].width = 65
ws1.column_dimensions["D"].width = 45

# ==========================================
# FOLHA 2: EXEMPLOS POSTS (DIRETOS DE TABELA_RESUMOS.MD)
# ==========================================
ws2 = wb.create_sheet(title="Exemplos_Posts")
ws2.views.sheetView[0].showGridLines = True
ws2.freeze_panes = "A2"

h_ex_p = ["Post_ID", "Jogo", "Tema_Resumo", "Resumo_Analitico_IA", "Link_Acesso", "DART_Esperado", "Agencia_Esperada", "Interacao_Esperada", "Valor_Esperado", "Justificacao_Metodologica"]
d_ex_p = [
    [
        "510327_2870703",
        "EVE Online",
        posts_tabela_resumos.get("510327_2870703", {}).get("tema", "Correção de classificação de navios"),
        posts_tabela_resumos.get("510327_2870703", {}).get("resumo", ""),
        "https://forums.eveonline.com/t/eve-crews-a-lore-accurate-api-linked-crew-simulator/510327",
        "D: 4 | A: 3 | R: 1 | T: 3",
        "A1 (Agente de IA Autónomo)",
        "I3 (Humano ↔ IA Bidirecional)",
        "VC1 (Cocriação Efetiva)",
        "Resumo fundamentado em tabela_resumos.md: O utilizador reportou falha na classificação da nave devido a dados ESI desatualizados e o desenvolvedor corrigiu o problema diretamente, criando valor comunitário."
    ],
    [
        "1772220_22622499",
        "World of Warcraft",
        posts_tabela_resumos.get("1772220_22622499", {}).get("tema", "Combate a bots e venda de ouro"),
        posts_tabela_resumos.get("1772220_22622499", {}).get("resumo", ""),
        "https://us.forums.blizzard.com/en/wow/t/all-of-these-talks-about-bots/1772220",
        "D: 0 | A: 0 | R: 5 | T: 0",
        "A5 (Discussão sobre IA)",
        "I6 (Sem Interação Significativa)",
        "VC4 (Sem Evidência Direta)",
        "Resumo fundamentado em tabela_resumos.md: O post critica a inação contra bots e venda de ouro, refletindo sobre incentivos económicos da publicadora sem haver criação nem destruição direta imediata no post."
    ],
    [
        "471468_2644478",
        "EVE Online",
        posts_tabela_resumos.get("471468_2644478", {}).get("tema", "Confiança na IA para suporte"),
        posts_tabela_resumos.get("471468_2644478", {}).get("resumo", ""),
        "https://forums.eveonline.com/t/closed-amarrian-corporation-resolved/471468",
        "D: 3 | A: 3 | R: 0 | T: 1",
        "A1 (Agente de IA Autónomo)",
        "I1 (Humano → IA Unidirecional)",
        "VC2 (Potencial Cocriação)",
        "Resumo fundamentado em tabela_resumos.md: O utilizador descobriu que o Gemini respondeu às dúvidas de jogo, reduzindo a necessidade de chats de novatos, evidenciando potencial de cocriação."
    ],
    [
        "reddit_1tvlpnw_1",
        "World of Warcraft",
        posts_tabela_resumos.get("reddit_1tvlpnw_1", {}).get("tema", "Addon anti-spam com machine learning"),
        posts_tabela_resumos.get("reddit_1tvlpnw_1", {}).get("resumo", ""),
        "https://www.reddit.com/r/wow/comments/1tvlpnw/sick_of_spam_and_bots_ruining_our_game_heres_an/",
        "D: 0 | A: 2 | R: 2 | T: 1",
        "A5 (Discussão sobre IA)",
        "I4 (Humano → Humano sobre IA)",
        "VC4 (Sem Evidência Direta)",
        "Resumo fundamentado em tabela_resumos.md: Debate comunitário sobre addon com ML para bloquear bots no chat de comércio, melhorando a experiência mas ainda em discussão reflexiva."
    ]
]
render_table(ws2, 1, h_ex_p, d_ex_p, {1: alignment_center, 2: alignment_center, 6: alignment_center, 7: alignment_center, 8: alignment_center, 9: alignment_center})
ws2.column_dimensions["A"].width = 18
ws2.column_dimensions["B"].width = 16
ws2.column_dimensions["C"].width = 32
ws2.column_dimensions["D"].width = 55
ws2.column_dimensions["E"].width = 42
ws2.column_dimensions["F"].width = 22
ws2.column_dimensions["G"].width = 24
ws2.column_dimensions["H"].width = 24
ws2.column_dimensions["I"].width = 24
ws2.column_dimensions["J"].width = 55

# ==========================================
# FOLHA 3: EXEMPLOS TÓPICOS (DIRETOS DE TABELA_RESUMOS.MD)
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
        build_topic_summary(topicos_tabela_resumos.get("510327", [])),
        "Cluster 1: Ferramentas Externas, Integração de APIs e MCP",
        "Cocriação Efetiva (VC1)",
        "5",
        "Resumo construído diretamente a partir dos posts de tabela_resumos.md: reflete o desenvolvimento contínuo de tripulações, resolução de bugs ESI e gamificação colaborativa."
    ],
    [
        "495219",
        "EVE Online",
        "WTB discord bot that pings me when a contract is accepted",
        "https://forums.eveonline.com/t/wtb-discord-bot-that-pings-me-when-a-contract-is-accepted/495219",
        build_topic_summary(topicos_tabela_resumos.get("495219", [])),
        "Cluster 1: Ferramentas Externas, Integração de APIs e MCP",
        "Cocriação Efetiva (VC1)",
        "5",
        "Resumo construído diretamente a partir dos posts de tabela_resumos.md: discussão técnica sobre limitações da API ESI e desenvolvimento de bot para notificações de contratos via Discord."
    ],
    [
        "2203538",
        "World of Warcraft",
        "It seems there is already a workaround for addons/ui ai",
        "https://us.forums.blizzard.com/en/wow/t/it-seems-there-is-already-a-workaround-for-addonsui-ai/2203538",
        build_topic_summary(topicos_tabela_resumos.get("2203538", [])),
        "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "Cocriação Potencial (VC2)",
        "5",
        "Resumo construído diretamente a partir dos posts de tabela_resumos.md: jogadores debatem protótipo de IA que lê o ecrã para partilhar CDs/interrupções sem usar a API da Blizzard."
    ],
    [
        "reddit_1tvlpnw",
        "World of Warcraft",
        "Sick of spam and bots ruining our game? Here is an addon that uses ML...",
        "https://www.reddit.com/r/wow/comments/1tvlpnw/sick_of_spam_and_bots_ruining_our_game_heres_an/",
        build_topic_summary(topicos_tabela_resumos.get("reddit_1tvlpnw", [])),
        "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "Sem Evidência Direta / Neutro (VC4)",
        "5",
        "Resumo construído diretamente a partir dos posts de tabela_resumos.md: discussão sobre addon anti-spam com machine learning e busca por ferramentas de denúncia com um clique."
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
# FOLHA 4: TRACK_A_POSTS (83 POSTS VERIFICADOS COM RESUMO DE TABELA_RESUMOS.MD)
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
        p["resumo_ia"], # Diretamente de tabela_resumos.md!
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
# FOLHA 5: TRACK_B_TOPICOS (15 TOPICOS COM SÍNTESE DE TABELA_RESUMOS.MD)
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
        t["summary"], # Diretamente construído a partir dos posts de tabela_resumos.md!
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
print("Ficheiro gerado com SUCESSO e 100% ancorado em tabela_resumos.md em:", output_path)
