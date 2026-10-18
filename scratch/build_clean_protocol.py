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

# Resumos analíticos aprofundados e detalhados dos 15 tópicos da Track B (baseados em resumos_discussoes_topicos.md; estritamente <= 150 palavras)
resumos_analiticos_topicos = {
    "1tdxixs": enforce_max_words(
        "Discussão comunitária sobre o anúncio do CEO da CCP Games, Hilmar Pétursson, referente à integração de inteligência artificial generativa e blockchain no ecossistema de EVE Online. O debate é dominado por um tom marcadamente cético, sarcástico e irónico, onde os jogadores ridicularizam o alinhamento com modas corporativas e termos de marketing desprovidos de utilidade lúdica tangível. Embora alguns utilizadores admitam hipóteses especulativas de cocriação potencial (VC2) na sofisticação tática de NPCs ou em copilotos de mercado, a esmagadora maioria expressa receio de codestruição de valor (VC3). As críticas convergem para a desconfiança em modelos preditivos opacos, o risco de monetização agressiva via tokens e o desvio de recursos de desenvolvimento essenciais para a correção da dívida técnica acumulada no jogo.",
        150
    ),
    "2039353": enforce_max_words(
        "O tópico aborda a tentativa de utilizar o ChatGPT para decifrar, calcular e prever o funcionamento do sistema oculto de Matchmaking Rating (MMR) no PvP competitivo de World of Warcraft. A discussão divide-se entre jogadores que procuram assistência cognitiva da IA para compreender flutuações de rating e veteranos que demonstram a falibilidade dos LLMs perante algoritmos proprietários e não documentados da Blizzard. Evidenciam-se episódios de codestruição de valor (VC3) decorrentes de alucinações matemáticas convincentes, nas quais a IA gera fórmulas plausíveis mas inteiramente erradas, induzindo os utilizadores em erro sobre ganhos de pontuação. O debate conclui que a IA opera como um simulador de certezas estatísticas sem acesso a dados reais, reforçando a necessidade de escrutínio crítico humano e transparência algorítmica inexistente na infraestrutura oficial.",
        150
    ),
    "510327": enforce_max_words(
        "Apresentação e desenvolvimento colaborativo do simulador comunitário 'EVE Crews', que articula a API pública ESI de EVE Online com o assistente Claude para estimar e simular tripulações em naves espaciais com base no cânone oficial e no volume dos cascos. Trata-se de um caso emblemático de cocriação efetiva de valor (VC1) e cooperação triádica simétrica (Humano-IA-Comunidade). Os utilizadores testam a aplicação, apontam discrepâncias em naves capitais e o programador, assistido iterativamente pelo modelo, reescreve as regras de inferência e publica atualizações em tempo real. Destaca-se a elevada transparência do projeto através de um painel de diagnóstico público que expõe a lógica de decisão do agente, mitigando riscos de alucinação e democratizando o acesso a dados complexos de telemetria para a comunidade.",
        150
    ),
    "1mctiz6": enforce_max_words(
        "O autor relata a sua experiência ao utilizar o Google Gemini como copiloto criativo de brainstorming para conceber conceitos operacionais e teorias de jogo em EVE Online. A comunidade reage com uma mistura de humor e debate reflexivo (VC4 e potencial VC2), explorando a utilidade de assistentes generativos na ideação preliminar sem substituição do discernimento humano. Embora a IA demonstre capacidade para estruturar ideias narrativas e estratégias organizacionais de corporação, os participantes sublinham limitações severas em tarefas numéricas rigorosas, como o balanceamento de slots de montagem (fitting) e consumo de energia, onde o modelo alucina atributos inexistentes. A discussão evidencia que a IA funciona eficazmente como parceiro de diálogo conceitual, mas exige validação empírica humana contínua em mecânicas sistémicas.",
        150
    ),
    "481937": enforce_max_words(
        "O tópico debate o impacto económico da mecânica de compressão de minério em EVE Online, questionando se a facilidade logística representa uma vantagem desproporcional para operações automatizadas de mineração (bots). O post inicial denuncia que a compressão permite projetar minério de regiões isoladas e remotas diretamente para os mercados centrais, quebrando barreiras naturais de transporte. A intervenção comunitária contesta essa visão binária, salientando que a funcionalidade beneficia igualmente industriais, mineradores e transportadores legítimos. A discussão exemplifica a tensão sociotécnica contínua em torno de risco e justiça distributiva: melhorias de qualidade de vida desenhadas para jogadores humanos reduzem simultaneamente o atrito operacional para scripts ilícitos, alimentando receios de inflação e desestabilização económica sem que haja falha intrínseca na tecnologia.",
        150
    ),
    "reddit_1rnbqbh": enforce_max_words(
        "Discussão em r/wow na qual os jogadores debatem se os textos de missões recentes de World of Warcraft foram redigidos por modelos de IA generativa, apontando repetições estilísticas, descrições genéricas e perda de profundidade narrativa. A comunidade divide-se entre suspeitas de automatização opaca ('AI slop') por parte da Blizzard para cortar custos operacionais e argumentos de que a degradação na escrita decorre de prazos apertados, despedimentos em equipas criativas e sobrecarga de pessoal humano. O debate reflete forte sensibilidade à Transparência e codestruição de valor relacional (VC3), com exigências de rotulagem explícita caso ferramentas generativas sejam integradas. Conclui-se que, independentemente da autoria algorítmica real, a perceção de desumanização textual corrói a imersão e a confiança na publicadora.",
        150
    ),
    "503747": enforce_max_words(
        "Debate macro-sociológico e reflexivo no fórum oficial de EVE Online sobre as repercussões da inteligência artificial avançada e da automação na economia global, no mercado de trabalho e na sua transposição para o ecossistema virtual do jogo. Os utilizadores analisam paralelos históricos de revoluções industriais, o impacto da IA generativa na desvalorização do trabalho intelectual e o risco de concentração de riqueza e desigualdade sistémica. No contexto do jogo, discute-se como agentes autónomos podem quebrar o valor do esforço humano na mineração e na produção industrial, alterando incentivos de participação lúdica. O tom varia entre especulação filosófica fria e ironia mordaz sobre a substituição de funções comunitárias, categorizando-se predominantemente em VC4 com elevada saliência de Risco percebido.",
        150
    ),
    "2152188": enforce_max_words(
        "Relato de um bug no cliente de jogo envolvendo mascotes felinas no qual o utilizador, ao submeter tickets de suporte à Blizzard, recebe respostas genéricas, desconexas e inadequadas, atribuídas a um sistema automatizado opaco ('ChatGPT GM'). A comunidade reage com profunda indignação e frustração coletiva, partilhando episódios idênticos de encerramento arbitrário de chamados sem qualquer diagnóstico técnico humano. Trata-se de uma evidência cabal de codestruição severa de valor (VC3), onde a substituição de Game Masters qualificados por respostas algorítmicas padronizadas destrói a confiança institucional, elimina o diálogo efetivo e aliena os jogadores pagantes. A discussão critica a opacidade da publicadora e exige a reintegração imperativa de humanos no circuito de atendimento e suporte ao cliente.",
        150
    ),
    "1i6m4i6": enforce_max_words(
        "O autor analisa criticamente a promessa de que a IA 'revolucionará o mundo', testando o ChatGPT e o Google Gemini em consultas de navegação e missões em World of Warcraft. A discussão contrasta a precisão direta do ChatGPT com os desvios alucinatórios e pedidos de desculpa teatrais do Gemini ao sugerir rotas absurdas entre Orgrimmar e Ratchet. A comunidade explora este contraste com humor e anedotas profissionais, sublinhando o fenómeno da IA 'confiantemente incorreta'. Estabelece-se o consenso de que os LLMs podem atuar como copilotos úteis (A4), mas exigem que o jogador detenha conhecimento prévio suficiente para identificar erros crassos, concluindo que o uso acrítico de respostas generativas sem escrutínio humano gera desinformação e momentos cómicos no ecossistema lúdico.",
        150
    ),
    "reddit_1q7m0sl": enforce_max_words(
        "Debate sobre a introdução especulativa de um assistente conversacional inteligente ('Aura AI') para apoio a jogadores em World of Warcraft. A comunidade polariza-se: jogadores pragmáticos reconhecem potencial de cocriação (VC2) na redução da íngreme curva de aprendizagem para novatos, argumentando que alucinações de jogo acarretam baixo risco face à desinformação frequente em canais de ajuda. Em oposição, utilizadores céticos rejeitam a proliferação de 'AI slop', temendo que a publicadora substitua tutoriais nativos por saídas probabilísticas imprecisas. Emerge a exigência rigorosa de que qualquer assistente seja estritamente opcional (opt-in), respeite o cânone narrativo e permaneça confinado ao auxílio contextual sem interferir no mistério e na descoberta fundamentais da experiência MMORPG.",
        150
    ),
    "2116712": enforce_max_words(
        "Denúncia técnica e contundente sobre a proliferação descontrolada de 'pixel bots' no PvP competitivo (arenas e Solo Shuffle) de World of Warcraft. O autor e outros jogadores experientes descrevem como a barreira de entrada da batota foi eliminada pela conjugação de WeakAuras de um pixel com scripts Python gerados em minutos por LLMs (ChatGPT). Estes sistemas executam interrupções de feitiço e salvaguardas defensivas com tempos de reação sub-humanos (<100ms) e padrões que simulam aleatoriedade para contornar a deteção. O tópico ilustra um cenário extremo de codestruição de valor (VC3) impulsionado por IA: destruição do fair play, erosão da integridade competitiva e revolta comunitária perante a incapacidade e passividade do sistema anti-cheat da Blizzard em banir infratores.",
        150
    ),
    "512367": enforce_max_words(
        "Proposta detalhada de design conceptual defendendo a criação do 'Ask Aura', um assistente de IA circunscrito (bounded AI) desenhado para atuar exclusivamente como intérprete contextual de documentação oficial, cânone, patch notes e manuais da EVE Academy, sem permissão para inventar conteúdo generativo. A comunidade acolhe favoravelmente o rigor metodológico da proposta, mas identifica desafios técnicos incontornáveis: mesmo sistemas ancorados em recuperação de informação (RAG) sofrem alucinações semânticas que podem disseminar erros graves em mecânicas complexas. Adicionalmente, debate-se o risco sociocultural de desvalorizar o vasto repositório de wikis e guias gerados pela própria comunidade, que constituem pilares históricos da sociabilidade e cocriação de valor (VC1/VC2) no ecossistema de New Eden.",
        150
    ),
    "reddit_1kylpvy": enforce_max_words(
        "O autor partilha a utilização do ChatGPT Plus para planear e conciliar horários de trabalho com a rotação de assaltos no World of Warcraft, propondo a evolução de companheiros de IA integrados no jogo. A comunidade analisa criticamente a dualidade da ferramenta: reconhece-se utilidade real como copiloto organizacional e de roleplay (A4/VC2), mas alertam-se para falhas graves decorrentes de bases de dados desatualizadas face a patches recentes do WoW. Os participantes recomendam verificação cruzada obrigatória com o Wowhead e destacam ferramentas especializadas comunitárias (como Gylvessa) que superam modelos genéricos. O debate ilustra como a assistência de IA ganha relevância quando confinada à organização e à criação narrativa, exigindo sempre validação humana externa contra mecânicas ativas.",
        150
    ),
    "2176376": enforce_max_words(
        "Discussão concisa focada no desejo de servidores 'evergreen' com todo o conteúdo histórico desbloqueado, recorrendo a companheiros de grupo gerados por IA para viabilizar masmorras e raids antigas sem dependência de grupos humanos, contornando o modelo sazonal e a remoção de recompensas (FOMO). Os participantes distinguem rigorosamente scripts determinísticos convencionais de agentes inteligentes de IA, apontando que servidores privados funcionam como laboratórios pioneiros para testes de automação cooperativa antes da sua adoção oficial (como nas Follower Dungeons). O tema oscila entre o potencial de inclusão e acessibilidade para jogadores a solo (VC2) e a reflexão sobre o impacto do isolamento social num ecossistema cuja premissa ontológica é a interação multijogador em massa (VC4).",
        150
    ),
    "reddit_1r1dd9i": enforce_max_words(
        "Análise técnica profunda elaborada por um engenheiro de software demonstrando os mecanismos que levam addons desenvolvidos via vibe coding (código gerado por IA sem auditoria) a causar quebras drásticas de taxa de frames (FPS) no World of Warcraft. O debate examina falhas de arquitetura em Lua, tais como o uso indiscriminado do manipulador OnUpdate (que reexecuta a cada frame) em vez de eventos orientados (BAG_UPDATE_DELAYED), ineficiências de garbage collection e ausência de tratamento de exceções. Embora contraexemplos empíricos provem que prompts refinados geram código eficiente, a comunidade conclui que a IA atua como um multiplicador de competência: amplia a produtividade de programadores experientes (VC1), mas propaga código disfuncional e codestruição de performance (VC3) quando manuseada por utilizadores desprovidos de literacia técnica.",
        150
    )
}

def get_topic_synthesis(tid, posts_list, fallback_title=""):
    if tid in resumos_analiticos_topicos:
        return resumos_analiticos_topicos[tid]
    # Se presente em topic_insights, sintetizar
    if tid in topic_insights:
        ext = topic_insights[tid].get("resumo_extenso_discussao", "")
        if ext:
            return enforce_max_words(ext, 150)
    if not posts_list:
        return f"Discussão sobre {fallback_title} nos fóruns comunitários."
    resumos_text = " ".join([p["resumo"] for p in posts_list[:3]])
    return enforce_max_words(f"A comunidade debate os seguintes aspetos em torno do tema: {resumos_text}", 150)

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
        "summary": enforce_max_words(get_topic_synthesis(tid, t_posts, t.get("title", "")), 150),
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

add_sec_header(ws1, "2. DIRETRIZES DE AUDITORIA, FIDELIDADE DE SÍNTESE E EXTENSÃO ANALÍTICA", r + 1, "D")
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
    "REGRAS METODOLÓGICAS DE EXTENSÃO:\n"
    "• Track A (Posts Individuais): Resumos analíticos concisos respeitando o limite estrito de no máximo 60 palavras.\n"
    "• Track B (Tópicos de Discussão): Resumos analíticos aprofundados baseados nas discussões dos tópicos, com extensão detalhada de no máximo 150 palavras."
)
c_desc.font = font_cell
c_desc.alignment = alignment_wrap
ws1.row_dimensions[r+2].height = 145
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
# ==========================================
# FOLHA 3: EXEMPLOS TÓPICOS (ATUALIZADOS E <= 150 PALAVRAS)
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
            "Apresentação e desenvolvimento colaborativo do simulador comunitário 'EVE Crews', que articula a API pública ESI de EVE Online com o assistente Claude para estimar e simular tripulações em naves espaciais com base no cânone oficial e no volume dos cascos. Trata-se de um caso emblemático de cocriação efetiva de valor (VC1) e cooperação triádica simétrica (Humano-IA-Comunidade). Os utilizadores testam a aplicação, apontam discrepâncias em naves capitais e o programador, assistido iterativamente pelo modelo, reescreve as regras de inferência e publica atualizações em tempo real. Destaca-se a elevada transparência do projeto através de um painel de diagnóstico público que expõe a lógica de decisão do agente, mitigando riscos de alucinação e democratizando o acesso a dados complexos de telemetria para a comunidade.",
            150
        ),
        "Cluster 1: Ferramentas Externas, Integração de APIs e MCP",
        "Cocriação Efetiva (VC1)",
        "5",
        "Resumo detalhado de 121 palavras fiel à discussão: reflete a arquitetura API/Claude, resolução colaborativa de bugs e transparência de diagnóstico."
    ],
    [
        "508618",
        "EVE Online",
        "Recorded a bot in high sec - but why even bother?",
        "https://forums.eveonline.com/t/recorded-a-bot-in-high-sec-but-why-even-bother/508618",
        enforce_max_words(
            "Discussão reflexiva e desiludida no fórum de EVE Online iniciada por um jogador que gravou e denunciou um minerador automatizado (bot) no espaço de alta segurança (highsec), questionando a utilidade do esforço. A comunidade reage com cinismo e frustração acumulada, partilhando evidências de ineficácia nas punições da CCP e contorno trivial de banimentos de IP através de VPNs e novas contas. Trata-se de um caso marcante de codestruição de valor (VC3) motivado por desamparo institucional e baixa Transparência nas ações da editora. O debate aprofunda as motivações do Real Money Trading (RMT) e a assimetria entre o custo de reportar e a imunidade percebida dos operadores de bots, consolidando um sentimento de abandono da integridade económica do jogo.",
            150
        ),
        "Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning",
        "Codestruição de Valor (VC3)",
        "5",
        "Resumo aprofundado de 118 palavras: retrata fielmente o cinismo comunitário, a erosão de confiança institucional e a codestruição de valor por bots impunes."
    ],
    [
        "reddit_1tvlpnw",
        "World of Warcraft",
        "Sick of spam and bots ruining our game? Here is an addon that uses ML...",
        "https://www.reddit.com/r/wow/comments/1tvlpnw/sick_of_spam_and_bots_ruining_our_game_heres_an/",
        enforce_max_words(
            "Apresentação e escrutínio comunitário de uma proposta de addon para World of Warcraft desenhado para utilizar algoritmos de Machine Learning locais na deteção e filtragem em tempo real de mensagens de spam, publicidade ilícita e serviços de boosting nos canais de conversação públicos. A comunidade debate a viabilidade técnica da solução, levantando preocupações sobre falsos positivos, sobrecarga computacional de inferência no cliente e o risco de retaliação ou exploração por parte dos spammers. Classificado predominantemente em VC4 com potencial VC2, o tópico reflete o esforço proativo de jogadores em criar barreiras defensivas inteligentes contra a poluição conversacional, enquanto questiona a ausência de soluções nativas eficazes implementadas diretamente pela Blizzard nos servidores oficiais.",
            150
        ),
        "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "Reflexão Crítica sobre Valor (VC4)",
        "5",
        "Resumo denso de 112 palavras: capta o debate sobre viabilidade de ML local no cliente, risco de falsos positivos e inação da publicadora."
    ],
    [
        "reddit_1v3v2p2",
        "World of Warcraft",
        "Claude Code Success",
        "https://www.reddit.com/r/wow/comments/1v3v2p2/claude_code_success/",
        enforce_max_words(
            "Relato de sucesso empírico no qual um programador comunitário de World of Warcraft documenta a utilização da ferramenta de IA generativa Claude Code para atualizar e restaurar o funcionamento de um addon complexo de interface danificado por alterações recentes de patch. O autor detalha o fluxo iterativo de colaboração simétrica com o agente: fornecimento do anúncio técnico oficial da Blizzard (blue post), diagnóstico de regressões no código Lua e aplicação guiada de correções lógicas. Trata-se de uma demonstração explícita de cocriação efetiva de valor (VC1) e vibe-coding assistido de alta eficácia, ilustrando como copilotos de IA democratizam a manutenção de software comunitário e reduzem o tempo de reparação de ferramentas vitais para a experiência lúdica.",
            150
        ),
        "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "Cocriação Efetiva (VC1)",
        "5",
        "Resumo fiel de 115 palavras: detalha o ciclo iterativo com Claude Code, superação de quebras de API pós-patch e cocriação de valor."
    ]
]
render_table(ws3, 1, h_ex_t, d_ex_t, {1: alignment_center, 2: alignment_center, 6: alignment_wrap, 7: alignment_center, 8: alignment_center})
ws3.column_dimensions["A"].width = 16
ws3.column_dimensions["B"].width = 16
ws3.column_dimensions["C"].width = 38
ws3.column_dimensions["D"].width = 42
ws3.column_dimensions["E"].width = 75
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
        enforce_max_words(p["resumo_ia"], 60), # Resumo do post conciso <= 60 palavras
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
# FOLHA 5: TRACK_B_TOPICOS (15 TOPICOS COM RESUMOS DETALHADOS <= 150 PALAVRAS)
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
        enforce_max_words(t["summary"], 150), # Resumo do tópico aprofundado <= 150 palavras
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
ws5.column_dimensions["E"].width = 80
for col_l in ["F", "G", "H", "I", "J", "K", "L"]:
    ws5.column_dimensions[col_l].width = 26

output_path = "output/Protocolo_Auditoria_Humana_Formatado.xlsx"
wb.save(output_path)
print("Ficheiro gerado com SUCESSO com resumos aprofundados (Track B <= 150 palavras, Track A <= 60 palavras) em:", output_path)
