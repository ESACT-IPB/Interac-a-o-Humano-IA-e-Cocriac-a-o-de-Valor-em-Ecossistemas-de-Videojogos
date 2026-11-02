# Relatório DART-NET v4.0: Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos

**Análise ao Nível do Tópico de Discussão entre EVE Online (Sandbox) e World of Warcraft (Controlado)**

> [!IMPORTANT]
> **Corpus e codificação (versão de 2 de novembro de 2026)**: a análise incide sobre **139 tópicos de discussão completos** (69 de *EVE Online* e 70 de *World of Warcraft*; 5.263 posts), lidos do primeiro ao último post. Cada tópico foi codificado como um todo pelo modelo `deepseek-v4-pro`, sem ver codificações anteriores, em duas passagens: (i) cluster temático, dinâmica de valor (VC1–VC4) e ironia; (ii) tipo de IA (A1–A6), interação (I1–I6) e as quatro dimensões DART (0–5). Todas as classificações vêm com uma citação literal do tópico, verificada automaticamente. A codificação humana cega de uma amostra de 47 tópicos valida estas classificações (Secção 7). O percurso metodológico anterior, incluindo a codificação de cada post isolado, está documentado no **Anexo A**.

---

## 1. Sumário Metodológico e Framework DART-NET v4.0

### 1.1 Enquadramento Teórico e Unidade de Análise

O presente relatório aplica a framework **DART-NET v4.0** (Prahalad & Ramaswamy, 2004; Vargo & Lusch, 2016; Kozinets, 2020) à análise da interação entre humanos e agentes de inteligência artificial (IA) em ecossistemas de videojogos. O modelo DART original — **Diálogo, Acesso, Risco e Transparência** — constitui a matriz conceptual para avaliar a qualidade das interações sociotécnicas. A **unidade de análise é o tópico de discussão** (*thread*): cada tópico é lido e codificado como um todo, do post de abertura ao desfecho. Os posts individuais servem de fonte para as citações literais que sustentam cada classificação. A comparação entre os dois ecossistemas (*EVE Online* e *World of Warcraft*) constitui o nível de análise comparativo do estudo.

### 1.2 Distinção Fundamental: IA vs. Automação Convencional (A1–A6)

A taxonomia DART-NET distingue agentes de IA de sistemas de automação convencional, para evitar a inflação conceptual que frequentemente caracteriza o discurso público sobre IA. Um agente de IA é um sistema computacional capaz de executar tarefas, tomar decisões ou agir com algum grau de autonomia em nome de, ou em interação com, um jogador. Quando a evidência é insuficiente, um bot não é classificado como IA.

| Código | Classificação | Definição Operacional |
|--------|---------------|----------------------|
| **A1** | Agente de IA | Há evidência de que o sistema usa IA e tem algum grau de autonomia. |
| **A2** | Bot Convencional | Há software automatizado, mas sem evidência suficiente de que seja baseado em IA. |
| **A3** | Script / Automação | Script, macro ou automação determinística, sem evidência de IA. |
| **A4** | Humano Assistido por IA | A IA ajuda o jogador, mas o humano continua a ser quem decide. |
| **A5** | Discussão sobre IA | Discute-se IA, sem descrever um uso concreto de um agente de IA. |
| **A6** | Irrelevante | O conteúdo não tem relação com IA nos videojogos. |

Ao nível do tópico regista-se o **tipo principal** (o que melhor caracteriza o tópico no seu conjunto: o tipo do episódio concreto central, ou A5 quando o tópico é sobretudo debate) e os **tipos presentes** (todos os A1–A4 de que há um episódio concreto descrito em algum post, mesmo secundário).

### 1.3 Taxonomia de Cocriação e Codestruição de Valor (VC1–VC4)

No enquadramento da *Service-Dominant Logic* (Vargo & Lusch, 2004, 2016) e do modelo DART (Prahalad & Ramaswamy, 2004), o valor não é um atributo intrínseco ou estático embutido na tecnologia, mas emerge iterativamente nas práticas de cocriação de serviço entre atores humanos e não-humanos. Quando a interação é mediada por sistemas de inteligência artificial, o desfecho pode oscilar entre a sinergia colaborativa e a disrupção prejudicial — um fenómeno teorizado como **codestruição de valor** (*Value Co-Destruction*; Plé & Chumpitaz Cáceres, 2010; Echeverri & Skålén, 2011), caracterizado pelo desalinhamento acidental ou intencional na integração de recursos.

Para operacionalizar e medir este espetro sociotécnico em comunidades de videojogos, o protocolo DART-NET estabelece a taxonomia ordinal de quatro categorias de valor (**VC** — *Value Co-creation*):

| Código | Classificação de Valor | Definição Operacional e Papel Sociotécnico |
| :--- | :--- | :--- |
| **VC1** | **Cocriação Efetiva de Valor** (*Value Co-Creation*) | Interações colaborativas simétricas e bem-sucedidas entre jogador(es) e IA que resultam em benefícios tangíveis verificáveis (ex.: desenvolvimento conjunto de ferramentas comunitárias, superação de barreiras de entrada, expansão de capacidades criativas ou resolução colaborativa de problemas lúdicos). |
| **VC2** | **Potencial Cocriação de Valor** (*Potential Value Co-Creation*) | Evidências empíricas de intenção, teste experimental ou proposta concetual de cocriação com IA, cuja materialização tangível de valor permanece incipiente, em fase de protótipo ou condicionada a desenvolvimentos futuros. |
| **VC3** | **Codestruição de Valor** (*Value Co-Destruction*) | Interações que produzem danos sistémicos ou individuais, tais como perdas patrimoniais no jogo (ex.: perda de naves em combate por alucinações de copilotos), quebra de confiança institucional, proliferação de assimetrias competitivas injustas ou atritos gerados por moderação e apoio ao cliente automatizados opacos. |
| **VC4** | **Sem Evidência Direta / Neutro** (*No Evidence of Value*) | Discussões analíticas, debates reflexivos ou considerações normativas sobre IA desprovidas de relatos de ganhos ou perdas imediatas no ecossistema empírico dos jogadores. |

### 1.4 Questões de Investigação

A investigação é orientada por **três macro-questões de investigação**, desdobradas em subquestões complementares que articulam a agência tecnológica, os blocos constitutivos de valor e a governança dos ecossistemas:

* **QI1. Que tipos de agentes de IA e que formas de interação humano-IA caracterizam os MMORPG analisados?**
  * **QI1a**: Qual é a proporção de agentes de IA autónomos face a bots e scripts convencionais?
  * **QI1b**: Como se estruturam as interações humano-IA e que padrões emergem entre o ecossistema sandbox e o controlado?
* **QI2. Em que medida essas interações cocriam ou codestroem valor, e que papel desempenham as dimensões do modelo DART?**
  * **QI2a**: Em que medida se verificam as dimensões Diálogo, Acesso, Risco e Transparência nas interações documentadas?
  * **QI2b**: Que evidências empíricas sustentam a ocorrência de cocriação (VC1/VC2) face à codestruição (VC3) de valor?
* **QI3. Como é que a arquitetura de governança de cada ecossistema condiciona a cocriação de valor com IA, e que implicações daí decorrem?**
  * **QI3a**: Que diferenças sistemáticas existem entre EVE Online (sandbox aberto) e World of Warcraft (ecossistema controlado) na configuração DART e na dinâmica de valor?
  * **QI3b**: Que implicações teóricas e práticas emergem para o desenho de ecossistemas de videojogos com IA integrada?

### 1.5 Metodologia de Recolha e Constituição do Corpus

**Fontes**: fóruns oficiais (Discourse) da Blizzard e da CCP, os subreddits r/wow, r/classicwow, r/woweconomy e r/Eve, e discussões da Steam Community. A lista de tópicos-alvo (`data/target_corpus_303.json`) tem 303 entradas, que correspondem a 290 tópicos únicos (164 entradas de *World of Warcraft* e 139 de *EVE Online*); a revisão v4.1 corrigiu-a para 291 entradas (`data/target_corpus_v4_1.json`). Os tópicos foram identificados com palavras-chave de descoberta (`config.DISCOVERY_KEYWORDS`: por exemplo "AI agent", "LLM", "ChatGPT", "Claude", "Copilot", "MCP", "vibe coding", "botting", "machine learning").

**Recolha e seleção dos tópicos** (recolha concluída a 9 de setembro de 2026):

| Etapa | Tópicos | Posts | O que acontece |
| :--- | :---: | :---: | :--- |
| Tópicos-alvo únicos | 290 | — | Lista de tópicos a recolher |
| Tópicos recolhidos (`data/raw/`) | 253 | ≈ 8.980 | 37 tópicos não foram recolhidos (entre eles as 18 entradas do fórum MMO-Champion, em vBulletin) |
| Filtros da recolha (`ScraperAgent`) | 217 | 6.485 | Saem os posts anteriores a 1 de janeiro de 2024 e os de menos de 50 caracteres; 36 tópicos ficam sem posts |
| Seleção por relevância (`SemanticValidatorAgent`, `deepseek-v4-flash`) | 152 | — | Fica no corpus o tópico com pelo menos um post que fale de IA |
| Revisão v4.1 | 151 | — | Fusão do tópico duplicado `3000003` e correção do jogo de 14 tópicos do r/Eve (Secção 8.1) |
| Tópicos completos | 151 | 5.662 | Todos os posts recolhidos de cada tópico, por ordem cronológica, com o post de abertura sempre incluído (Secção 8.2) |
| **Exclusão de tópicos sem IA** | **139** | **5.263** | **Saem 12 tópicos que a codificação classificou como A6: o tema não é IA** |

**Exclusão dos tópicos sem IA**: 12 tópicos entraram no corpus porque algum post mencionava termos como "bot", "copilot" ou "automation", mas a codificação do tópico completo classificou-os como A6, porque o tema é outro (por exemplo, a nova região Exordium de EVE, *multiboxing*, blockchain/NFT ou um *addon* de pesca). Dez são de *EVE Online* e dois de *World of Warcraft*. A lista e a justificação de cada um estão em `data/analysis/corpus_topicos_v4_1_final.json`.

**Anonimização**: os autores foram substituídos por pseudónimos (`Player_N`) e os emails, URLs e números longos foram retirados do texto antes de qualquer envio ao modelo.

### 1.6 Codificação dos Tópicos

A escolha do tópico como unidade apoia-se em três princípios:

1. **Indexicalidade conversacional (HCI / CSCW)**: em plataformas assíncronas como *Reddit* e *Discourse*, um post é um **turno conversacional** (Clark & Brennan, 1991; Bakhtin, 1986) cujo significado depende do post de abertura, das mensagens anteriores e das respostas seguintes.
2. **Natureza relacional e temporal do valor**: a cocriação (`VC1`/`VC2`) e a codestruição (`VC3`) de valor são processos relacionais (Prahalad & Ramaswamy, 2004; Vargo & Lusch, 2016; Plé & Chumpitaz Cáceres, 2010) que se desenvolvem ao longo da discussão: proposta ou queixa inicial → escrutínio da comunidade → iteração com a IA → estabilização ou rutura.
3. **Pragmática subcultural e ironia (*Game Studies* e Netnografia)**: as comunidades de MMORPG recorrem com frequência a ironia, sarcasmo e paródia (Consalvo, 2007; Kozinets, 2020). O sentido figurativo de uma mensagem só se torna claro no contexto completo da discussão.

**Procedimento**: o modelo `deepseek-v4-pro` lê cada tópico completo, por ordem cronológica, e aplica as mesmas instruções dadas aos codificadores humanos (Secção 7). A codificação faz-se em duas passagens independentes:

| Passagem | Script | Campos codificados |
| :--- | :--- | :--- |
| 1 | `scratch/v4_1/02_codificacao_holistica_topicos.py --completos` | Cluster temático (1–5), VC principal e secundário, confiança (1–3), ironia/sátira, citação de evidência |
| 2 | `scratch/v4_1/13_codificacao_topicos_agente_interacao_dart.py` | Tipo de IA principal e presentes (A1–A6), interação principal e presentes (I1–I6), Diálogo, Acesso, Risco e Transparência (0–5) com citação para cada pontuação acima de zero, confiança (1–3) |

**Ancoragem literal (*verbatim grounding*)**: cada classificação vem com uma citação do tópico, que é verificada automaticamente contra o texto; se a citação não aparecer, o modelo é chamado a corrigi-la. No corpus final, as 139 citações de VC e todas as citações DART, menos uma, aparecem literalmente no texto. A verificação garante que as citações existem, mas não que a interpretação esteja certa: é isso que a codificação humana valida (Secção 7).

**Qualidade da codificação automática**: confiança alta (3) em 86 dos 139 tópicos na passagem 1 e em 83 na passagem 2. Só o tópico `510327` (183 posts) ultrapassou o limite de texto e foi lido até cerca de 300.000 caracteres.

---

## 2. Tipos de IA e Interações

### 2.1 Tipo de IA nos Tópicos (A1–A5)

| Tipo de IA principal | Total (N = 139) | EVE Online (N = 69) | World of Warcraft (N = 70) |
| :--- | :---: | :---: | :---: |
| **A1 (Agente de IA)** | 14 (10,1%) | 11 (15,9%) | 3 (4,3%) |
| **A2 (Bot convencional)** | 1 (0,7%) | 1 (1,4%) | 0 |
| **A3 (Script / automação)** | 0 | 0 | 0 |
| **A4 (Humano assistido por IA)** | 19 (13,7%) | 10 (14,5%) | 9 (12,9%) |
| **A5 (Discussão sobre IA)** | 105 (75,5%) | 47 (68,1%) | 58 (82,9%) |
| **Tópicos com um uso concreto de IA (A1 ou A4 presentes)** | **32 (23,0%)** | **20 (29,0%)** | **12 (17,1%)** |

**Análise**: três em cada quatro tópicos são debate sobre IA (A5): opiniões, receios, especulação e normas. Um em cada quatro relata um uso concreto de IA, quase sempre um agente com autonomia (A1: servidores MCP, ferramentas que leem a API do jogo, respostas de suporte geradas por IA) ou um jogador assistido por um LLM (A4: *addons*, aplicações ou planeamento feitos com ajuda de ChatGPT ou Claude). Nenhum tópico tem como episódio concreto um bot convencional ou um script sem IA (A2/A3 presentes: 0); os tópicos sobre bots e batota são debate (A5). Os usos concretos são mais frequentes em *EVE Online* (29,0% dos tópicos) do que em *World of Warcraft* (17,1%), sobretudo pelos agentes A1 (11 vs. 3 tópicos).

### 2.2 Interações Humano-IA nos Tópicos (I1–I6)

| Interação principal | Total (N = 139) | EVE Online (N = 69) | World of Warcraft (N = 70) |
| :--- | :---: | :---: | :---: |
| **I1 (Humano → IA)** | 5 (3,6%) | 3 (4,3%) | 2 (2,9%) |
| **I2 (IA → Humano)** | 3 (2,2%) | 2 (2,9%) | 1 (1,4%) |
| **I3 (Humano ↔ IA)** | 21 (15,1%) | 13 (18,8%) | 8 (11,4%) |
| **I4 (Humano → Humano sobre IA)** | 107 (77,0%) | 49 (71,0%) | 58 (82,9%) |
| **I5 (Humano → ambiente mediado por IA)** | 3 (2,2%) | 2 (2,9%) | 1 (1,4%) |
| **Tópicos com interação direta (I1, I2, I3 ou I5 presentes)** | **32 (23,0%)** | **20 (29,0%)** | **12 (17,1%)** |

**Análise**: a interação dominante é a discussão entre humanos sobre IA (I4, 77,0%). Nos tópicos com interação direta, a forma mais comum é a bidirecional (I3: 21 tópicos), em que o jogador itera com a IA (pede, testa, corrige, volta a pedir), sobretudo no desenvolvimento de ferramentas e *addons*. Entre os 139 tópicos, as interações presentes são I3 em 21, I1 em 8, I2 em 7 e I5 em 3.

---

## 3. Análise por Dimensão DART

### 3.1 Visão Global

As quatro dimensões são pontuadas de 0 (ausente) a 5 (explícita e central) para cada tópico no seu conjunto.

| Dimensão DART | Média (0–5) | Tópicos com pontuação ≥ 3 | EVE Online (média) | World of Warcraft (média) |
| :--- | :---: | :---: | :---: | :---: |
| **Diálogo (D)** | 2,15 | 51 (36,7%) | 2,20 | 2,10 |
| **Acesso (A)** | 2,30 | 67 (48,2%) | **2,75** | 1,86 |
| **Risco (R)** | **2,43** | 75 (54,0%) | 2,26 | **2,60** |
| **Transparência (T)** | 2,22 | 65 (46,8%) | 2,12 | **2,33** |

O Risco é a dimensão mais presente: mais de metade dos tópicos (54,0%) tem Risco forte ou superior. O Diálogo é a menos presente.

### 3.2 Diálogo (Média: 2,15/5)

O Diálogo avalia a comunicação, o feedback e a influência mútua entre jogadores e IA (ou entre jogadores e editora sobre a IA). As pontuações máximas surgem em tópicos onde o jogador conversa com uma IA integrada nas suas ferramentas de jogo:
- **`reddit_1pftbpi`** (*I fine tuned Aura to act as a real AI copilot*, EVE Online; D = 5): *"I also added text to speech and speech to text with a voice close to the in game Aura to allow natural conversation."*
- **`reddit_1vy3jwo`** (*I created ChatGPT copilot for EVE*, EVE Online; D = 5): *"whenever i talk with chatgpt while playing eve online it just act like my copilot and it has access to everything ESI capable of"*
- **`510327`** (*EVE Crews*, EVE Online; D = 5): *"I’ll point the AI hive mind at the problem and see if we can get to the bottom of it."*

### 3.3 Acesso (Média: 2,30/5)

O Acesso avalia como a IA muda ou facilita o acesso a informação, recursos, capacidades e decisões. É a dimensão com maior diferença entre jogos (EVE 2,75 vs. WoW 1,86) e a mais alta nos tópicos de cocriação (Secção 5.1). Oito tópicos têm Acesso máximo (5), todos de *EVE Online*, por exemplo:
- **`513384`** (*Eve-mentor-mcp*; A = 5): *"26 tools so far: Loss analysis with full fit detail... Recursive skill-prerequisite planning..."*
- **`507123`** (*EVE ONE - Your all in one management portal*; A = 5): *"you can now have access to your EVE Mail, calendar and follow up with your skills or marketplace prices from everywhere"*
- **`502655`** (*Battlefield.Space*; A = 5): *"instead of a pile of killmails, you get a brief that answers “what do I need to know about these people or this place"*

### 3.4 Risco (Média: 2,43/5)

O Risco abrange batota e vantagem injusta, riscos económicos, segurança, dependência, manipulação e perda de controlo. É a dimensão mais presente no corpus e a mais alta em *World of Warcraft* (2,60). Exemplos com Risco 4–5:
- **`503747`** (*AI and the effect on Economy/Society*, EVE Online; R = 5): *"Also we are looking at massive job loss directly due to AI and it’s ability to perform lots of tasks"*
- **`reddit_1ormrc6`** (*Are AIs the new bot-herders...*, EVE Online; R = 4): *"Unfair advantage. Will players using a paid AI assistant for market analysis or tactics gain an unfair advantage?"*
- **`1jukb0x`** (*Psa For The New Bros Dont Ask Chatgpt About Eve*, EVE Online; R = 4): *"Whatever you ask, you will get terrible information most of the time."*

### 3.5 Transparência (Média: 2,22/5)

A Transparência abrange a divulgação do uso de IA, a explicabilidade, a opacidade e a responsabilização. Nenhum tópico atinge 5; os mais altos (4) dividem-se entre transparência **praticada** e transparência **reivindicada**:
- praticada, em *EVE Online*: **`reddit_1sq7b1r`** (*Eve Market Scout (LLM coded project)*): *"At least I didn't conceal it like the last 3 apps."*; **`506798`** (*Aura Guidance (Beta) Feedback Thread*): *"When Aura is not confident in an answer, it will redirect players to Rookie Help chat."*
- reivindicada, em *World of Warcraft*: **`2101219`** (*Blizzard’s Algorithmic Absurdity*): *"calls for transparency shrugged off"*.

A Transparência é mais alta em *World of Warcraft* (2,33 vs. 2,12), e chega a 2,89 nos tópicos de suporte e moderação (Cluster 3), sobretudo como exigência dirigida à editora.

---

## 4. Análise Comparativa de Jogos: Sandbox vs. Controlado

### 4.1 Distribuição do Corpus

| Jogo | Tópicos | Posts | Posts por tópico |
| :--- | :---: | :---: | :---: |
| **EVE Online (Sandbox)** | 69 (49,6%) | 2.045 | 29,6 |
| **World of Warcraft (Controlado)** | 70 (50,4%) | 3.218 | 46,0 |
| **Total** | **139** | **5.263** | **37,9** |

### 4.2 Perfil dos Dois Ecossistemas

| Dimensão | EVE Online (Sandbox Aberto) | World of Warcraft (Ambiente Controlado) |
| :--- | :---: | :---: |
| Tópicos com uso concreto de IA (A1/A4) | **29,0%** | 17,1% |
| Tópicos com interação direta (I1/I2/I3/I5) | **29,0%** | 17,1% |
| DART médio (D / A / R / T) | 2,20 / **2,75** / 2,26 / 2,12 | 2,10 / 1,86 / **2,60** / **2,33** |
| VC1 (Cocriação efetiva) | **33,3%** (23) | 8,6% (6) |
| VC2 (Potencial de cocriação) | 8,7% (6) | 11,4% (8) |
| VC3 (Codestruição) | 10,1% (7) | **21,4%** (15) |
| VC4 (Sem evidência direta) | 47,8% (33) | 58,6% (41) |
| Impacto ativo (VC1 + VC2 + VC3) | 52,2% (36) | 41,4% (29) |
| Clusters (C1/C2/C3/C4/C5) | 16 / 9 / 0 / 19 / 25 | 1 / 14 / 9 / 21 / 25 |

**Interpretação**:
1. **Tipo de valor**: *EVE Online* tem quase quatro vezes mais tópicos de cocriação efetiva (VC1: 33,3% vs. 8,6%); *World of Warcraft* tem o dobro da codestruição (VC3: 21,4% vs. 10,1%).
2. **Acesso e Risco**: o perfil DART acompanha esta diferença. EVE tem mais Acesso (2,75 vs. 1,86), em linha com a infraestrutura aberta de APIs (ESI e MCP); WoW tem mais Risco (2,60 vs. 2,26) e mais Transparência reivindicada (2,33 vs. 2,12).
3. **Temas**: as ferramentas ligadas por API (Cluster 1) são quase exclusivas de EVE (16 de 17 tópicos); o suporte e a moderação automatizados (Cluster 3) são exclusivos de WoW (9 tópicos). Os copilotos e o *vibe-coding* (Cluster 5) estão igualmente presentes nos dois (25 tópicos cada).
4. **Cautela**: são associações observadas em dois ecossistemas, não relações causais, e assentam na codificação automática, a confirmar pela validação humana (Secção 7).

### 4.3 Tipologia Emergente de Tópicos: Os 5 Clusters Sociotécnicos

O cluster de cada tópico é o atribuído na codificação do tópico completo (passagem 1).

| Cluster | Tópicos | EVE / WoW | DART médio (D / A / R / T) | VC1 / VC2 / VC3 / VC4 | Tipo de IA principal |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Ferramentas Externas, APIs e MCP** | 17 (12,2%) | 16 / 1 | 2,47 / **4,12** / 1,82 / 2,47 | **15** / 0 / 0 / 2 | A1: 10, A4: 3, A5: 4 |
| **2. Fair Play, Deteção Algorítmica e Integridade Competitiva** | 23 (16,5%) | 9 / 14 | 1,52 / 1,17 / **3,04** / 1,78 | 0 / 0 / **10** / 13 | A5: 22, A2: 1 |
| **3. Suporte ao Cliente, Moderação Automatizada e Banning** | 9 (6,5%) | 0 / 9 | 2,00 / 0,89 / 2,56 / **2,89** | 0 / 0 / **6** / 3 | A5: 8, A1: 1 |
| **4. Agentes Oficiais In-Game** | 40 (28,8%) | 19 / 21 | 2,10 / 1,93 / 2,42 / 2,10 | 0 / 3 / 1 / **36** | A5: 39, A1: 1 |
| **5. Copilotos, Addons e Vibe-Coding** | 50 (36,0%) | 25 / 25 | 2,40 / 2,76 / 2,34 / 2,32 | **14** / **11** / 5 / 20 | A5: 32, A4: 16, A1: 2 |

1. **Cluster 1** — desenvolvimento de ferramentas que ligam a IA a dados vivos do jogo (ESI, *Model Context Protocol*, *killboards*). Tem o Acesso mais alto do estudo (4,12) e é o núcleo da cocriação: 15 dos 17 tópicos são VC1.
2. **Cluster 2** — bots, batota assistida por IA, deteção de automação e integridade do PvP e dos mercados. Tem o Risco mais alto (3,04) e concentra quase metade da codestruição (10 dos 22 tópicos VC3).
3. **Cluster 3** — uso de IA pela editora em tickets, moderação e sanções. Só existe em *World of Warcraft*; tem o Acesso mais baixo (0,89) e a Transparência mais alta (2,89), reivindicada contra a opacidade do suporte; 6 dos 9 tópicos são VC3.
4. **Cluster 4** — companheiros, NPCs e assistentes criados pela editora (*Follower Dungeons*, *Delves*/Brann, *Aura*). É sobretudo debate e avaliação (36 dos 40 tópicos são VC4).
5. **Cluster 5** — o jogador usa um LLM externo como assistente para *addons*, macros, planeamento ou *brainstorming*. É o maior cluster, o mais diverso no valor (14 VC1, 11 VC2, 5 VC3) e onde se concentra o uso assistido (A4: 16 tópicos).

#### 4.3.1 Critério Operacional de Fronteira: Distinção entre o Cluster 1 e o Cluster 5

Dado que tanto o **Cluster 1** como o **Cluster 5** envolvem a utilização de modelos de linguagem (Claude, ChatGPT, Gemini, GitHub Copilot), programação comunitária e dinâmicas de cocriação de valor (`VC1` e `VC2`), o protocolo estabelece um **critério de fronteira estrito** baseado na arquitetura de ligação aos dados do jogo:

* **Cluster 1 (Integração de Sistemas, APIs e MCP)**: A ferramenta ou o agente de IA **comunica programaticamente com endpoints de dados vivos do jogo via API** (ex.: API pública *ESI* de *EVE Online*, servidores *Model Context Protocol* — MCP ou telemetria de *killboards*). O foco incide sobre uma aplicação externa, plataforma web ou servidor que extrai dados estruturados do ecossistema em tempo real.
* **Cluster 5 (Copilotos, Addons e *Vibe-Coding*)**: O jogador interage com um LLM externo como **assistente ou copiloto pessoal**, sem ligação direta por API entre a IA e o servidor do jogo. **O utilizador humano atua como ponte manual**: copia mensagens de erro, documentação (*blue posts*) ou descrições funcionais para o chat da IA, gera ou depura código local (ex.: *Addons* em Lua ou *WeakAuras* para o cliente de *World of Warcraft*) ou realiza sessões de *brainstorming*, planeamento e consulta sobre mecânicas do jogo.

| Dimensão de Contraste | **Cluster 1: Ferramentas Externas, APIs e MCP** | **Cluster 5: Copilotos, Addons e *Vibe-Coding*** |
| :--- | :--- | :--- |
| **Papel da IA** | Motor integrado numa aplicação ou ligado diretamente a *endpoints* de dados do jogo (tipicamente **A1**). | Assistente/copiloto pessoal de programação local ou consulta conversacional (tipicamente **A4**, ou **A5** quando só se discute). |
| **Fluxo de Dados** | **Automatizado via API** (Servidor do Jogo ↔ API ESI / MCP ↔ Agente IA). | **Mediado Manualmente pelo Humano** (Jogador copia/cola *prompt* ou código ↔ LLM externo). |
| **Artefacto Principal** | Aplicações web comunitárias, servidores MCP, painéis de telemetria e simuladores ligados à API oficial. | *Addons* locais em Lua, *WeakAuras*, macros de interface ou consultas de planeamento/*brainstorming*. |
| **Indicadores Empíricos no Corpus** | `API`, `ESI`, `MCP Server`, `Endpoint`, `Telemetry`, `Live Data`, `zKillboard`. | `Vibe-coding`, `Lua`, `Addon`, `WeakAura`, `Claude Code`, `OnUpdate`, `FPS`, `Brainstorm`. |
| **Casos Verificados no Corpus** | • **`510327`** (*EVE Crews*: simulador web ligado à API ESI com regras calibradas via Claude);<br>• **`516433`** (*EVE MCP Server*: exposição de *endpoints* ESI para consulta direta por assistentes de IA). | • **`reddit_1v3v2p2`** (*Claude Code Success*: reparação de *addon* Lua pós-*patch* via *blue post*);<br>• **`reddit_1r1dd9i`** (*Vibe Coded AddOns*: impacto de performance em Lua e uso de `OnUpdate`);<br>• **`1mctiz6`** e **`1i6m4i6`** (uso do Gemini/ChatGPT para *brainstorming* e rotas de navegação). |

### 4.4 Casos Paradigmáticos de Tópicos de Discussão

| ID Tópico | Título | Jogo / Cluster | IA / Interação | DART (D/A/R/T) | VC | Evidência literal |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **`510327`** | *EVE Crews: A lore-accurate\* API-linked crew simulator* | EVE / C5 | A4 / I3 | 5 / 5 / 3 / 4 | **VC1** | *"After years of writing about it, the AI-assisted coding era finally gave me a way to build it - so here’s EVE Crews."* |
| **`516433`** | *EVE MCP Server — querying ESI from Claude, Copilot and other AI assistants* | EVE / C1 | A1 / I1 | 3 / 5 / 2 / 3 | **VC1** | *"EVE MCP Server is an open-source Model Context Protocol server exposing EVE’s public ESI endpoints as tools an AI assistant can call directly."* |
| **`reddit_1v3v2p2`** | *Claude Code Success* | WoW / C5 | A4 / I3 | 4 / 4 / 2 / 1 | **VC1** | *"It worked for atlaslootclassic, going to test others next."* |
| **`2152188`** | *[MoP] bug with cat pets. ChatGPT GM* | WoW / C3 | A1 / I2 | 2 / 1 / 2 / 4 | **VC3** | *"The GM’s post was riddled with M-Dashes (These — things) and even weirder was a multiple links that lead to nowhere and forum topics that don’t exist."* |
| **`2116712`** | *Another layer of cheating, Pixel bots are out of control* | WoW / C2 | A5 / I4 | 1 / 2 / 4 / 2 | **VC3** | *"Pixel bots are, and have been a thing for well over a decade at this point. Only now, it’s easier than ever to make."* |
| **`1jukb0x`** | *Psa For The New Bros Dont Ask Chatgpt About Eve* | EVE / C5 | A5 / I4 | 3 / 3 / 4 / 3 | **VC3** | *"I asked about the deimosin general out of curisoity and it gave me this abomination of an example fitting"* |

O `1jukb0x` mostra um limite da codificação automática: o post de abertura relata um uso concreto (um *fit* errado dado pelo ChatGPT), mas o tópico foi classificado como A5/I4, porque a discussão que se segue é sobretudo debate. Casos como este são o objeto da validação humana.

---

## 5. Cocriação e Codestruição de Valor (VC1–VC4)

### 5.1 Distribuição da Dinâmica de Valor

| Dinâmica de valor | Total (N = 139) | EVE Online (N = 69) | World of Warcraft (N = 70) | DART médio (D / A / R / T) |
| :--- | :---: | :---: | :---: | :---: |
| **VC1 (Cocriação efetiva)** | 29 (20,9%) | 23 (33,3%) | 6 (8,6%) | 2,86 / **3,97** / 1,86 / 2,45 |
| **VC2 (Potencial de cocriação)** | 14 (10,1%) | 6 (8,7%) | 8 (11,4%) | 2,14 / 2,79 / 1,57 / 1,71 |
| **VC3 (Codestruição)** | 22 (15,8%) | 7 (10,1%) | 15 (21,4%) | 1,73 / 1,27 / **2,68** / 2,36 |
| **VC4 (Sem evidência direta)** | 74 (53,2%) | 33 (47,8%) | 41 (58,6%) | 2,00 / 1,86 / 2,74 / 2,19 |
| **Impacto ativo (VC1 + VC2 + VC3)** | **65 (46,8%)** | 36 (52,2%) | 29 (41,4%) | — |

**Análise**:
1. Perto de metade dos tópicos (46,8%) tem uma dinâmica de valor ativa. A cocriação efetiva (20,9%) é mais frequente do que a codestruição (15,8%).
2. **Valor e DART**: os tópicos de cocriação efetiva têm o Acesso mais alto (3,97) e o Risco mais baixo (1,86); os de codestruição têm o Acesso mais baixo (1,27) e o Risco alto (2,68). São associações entre médias, não relações causais.
3. **Valor e tipo de IA**: dos 33 tópicos cujo tipo principal é um uso concreto (A1 ou A4), 25 são de cocriação efetiva. Dos 22 tópicos de codestruição, 21 são debate (A5): a codestruição aparece sobretudo em queixas e denúncias (suporte automatizado, bots, conselhos errados de LLMs) discutidas pela comunidade.

### 5.2 Evidências Paradigmáticas de Cocriação de Valor (VC1)

- **`516433`** e **`513384`** (EVE Online, Cluster 1): servidores MCP abertos que dão a assistentes de IA acesso direto aos dados do jogo. *"I’ve released eve-mentor-mcp, an MIT-licensed MCP server aimed at the new-player and returning-player learning problem rather than at veterans."*
- **`510327`** (EVE Online, Cluster 5): o autor desenvolve uma aplicação com ajuda intensiva de IA e corrige-a em conjunto com a comunidade ao longo do tópico.
- **`reddit_1v3v2p2`** (World of Warcraft, Cluster 5): um jogador repara *addons* com o Claude Code depois de uma alteração da Blizzard: *"It worked for atlaslootclassic, going to test others next."*

### 5.3 Evidências Paradigmáticas de Codestruição de Valor (VC3)

- **`2152188`** e **`2147065`** (World of Warcraft, Cluster 3): respostas de suporte identificadas pelos jogadores como automáticas ou inúteis. *"The third ticket told me to turn off/on filters so I can see the items properly. Worthless."*
- **`2101219`** (World of Warcraft, Cluster 2): sanções automáticas no PvP contestadas como opacas. *"Blizzard’s auto-ban algo in Alterac Valley is a pathetic excuse for moderation"*
- **`1ofu78l`** (EVE Online, Cluster 5): um jogador novo segue o conselho de um LLM em vez do da sua frota. *"A 5 player fleet asked me to join and warp to them but I declined(because ChatGPT told me it was not safe 😭)"*

---

## 6. Reflexão sobre as Questões de Investigação

> As respostas assentam na codificação dos 139 tópicos completos, sustentada por citações literais dos posts, e estão sujeitas à validação humana em curso (Secção 7).

### 6.1 QI1: Tipologia de Agentes de IA e Formas de Interação Humano-IA
*Pergunta Central: Que tipos de agentes de IA e que formas de interação humano-IA caracterizam os MMORPG analisados?*

#### 6.1.1 QI1a: Proporção de Agentes de IA Autónomos face a Bots e Scripts Convencionais
**Resposta**: os agentes de IA com autonomia (A1) são o tipo principal em 14 tópicos (10,1%) e a assistência por IA (A4) em 19 (13,7%); bots convencionais e scripts (A2/A3) são o tipo principal em apenas 1 tópico, e nenhum tópico tem um bot ou script sem IA como episódio concreto. O debate sobre IA (A5) domina (75,5%). Os tópicos sobre bots e batota existem (Cluster 2: 23 tópicos), mas são debate sobre IA e automação, e não relatos de bots convencionais. A seleção dos tópicos por palavras-chave de IA (Secção 1.5) contribui para este resultado: o corpus mede a discussão sobre IA, e não a presença de bots no ecossistema.

#### 6.1.2 QI1b: Estruturas de Interação Humano-IA e Padrões entre Sandbox e Controlado
**Resposta**: a interação dominante é a discussão entre humanos sobre IA (I4: 77,0% dos tópicos). Em 23,0% dos tópicos há interação direta com IA, sobretudo bidirecional (I3: 21 tópicos).
* Em **EVE Online**, a interação direta é mais frequente (29,0% dos tópicos) e assenta em ferramentas que ligam a IA à API do jogo (servidores MCP, *killboards* narrativos, copilotos com acesso à ESI), com 11 tópicos de agentes A1.
* Em **World of Warcraft**, a interação direta é menos frequente (17,1%) e ocorre sobretudo fora do jogo, com LLMs externos usados para criar e reparar *addons* (A4: 9 tópicos); a IA da editora aparece sobretudo como objeto de queixa no suporte (Cluster 3).

### 6.2 QI2: Cocriação, Codestruição de Valor e o Papel das Dimensões DART
*Pergunta Central: Em que medida essas interações cocriam ou codestroem valor, e que papel desempenham as dimensões do modelo DART?*

#### 6.2.1 QI2a: Verificação das Dimensões Diálogo, Acesso, Risco e Transparência
**Resposta**: as quatro dimensões estão presentes nos tópicos, com médias entre 2,15 e 2,43 (em 0–5). O Risco é a mais presente (2,43; forte ou superior em 54,0% dos tópicos), seguido do Acesso (2,30), da Transparência (2,22) e do Diálogo (2,15). O Acesso concentra-se nas ferramentas por API (Cluster 1: 4,12), o Risco no fair play (Cluster 2: 3,04) e a Transparência no suporte e moderação (Cluster 3: 2,89).

#### 6.2.2 QI2b: Evidências Empíricas de Cocriação (VC1/VC2) vs. Codestruição (VC3) de Valor
**Resposta**: 46,8% dos tópicos têm uma dinâmica de valor ativa: 20,9% de cocriação efetiva, 10,1% de potencial de cocriação e 15,8% de codestruição. A cocriação está associada a Acesso alto e Risco baixo (VC1: A 3,97, R 1,86) e concentra-se nas ferramentas por API e nos copilotos (Clusters 1 e 5: 29 dos 29 tópicos VC1). A codestruição está associada a Acesso baixo e Risco alto (VC3: A 1,27, R 2,68) e concentra-se no fair play e no suporte (Clusters 2 e 3: 16 dos 22 tópicos VC3). Na amostra já validada, o codificador humano concorda com a classificação de valor em 15 de 17 tópicos (Secção 7.2).

### 6.3 QI3: Governança do Ecossistema e Implicações para o Design com IA
*Pergunta Central: Como é que a arquitetura de governança de cada ecossistema condiciona a cocriação de valor com IA, e que implicações daí decorrem?*

#### 6.3.1 QI3a: Diferenças Sistemáticas entre EVE Online e World of Warcraft na Configuração DART e Dinâmica de Valor
**Resposta (Síntese Comparativa)**: a arquitetura de governança e a infraestrutura técnica estão associadas a perfis de valor distintos. Como o estudo é observacional e compara apenas dois ecossistemas, estas associações não permitem conclusões causais.

No ecossistema **Sandbox de *EVE Online***, a API ESI aberta e a adoção do *Model Context Protocol* (MCP) dão aos jogadores um papel de co-desenvolvedores. O Acesso é claramente superior (2,75 vs. 1,86 em *WoW*) e 33,3% dos tópicos são de cocriação efetiva (VC1), contra 8,6% em *WoW*. Dos 23 tópicos VC1 de EVE, 14 são ferramentas ligadas por API (Cluster 1) e 9 copilotos (Cluster 5).

No ecossistema **Controlado de *World of Warcraft***, a governança da Blizzard é centralizada: a sandbox de *addons* em Lua tem restrições rigorosas e a IA oficial está confinada a ambientes de jogo assistido (*Follower Dungeons* e *Delves*). A codestruição é o dobro da de EVE (VC3: 21,4% vs. 10,1%), concentrada em sanções automáticas, bots no PvP e suporte automatizado; o Risco (2,60) e a Transparência reivindicada (2,33) são mais altos. A cocriação em *WoW* surge sobretudo nas margens informais: 5 dos 6 tópicos VC1 de *WoW* são copilotos e *vibe-coding* (Cluster 5).

> **Nota de cautela**: estes resultados vêm da codificação automática dos tópicos e devem ser confirmados pela codificação humana cega (Secção 7) antes de serem apresentados como resultado final.

#### 6.3.2 QI3b: Implicações Teóricas e Práticas para o Desenho de Ecossistemas de Videojogos com IA Integrada
**Resposta**:
1. **Implicações teóricas**: o Acesso e o Risco funcionam como dimensões que acompanham a direção do valor: tópicos com acesso técnico programável tendem à cocriação, tópicos com risco percebido elevado e opacidade tendem à codestruição. Para estudos netnográficos assistidos por LLM, a lição metodológica é que o valor deve ser codificado sobre a discussão completa, incluindo o post de abertura e as respostas que não mencionam IA, porque é aí que se lê o desfecho e o tom (Anexo A).
2. **Implicações práticas para estúdios e designers**: o sucesso das ferramentas comunitárias baseadas em MCP em *EVE Online* sugere que as editoras devem disponibilizar **interfaces abertas, programáveis e auditáveis**. Inversamente, a automação opaca do suporte e da moderação observada em *WoW* está associada à degradação do valor relacional. Recomenda-se a adoção de salvaguardas contra alucinações, explicabilidade nas regras algorítmicas e intervenção humana no circuito (*human-in-the-loop*) para decisões sancionatórias.

---

## 7. Validação Humana: Codificação Cega ao Nível do Tópico

### 7.1 Protocolo

O protocolo anterior (Track B, Rondas 1 e 2) foi **substituído**: os codificadores tinham acesso aos resumos e às classificações da pipeline, o que impedia uma validação independente (Anexo A). O protocolo atual decorre em duas etapas, com um ficheiro por codificador e por etapa em `output/`.

**Amostra (N = 47 tópicos, 33,8% dos 139; um codificador por tópico, sem repetições)**:
* o Prof. JPaulo mantém os 17 tópicos que já tinha codificado e que estão no corpus final (o `481937`, classificado como A6, saiu sem substituição);
* os Profs. Emmanoel, Roger e Gomide codificam 10 tópicos cada, sorteados por cluster e jogo entre os restantes, sem tópicos com mais de 100 posts (`scratch/v4_1/10_amostra_auditoria_sem_repeticoes.py`, semente 20261102). Os três tópicos A6 que lhes tinham saído (`1s9et4k`, `509843`, `1w4y0sn`) foram substituídos por outros do mesmo cluster e jogo (`2257438`, `512939`, `432317`; `16_corpus_final_sem_A6.py`).

| Codificador | Tópicos | Jogo (EVE / WoW) | Cluster (C1/C2/C3/C4/C5) | Posts a ler |
| :--- | :---: | :---: | :---: | :---: |
| **Prof. JPaulo** | 17 | 7 / 10 | 1 / 1 / 1 / 5 / 9 | 770 |
| **Prof. Emmanoel** | 10 | 5 / 5 | 2 / 2 / 2 / 2 / 2 | 310 |
| **Prof. Roger** | 10 | 5 / 5 | 2 / 2 / 2 / 2 / 2 | 251 |
| **Prof. Gomide** | 10 | 5 / 5 | 2 / 2 / 2 / 2 / 2 | 293 |
| **Total** | **47** | **22 / 25** | **7 / 7 / 7 / 11 / 15** | |

**Justificação do tamanho**: sem repetições, a validação é o acordo de cada codificador com a codificação automática. Com um acordo à volta de 75%, a margem do IC95% é de cerca de ±12 pp com 47 tópicos; acima disso cada tópico a mais ganha pouco face ao tempo de leitura. **Contrapartida**: não é possível calcular o acordo entre codificadores humanos.

**Etapa 1 — Codificação cega** (`etapa_1_Codificacao_Topicos_<nome>.xlsx`): cada codificador lê o tópico original através de uma hiperligação e preenche, sem ver resumos nem classificações automáticas, os campos Cluster (1–5), VC principal e secundário, Confiança (1–3), Evidência (citação literal), Ironia/Sátira e Notas, e ainda o tipo de IA principal e presentes, a interação principal e presentes e as quatro dimensões DART (0–5). As instruções são as mesmas dadas à codificação automática.

**Etapa 2 — Avaliação dos resumos da IA** (`etapa_2_Avaliacao_Resumos_<nome>.xlsx`): depois da Etapa 1, cada codificador avalia o resumo do tópico gerado pela pipeline (agente `TopicDiscussionAnalystAgent`, Secção 8.3) quanto à Fidelidade da Síntese (1–5), Erros Factuais, Omissões Relevantes e Leitura do Tom Retórico.

**Análise prevista**: a chave `Chave_Analise_NAO_PARTILHAR_com_codificadores.xlsx` (não partilhada com os codificadores) reúne, para cada tópico, o codificador e a codificação automática (VC, cluster, tipo de IA, interação e DART). A análise vai calcular, por codificador e no conjunto dos 47 tópicos, a percentagem de acordo e o κ de Cohen para o VC principal, o cluster, o tipo de IA e a interação, e a diferença média nas pontuações DART. Na amostra, a codificação automática dá 21 VC4, 9 VC1, 7 VC2 e 10 VC3.

**Estado (2 de novembro de 2026)**: o Prof. JPaulo concluiu as duas etapas para VC e cluster (falta preencher as colunas de tipo de IA, interação e DART, acrescentadas depois); os ficheiros dos Profs. Emmanoel, Roger e Gomide estão prontos e ainda não foram preenchidos.

#### 7.1.1 VC Principal e VC Secundário: Regra e Justificação Metodológica

A codificação regista, para cada tópico, um **VC principal** (obrigatório) e um **VC secundário** (opcional). As duas colunas têm papéis diferentes:

| | VC Principal | VC Secundário |
| :--- | :--- | :--- |
| **Estatuto** | Obrigatório; uma única categoria (VC1–VC4) | Opcional; VC1–VC4, diferente do principal |
| **Quando se usa** | Sempre: dinâmica que melhor descreve a discussão no seu conjunto | Só quando há um episódio concreto de outra dinâmica, apontável num post |
| **Uso na análise** | κ de Cohen com a codificação automática; conclusões sobre a QI2b e a QI3a | Descrição da ambivalência (por exemplo, tópicos que combinam VC1 e VC3) e cálculo do acordo parcial com a codificação automática |

**Justificação**:
1. **O κ exige categorias mutuamente exclusivas.** A comparação com a codificação automática só pode ser calculada sobre uma única categoria por tópico. Por isso, todas as conclusões assentam no VC principal.
2. **O valor é muitas vezes ambivalente.** Cocriação e codestruição podem ocorrer na mesma discussão: é a formação interativa de valor (Echeverri & Skålén, 2011; Plé & Chumpitaz Cáceres, 2010). Na primeira leitura do Prof. JPaulo, 7 dos 15 tópicos receberam duas categorias. O secundário preserva essa informação sem a misturar com a medida principal.
3. **Permite medir acordo parcial.** Se o VC principal do codificador for o secundário da codificação automática (ou vice-versa), o caso conta como acordo parcial e não como desacordo total. Isso distingue desacordos de fronteira de desacordos substantivos.
4. **O secundário não serve para registar dúvidas.** Se fosse usado assim, o acordo parcial ficaria artificialmente inflacionado. A dúvida regista-se na Confiança (1–3) e nas Notas.

**Uso do secundário na codificação automática**: o modelo atribui VC secundário a poucos tópicos (16 dos 151 na versão dos tópicos completos). O uso do secundário pelos codificadores humanos será reportado de forma descritiva e não entra no cálculo do κ.

### 7.2 Resultados Preliminares: Codificação do Prof. JPaulo (N = 17)

O Prof. JPaulo codificou os seus tópicos duas vezes. A **codificação original** foi cega, feita antes de conhecer qualquer resultado automático. A **recodificação** foi feita depois e **não é cega**, porque o codificador já tinha visto a comparação com a codificação automática; mudou o VC principal em 2 tópicos, ambos no sentido da codificação automática. Por isso, **a medida de validação é a codificação original**.

**Etapa 1 — acordo com a codificação automática**:

| Comparação (N = 17) | Codificação original (cega) | Recodificação (não cega) |
| :--- | :---: | :---: |
| VC principal | **15/17** (κ = 0,83) | 16/17 (κ = 0,91) |
| Cluster | **14/17** (κ = 0,72) | 14/17 (κ = 0,72) |

* No VC principal, o acordo é quase perfeito (κ = 0,83; IC95% do acordo: 66–97%). Os 2 desacordos da codificação original são de fronteira entre VC1 e VC2 (`1hlv8xy`, `reddit_1kylpvy`): em nenhum caso o humano viu cocriação onde a codificação automática viu codestruição, ou vice-versa.
* No cluster, os 3 desacordos envolvem as fronteiras 1/5 e 4/5 (ferramentas por API vs. copilotos; agentes oficiais vs. copilotos), já assinaladas na Secção 4.3.1.
* Com um só codificador e 17 tópicos, estes valores são indicativos.

**Etapa 2 — fidelidade dos resumos**:

| Medida (N = 17) | Resumos antigos | Resumos atuais (tópico completo) |
| :--- | :---: | :---: |
| Fidelidade média (1–5) | 3,29 | **4,24** |
| Resumos com fidelidade ≥ 4 | 8 | **16** |
| Com erros factuais | 8 | **2** |
| Com omissões relevantes | 8 | **2** |
| Tom retórico lido corretamente | 11 (1 incorreto) | **13** (0 incorretos) |

* Os resumos antigos foram gerados a partir de uma versão incompleta dos tópicos: só os posts que passaram o filtro de relevância, sem o post de abertura do Reddit, fora da ordem cronológica e, em 4 tópicos, com o jogo errado (Secção 8.2). Os resumos atuais usam o mesmo agente, prompt e modelo, com o tópico completo.
* A fidelidade subiu em 9 tópicos, manteve-se em 6 e desceu em 2. Com 17 tópicos, a melhoria não é estatisticamente significativa (teste dos sinais: 9 de 11 alterações positivas, p = 0,07), mas a direção é clara: os resumos com fidelidade boa ou excelente passam de 8 para 16.
* A avaliação dos resumos antigos ficou registada no commit `c0e3f04`.

---

## 8. Reprodutibilidade e Gestão de Recursos

### 8.1 Revisão v4.1: Correções dos Dados

Todos os ficheiros da revisão v4.1 têm o sufixo `_v4_1`; os ficheiros originais não foram alterados.

| Ficheiro | Conteúdo |
| :--- | :--- |
| `scratch/v4_1/01_corrigir_dados.py` | Correção do jogo (14 tópicos), dos subreddits (3 tópicos), fusão do duplicado `3000003`, pseudonimização de 20 nomes, verificação literal da evidência DART |
| `data/analysis/netnography_results_v4_1.jsonl` | Corpus corrigido: 1.029 posts, 151 tópicos |
| `data/target_corpus_v4_1.json` | Catálogo de tópicos corrigido (303 → 291 entradas) |
| `data/analysis/correcoes_v4_1_log.json` | Registo de todas as correções |
| `scratch/v4_1/02_codificacao_holistica_topicos.py` | Codificação de cada tópico com `deepseek-v4-pro` (cluster, VC, ironia); com `--completos` lê os tópicos completos (Secção 8.2) |
| `data/analysis/topic_holistic_coding_v4_1.json`, `…_run1_sec_livre.json` | Versões anteriores, sobre os posts filtrados (Anexo A.7 e A.9) |
| `scratch/v4_1/03_comparacao_meso.py`, `04_estatisticas_relatorio.py` | Estatísticas da codificação post a post (Anexo A.1 e A.3) |

### 8.2 Tópicos Completos: Filtro de Relevância e Posts de Abertura do Reddit

A primeira versão da pipeline lia os tópicos de forma incompleta, por duas razões:

1. **Filtro de relevância post a post.** O `SemanticValidatorAgent` avaliava cada post isoladamente e só deixava passar os que falavam diretamente de IA (1.032 de 6.485 posts). As respostas como "concordo", os contra-argumentos e o desfecho da discussão quase nunca mencionam IA e eram cortadas. O filtro passou a servir só para selecionar os tópicos; a codificação lê todos os posts de cada tópico.
2. **Post de abertura do Reddit.** Em 54 dos 59 tópicos do Reddit a recolha guardou o título e os comentários, mas não o texto do post de abertura. O Reddit bloqueia pedidos automáticos, por isso o investigador guardou à mão as páginas HTML dos 59 tópicos (`Links_Reddit/`, `Links_Reedit_2/`), de onde foi extraído o post de abertura: 43 tinham texto, 4 eram só uma imagem, 1 era uma ligação externa, 6 foram removidos ou apagados pelo autor, e em 5 o post já estava na recolha. No fórum de EVE, o post de abertura do tópico `432317` (dezembro de 2023) foi recuperado dos dados recolhidos. O post de abertura entra sempre, mesmo que seja anterior a 2024 ou curto.

| Ficheiro | Conteúdo |
| :--- | :--- |
| `scratch/v4_1/08_extrair_posts_abertura_reddit.py` → `data/raw_reddit_op/reddit_posts_abertura.json` | Post de abertura extraído das páginas HTML do Reddit (não incluído no repositório: contém nomes de utilizador reais) |
| `scratch/v4_1/05_corpus_topicos_completos.py` → `data/processed/topicos_completos_v4_1.jsonl` | Corpus de tópicos completos, anonimizado (151 tópicos, 5.662 posts) |
| `scratch/v4_1/02_codificacao_holistica_topicos.py --completos` → `data/analysis/topic_holistic_coding_v4_1_completos.json` | Passagem 1: cluster, VC e ironia |
| `scratch/v4_1/13_codificacao_topicos_agente_interacao_dart.py` → `data/analysis/topic_coding_ai_interacao_dart_v4_1_completos.json` | Passagem 2: tipo de IA, interação e DART |
| `scratch/v4_1/16_corpus_final_sem_A6.py` → `data/analysis/corpus_topicos_v4_1_final.json` | Corpus final de 139 tópicos e lista dos 12 excluídos |
| `scratch/v4_1/15_estatisticas_topicos.py` → `data/analysis/estatisticas_topicos_v4_1.json` | Todas as estatísticas deste relatório |
| `scratch/v4_1/06_resumos_topicos_completos.py` → `data/analysis/topic_discussions_insights_v4_1_completos.json` | Resumos dos tópicos da Etapa 2 |
| `scratch/v4_1/10_…`, `11_…`, `12_…`, `14_…` | Amostra da validação humana, ficheiros das Etapas 1 e 2 e chave de análise |

### 8.3 Resumos dos Tópicos (TopicDiscussionAnalystAgent)

O agente [`TopicDiscussionAnalystAgent`](../agents/topic_discussion_analyst_agent.py) (`deepseek-v4-flash`) produz, para cada tópico, um resumo longo que reconstrói a discussão: o gatilho inicial, as reações divergentes, os contra-argumentos, as ferramentas envolvidas, a dinâmica de valor, as dimensões DART e o tom retórico (incluindo sátira e ironia). Na versão atual, os resumos são gerados a partir do tópico completo (`scratch/v4_1/06_resumos_topicos_completos.py`) e são os avaliados pelos codificadores humanos na Etapa 2 (Secção 7). A descrição da versão anterior do agente e da restante pipeline está no Anexo A.8.

### 8.4 Monitorização e Custo Global da Pipeline

* **Custo registado**: **25,80 USD** em `data/interim/custos_pipeline.json` (`deepseek-v4-flash` e `deepseek-v4-pro`), que inclui a pipeline original (~21,50 USD) e a revisão v4.1.
* **Codificação dos tópicos completos**: a passagem 2 (tipo de IA, interação e DART) e os resumos da Etapa 2 custaram ~1,02 USD; a passagem 1 custou ~1 USD em cada uma de duas corridas, das quais só a segunda ficou registada (a primeira perdeu-se num erro de escrita concorrente do ficheiro de custos, entretanto corrigido).

---

## Anexo A — Histórico Metodológico

> Este anexo documenta o percurso metodológico anterior à versão atual. Os números referem-se ao corpus de 151 tópicos e aos 1.029 posts codificados um a um, e **não são usados nas conclusões** do relatório. Ficam registados para rastreabilidade.

### A.1 Codificação Post a Post (Pipeline v3.0)

Na primeira versão, cada post que passava o filtro de relevância (1.032; 1.029 após a revisão v4.1) foi codificado isoladamente pelo `NetnographyAgent` (`deepseek-v4-flash`) com A1–A6, I1–I6, VC1–VC4 e as quatro pontuações DART. Os resultados estão em `data/analysis/netnography_results_v4_1.jsonl`. As tabelas seguintes são as da versão anterior do relatório.

#### A.1.1 Tipos de IA e Interações por Post

> **Nota Metodológica de Enquadramento (Abordagem Multinível Incorporada)**:  
> As contagens e frequências apresentadas nesta secção e na Secção 3 (N = 824 posts) representam a **camada micro-empírica atomizada**, funcionando como um inventário descritivo dos turnos comunicativos e linha de base granular. Em estrito cumprimento da metodologia DART-NET v4.0, estes números **não devem ser interpretados como conclusões substantivas isoladas sobre o valor do ecossistema**, mas sim como a matéria-prima empírica cuja significação teórica plena se consolida ao nível dos **151 tópicos de discussão** (Secções 4, 6 e 7).

##### A.1.1.1 Distribuição de Tipos de IA (A1–A5 no Corpus Refinado)

Após a remoção do ruído residual (A6) e da automação mecânica desprovida de DART, a distribuição dos **824 posts refinados** revela o perfil descritivo dos turnos comunicativos no corpus:

| Tipo de IA | Frequência | Percentagem | Papel no Ecossistema |
| :--- | :---: | :---: | :--- |
| **A5 (Discussão Reflexiva sobre IA)** | 636 | 77,2% | Discurso crítico, expectativas éticas, impacto no mercado de trabalho e futuro do design de videojogos. |
| **A1 (Agente de IA Autónomo / LLM)** | 95 | 11,5% | Agentes com raciocínio contextual, LLMs integrados, companheiros de tripulação e bots generativos. |
| **A4 (Humano Assistido por IA)** | 59 | 7,2% | Copilotos de código, criação de macros assistidas por IA (vibe-coding) e ferramentas de análise situacional. |
| **A2 (Bot Convencional Relevante)** | 17 | 2,1% | Automações que afetam criticamente as dimensões DART (ex.: transparência de dados em APIs ou moderação). |
| **A3 (Script / Automação Determinística)** | 17 | 2,1% | Scripts determinísticos com impacto direto em acesso a dados ou interfaces externas. |
| **A6 (Ruído / Não-IA)** | **0** | **0,0%** | *(Integralmente expurgado na fase de poda metodológica).* |
| **Total** | **824** | **100,0%** | **Corpus Empírico Refinado** |

**Análise**: No corpus purificado, as interações e discussões com relevância direta de IA (A1 + A4) representam cerca de **18,7%** do ecossistema, comprovando que quase um em cada cinco posts empíricos envolve agência autónoma ou hibridismo humano-máquina. A predominância de A5 (77,2%) reflete que os ecossistemas de videojogos operam primariamente como arenas de negociação social sobre a introdução da IA.

**Contributo micro para a QI1a (Proporção de Agentes Autónomos vs. Bots; resposta na Secção 6.1.1)**: A proporção de agentes de IA autónomos (A1: 11,5%) e de assistência híbrida (A4: 7,2%) supera substancialmente a presença de bots e scripts convencionais residuais (A2+A3: 4,1%). Este resultado demonstra que, ao expurgar o ruído e o farming mecânico do século passado, o ecossistema atual encontra-se fortemente polarizado entre o **discurso sociotécnico reflexivo (A5)** e a **experimentação ativa com agentes e copilotos modernos (A1/A4)**.

##### A.1.1.2 Estruturas de Interação Humano-IA (I1–I6)

| Tipo de Interação | Frequência | Percentagem | Natureza Empírica |
| :--- | :---: | :---: | :--- |
| **I4 (Humano → Humano sobre IA)** | 640 | 77,7% | Trocas sociais sobre impacto, ética, receio de substituição e viabilidade de IA nos jogos. |
| **I6 (Sem interação significativa)** | 67 | 8,1% | Menções contextuais breves, que caíram drasticamente de 34,0% para apenas 8,1% após a poda. |
| **I3 (Humano ↔ IA Bidirecional)** | 56 | 6,8% | Loops de interação contínua, simulação com copilotos e diálogos iterativos (núcleo de cocriação). |
| **I1 (Humano → IA Unidirecional)** | 48 | 5,8% | Comandos diretos, prompts, consultas de informação e instruções a copilotos ou LLMs. |
| **I5 (Humano → Ambiente mediado por IA)** | 6 | 0,7% | Exploração de instâncias com bots dinâmicos (Follower Dungeons) e interfaces de inteligência. |
| **I2 (IA → Humano Unidirecional)** | 7 | 0,8% | Recomendações proativas, alertas situacionais e relatórios gerados autonomamente por agentes. |
| **Total** | **824** | **100,0%** | — |

**Análise**: As interações diretas e ativas com agentes de IA (I1 + I2 + I3 + I5) somam agora **14,2% do corpus** (117 posts), revelando uma penetração técnica muito superior à observada na amostra não filtrada. Destaca-se a solidez das interações bidirecionais (I3: 6,8%), que formam a base analítica para a cocriação simétrica de valor.

**Contributo micro para a QI1b (Estruturas de Interação Humano-IA; resposta na Secção 6.1.2)**: Embora o discurso social comunitário (I4: 77,7%) continue a ser a forma dominante de circulação de sentido em torno da IA, o corpus refinado revela uma camada técnica viva de interações diretas (14,2%), liderada por fluxos bidirecionais (I3) e de comando direto (I1).

---

#### A.1.2 Dimensões DART por Post

> **Nota Metodológica de Enquadramento (Abordagem Multinível Incorporada)**:  
> As pontuações DART apresentadas nesta secção avaliam a intensidade dos micro-atos comunicativos contidos em cada um dos **824 posts refinados**. Servem como uma aferição de sensibilidade granular e inventário de referências textuais imediatas. A configuração sistémica completa do vetor DART — que traduz a maturidade sociotécnica real do ambiente lúdico — consolida-se através da ponderação agregada ao nível dos **151 tópicos de discussão** (Secção 4.3).

##### A.1.2.1 Visão Global das Pontuações no Corpus Refinado

| Dimensão DART | Média no Corpus Refinado (0–5) | Média só com Evidência Verbatim (0–5) | Interpretação Metodológica |
| :--- | :---: | :---: | :--- |
| **Diálogo (D)** | **1,09** | 1,08 | Presença ativa em canais de feedback, loops de copilotos e comandos iterativos. |
| **Acesso (A)** | **1,21** | 1,19 | Disponibilização de inteligência de jogo, endpoints de API e copilotos de dados. |
| **Risco (R)** | **1,62** | 1,54 | Dimensão mais saliente: apreensão com desequilíbrio competitivo, assimetria e dependência. |
| **Transparência (T)** | **1,34** | 1,28 | Reivindicação de explicabilidade técnica, rotulagem de IA e diagnóstico auditável. |

Com a exclusão dos 172 posts "Zero DART", todas as quatro dimensões apresentam valores médios superiores a 1,0, e todas as mensagens retidas têm pontuação em pelo menos uma dimensão. Esta propriedade decorre do próprio critério de exclusão e não constitui, por si só, evidência adicional de substância empírica.

**Verificação da evidência (v4.1)**: cada pontuação DART acima de zero vem acompanhada de uma citação justificativa produzida pelo LLM. A revisão v4.1 confirmou se essa citação existe literalmente no post. A coluna "só com evidência verbatim" atribui zero às pontuações cuja citação não foi encontrada no texto (total ou parcialmente). As médias descem no máximo 0,08 pontos (Risco), e a ordem das dimensões mantém-se.

##### A.1.2.2 Diálogo (Média: 1,09/5)

A dimensão Diálogo avalia a capacidade de comunicação bidirecional, reciprocidade e negociação entre utilizadores humanos e instâncias de IA.

**Evidências empíricas no corpus refinado**:

- **Post 510327_2912893** (EVE Online, A1, I3, VC1): Pontuação de Diálogo = **5/5**. Interação direta e aberta onde o próprio modelo é integrado na mediação comunitária: *"I’m Claude — the AI assistant he works with on EVE Crews... it’s more honest — it reflects how the tool is actually made."* O diálogo atinge o nível máximo de reciprocidade entre programador, comunidade e agente.
- **Post 510327_2913288** (EVE Online, A1, I3, VC1): Pontuação de Diálogo = **5/5**. Demonstração de ciclo iterativo de suporte: *"Here’s a more detailed response from Claude regarding your issues, for your info... we tweaked the classification rules."*
- **Post 1i6m4i6_87** (World of Warcraft, A1, I3, VC4): Pontuação de Diálogo = **5/5**. Reflexão crítica sobre a calibração do diálogo humano-máquina: *"AI can be confidently incorrect... It's best to go in with some level of knowledge about the question you're asking, so you can recognize when it's wrong."*

**Análise**: O Diálogo floresce com particular intensidade nos ecossistemas com ferramentas abertas e assistentes integrados, onde a IA não opera como um oráculo passivo, mas como um interlocutor interativo de cocriação.

##### A.1.2.3 Acesso (Média: 1,21/5)

A dimensão Acesso investiga como os sistemas de IA facilitam, democratizam ou restringem o acesso a recursos, conhecimento tático e capacidades computacionais no jogo.

**Evidências empíricas no corpus refinado**:

- **Post 513384_2889848** (EVE Online, A1, I1, VC1): Pontuação de Acesso = **5/5**. O utilizador documenta a expansão radical de acesso através de servidores MCP: *"It gives Claude (or any MCP client) live EVE data with judgment baked in. 26 tools available for market, fittings, navigation."*
- **Post 516433_2913324** (EVE Online, A1, I1, VC1): Pontuação de Acesso = **5/5**. Acesso programático a dados do jogo: *"exposing EVE’s public ESI endpoints as tools an AI assistant can call directly."*
- **Post 492935_2751948** (EVE Online, A5, I4, VC2): Pontuação de Acesso = **5/5**. Democratização linguística e cognitiva: *"It is not about replacing English, but about expanding access and participation."*

**Análise**: O Acesso surge como o pilar mais funcionalmente transformador do DART: a IA quebra a barreira de entrada da extrema complexidade de folhas de cálculo e dados de API em jogos sandbox.

##### A.1.2.4 Risco (Média: 1,62/5)

A dimensão Risco constitui a faceta mais proeminente e articulada no discurso empírico dos jogadores (1,62/5), englobando preocupações de justiça distributiva (*fair play*), exploração económica e perda de agência.

**Evidências empíricas no corpus refinado**:

- **Post reddit_1ormrc6_1** (EVE Online, A5, I4, VC3): Pontuação de Risco = **5/5**. Preocupação explícita com assimetria económica e vantagens indevidas: *"Unfair advantage. Will players using a paid AI assistant for market analysis or crafting get an edge that free-to-play users cannot match?"*
- **Post 2116712_27042848** (World of Warcraft, A5, I4, VC3): Pontuação de Risco = **5/5**. Dano à integridade do ambiente competitivo de PvP: *"This is an epidemic, and feel I see AT LEAST one of these in each lobby. When are proactive algorithmic bans coming?"*
- **Post 1ph9o3i_22** (EVE Online, A4, I3, VC3): Pontuação de Risco = **4/5**. Alucinações de modelos generativos que causam perdas de ativos espaciais: *"MISTAKES WERE MADE."*

**Análise**: Ao contrário da visão tecnicista que associa o risco apenas à batota mecânica, os utilizadores no corpus refinado articulam riscos epistémicos sofisticados: a emergência de "vibe-cheating", a opacidade dos modelos proprietários e a dependência psicológica ou técnica de copilotos de decisão rápida.

##### A.1.2.5 Transparência (Média: 1,34/5)

A dimensão Transparência mensura a visibilidade das regras algorítmicas, a rotulagem de conteúdo gerado por IA e a explicabilidade das decisões dos agentes.

**Evidências empíricas no corpus refinado**:

- **Post 510327_2913288** (EVE Online, A1, I3, VC1): Pontuação de Transparência = **5/5**. Disponibilização de instrumentação direta para auditoria: *"The diagnostics panel exists because you couldn’t reach a browser console — and provides complete visibility into AI decisions."*
- **Post 2318118_29656965** (World of Warcraft, A5, I4, VC3): Pontuação de Transparência = **5/5**. Exigência de rotulagem e escrutínio público das editoras: *"they say they didn’t use AI, but the devs could’ve at some point especially for generative texture work, we demand disclosure."*
- **Post 510327_2866379** (EVE Online, A1, I3, VC1): Pontuação de Transparência = **5/5**. Documentação explícita de parâmetros analíticos: *"The crew numbers in EVE Crews are derived from a blend of official CCP lore, historical documentation and ship volume metrics."*

**Análise**: Com o jogo corrigido (v4.1), a Transparência média por post é **mais alta em World of Warcraft** (1,26) do que em EVE Online (1,06), no corpus ativo de 1.029 posts. A diferença está sobretudo na natureza da transparência: em EVE Online é construída pelos criadores de ferramentas comunitárias (logs e diagnósticos abertos); em World of Warcraft é sobretudo **reivindicada** contra a opacidade das políticas corporativas da Blizzard, o que faz subir a pontuação sem que haja transparência efetiva.

---

#### A.1.3 Dinâmica de Valor por Post — Inventário

> **Nota Epistemológica Central**:  
> A distribuição de frequências abaixo (N = 824 posts) constitui um **inventário descritivo da camada micro-empírica** e funciona como **contraste** para a leitura ao nível do tópico (Secção 1.7.1).

| Categoria de Valor | Frequência Micro (N = 824) | Percentagem Micro | Papel na Arquitetura Multinível DART-NET v4.0 |
| :--- | :---: | :---: | :--- |
| **VC1 (Cocriação de Valor Efetiva)** | 26 | 3,2% | Turnos onde a solução finalizada é partilhada pontualmente. *(Meso: 20,5% holística / 12,6% regra)* |
| **VC2 (Potencial Cocriação de Valor)** | 72 | 8,7% | Ideias, propostas e intenções comunicadas em mensagens únicas. *(Meso: 9,9% holística / 12,6% regra)* |
| **VC3 (Codestruição de Valor)** | 90 | 10,9% | Denúncias pontuais, queixas de bans ou relatos de alucinações. *(Meso: 15,2% holística / 23,2% regra)* |
| **VC4 (Sem Evidência Direta / Reflexão)** | 636 | 77,2% | Turnos intermédios de debate, perguntas e diálogo exploratório. *(Meso: 54,3% holística / 51,7% regra)* |
| **Total** | **824** | **100,0%** | **Linha de Base Micro-Empírica de Contraste** |

**Análise do Contraste Teórico**:  
Ao nível do post, as mensagens com impacto ativo de valor (VC1 + VC2 + VC3) são **22,8%** (188 posts), contra 77,2% em VC4. A codestruição (VC3: 10,9%) é mais frequente do que a cocriação efetiva (VC1: 3,2%). Ao nível do tópico, perto de metade das discussões tem impacto ativo (45,7% na leitura holística). Estas duas proporções medem coisas diferentes: a primeira, a fração de turnos com valor explícito; a segunda, a fração de discussões cujo desfecho global é de cocriação ou codestruição. A diferença entre elas não deve ser lida como um "ganho" do nível meso (ver o modelo nulo na Secção 1.7.1). Ao nível do tópico, e na leitura holística, a ordem inverte-se: a cocriação efetiva (20,5%) supera a codestruição (15,2%).

### A.2 Poda Metodológica dos Posts

Em investigação netnográfica e estudos de cocriação de valor mediada por tecnologia (Kozinets, 2020; Prahalad & Ramaswamy, 2004; Vargo & Lusch, 2004), a validade do construto empírico depende criticamente da eliminação de ruído semântico e de dados espúrios que não representem o fenómeno sob escrutínio. 

Por conseguinte, foi aplicado um **protocolo rigoroso de refinamento epistémico** para expurgar do corpus analítico três categorias de mensagens que enfraqueciam a precisão teórica do estudo:

| Categoria Excluída | Critério Operacional | Frequência | Justificação Teórica e Metodológica |
| :--- | :--- | :---: | :--- |
| **1. Não-IA / Ruído Residual** | `ai_type == "A6"` | 51 posts | **Preservação dos Limites do Construto**: Mensagens classificadas como A6 representam falsos positivos da pesquisa booleana nos fóruns (ex.: lore de classes em WoW, conversas contextuais de guilda, gírias ou menções incidentais de "AI" fora do contexto de tecnologia). A sua permanência no corpus inflacionava artificialmente as métricas de não-interação (`I6`) e ausência de valor (`VC4`), gerando um viés de diluição analítica. |
| **2. Posts com "Zero DART"** | `D=0, A=0, R=0, T=0` | 172 posts | **Exigência Teórica dos Blocos Construtivos de Cocriação**: O modelo DART (Prahalad & Ramaswamy, 2004) postula que o valor cocriado emerge da interação ativa nos blocos de Diálogo, Acesso, Avaliação de Risco e Transparência. Um post que pontue zero em todas as quatro dimensões não oferece substância empírica para responder a nenhuma das três macro-questões de investigação (QI1 a QI3). A sua exclusão assegura que 100% dos dados retidos contenham evidência observável de pelo menos uma dimensão DART. |
| **3. Queixas de Bots Mecânicos / Farming Tradicional** | Tópicos de gold farming, pixel scripts, casino bots e fishing macros (A2) | 33 posts | **Filtro Paradigmático (Automação Convencional vs. IA Moderna)**: O foco da investigação reside no impacto da inteligência artificial generativa, autónoma e adaptativa da era pós-2024 (LLMs, copilotos, agentes MCP, decisões contextuais). Queixas antigas sobre farming mecânico e bots determinísticos de repetição (fenómeno comum nos MMOs desde 2005) representam batota convencional sem qualquer agência inteligente ou dimensão cocriativa. A sua eliminação clarifica a fronteira sociotécnica do estudo. |

> [!NOTE]
> **Consolidação do Experimento de Poda (Fase 3.5) e Reintegração Conversacional na Framework v4.0**:
> * Da aplicação dos critérios de poda preliminar (Fase 3.5) resultou a exclusão experimental de **207 posts únicos** (48 posts apresentavam simultaneamente classificação A6 e pontuação Zero-DART), catalogados detalhadamente em `data/analysis/excluded_posts_log.json`.
> * Esse corte gerou o subset de **825 posts refinados** utilizado nas Secções 2, 3 e 5 como **linha de base micro-empírica de contraste**, demonstrando empiricamente que a análise atómica isolada gera uma distorção analítica severa (77,2% em VC4 e 3,2% em VC1).
> * **Reintegração Conversacional**: Contudo, na Fase 6, ao elevar a unidade de análise para o **Tópico de Discussão (Nível Meso)**, constatou-se que a eliminação de posts no nível atómico causava a perda de 9 discussões inteiras (como o tópico `481937` em EVE Online, cujos únicos 2 posts tinham sido excluídos no corte atómico) e amputava diálogos vitais. Para preservar a integridade conversacional de todo o ecossistema, o ficheiro ativo `data/analysis/netnography_results.jsonl` unifica a totalidade dos **1.032 posts validados** integrados nos **152 tópicos ativos de discussão** em `data/analysis/thread_level_results.json`.
> * O corpus original de 1.032 posts permanece igualmente salvaguardado em `data/analysis/netnography_results_1032_unpruned.jsonl`.
> * **Revisão v4.1**: após a fusão do tópico duplicado `3000003`, o corpus ativo tem **1.029 posts em 151 tópicos** (`data/analysis/netnography_results_v4_1.jsonl`). Aplicando o mesmo registo de exclusões, o corte de contraste tem **824 posts** (205 dos 207 posts excluídos continuam no corpus; os outros 2 eram duplicados removidos).

### A.3 Comparação entre a Codificação Post a Post e a do Tópico

Estabelecer o **Tópico de Discussão (N = 151)** como **Unidade Primária de Sentido, Análise e Teorização** e manter o **Post Individual (N = 1.029 ativos / 824 no corte de contraste)** como **Unidade Incorporada de Ancoragem Empírica (*Verbatim Grounding*) e Contraste Crítico** é uma das contribuições metodológicas do estudo. A revisão v4.1 testou esta comparação de três formas: (i) com a mesma base de posts nos dois níveis; (ii) contra um modelo nulo; (iii) com uma codificação holística independente dos tópicos.

| Dimensão de Valor | Micro: corte de contraste (N = 824 posts) | Micro: corpus ativo (N = 1.029 posts) | Meso — regra de agregação (N = 151 tópicos) | Meso — leitura holística cega (N = 151 tópicos) |
| :--- | :---: | :---: | :---: | :---: |
| **VC1 (Cocriação Efetiva)** | `3,2%` (26) | `2,5%` (26) | `12,6%` (19) | **`20,5%` (31)** |
| **VC2 (Potencial de Cocriação)** | `8,7%` (72) | `7,2%` (74) | `12,6%` (19) | **`9,9%` (15)** |
| **VC3 (Codestruição)** | `10,9%` (90) | `11,3%` (116) | `23,2%` (35) | **`15,2%` (23)** |
| **VC4 (Sem Evidência Direta)** | `77,2%` (636) | `79,0%` (813) | `51,7%` (78) | **`54,3%` (82)** |
| **Impacto Ativo (VC1 + VC2 + VC3)** | **`22,8%`** (188) | **`21,0%`** (216) | **`48,3%`** (73) | **`45,7%`** (69) |

*A leitura holística usa o tópico completo (5.662 posts, incluindo o post de abertura); as outras colunas usam os posts que passaram o filtro de relevância.*

**Leitura dos resultados**:
1. **A regra de agregação, por si só, não demonstra o ganho meso.** A pipeline classifica um tópico como VC1 se pelo menos um dos seus posts for VC1, e como VC3 se tiver mais posts VC3 do que VC2. Pela mesma lógica, quanto mais posts um tópico tem, mais provável é que fique com impacto ativo. Para medir esse efeito, os rótulos dos posts foram baralhados aleatoriamente entre tópicos, mantendo o tamanho de cada tópico (5.000 simulações). Com rótulos baralhados, a mesma regra produz em média **57,7%** de tópicos com impacto ativo (IC95%: 52,3–62,9%). O valor observado (48,3%) fica **abaixo** desse intervalo. O salto de ~21–23% para ~48% resulta, portanto, da regra e não constitui evidência empírica de cocriação ao nível do tópico.
2. **A leitura holística independente chega a uma proporção semelhante por outra via.** O `deepseek-v4-pro` leu cada tópico completo (todos os posts recolhidos e o post de abertura), por ordem cronológica, sem ver os rótulos dos posts, e aplicou as mesmas instruções dadas aos codificadores humanos. Resultado: **45,7%** de impacto ativo, com as 151 citações de evidência verificadas literalmente no texto. Isto sustenta que perto de metade das discussões tem uma dinâmica de valor ativa. O resultado é estável: lida só sobre os posts filtrados, a leitura holística dava 46,4%, e duas corridas sobre esses posts mantiveram o VC principal em 142 dos 151 tópicos (κ = 0,91 teste-reteste). Entre os posts filtrados e o tópico completo, o VC principal mantém-se em 78,8% dos tópicos (κ = 0,67; Secção 8.6).
3. **As duas leituras meso não identificam os mesmos tópicos.** O acordo entre a regra e a leitura holística é de apenas **49,7%** (κ = 0,22, acordo fraco). A leitura holística atribui mais cocriação efetiva (VC1: 31 vs. 19 tópicos) e menos codestruição (VC3: 23 vs. 35). Por exemplo, 20 dos 35 tópicos que a regra marca como VC3 são, na leitura holística, VC4: queixas genéricas sem dano concreto relatado.
4. **Conclusão operacional**: a proporção agregada (~48%) é robusta às duas leituras, mas a distribuição entre VC1, VC2 e VC3 depende do método. As conclusões substantivas sobre cocriação vs. codestruição devem apoiar-se na leitura holística e ser confirmadas pela codificação humana cega em curso (Secção 7.3).

### A.4 Auditorias da Codificação Post a Post

#### A.4.1 Auditoria Cega Qualitativa (QualityGuardAgent)
A auditoria independente conduzida com o modelo `deepseek-v4-pro` sobre uma amostra de **159 codificações do corpus refinado** consolidou métricas de excelência:
* **Score Médio Global de Consistência**: **`91,31%`** (limiar crítico ≥ 70% amplamente superado);
* **Veracidade das Evidências Literais**: **100%** de citações verificadas no texto original;
* **Casos Sinalizados com Alerta**: Apenas 8 casos em 159 análises auditadas, decorrentes exclusivamente de limiares conservadores de confiança.

#### A.4.2 Calibração da Fila de Validação Humana
* **Total de Posts com Validação Manual Prioritária (`human_review_required = True`)**: **707 posts (85,8% do corte de 824)**
* **Critérios de Sinalização**: Confiança analítica < 0,80, jargões altamente contextualizados, sarcasmo e ambiguidade entre categorias de fronteira.

### A.5 Arquitetura Não Destrutiva e Poda Metodológica
A pipeline garantiu a total rastreabilidade da investigação:
1. **Camada 1 (Raw Data)**: Preservados 430 ficheiros brutos intactos em `data/raw/`;
2. **Camada 2 (AI Coding)**: Registo integral das 1.032 codificações validadas em `data/analysis/netnography_results.jsonl` (organizadas nos 152 tópicos ativos de discussão) e preservação do arquivo não podado em `data/analysis/netnography_results_1032_unpruned.jsonl`;
3. **Log de Poda Auditável**: Documentação individualizada dos 207 posts avaliados no experimento preliminar de poda da Fase 3.5 em `data/analysis/excluded_posts_log.json`;
4. **Camada v4.1 (Correções)**: corpus corrigido com 1.029 posts / 151 tópicos em `data/analysis/netnography_results_v4_1.jsonl`, sem alterar os ficheiros anteriores (Secção 8.5).

### A.6 O Agente de Síntese de Tópicos (ThreadSynthesisAgent) e Entregáveis Analíticos

Na Fase 4.5 da investigação, o ecossistema multiagente foi expandido com a conceção e implementação do [`ThreadSynthesisAgent`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/thread_synthesis_agent.py), atualizado para a versão **DART-NET v4.0** para operacionalizar a Arquitetura Multinível Incorporada:

1. **Agregação Algorítmica com Preservação dos Posts Constituintes**: O agente agrupa com fidelidade os posts validados nos seus **152 tópicos de discussão ativos** (65 em EVE Online e 87 em World of Warcraft na versão original; **151 tópicos, 79 EVE / 72 WoW** após a revisão v4.1), mantendo em cada ficha de tópico a lista explícita dos seus `post_ids` constituintes (*Ancoragem Micro*), o cluster sociotécnico calibrado, o vetor DART médio ponderado, as frequências taxonómicas e o código de valor emergente.
2. **Entregável Estruturado JSON**: Os resultados estruturados de todos os tópicos foram consolidados em [`data/analysis/thread_level_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/thread_level_results.json), contendo metadados completos, lista de posts incorporados, métricas DART individuais, dinâmicas de valor e citações paradigmáticas.
3. **Catálogo Sistemático e Macro-Síntese**: Foi gerado o documento exaustivo [`output/analise_agregada_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/analise_agregada_topicos.md) (com 3.928 linhas), que inclui uma ficha analítica sistemática para cada um dos 152 tópicos (com os seus posts e campos preservados) e a formalização teórica dos 5 clusters sociotécnicos calibrados.
4. **Articulação Teórica Multinível**: Este módulo fecha o ciclo investigativo entre o nível Meso (tópico como unidade primária de sentido), o nível Micro incorporado (post como evidência literal verificável) e o nível Macro (ecossistemas sandbox vs. controlados), assegurando total rigor netnográfico segundo Kozinets (2020) e Prahalad & Ramaswamy (2004).

### A.7 Comparação entre os Posts Filtrados e o Tópico Completo

Ao avaliar os resumos da Etapa 2, o Prof. JPaulo verificou que vários resumos davam aos tópicos muito menos posts do que as páginas tinham. A verificação mostrou duas causas:

1. **Filtro de relevância post a post.** O `SemanticValidatorAgent` avalia cada post isoladamente e só deixa passar os que falam diretamente de IA. Nos 18 tópicos da amostra do Prof. JPaulo, dos 778 posts recolhidos (já sem os posts anteriores a 2024 e os de menos de 50 caracteres) só 110 passaram o filtro; no corpus inteiro, 1.032 de 6.485. O filtro é adequado à codificação de cada post, mas não à leitura de um tópico: respostas como "concordo", contra-argumentos ou o desfecho da discussão quase nunca mencionam IA e eram cortadas. Os resumos e a leitura holística liam, por isso, uma discussão fragmentada, enquanto os codificadores humanos leem a página completa.
2. **Post de abertura do Reddit.** Em 54 dos 59 tópicos do Reddit a recolha guardou o título e os comentários, mas não o texto do post de abertura. O Reddit bloqueia pedidos automáticos e os browsers usados pelo assistente não o podem abrir, por isso o investigador guardou à mão as páginas HTML dos 59 tópicos (`Links_Reddit/`, `Links_Reedit_2/`), de onde foi extraído o post de abertura. Desses, 43 tinham texto, 4 eram só uma imagem, 1 era uma ligação externa, 6 foram removidos ou apagados pelo autor, e em 5 o post já estava na recolha. No fórum de EVE, o post de abertura do tópico `432317` (dezembro de 2023) foi recuperado dos dados recolhidos.

**Correção**: a leitura holística e os resumos da Etapa 2 passaram a ler o tópico completo: todos os posts recolhidos (5.662), por ordem cronológica, com o jogo corrigido e com o post de abertura, que entra sempre, mesmo que seja anterior a 2024 ou curto. Autores e texto foram anonimizados como no resto do corpus. A codificação de cada post (A/I/VC/DART), a regra de agregação e o modelo nulo não mudam.

| Leitura holística (N = 151) | Posts filtrados | Tópico completo, sem post de abertura | **Tópico completo, com post de abertura** |
| :--- | :---: | :---: | :---: |
| VC1 / VC2 / VC3 / VC4 | 26 / 20 / 24 / 81 | 31 / 15 / 21 / 84 | **31 / 15 / 23 / 82** |
| Impacto ativo — total | 46,4% | 44,4% | **45,7%** |
| Impacto ativo — EVE / WoW | 53,2% / 38,9% | 44,3% / 44,4% | **48,1% / 43,1%** |
| Confiança alta (3) | 57 | 90 | **96** |
| Citações verificadas literalmente | 150 | 151 | **151** |
| Acordo com a codificação original (cega) do Prof. JPaulo nos 18 tópicos (VC / cluster) | 12 / 17 | 13 / 16 | **15 / 15** |

* Entre os posts filtrados e o tópico completo, o VC principal mantém-se em 78,8% dos tópicos (κ = 0,67) e o cluster em 80,1% (κ = 0,73). O acréscimo do post de abertura mudou o VC principal em 8 dos 59 tópicos do Reddit.
* A proporção global de impacto ativo é robusta (44–46% nas três versões). O que muda é a comparação entre jogos: a vantagem de EVE no impacto ativo era em parte um efeito do filtro. A diferença no tipo de valor (mais VC1 em EVE, mais VC3 em WoW) mantém-se e acentua-se.
* Com o texto completo, o modelo atribui confiança alta a muito mais tópicos (96 vs. 57).
* O tópico `510327` (183 posts) ultrapassa o limite de texto e foi lido até cerca de 300.000 caracteres.

| Ficheiro | Conteúdo |
| :--- | :--- |
| `scratch/v4_1/08_extrair_posts_abertura_reddit.py` → `data/raw_reddit_op/reddit_posts_abertura.json` | Post de abertura extraído das páginas HTML do Reddit |
| `scratch/v4_1/05_corpus_topicos_completos.py` → `data/processed/topicos_completos_v4_1.jsonl` | Corpus de tópicos completos, anonimizado (5.662 posts) |
| `scratch/v4_1/02_codificacao_holistica_topicos.py --completos` → `data/analysis/topic_holistic_coding_v4_1_completos.json` | Leitura holística definitiva, usada neste relatório (151/151 tópicos, 0 erros, 151/151 citações verificadas) |
| `data/analysis/topic_holistic_coding_v4_1_completos_sem_op.json` | Leitura holística do tópico completo antes de recuperar os posts de abertura |
| `scratch/v4_1/06_resumos_topicos_completos.py` → `data/analysis/topic_discussions_insights_v4_1_completos.json` | Resumos novos dos tópicos da Etapa 2: os 37 da primeira amostra e os 30 da amostra sem repetições, 62 no total (mesmo agente, prompt e modelo que os originais) |
| `scratch/v4_1/10_amostra_auditoria_sem_repeticoes.py` → `data/analysis/amostra_auditoria_v4_1_sem_repeticoes.json` | Amostra da auditoria humana sem repetições (48 tópicos, Secção 7.3) |
| `scratch/v4_1/11_ficheiros_auditoria_sem_repeticoes.py`, `12_chave_sem_repeticoes.py` | Ficheiros das Etapas 1 e 2 dos Profs. Emmanoel, Roger e Gomide e chave de análise para a nova amostra |
| `scratch/v4_1/03_comparacao_meso.py --completos` e `04_estatisticas_relatorio.py --completos` | Comparação meso e estatísticas do relatório com a leitura holística definitiva (`*_v4_1_completos.json`) |
| `scratch/v4_1/07_comparacao_topicos_completos.py` → `data/analysis/comparacao_topicos_completos_v4_1.json` | Comparação entre a leitura dos posts filtrados e a do tópico completo |

### A.8 Versão Anterior do Agente de Resumos e Arquitetura da Pipeline v4.0

Para solucionar lacunas interpretativas decorrentes da análise atómica isolada — nomeadamente o risco de alucinação de LLMs ao interpretarem literalmente paródias, sátiras corporativas ou piadas comunitárias —, a arquitetura foi expandida com o agente especialista [`TopicDiscussionAnalystAgent`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/topic_discussion_analyst_agent.py):

1. **Análise Qualitativa Aprofundada sem Limitação de Extensão**:
   * O agente reconstrói a trajetória deliberativa completa de cada uma das **152 discussões ativas**, sem restrições de palavras.
   * Produz narrativas ricas que articulam o gatilho inicial da discussão, reações divergentes, contra-argumentos, ferramentas técnicas envolvidas, dinâmicas de cocriação (VC1/VC2) vs. codestruição (VC3), dimensões DART e um diagnóstico retórico minucioso.
   * Os entregáveis completos foram consolidados em [`output/resumos_discussoes_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/resumos_discussoes_topicos.md) (4.878 linhas) e [`data/analysis/topic_discussions_insights.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/topic_discussions_insights.json).

2. **Protocolo de Confronto Post-Tópico e Deteção Sistemática de Sátira**:
   * O gerador da tabela de síntese ([`summary_table_generator.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/summary_table_generator.py)) foi reformulado para processar a totalidade dos **1.032 posts** do corpus empírico sem perda de dados.
   * Cada post individual é sistematicamente confrontado com o contexto e tom do seu tópico de origem extraído pelo `TopicDiscussionAnalystAgent`. Posts satíricos (como o caso paradigmático do bot paródico CCP Copilot em EVE Online, anteriormente mal interpretado como anúncio corporativo real) passam a ser explicitamente rotulados com `[Sátira/Ironia]` ou `[Humor/Piada]`.
   * No entregável consolidado [`output/tabela_resumos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_resumos.md) (1.032 linhas), **238 posts** foram formalmente demarcados com tags explícitas de sátira/humor e **383 posts** contêm contextualização retórica de ironia ou crítica jocosa, eliminando falsos positivos literais.

3. **Arquitetura Consolidada de 8 Agentes da Pipeline DART-NET v4.0**:
   * A orquestração formal (`orchestrator.py`, refletida em [`output/fluxograma_implementacao.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/fluxograma_implementacao.md)) estabelece uma cadeia contínua de 8 agentes:
     1. `DiscoveryAgent` (Mapeamento de ecossistemas e fontes de dados)
     2. `ExtractionAgent` (Recolha de fóruns Discourse e Reddit)
     3. `PreprocessingAgent` (Anonimização e higienização empírica)
     4. `NetnographyAgent` (Codificação Micro de ancoragem DART, A1–A6, I1–I6, VC1–VC4 para 1.032 posts)
     5. `QualityGuardAgent` (Auditoria cega qualitativa com DeepSeek-v4-Pro)
     6. `TopicDiscussionAnalystAgent` (Análise profunda de nível Meso: discussões, insights e sátira/ironia em 152 tópicos)
     7. `ThreadSynthesisAgent` (Síntese multinível incorporada Meso-Micro e calibração dos 5 clusters sociotécnicos)
     8. `HumanAuditorAgent / SummaryTableGenerator` (Auditoria humana de alto nível Track B e ancoragem Micro Track A)

### A.9 Nota sobre as Corridas da Leitura Holística sobre os Posts Filtrados

**Nota sobre a leitura holística automática**: a primeira corrida foi feita com o secundário livre e atribuiu-o a 19 dos 151 tópicos (7 deles VC4). A segunda corrida, que é a usada neste relatório, foi feita com o secundário limitado a VC1–VC3; o modelo passou a atribuí-lo a apenas 2 tópicos. Essa restrição foi depois retirada do protocolo, e o VC4 voltou a ser aceite como secundário.
* A restrição só afetava o VC secundário, que não entra em nenhuma estatística deste relatório. Os resultados da leitura holística mantêm-se válidos.
* Entre as duas corridas, o VC principal manteve-se em 142 tópicos (κ = 0,91).
* Para o LLM, o secundário contribui pouco: na primeira corrida explicava apenas 2 dos 73 desacordos entre a regra de agregação e a leitura holística.
* O uso do secundário pelos codificadores humanos será reportado de forma descritiva e não entra no cálculo do κ.
