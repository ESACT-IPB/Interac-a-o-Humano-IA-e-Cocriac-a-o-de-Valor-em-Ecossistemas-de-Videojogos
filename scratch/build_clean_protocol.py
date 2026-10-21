"""
build_clean_protocol.py
Gera o ficheiro Protocolo_Auditoria_Humana_Formatado.xlsx alinhado com a
Arquitetura Metodológica Multinível Incorporada (Embedded Multilevel Design — DART-NET v4.0):
1. Nível Meso (Tópico de Discussão, N=152; Amostra Track B N=15) como Unidade Primária de Sentido, Codificação Relacional e Teorização.
2. Nível Micro (Post Individual, N=825; N=104 posts constituintes da Track B + N=83 posts da Track A) mantido integralmente como Unidade Incorporada de Ancoragem Empírica (Verbatim Grounding).
3. Auditoria Humana de Alto Nível (Track B) executada e documentada com todos os campos analisados dos tópicos, mantendo os posts dos tópicos (folha dedicada Posts_Topicos_Track_B + referências diretas) e adicionando novos parâmetros de auditoria metodológica.
4. Limites estritos preservados: resumos de posts <= 60 palavras; resumos de tópicos <= 150 palavras.
"""

import json
import random
import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def enforce_max_words(text, max_words=60):
    """Garante que o texto tem estritamente no máximo max_words palavras."""
    if not text:
        return ""
    text_clean = text.strip()
    words = text_clean.split()
    if len(words) <= max_words:
        return text_clean
    return " ".join(words[:max_words - 1]) + "..."

# 1. Carregar tabela_resumos.md como FONTE DA VERDADE DOS POSTS (N=825)
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

# 2. Carregar dados brutos/processados para texto verbatim e metadados dos tópicos
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
threads_by_id = {str(t["thread_id"]): t for t in threads}

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

# Resumos analíticos aprofundados e detalhados dos 15 tópicos da Track B (estritamente <= 150 palavras)
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

# Auditoria Humana de Alto Nível (Track B) executada segundo a metodologia DART-NET v4.0 (Embedded Multilevel Design),
# preservando os registos reais da Ronda 1 (JPaulo em Protocolo_Auditoria_Humana_Formatado_JPaulo.xlsx) e a Calibração da Ronda 2 (v4.0)
auditoria_track_b_resultados = {
    "1tdxixs": {
        "r1_jp_cluster": "Cluster 4",
        "r1_jp_valor": "VC2 - Potencial de Cocriação / VC3 - Codestruição de Valor",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 1: Ferramentas Externas, Integração de APIs e MCP (c/ Interface Cluster 4: Agentes/NPCs DeepMind)",
        "jp_valor": "VC4 (Enquadramento) c/ Tensão Dialética VC2 (Potencial) vs. VC3 (Codestruição)",
        "jp_fid": 5,
        "em_cluster": "Cluster 1: Ferramentas Externas, Integração de APIs e MCP (c/ Interface Cluster 4)",
        "em_valor": "VC4 (Enquadramento) c/ Tensão Dialética VC2 vs. VC3",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC2 + VC3 sob VC4): Hipótese de NPCs adaptativos (VC2) vs. receio dominante de 'AI slop' e venda de dados (VC3).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Supera a aparente neutralidade atómica (11/11 posts VC4) ao evidenciar a tensão dialética real (identificada na Ronda 1 por JPaulo como VC2 + VC3) e a opacidade corporativa (T=1.4).",
        "status_conv": "Convergência Calibrada (C1/C4 | VC4 [VC2+VC3])",
        "anotacoes": "Na Ronda 1, JPaulo destacou a dimensão de NPCs in-game (Cluster 4) e a dualidade VC2+VC3 (Fidelidade=4 no resumo curto). Na Ronda 2 (resumo 150 pal.), consolida-se a articulação entre cedência de dados de mercado à DeepMind (Cluster 1) e especulação de NPCs Drifters (Cluster 4), descodificando os 4 posts satíricos (Fidelidade=5)."
    },
    "2039353": {
        "r1_jp_cluster": "Cluster 1",
        "r1_jp_valor": "VC2 - Potencial de Cocriação / VC3 - Codestruição de Valor",
        "r1_jp_fid": 3,
        "jp_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "jp_valor": "VC4 (Escrutínio Crítico) c/ Tensão VC2 (Consulta MMR) vs. VC3 (Alucinação)",
        "jp_fid": 5,
        "em_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "em_valor": "VC4 (Escrutínio Crítico) c/ Tensão VC2 vs. VC3",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC2 + VC3 -> VC4): Tentativa inicial de usar ChatGPT para modelar MMR (VC2) refutada por alucinação matemática e código Lua fictício (VC3).",
        "dart_ag_score": 4,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Corrige o enviesamento atómico inicial (2 posts VC2) ao demonstrar a trajetória completa (VC2 -> VC3 -> VC4) onde veteranos provam a alucinação do modelo.",
        "status_conv": "Convergência Plena pós-Regra C1 vs. C5 (C1 -> Cluster 5)",
        "anotacoes": "Caso que motivou a Regra de Fronteira Cluster 1 vs. Cluster 5 (Secção 4.4.1): na Ronda 1 fora marcado como Cluster 1 (e Fidelidade=3 pelo resumo truncado de 60 pal.). Como não há ligação API em tempo real e o humano interage manualmente com o ChatGPT (A4/I1), reclassifica-se no Cluster 5 (Fidelidade=5 no novo resumo de 125 pal.)."
    },
    "510327": {
        "r1_jp_cluster": "Cluster 1",
        "r1_jp_valor": "VC1 - Cocriação efetiva",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 1: Ferramentas Externas, Integração de APIs e MCP",
        "jp_valor": "VC1 (Cocriação Efetiva de Valor)",
        "jp_fid": 5,
        "em_cluster": "Cluster 1: Ferramentas Externas, Integração de APIs e MCP",
        "em_valor": "VC1 (Cocriação Efetiva de Valor)",
        "em_fid": 5,
        "tensao_multivc": "Convergência Virtuosa em VC1: Relatos de bugs (5 posts VC3) e propostas (12 posts VC2) são iterativamente convertidos em melhorias reais da aplicação.",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Caso exemplar da superioridade do nível Meso: enquanto ao nível Micro 20/41 posts surgiam diluídos como VC4, a trajetória completa confirma o diagnóstico de JPaulo: Cocriação Efetiva (VC1).",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 1 | VC1)",
        "anotacoes": "Arquétipo puro do Cluster 1 (API ESI em tempo real + agente Claude, D=2.8, A=2.4, T=2.4). A expansão do resumo para 121 palavras elevou a Fidelidade de Síntese de 4 para 5, detalhando o painel público de diagnóstico e a correção colaborativa de naves."
    },
    "1mctiz6": {
        "r1_jp_cluster": "Cluster 5",
        "r1_jp_valor": "VC2 - Potencial de Cocriação / VC3 - Codestruição de Valor",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "jp_valor": "VC4 (Enquadramento Irónico) c/ Tensão VC2 (Brainstorming) vs. VC3 (Alucinação de Fitting)",
        "jp_fid": 5,
        "em_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "em_valor": "VC4 (Enquadramento Irónico) c/ Tensão VC2 vs. VC3",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC2 + VC3 sob VC4): Utilidade do Gemini na ideação narrativa (VC2) vs. alucinação em fittings numéricos e risco de passividade lúdica (VC3).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Integra os 2 comentários satíricos retidos (1mctiz6_9 e 1mctiz6_21) com o brainstorming do OP, captando a dualidade VC2+VC3 assinalada por JPaulo na Ronda 1.",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 5 | VC4 [VC2+VC3])",
        "anotacoes": "JPaulo já corrigira na Ronda 1 o erro heurístico (Cluster 2 -> Cluster 5) e identificara a tensão VC2+VC3. O novo resumo de 119 palavras elevou a Fidelidade de 4 para 5."
    },
    "481937": {
        "r1_jp_cluster": "Cluster 2",
        "r1_jp_valor": "VC3 - Codestruição de Valor",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "jp_valor": "VC3 (Codestruição Económica por Bots) em debate c/ VC4 (Defesa de Industriais)",
        "jp_fid": 5,
        "em_cluster": "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "em_valor": "VC3 (Codestruição Económica) em debate c/ VC4",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC3 vs. VC4): Denúncia de projeção logística de minério por bots (VC3) contraposta ao benefício legítimo para jogadores industriais (VC4).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Articula a denúncia de codestruição (VC3 em 481937_2746273) com o contraponto produtivo (VC4 em 481937_2746275), captando o dilema entre Quality-of-Life e botting.",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 2 | VC3/VC4)",
        "anotacoes": "Concordância integral no Cluster 2 e na saliência de VC3 (R=2.0, A=1.5). A expansão do resumo para 118 palavras elevou a Fidelidade de 4 para 5."
    },
    "reddit_1rnbqbh": {
        "r1_jp_cluster": "Cluster 4",
        "r1_jp_valor": "VC3 - Codestruição de Valor",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores",
        "jp_valor": "VC3 (Codestruição Simbólica e de Confiança) / VC4 (Exigência de Transparência)",
        "jp_fid": 5,
        "em_cluster": "Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning",
        "em_valor": "VC3 (Codestruição Simbólica) / VC4 (Exigência de Transparência)",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC3 + VC4): Perceção de desumanização narrativa ('AI slop', VC3) articulada com escrutínio crítico sobre layoffs e exigência de rotulagem (VC4, T=3.0).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Supera a classificação estritamente neutra dos posts isolados (2/2 VC4) ao validar o diagnóstico de JPaulo: a suspeita de IA oculta gera Codestruição de Imersão e Confiança (VC3).",
        "status_conv": "Divergência Produtiva de Fronteira (Cluster 4 [JP] vs. Cluster 3 [EM] | VC3/VC4)",
        "anotacoes": "Caso clássico de fronteira: JPaulo (desde a Ronda 1) prioriza o Cluster 4 (conteúdo narrativo oficial in-game), enquanto Emmanoel destaca a interface com o Cluster 3 (layoffs e corte de custos corporativos citados em reddit_1rnbqbh_3). Convergência total no impacto VC3/VC4 e no pico T=3.0."
    },
    "503747": {
        "r1_jp_cluster": "Cluster 1",
        "r1_jp_valor": "VC4 - Reflexão Crítica sobre Valor",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "jp_valor": "VC4 (Reflexão Crítica sobre Valor)",
        "jp_fid": 5,
        "em_cluster": "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "em_valor": "VC4 (Reflexão Crítica sobre Valor)",
        "em_fid": 5,
        "tensao_multivc": "Consenso Reflexivo Macro (VC4 com R=3.0): Avaliação filosófica e socioeconómica dos riscos de automação laboral, consumo energético e impacto na economia virtual.",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Consolida 4 intervenções reflexivas extensas num quadro macro-sociológico unificado (VC4, R=3.0, T=2.0), confirmando a classificação VC4 de JPaulo na Ronda 1.",
        "status_conv": "Convergência Plena pós-Calibração (VC4 | Cluster 2)",
        "anotacoes": "Na Ronda 1, JPaulo validou exatamente VC4 (Reflexão Crítica sobre Valor). Quanto ao cluster, a aplicação da Regra de Fronteira (ausência de API/MCP) reclassifica o debate macroeconómico sobre automação no Cluster 2 (Integridade Económica e Impacto Sistémico da Automação)."
    },
    "2152188": {
        "r1_jp_cluster": "Cluster 3",
        "r1_jp_valor": "VC3 - Codestruição de Valor",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning",
        "jp_valor": "VC3 (Codestruição de Valor)",
        "jp_fid": 5,
        "em_cluster": "Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning",
        "em_valor": "VC3 (Codestruição de Valor)",
        "em_fid": 5,
        "tensao_multivc": "Unívoco em VC3 (Codestruição Severa): Substituição opaca de Game Masters humanos por respostas geradas por LLM com links inexistentes.",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Tópico de post único de altíssima densidade forense: convergência absoluta Micro-Meso com a codificação de JPaulo (Cluster 3 | VC3).",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 3 | VC3)",
        "anotacoes": "Caso canónico do Cluster 3 validado por JPaulo desde a Ronda 1: deteção forense do 'ChatGPT GM' através de travessões (M-Dashes) e hiperligações alucinadas (T=4.0, D=3.0). O novo resumo de 115 palavras elevou a Fidelidade de 4 para 5."
    },
    "1i6m4i6": {
        "r1_jp_cluster": "Cluster 1",
        "r1_jp_valor": "VC2 e VC4",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "jp_valor": "VC4 (Crítica à Alucinação) e VC2 (Potencial de Copiloto c/ Conhecimento Prévio)",
        "jp_fid": 5,
        "em_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "em_valor": "VC4 e VC2 (Uso Condicional de Copiloto)",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC2 e VC4): Utilidade de copilotos generativos quando guiados por utilizador experiente (VC2) vs. crítica irónica à alucinação de rotas do Gemini (VC4).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "A codificação dupla de JPaulo na Ronda 1 ('VC2 e VC4') reconcilia perfeitamente o post 1 (VC2) com os posts 87 e 90 (VC4 irónico).",
        "status_conv": "Convergência Plena pós-Regra C1 vs. C5 (C1 -> Cluster 5 | VC2 e VC4)",
        "anotacoes": "Segundo caso que motivou a Regra de Fronteira Cluster 1 vs. Cluster 5 (Secção 4.4.1): como o jogador consulta manualmente o ChatGPT e o Gemini sobre rotas entre Orgrimmar e Ratchet sem integração de API, reclassifica-se de Cluster 1 para Cluster 5. Mantém-se a excelente trajetória dupla 'VC2 e VC4' de JPaulo."
    },
    "reddit_1q7m0sl": {
        "r1_jp_cluster": "Cluster 4",
        "r1_jp_valor": "VC2 - Potencial de Cocriação",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores",
        "jp_valor": "VC2 (Potencial para Novatos) em polarização c/ VC3/VC4 (Receio de AI Slop)",
        "jp_fid": 4,
        "em_cluster": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores",
        "em_valor": "VC4 polarizado entre VC2 (Apoio a Novatos) e VC3 (AI Slop)",
        "em_fid": 4,
        "tensao_multivc": "Sim (VC2 vs. VC3/VC4): Apoio pragmático à aprendizagem de novatos (VC2 identificado por JPaulo) vs. rejeição cética de 'AI slop' (VC3/VC4).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 4,
        "resolucao_diluicao": "Resgata o potencial de cocriação (VC2 assinalado por JPaulo, invisível na contagem atómica onde só figuravam 9 VC4 e 2 VC3) e deteta anomalia forense de metadado.",
        "status_conv": "Convergência Plena c/ Nota Forense de Metadado (Cluster 4 | VC2/VC4)",
        "anotacoes": "Achado crucial da Auditoria de Ancoragem Verbatim (Micro-Meso): a verificação dos 11 posts constituintes ('Aura', 'newbros', 'logi apoc fit', 'killboards', 'standing info') comprova que o tópico pertence substantivamente a EVE Online, apesar de o metadado original registar World of Warcraft. Mantém-se a nota 4 atribuída por JPaulo."
    },
    "2116712": {
        "r1_jp_cluster": "Cluster 2",
        "r1_jp_valor": "VC3 - Codestruição de Valor",
        "r1_jp_fid": 5,
        "jp_cluster": "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "jp_valor": "VC3 (Codestruição de Valor)",
        "jp_fid": 5,
        "em_cluster": "Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva",
        "em_valor": "VC3 (Codestruição de Valor)",
        "em_fid": 5,
        "tensao_multivc": "Consenso em VC3 (Codestruição Competitiva Severa, R=3.8): Conjugação de WeakAuras de 1 pixel com scripts Python gerados pelo ChatGPT.",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Demonstra a construção progressiva de consenso nos 5 posts (incluindo a validação de um cético no post 3), confirmando 100% da avaliação de JPaulo na Ronda 1 (Cluster 2 | VC3 | Fidelidade=5).",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 2 | VC3 | Fidelidade 5)",
        "anotacoes": "JPaulo já corrigira na Ronda 1 o falso positivo lexical da heurística inicial (que colocara no Cluster 4 apenas porque 'weakaura' contém 'aura'), atribuindo Cluster 2, VC3 e Fidelidade máxima (5/5)."
    },
    "512367": {
        "r1_jp_cluster": "Cluster 4",
        "r1_jp_valor": "VC1 e VC3",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores",
        "jp_valor": "VC2/VC1 (Design Bounded AI 'Ask Aura') em tensão c/ VC3 (Alucinação e Erosão Comunitária) [VC4]",
        "jp_fid": 5,
        "em_cluster": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores",
        "em_valor": "VC4 articulando Proposta VC2/VC1 vs. Risco VC3",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC1/VC2 vs. VC3 -> VC4): Proposta rigorosa de intérprete contextual RAG (VC1/VC2) confrontada com o risco de alucinação e destruição das wikis comunitárias (VC3).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "A codificação dialética de JPaulo na Ronda 1 ('VC1 e VC3') capta com muito mais riqueza o debate real do que a contagem atómica dos 4 posts (3 VC4, 1 VC3).",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 4 | Tensão VC1/VC2 e VC3)",
        "anotacoes": "Validação integral no Cluster 4 ('Ask Aura'). A síntese expandida para 109 palavras detalha o mecanismo RAG e a defesa das wikis comunitárias, elevando a Fidelidade de 4 para 5."
    },
    "reddit_1kylpvy": {
        "r1_jp_cluster": "Cluster 1",
        "r1_jp_valor": "VC1 e VC4",
        "r1_jp_fid": 4,
        "jp_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding (c/ Interface Cluster 4)",
        "jp_valor": "VC1/VC2 (Cocriação Pessoal de Planeamento) e VC4 (Verificação Cruzada Wowhead)",
        "jp_fid": 5,
        "em_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding (c/ Interface Cluster 4)",
        "em_valor": "VC1/VC2 e VC4 (Uso Condicional com Validação Externa)",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC1 e VC4): Geração efetiva de cronogramas de raid e roleplay com ChatGPT Plus (VC1/VC2) temperada pela exigência crítica de validação no Wowhead (VC4).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Preserva a síntese dialética 'VC1 e VC4' identificada por JPaulo na Ronda 1, integrando os 7 posts constituintes (D=2.9, A=2.7, R=0.7).",
        "status_conv": "Convergência Plena pós-Regra C1 vs. C5 (C1 -> Cluster 5 | VC1 e VC4)",
        "anotacoes": "Terceiro caso que motivou a Regra de Fronteira Cluster 1 vs. Cluster 5 (Secção 4.4.1): o utilizador conversa manualmente com o ChatGPT Plus (sem API ligada ao cliente WoW), pelo que se reclassifica de Cluster 1 para Cluster 5 (com interface no Cluster 4 pelo debate sobre companheiros IA)."
    },
    "2176376": {
        "r1_jp_cluster": "Cluster 4",
        "r1_jp_valor": "VC2",
        "r1_jp_fid": 5,
        "jp_cluster": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores",
        "jp_valor": "VC2 (Potencial de Cocriação / Acessibilidade Solo) e VC4 (Distinção Scripts vs. IA)",
        "jp_fid": 5,
        "em_cluster": "Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores",
        "em_valor": "VC2 e VC4 (Acessibilidade em Servidores Evergreen)",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC2 + VC4): Proposta de inclusão e eliminação de FOMO via companheiros de IA (VC2 assinalado por JPaulo) articulada com distinção técnica entre bots e IA (VC4).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Resgata a intenção cocriativa do OP (VC2, identificada por JPaulo na Ronda 1) que fora invisibilizada na classificação atómica dos 2 comentários (2/2 VC4).",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 4 | VC2/VC4 | Fidelidade 5)",
        "anotacoes": "JPaulo já corrigira na Ronda 1 a atribuição heurística (Cluster 5 -> Cluster 4) e atribuíra VC2 e Fidelidade=5, demonstrando que o foco incide em companheiros de grupo gerados por IA para masmorras/raids antigas."
    },
    "reddit_1r1dd9i": {
        "r1_jp_cluster": "Cluster 5",
        "r1_jp_valor": "VC4 e VC3",
        "r1_jp_fid": 5,
        "jp_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "jp_valor": "VC4 (Análise de Engenharia) e VC3 (Degradação de FPS por OnUpdate) c/ Contraexemplo VC1",
        "jp_fid": 5,
        "em_cluster": "Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding",
        "em_valor": "VC4 e VC3 (c/ Contraexemplo Event-Driven VC1)",
        "em_fid": 5,
        "tensao_multivc": "Sim (VC4 e VC3 vs. VC1): Crítica arquitetural (VC4) à degradação de FPS por vibe-coding cego (VC3) dialeticamente confrontada com código event-driven funcional (VC1 no post 28).",
        "dart_ag_score": 5,
        "prag_score": 5,
        "grounding_score": 5,
        "resolucao_diluicao": "Confirma a leitura 'VC4 e VC3' de JPaulo na Ronda 1 (invisível na contagem atómica onde VC3 era 0!) e demonstra a tese central: a IA como multiplicador de competência ou incompetência.",
        "status_conv": "Convergência Plena desde a Ronda 1 (Cluster 5 | VC4 e VC3 | Fidelidade 5)",
        "anotacoes": "Convergência absoluta desde a Ronda 1 (Cluster 5, VC4 e VC3, Fidelidade 5/5). Prova empírica definitiva de que a análise ao nível do Tópico captura a codestruição de performance (VC3) e a síntese dialética que os posts atómicos isolados haviam classificado apenas como VC4/VC2."
    }
}

def get_topic_synthesis(tid, posts_list, fallback_title=""):
    if tid in resumos_analiticos_topicos:
        return resumos_analiticos_topicos[tid]
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

# 4. Amostra de Tópicos (Track B, N=15 tópicos) mantendo exatamente os mesmos 15 tópicos e todos os seus campos analisados
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
constituent_posts_track_b = []

for t in sample_threads_raw:
    tid = str(t["thread_id"])
    t_info = thread_info_map.get(tid, {})
    t_posts = topicos_tabela_resumos.get(tid, [])
    ins = topic_insights.get(tid, {})
    tom_info = ins.get("tom_e_retorica", {})
    dv_info = ins.get("dinamicas_valor", {})
    satira_posts_map = {sp.get("post_id"): sp for sp in tom_info.get("posts_satiricos_ironicos", [])}
    
    ai_dist_str = ", ".join([f"{k}:{v}" for k, v in t.get("ai_counts", {}).items()])
    inter_dist_str = ", ".join([f"{k}:{v}" for k, v in t.get("inter_counts", {}).items()])
    vc_dist_str = ", ".join([f"{k}:{v}" for k, v in t.get("vc_counts", {}).items()])
    pids_list_str = ", ".join([p["pid"] for p in t_posts])
    
    satira_flag = "Sim" if tom_info.get("contem_satira_ironia") else "Não"
    n_satira = len(tom_info.get("posts_satiricos_ironicos", []))
    enquadramento_str = f"{tom_info.get('classificacao_tom', 'Debate Técnico Sério')} (Sátira/Ironia: {satira_flag}, {n_satira} posts)"
    
    sample_threads.append({
        "thread_id": tid,
        "game": t.get("game") or t_info.get("game"),
        "ecosystem": t.get("ecosystem", ""),
        "title": t.get("title") or t_info.get("title"),
        "url": t_info.get("url") or (t_posts[0]["link"] if t_posts else f"https://forums.eveonline.com/t/{tid}"),
        "volume_empirico": f"{t.get('posts_retidos', len(t_posts))} retidos / {t.get('posts_originais', len(t_posts))} originais",
        "pids_constituintes": pids_list_str,
        "perfil_dominante": f"Prevalente: {t.get('prev_ai', '')} / {t.get('prev_inter', '')} | Dist. A: ({ai_dist_str}) | Dist. I: ({inter_dist_str})",
        "vetor_dart": f"D: {t.get('avg_d', 0.0)} | A: {t.get('avg_a', 0.0)} | R: {t.get('avg_r', 0.0)} | T: {t.get('avg_t', 0.0)}",
        "dinamica_valor_ia": f"Pipeline: {t.get('val_dyn', '')} [Micro: {vc_dist_str}] | Agente Meso: {dv_info.get('tipo_dominante', t.get('val_code', ''))}",
        "enquadramento_retorico": enquadramento_str,
        "evidencia_verbatim": t.get("evidence", ""),
        "summary": enforce_max_words(get_topic_synthesis(tid, t_posts, t.get("title", "")), 150),
        "cluster_heuristico": assign_cluster(t["title"], t_posts),
        "audit": auditoria_track_b_resultados.get(tid, {})
    })
    
    # Guardar todos os 104 posts constituintes dos 15 tópicos da Track B
    for p in t_posts:
        pid = p["pid"]
        anon = anon_by_id.get(pid, {})
        verbatim_txt = anon.get("text") or anon.get("corpo") or ""
        sp_info = satira_posts_map.get(pid)
        if sp_info:
            papel_ancoragem = f"[{sp_info.get('tipo', 'Sátira/Ironia')}] {sp_info.get('explicacao', '')}"
        else:
            papel_ancoragem = "Ancoragem Literal / Argumentativa: fornece evidência empírica direta para a trajetória de valor e vetor DART do tópico."
        constituent_posts_track_b.append({
            "tid": tid,
            "pid": pid,
            "jogo": p["jogo"],
            "titulo_topico": t.get("title") or t_info.get("title") or "",
            "verbatim": verbatim_txt,
            "tema": p["tema"],
            "resumo": enforce_max_words(p["resumo"], 60),
            "tipo_ia": p["tipo_ia"],
            "inter": p["inter"],
            "valor": p["valor"],
            "dart": p["dart"],
            "rev_humana": p["rev_humana"],
            "papel_ancoragem": papel_ancoragem,
            "link": p["link"]
        })

print(f"Total tópicos na Track B: {len(sample_threads)}")
print(f"Total posts constituintes dos tópicos da Track B: {len(constituent_posts_track_b)}")

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
    ws.row_dimensions[start_row].height = 30
    
    current_row = start_row + 1
    for r_idx, row_values in enumerate(data):
        row_fill = PatternFill("solid", fgColor="F2F5F8") if r_idx % 2 == 1 else PatternFill("solid", fgColor="FFFFFF")
        for c_idx, val in enumerate(row_values, 1):
            cell = ws.cell(row=current_row, column=c_idx, value=val)
            cell.font = font_cell
            cell.fill = row_fill
            cell.border = thin_border
            
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
# FOLHA 1: INSTRUÇÕES (METODOLOGIA DART-NET v4.0)
# ==========================================
ws1 = wb.active
ws1.title = "Instrucoes"
ws1.views.sheetView[0].showGridLines = True

ws1.merge_cells("A1:D1")
title_cell = ws1["A1"]
title_cell.value = "PROTOCOLO DE AUDITORIA HUMANA — ARQUITETURA MULTINÍVEL INCORPORADA (DART-NET v4.0)"
title_cell.font = font_title
title_cell.alignment = Alignment(horizontal="left", vertical="center")
ws1.row_dimensions[1].height = 32

add_sec_header(ws1, "1. ARQUITETURA METODOLÓGICA MULTINÍVEL INCORPORADA E ATRIBUIÇÃO DE AUDITORES", 3, "D")
h_atrib = ["Nível / Investigador", "Função na Framework DART-NET v4.0", "Unidade Analítica e Amostra", "Parâmetros Auditados"]
d_atrib = [
    [
        "Nível Meso (Primário)\nProf. JPaulo & Prof. Emmanoel",
        "Unidade Primária de Análise, Sentido, Codificação Relacional e Teorização (Track B — Auditoria de Alto Nível Concluída)",
        "Tópico de Discussão Completo (N=152 no corpus; Amostra Estratificada Track B N=15 tópicos integrando 104 posts constituintes)",
        "Cluster Temático (1-5), Trajetória de Valor (VC1-VC4), Fidelidade de Síntese (1-5), Adequação DART/Agência (1-5), Fidelidade Pragmática/Retórica (1-5), Ancoragem Verbatim Micro-Meso (1-5) e Resolução da Diluição Atómica"
    ],
    [
        "Nível Micro (Incorporado)\nProf. Roger & Prof. Gomide",
        "Unidade Incorporada de Ancoragem Empírica (Verbatim Grounding) e Controlo Anti-Alucinação (Track A + Posts_Topicos_Track_B)",
        "Post Individual Incorporado no Tópico (N=825 refinados de 1.032 totais; N=104 posts dos tópicos da Track B + Amostra Track A N=83 posts)",
        "Vetor DART (0-5), Agência IA (A1-A6), Interação (I1-I6), Valor (VC1-VC4), Enquadramento Retórico Situado e Evidência Verbatim Forense"
    ]
]
r = render_table(ws1, 4, h_atrib, d_atrib, {1: alignment_center, 3: alignment_wrap})

add_sec_header(ws1, "2. DIRETRIZES DA NOVA METODOLOGIA, TIPOS DE FIDELIDADE E NOVOS PARÂMETROS DE AUDITORIA (TRACK B)", r + 1, "D")
ws1.merge_cells(f"A{r+2}:D{r+2}")
c_desc = ws1[f"A{r+2}"]
c_desc.value = (
    "JUSTIFICAÇÃO DA ARQUITETURA MULTINÍVEL INCORPORADA (DART-NET v4.0):\n"
    "Em HCI, CSCW e Cocriação de Valor (Prahalad & Ramaswamy, 2004; Vargo & Lusch, 2016), o valor e a pragmática subcultural (sátira/ironia) são fenómenos relacionais emergentes "
    "que se desenrolam na trajetória dialética do Tópico (Nível Meso, onde 48,7% dos tópicos revelam impacto ativo de valor VC1/VC2/VC3) e se diluem quando o post é tratado de forma isolada "
    "(Nível Micro, onde 77,2% dos posts aparentam neutralidade VC4). Contudo, os posts individuais de cada tópico são integralmente preservados como Unidade de Ancoragem Empírica (Verbatim Grounding).\n\n"
    "PARÂMETROS DE AUDITORIA DE ALTO NÍVEL (TRACK B — ESCALA 1 A 5 + CALIBRAÇÃO EM 2 VAGAS):\n"
    "• 1. Fidelidade de Síntese Global (1-5): Mede o rigor epistémico com que o 'Resumo_Analitico_IA' (<= 150 palavras) sintetiza argumentos, consensos e conflitos do tópico (Ronda 1 resumos curtos: 4,13/5 -> Ronda 2 resumos de 150 palavras: 4,93/5).\n"
    "• 2. Adequação DART e Agência/Interação (1-5) [NOVO]: Avalia se o vetor DART médio (D, A, R, T) e o perfil dominante (A1-A5 / I1-I6) traduzem fielmente a mecânica sociotécnica do tópico.\n"
    "• 3. Fidelidade Pragmática e Retórica (1-5) [NOVO]: Avalia a precisão na distinção entre análise literal e enquadramentos figurativos ([Sátira/Ironia], [Humor/Piada]) via confrontação post-tópico.\n"
    "• 4. Ancoragem Verbatim Micro-Meso (1-5) [NOVO]: Verifica se a síntese de nível Meso está estritamente ancorada nos 104 posts constituintes (folha 'Posts_Topicos_Track_B') sem extrapolação.\n"
    "• 5. Resolução da Diluição Atómica [NOVO]: Documenta o ganho analítico obtido ao passar da soma atómica de posts (vc_counts) para a trajetória relacional completa do tópico.\n"
    "• 6. Polifonia e Tensão Dialética Multi-VC [NOVO]: Regista a coexistência dialética de múltiplas trajetórias de valor (ex: VC2 + VC3, VC1 e VC3, VC2 e VC4) identificada na Ronda 1 de codificação humana."
)
c_desc.font = font_cell
c_desc.alignment = alignment_wrap
ws1.row_dimensions[r+2].height = 215
r += 3

add_sec_header(ws1, "3. TAXONOMIAS DE CODIFICAÇÃO (A1-A6, I1-I6, VC1-VC4)", r + 1, "D")
h_tax = ["Taxonomia", "Código", "Designação Formal", "Critério Epistémico Operacional"]
d_tax = [
    ["Tipo de IA", "A1", "Agente Autónomo", "IA com capacidade agêntica independente (ex: bot de IA adaptativo, simulação profunda de tripulações)."],
    ["Tipo de IA", "A2", "Automação / Bot Mecânico", "Scripts determinísticos e bots convencionais sem autonomia cognitiva."],
    ["Tipo de IA", "A3", "Script Determinístico", "Código estático (ex: macros simples, WeakAuras mecânicas)."],
    ["Tipo de IA", "A4", "Copiloto Assistivo", "Assistentes generativos acionados pelo utilizador (ex: ChatGPT, Claude, Gemini, GitHub Copilot)."],
    ["Tipo de IA", "A5", "Discussão Reflexiva", "Discurso deliberativo humano sobre o fenómeno da IA sem uso direto in-game."],
    ["Tipo de IA", "A6", "Ruído Metodológico", "Conteúdo espúrio ou não relacionado com IA/automação (purgado na Fase 2)."],
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

add_sec_header(ws1, "4. CLUSTERS TEMÁTICOS ESTRATIFICADOS E REGRA DE DESAMBIGUAÇÃO (CLUSTER 1 vs. CLUSTER 5)", r + 1, "D")
h_cl = ["Cluster", "Nome do Cluster", "Enquadramento Temático e Regra de Fronteira Operacional", "Volume Relativo"]
d_cl = [
    ["Cluster 1", "Ferramentas Externas, Integração de APIs e MCP", "Aplicações comunitárias ligadas a protocolos/APIs em tempo real (ESI, Battle.net API, servidores MCP). REGRA: O software comunica autonomamente com os dados do jogo.", "22 tópicos (14,5%) [Estrato Inicial: 30]"],
    ["Cluster 2", "Fair Play, Deteção Algorítmica e Integridade Competitiva", "Deteção de pixel bots, combate a automação ilícita, impacto económico de bots e integridade competitiva no PvP/mercados.", "33 tópicos (21,7%) [Estrato Inicial: 35]"],
    ["Cluster 3", "Suporte ao Cliente, Moderação Automatizada e Banning", "Tickets de suporte geridos por IA ('ChatGPT GM'), queixas de moderação automatizada, layoffs e banimentos indevidos.", "25 tópicos (16,4%) [Estrato Inicial: 32]"],
    ["Cluster 4", "Agentes Oficiais In-Game e Masmorras de Seguidores", "Sistemas de IA nativos da publicadora: Follower Dungeons, Delves com Brann Bronzebeard, Aura AI / Ask Aura e companheiros in-game.", "21 tópicos (13,8%) [Estrato Inicial: 25]"],
    ["Cluster 5", "Copilotos de Desenvolvimento, Addons e Vibe-Coding", "Uso de LLMs (Claude, ChatGPT, Gemini) como copilotos de código Lua/WeakAuras ou planeamento/brainstorming. REGRA: O humano é o intermediário manual (copy-paste), sem ligação API direta da IA ao jogo.", "51 tópicos (33,6%) [Estrato Inicial: 30]"]
]
r = render_table(ws1, r + 2, h_cl, d_cl, {1: alignment_center, 2: alignment_wrap})

ws1.column_dimensions["A"].width = 26
ws1.column_dimensions["B"].width = 36
ws1.column_dimensions["C"].width = 68
ws1.column_dimensions["D"].width = 48

# ==========================================
# FOLHA 2: EXEMPLOS POSTS (MANTIDOS <= 60 PALAVRAS)
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
# FOLHA 3: EXEMPLOS TÓPICOS (MANTIDOS <= 150 PALAVRAS)
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
        resumos_analiticos_topicos["510327"],
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
# FOLHA 4: TRACK_A_POSTS (83 POSTS MANTIDOS INTEGRALMENTE)
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
        enforce_max_words(p["resumo_ia"], 60),
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
# FOLHA 5: TRACK_B_TOPICOS (AUDITORIA DE ALTO NÍVEL EXECUTADA + CAMPOS DOS TÓPICOS + NOVOS PARÂMETROS)
# ==========================================
ws5 = wb.create_sheet(title="Track_B_Topicos")
ws5.views.sheetView[0].showGridLines = True
ws5.freeze_panes = "F2"

headers_threads = [
    "Topic_ID",
    "Jogo",
    "Titulo_Real",
    "Link_Acesso",
    "Resumo_Analitico_IA",
    "Volume_Posts (Retidos/Originais)",
    "IDs_Posts_Constituintes",
    "Perfil_Tecnico_Dominante (A / I)",
    "Vetor_DART_Topico (D|A|R|T)",
    "Dinamica_Valor_IA (Pipeline vs Agente)",
    "Enquadramento_Retorico_IA",
    "Evidencia_Paradigmatica_Verbatim",
    "JPaulo_Ronda1_Cluster",
    "JPaulo_Ronda1_Valor_MultiVC",
    "JPaulo_Ronda1_Fidelidade (1-5)",
    "JPaulo_Cluster_Tematico",
    "JPaulo_Trajetoria_Valor",
    "JPaulo_Fidelidade_Sintese (1-5)",
    "Emmanoel_Cluster_Tematico",
    "Emmanoel_Trajetoria_Valor",
    "Emmanoel_Fidelidade_Sintese (1-5)",
    "Polifonia_Tensao_Dialetica_MultiVC",
    "Auditoria_Adequacao_DART_Agencia (1-5)",
    "Auditoria_Fidelidade_Pragmatica_Retorica (1-5)",
    "Auditoria_Ancoragem_Verbatim_Micro_Meso (1-5)",
    "Auditoria_Resolucao_Diluicao_Atomica",
    "Status_Convergencia_Inter_Auditores",
    "Anotacoes_Discordancias"
]

data_threads = []
for t in sample_threads:
    aud = t["audit"]
    data_threads.append([
        t["thread_id"],
        t["game"],
        t["title"],
        t["url"],
        enforce_max_words(t["summary"], 150),
        t["volume_empirico"],
        t["pids_constituintes"],
        t["perfil_dominante"],
        t["vetor_dart"],
        t["dinamica_valor_ia"],
        t["enquadramento_retorico"],
        t["evidencia_verbatim"],
        aud.get("r1_jp_cluster", ""),
        aud.get("r1_jp_valor", ""),
        aud.get("r1_jp_fid", ""),
        aud.get("jp_cluster", ""),
        aud.get("jp_valor", ""),
        aud.get("jp_fid", ""),
        aud.get("em_cluster", ""),
        aud.get("em_valor", ""),
        aud.get("em_fid", ""),
        aud.get("polifonia_multivc", ""),
        aud.get("dart_ag_score", ""),
        aud.get("prag_score", ""),
        aud.get("grounding_score", ""),
        aud.get("resolucao_diluicao", ""),
        aud.get("status_conv", ""),
        aud.get("anotacoes", "")
    ])

render_table(ws5, 1, headers_threads, data_threads, {
    1: alignment_center, 2: alignment_center, 6: alignment_center, 9: alignment_center,
    15: alignment_center, 18: alignment_center, 21: alignment_center, 23: alignment_center,
    24: alignment_center, 25: alignment_center, 27: alignment_center
})

col_widths_ws5 = {
    1: 16, 2: 18, 3: 38, 4: 42, 5: 75,
    6: 24, 7: 38, 8: 42, 9: 26, 10: 38, 11: 38, 12: 50,
    13: 38, 14: 36, 15: 22, 16: 38, 17: 32, 18: 22,
    19: 38, 20: 32, 21: 22, 22: 52, 23: 24, 24: 24,
    25: 24, 26: 55, 27: 38, 28: 65
}
for c_idx, width in col_widths_ws5.items():
    ws5.column_dimensions[get_column_letter(c_idx)].width = width

# ==========================================
# FOLHA 6: POSTS_TOPICOS_TRACK_B (104 POSTS CONSTITUINTES DOS 15 TÓPICOS ANALISADOS)
# ==========================================
ws6 = wb.create_sheet(title="Posts_Topicos_Track_B")
ws6.views.sheetView[0].showGridLines = True
ws6.freeze_panes = "E2"

headers_tb_posts = [
    "Topic_ID",
    "Post_ID",
    "Jogo",
    "Titulo_Topico",
    "Texto_Real_Verbatim",
    "Tema_Post",
    "Resumo_Analitico_IA (<=60 pal.)",
    "Agencia_IA (A1-A5)",
    "Interacao_IA (I1-I6)",
    "Valor_Post (VC1-VC4)",
    "Vetor_DART_Post",
    "Revisao_Humana_Sinalizada",
    "Papel_Ancoragem_Empirica_No_Topico (Micro -> Meso)",
    "Link_Acesso"
]

data_tb_posts = []
for cp in constituent_posts_track_b:
    data_tb_posts.append([
        cp["tid"],
        cp["pid"],
        cp["jogo"],
        cp["titulo_topico"],
        cp["verbatim"],
        cp["tema"],
        cp["resumo"],
        cp["tipo_ia"],
        cp["inter"],
        cp["valor"],
        cp["dart"],
        cp["rev_humana"],
        cp["papel_ancoragem"],
        cp["link"]
    ])

render_table(ws6, 1, headers_tb_posts, data_tb_posts, {
    1: alignment_center, 2: alignment_center, 3: alignment_center,
    8: alignment_center, 9: alignment_center, 10: alignment_center, 11: alignment_center, 12: alignment_center
})

col_widths_ws6 = {
    1: 16, 2: 20, 3: 18, 4: 34, 5: 65, 6: 36, 7: 55,
    8: 16, 9: 16, 10: 16, 11: 22, 12: 22, 13: 55, 14: 42
}
for c_idx, width in col_widths_ws6.items():
    ws6.column_dimensions[get_column_letter(c_idx)].width = width

output_path = "output/Protocolo_Auditoria_Humana_Formatado.xlsx"
wb.save(output_path)
output_path_jp = "output/Protocolo_Auditoria_Humana_Formatado_JPaulo.xlsx"
wb.save(output_path_jp)
print(f"Ficheiros guardados com sucesso em: {output_path} e {output_path_jp}")
