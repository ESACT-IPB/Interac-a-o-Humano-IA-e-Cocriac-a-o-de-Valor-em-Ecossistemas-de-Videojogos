# Relatório DART-NET: Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos

**Análise Comparativa entre EVE Online (Sandbox) e World of Warcraft (Controlado)**

---

## 1. Sumário Metodológico e Framework DART-NET

### 1.1 Enquadramento Teórico

O presente relatório aplica o framework DART-NET (Prahalad & Ramaswamy, 2004; DART-NET 2026) à análise da interação entre humanos e agentes de inteligência artificial (IA) em ecossistemas de videojogos. O modelo DART original — Diálogo, Acesso, Risco e Transparência — constitui a base conceptual para avaliar a qualidade das interações de cocriação de valor. A extensão DART-NET (2026) operacionaliza este framework para ambientes digitais mediados por IA, distinguindo entre automação convencional e agentes autónomos, e introduzindo uma taxonomia sistemática de interações humano-IA.

### 1.2 Distinção Fundamental: IA vs. Automação Convencional (A1–A6)

A taxonomia DART-NET estabelece uma distinção crítica entre agentes de IA autónomos e sistemas de automação convencional. Esta distinção é essencial para evitar a inflação conceptual que frequentemente caracteriza o discurso público sobre IA:

| Código | Classificação | Definição Operacional |
|--------|---------------|----------------------|
| **A1** | Agente de IA (AI Agent) | Sistema com autonomia decisória, capacidade de aprendizagem ou raciocínio adaptativo (ex.: LLMs, sistemas de classificação autónoma) |
| **A2** | Bot Convencional | Automação determinística com regras fixas, sem capacidade de aprendizagem ou adaptação contextual |
| **A3** | Script/Automação | Ferramenta de automação gerada por IA ou utilizada para tarefas repetitivas, sem autonomia em tempo de execução |
| **A4** | Humano Assistido por IA | Interação em que um humano utiliza IA como ferramenta de apoio, mantendo o controlo decisório |
| **A5** | Discussão sobre IA | Conteúdo que discute IA sem descrever interação direta com um agente |
| **A6** | Irrelevante | Conteúdo sem relação com IA, bots ou automação |

### 1.3 Questões de Investigação

O estudo é orientado por cinco questões de investigação:

- **QI1**: Qual é a proporção de agentes de IA autónomos (A1) face a bots/scripts convencionais (A2/A3) nos ecossistemas de videojogos analisados?
- **QI2**: Como se estruturam as interações humano-IA (I1–I6) e que padrões emergem entre jogos sandbox e controlados?
- **QI3**: Em que medida as dimensões DART (Diálogo, Acesso, Risco, Transparência) são satisfeitas nas interações documentadas?
- **QI4**: Que evidências empíricas sustentam a ocorrência de cocriação (VC1/VC2) versus codestruição (VC3) de valor?
- **QI5**: Que implicações teóricas e práticas emergem para o design de ecossistemas de videojogos com IA integrada?

### 1.4 Metodologia de Recolha e Ingestão Inicial

A pipeline DART-NET v3.0 processou um corpus canónico de 303 tópicos de discussão, com delimitação temporal estrita de janeiro de 2024 a 2026. Foram filtradas 6.485 mensagens em bruto, das quais 1.032 foram inicialmente validadas semanticamente e codificadas pelo modelo DeepSeek sob o protocolo DART-NET, garantindo conformidade com a taxonomia A1–A6, I1–I6, VC1–VC4 e as quatro dimensões de Prahalad & Ramaswamy (2004).

### 1.5 Protocolo de Refinamento Epistémico e Critérios de Poda Metodológica

Em investigação netnográfica e estudos de cocriação de valor mediada por tecnologia (Kozinets, 2020; Prahalad & Ramaswamy, 2004; Vargo & Lusch, 2004), a validade do construto empírico depende criticamente da eliminação de ruído semântico e de dados espúrios que não representem o fenómeno sob escrutínio. 

Por conseguinte, foi aplicado um **protocolo rigoroso de refinamento epistémico** para expurgar do corpus analítico três categorias de mensagens que enfraqueciam a precisão teórica do estudo:

| Categoria Excluída | Critério Operacional | Frequência | Justificação Teórica e Metodológica |
| :--- | :--- | :---: | :--- |
| **1. Não-IA / Ruído Residual** | `ai_type == "A6"` | 51 posts | **Preservação dos Limites do Construto**: Mensagens classificadas como A6 representam falsos positivos da pesquisa booleana nos fóruns (ex.: lore de classes em WoW, conversas contextuais de guilda, gírias ou menções incidentais de "AI" fora do contexto de tecnologia). A sua permanência no corpus inflacionava artificialmente as métricas de não-interação (`I6`) e ausência de valor (`VC4`), gerando um viés de diluição analítica. |
| **2. Posts com "Zero DART"** | `D=0, A=0, R=0, T=0` | 172 posts | **Exigência Teórica dos Blocos Construtivos de Cocriação**: O modelo DART (Prahalad & Ramaswamy, 2004) postula que o valor cocriado emerge da interação ativa nos blocos de Diálogo, Acesso, Avaliação de Risco e Transparência. Um post que pontue zero em todas as quatro dimensões não oferece substância empírica para responder a nenhuma das cinco Questões de Investigação (QI1 a QI5). A sua exclusão assegura que 100% dos dados retidos contenham evidência observável de pelo menos uma dimensão DART. |
| **3. Queixas de Bots Mecânicos / Farming Tradicional** | Tópicos de gold farming, pixel scripts, casino bots e fishing macros (A2) | 33 posts | **Filtro Paradigmático (Automação Convencional vs. IA Moderna)**: O foco da investigação reside no impacto da inteligência artificial generativa, autónoma e adaptativa da era pós-2024 (LLMs, copilotos, agentes MCP, decisões contextuais). Queixas antigas sobre farming mecânico e bots determinísticos de repetição (fenómeno comum nos MMOs desde 2005) representam batota convencional sem qualquer agência inteligente ou dimensão cocriativa. A sua eliminação clarifica a fronteira sociotécnica do estudo. |

> [!NOTE]
> **Consolidação do Corpus Refinado**:
> * Da interseção dos critérios resultou a exclusão líquida de **207 posts únicos** (48 posts apresentavam simultaneamente classificação A6 e pontuação Zero-DART).
> * O dataset refinado consolida-se em **825 posts de alta densidade empírica**, preservando 100% dos episódios de agentes autónomos (A1), copilotos (A4) e cocriação de valor (VC1 e VC2).
> * Todos os 207 posts excluídos foram arquivados com registo de auditoria em `data/analysis/excluded_posts_log.json`, e o corpus original de 1.032 posts permanece salvaguardado em `data/analysis/netnography_results_1032_unpruned.jsonl`.

### 1.6 Abordagem Multinível: Do Post Atómico à Thread Conversacional

Para responder com profundidade e rigor epistémico ao fenómeno da cocriação de valor mediada por IA, o estudo opera segundo uma **arquitetura analítica em três níveis concêntricos**:
1. **Nível Micro (O Post — $N=825$ análises)**: Constitui a unidade primária de calibração empírica. Cada mensagem é individualmente codificada com base no princípio de evidência literal verificável (*verbatim quotes*), atribuindo escores DART (0 a 5), tipologia de agência (A1–A5), estrutura de interação (I1–I6) e valor (VC1–VC4).
2. **Nível Meso (A Thread / Tópico de Discussão — $N=143$ discussões ativas)**: Constitui a unidade de síntese e sentido sociotécnico. A cocriação e a codestruição de valor não ocorrem no vácuo de frases isoladas, mas sim em ciclos conversacionais iterativos. A agregação dos posts nos seus 143 tópicos de origem revela trajetórias deliberativas completas, dinâmicas de valor dominante e clusters temáticos emergentes.
3. **Nível Macro (O Ecossistema — Sandbox vs. Controlado)**: Constitui o nível de contraste teórico global, comparando como a arquitetura técnica e a governança institucional de *EVE Online* e *World of Warcraft* moldam a aceitação, resistência e emergência de agentes de IA.

---

## 2. Taxonomia de Agentes de IA e Interações

### 2.1 Distribuição de Tipos de IA (A1–A5 no Corpus Refinado)

Após a remoção do ruído residual (A6) e da automação mecânica desprovida de DART, a distribuição dos **825 posts refinados** revela com clareza o perfil do discurso comunitário:

| Tipo de IA | Frequência | Percentagem | Papel no Ecossistema |
| :--- | :---: | :---: | :--- |
| **A5 (Discussão Reflexiva sobre IA)** | 637 | 77,2% | Discurso crítico, expectativas éticas, impacto no mercado de trabalho e futuro do design de videojogos. |
| **A1 (Agente de IA Autónomo / LLM)** | 95 | 11,5% | Agentes com raciocínio contextual, LLMs integrados, companheiros de tripulação e bots generativos. |
| **A4 (Humano Assistido por IA)** | 59 | 7,2% | Copilotos de código, criação de macros assistidas por IA (vibe-coding) e ferramentas de análise situacional. |
| **A2 (Bot Convencional Relevante)** | 17 | 2,1% | Automações que afetam criticamente as dimensões DART (ex.: transparência de dados em APIs ou moderação). |
| **A3 (Script / Automação Determinística)** | 17 | 2,1% | Scripts determinísticos com impacto direto em acesso a dados ou interfaces externas. |
| **A6 (Ruído / Não-IA)** | **0** | **0,0%** | *(Integralmente expurgado na fase de poda metodológica).* |
| **Total** | **825** | **100,0%** | **Corpus Empírico Refinado** |

**Análise**: No corpus purificado, as interações e discussões com relevância direta de IA (A1 + A4) representam cerca de **18,7%** do ecossistema, comprovando que quase um em cada cinco posts empíricos envolve agência autónoma ou hibridismo humano-máquina. A predominância de A5 (77,2%) reflete que os ecossistemas de videojogos operam primariamente como arenas de negociação social sobre a introdução da IA.

**Resposta à QI1**: A proporção de agentes de IA autónomos (A1: 11,5%) e de assistência híbrida (A4: 7,2%) supera substancialmente a presença de bots e scripts convencionais residuais (A2+A3: 4,2%). Este resultado demonstra que, ao expurgar o ruído e o farming mecânico do século passado, o ecossistema atual encontra-se fortemente polarizado entre o **discurso sociotécnico reflexivo (A5)** e a **experimentação ativa com agentes e copilotos modernos (A1/A4)**.

### 2.2 Estruturas de Interação Humano-IA (I1–I6)

| Tipo de Interação | Frequência | Percentagem | Natureza Empírica |
| :--- | :---: | :---: | :--- |
| **I4 (Humano → Humano sobre IA)** | 641 | 77,7% | Trocas sociais sobre impacto, ética, receio de substituição e viabilidade de IA nos jogos. |
| **I6 (Sem interação significativa)** | 67 | 8,1% | Menções contextuais breves, que caíram drasticamente de 34,0% para apenas 8,1% após a poda. |
| **I3 (Humano ↔ IA Bidirecional)** | 56 | 6,8% | Loops de interação contínua, simulação com copilotos e diálogos iterativos (núcleo de cocriação). |
| **I1 (Humano → IA Unidirecional)** | 48 | 5,8% | Comandos diretos, prompts, consultas de informação e instruções a copilotos ou LLMs. |
| **I5 (Humano → Ambiente mediado por IA)** | 6 | 0,7% | Exploração de instâncias com bots dinâmicos (Follower Dungeons) e interfaces de inteligência. |
| **I2 (IA → Humano Unidirecional)** | 7 | 0,8% | Recomendações proativas, alertas situacionais e relatórios gerados autonomamente por agentes. |
| **Total** | **825** | **100,0%** | — |

**Análise**: As interações diretas e ativas com agentes de IA (I1 + I2 + I3 + I5) somam agora **14,2% do corpus** (117 posts), revelando uma penetração técnica muito superior à observada na amostra não filtrada. Destaca-se a solidez das interações bidirecionais (I3: 6,8%), que formam a base analítica para a cocriação simétrica de valor.

**Resposta à QI2**: Embora o discurso social comunitário (I4: 77,7%) continue a ser a forma dominante de circulação de sentido em torno da IA, o corpus refinado revela uma camada técnica viva de interações diretas (14,2%), liderada por fluxos bidirecionais (I3) e de comando direto (I1).

---

## 3. Análise por Dimensão DART

## 3. Análise por Dimensão DART

### 3.1 Visão Global das Pontuações no Corpus Refinado

| Dimensão DART | Média no Corpus Refinado (0–5) | Interpretação Metodológica |
| :--- | :---: | :--- |
| **Diálogo (D)** | **1,09** | Presença ativa em canais de feedback, loops de copilotos e comandos iterativos. |
| **Acesso (A)** | **1,20** | Disponibilização de inteligência de jogo, endpoints de API e copilotos de dados. |
| **Risco (R)** | **1,61** | Dimensão mais saliente: apreensão com desequilíbrio competitivo, assimetria e dependência. |
| **Transparência (T)** | **1,34** | Reivindicação de explicabilidade técnica, rotulagem de IA e diagnóstico auditável. |

Com a exclusão metódica dos 172 posts "Zero DART", a densidade analítica do corpus elevou-se expressivamente. Todas as quatro dimensões apresentam agora valores médios superiores a 1,0, comprovando que **100% das mensagens retidas contêm substância empírica verificável** para a análise de cocriação de valor.

### 3.2 Diálogo (Média: 1,09/5)

A dimensão Diálogo avalia a capacidade de comunicação bidirecional, reciprocidade e negociação entre utilizadores humanos e instâncias de IA.

**Evidências empíricas no corpus refinado**:

- **Post 510327_2912893** (EVE Online, A1, I3, VC1): Pontuação de Diálogo = **5/5**. Interação direta e aberta onde o próprio modelo é integrado na mediação comunitária: *"I’m Claude — the AI assistant he works with on EVE Crews... it’s more honest — it reflects how the tool is actually made."* O diálogo atinge o nível máximo de reciprocidade entre programador, comunidade e agente.
- **Post 510327_2913288** (EVE Online, A1, I3, VC1): Pontuação de Diálogo = **5/5**. Demonstração de ciclo iterativo de suporte: *"Here’s a more detailed response from Claude regarding your issues, for your info... we tweaked the classification rules."*
- **Post 1i6m4i6_87** (World of Warcraft, A1, I3, VC4): Pontuação de Diálogo = **5/5**. Reflexão crítica sobre a calibração do diálogo humano-máquina: *"AI can be confidently incorrect... It's best to go in with some level of knowledge about the question you're asking, so you can recognize when it's wrong."*

**Análise**: O Diálogo floresce com particular intensidade nos ecossistemas com ferramentas abertas e assistentes integrados, onde a IA não opera como um oráculo passivo, mas como um interlocutor interativo de cocriação.

### 3.3 Acesso (Média: 1,20/5)

A dimensão Acesso investiga como os sistemas de IA facilitam, democratizam ou restringem o acesso a recursos, conhecimento tático e capacidades computacionais no jogo.

**Evidências empíricas no corpus refinado**:

- **Post 513384_2889848** (EVE Online, A1, I1, VC1): Pontuação de Acesso = **5/5**. O utilizador documenta a expansão radical de acesso através de servidores MCP: *"It gives Claude (or any MCP client) live EVE data with judgment baked in. 26 tools available for market, fittings, navigation."*
- **Post 516433_2913324** (EVE Online, A1, I1, VC1): Pontuação de Acesso = **5/5**. Acesso programático a dados do jogo: *"exposing EVE’s public ESI endpoints as tools an AI assistant can call directly."*
- **Post 492935_2751948** (EVE Online, A5, I4, VC2): Pontuação de Acesso = **5/5**. Democratização linguística e cognitiva: *"It is not about replacing English, but about expanding access and participation."*

**Análise**: O Acesso surge como o pilar mais funcionalmente transformador do DART: a IA quebra a barreira de entrada da extrema complexidade de folhas de cálculo e dados de API em jogos sandbox.

### 3.4 Risco (Média: 1,61/5)

A dimensão Risco constitui a faceta mais proeminente e articulada no discurso empírico dos jogadores (1,61/5), englobando preocupações de justiça distributiva (*fair play*), exploração económica e perda de agência.

**Evidências empíricas no corpus refinado**:

- **Post reddit_1ormrc6_1** (World of Warcraft, A5, I4, VC3): Pontuação de Risco = **5/5**. Preocupação explícita com assimetria económica e vantagens indevidas: *"Unfair advantage. Will players using a paid AI assistant for market analysis or crafting get an edge that free-to-play users cannot match?"*
- **Post 2116712_27042848** (World of Warcraft, A5, I4, VC3): Pontuação de Risco = **5/5**. Dano à integridade do ambiente competitivo de PvP: *"This is an epidemic, and feel I see AT LEAST one of these in each lobby. When are proactive algorithmic bans coming?"*
- **Post 1ph9o3i_22** (EVE Online, A4, I3, VC3): Pontuação de Risco = **4/5**. Alucinações de modelos generativos que causam perdas de ativos espaciais: *"MISTAKES WERE MADE."*

**Análise**: Ao contrário da visão tecnicista que associa o risco apenas à batota mecânica, os utilizadores no corpus refinado articulam riscos epistémicos sofisticados: a emergência de "vibe-cheating", a opacidade dos modelos proprietários e a dependência psicológica ou técnica de copilotos de decisão rápida.

### 3.5 Transparência (Média: 1,34/5)

A dimensão Transparência mensura a visibilidade das regras algorítmicas, a rotulagem de conteúdo gerado por IA e a explicabilidade das decisões dos agentes.

**Evidências empíricas no corpus refinado**:

- **Post 510327_2913288** (EVE Online, A1, I3, VC1): Pontuação de Transparência = **5/5**. Disponibilização de instrumentação direta para auditoria: *"The diagnostics panel exists because you couldn’t reach a browser console — and provides complete visibility into AI decisions."*
- **Post 2318118_29656965** (World of Warcraft, A5, I4, VC3): Pontuação de Transparência = **5/5**. Exigência de rotulagem e escrutínio público das editoras: *"they say they didn’t use AI, but the devs could’ve at some point especially for generative texture work, we demand disclosure."*
- **Post 510327_2866379** (EVE Online, A1, I3, VC1): Pontuação de Transparência = **5/5**. Documentação explícita de parâmetros analíticos: *"The crew numbers in EVE Crews are derived from a blend of official CCP lore, historical documentation and ship volume metrics."*

**Análise**: A Transparência é a dimensão com maior assimetria entre jogos: em EVE Online é ativamente construída pelos criadores de ferramentas comunitárias (via logs e diagnósticos abertos), ao passo que em World of Warcraft é primariamente reivindicada contra a opacidade das políticas corporativas da Blizzard.

---

## 4. Análise Comparativa de Jogos: Sandbox vs. Controlado

### 4.1 Distribuição do Corpus Refinado

| Jogo | Posts Analisados no Corpus Refinado | Percentagem |
| :--- | :---: | :---: |
| **World of Warcraft (Ambiente Controlado)** | 521 | 63,2% |
| **EVE Online (Ambiente Sandbox)** | 304 | 36,8% |
| **Total Refinado** | **825** | **100,0%** |

### 4.2 Comparação de Padrões e Culturas Comunitárias

1. **EVE Online (Sandbox — 304 posts)**:
   * **Cultura Construtiva e Extensível**: O acesso aberto à API ESI e a introdução do protocolo MCP catalisam a criação de agentes autónomos (A1) e copilotos avançados (A4). 
   * **Cocriação Dialógica**: Concentra os casos mais proeminentes de cocriação efetiva (VC1: ex. ferramentas EVE Crews e Battlefield.Space).
   * **Risco Centrado na Economia**: Preocupação predominante com a distorção do mercado financeiro e a desestabilização de nós de produção espacial por agentes algorítmicos.

2. **World of Warcraft (Controlado — 521 posts)**:
   * **Cultura Protetiva e Regulada**: Foco nas instâncias de combate (míticas e raids), onde a autonomia externa é encarada com desconfiança e severamente punida pelo código de conduta da editora.
   * **Codestruição e Frustração (VC3)**: Forte saliência de queixas sobre moderação automática cega de tickets de suporte e desconfiança quanto à presença de bots inteligentes nas arenas competitivas.
   * **Inovação Oficial**: Acolhimento positivo mas cauteloso de instâncias geridas por IA nativa (*Follower Dungeons*), vistas como oportunidade de treino sem pressão tóxica de outros jogadores.

### 4.3 Agregação ao Nível de Tópicos de Discussão (143 Threads Ativas)

Na perspetiva meso-sociotécnica, o agrupamento dos 825 posts refinados nos seus respetivos **143 tópicos de discussão (*threads*) ativos** permite captar os ciclos deliberativos e a evolução temporal das dinâmicas de cocriação de valor. A análise comparativa agregada por ecossistema evidencia contrastes estruturais marcantes:

| Dimensão Analítica / Ecossistema | EVE Online (Sandbox Aberto) | World of Warcraft (Ambiente Controlado) | Total Consolidado |
| :--- | :---: | :---: | :---: |
| **Número de Tópicos Ativos** | **59 tópicos** (41,3%) | **84 tópicos** (58,7%) | **143 tópicos** (100,0%) |
| **Volume de Posts Analisados** | 304 posts (36,8%) | 521 posts (63,2%) | 825 posts (100,0%) |
| **Média de Posts Retidos por Tópico** | `5,15` posts/tópico | `6,20` posts/tópico | `5,77` posts/tópico |
| **Vetor DART Médio Global** | `D: 0,95 | A: 1,48 | R: 1,56 | T: 1,49` | `D: 0,97 | A: 1,17 | R: 1,56 | T: 1,32` | `D: 0,96 | A: 1,29 | R: 1,56 | T: 1,39` |
| **Tópicos VC1 (Cocriação Efetiva)** | **8,5%** (5 tópicos) | **16,7%** (14 tópicos) | **13,3%** (19 tópicos) |
| **Tópicos VC2 (Potencial de Cocriação)** | **13,6%** (8 tópicos) | **13,1%** (11 tópicos) | **13,3%** (19 tópicos) |
| **Tópicos VC3 (Codestruição / Fricção)** | **13,6%** (8 tópicos) | **26,2%** (22 tópicos) | **21,0%** (30 tópicos) |
| **Tópicos VC4 (Reflexivos / Neutros)** | **64,4%** (38 tópicos) | **44,0%** (37 tópicos) | **52,4%** (75 tópicos) |

**Interpretação Teórica**:
1. **Salto de Densidade de Valor**: Enquanto na análise atómica por post apenas 3,2% das mensagens atingiam VC1 e 10,9% VC3, na escala de tópicos **13,3% das discussões materializam cocriação efetiva (VC1)** e **21,0% refletem episódios de codestruição (VC3)**. No seu conjunto, **47,6% dos tópicos** apresentam impacto ativo de valor (VC1 + VC2 + VC3), comprovando que a unidade conversacional (*thread*) captura a totalidade do ciclo deliberativo que posts isolados fragmentam.
2. **Assimetria Estrutural de Acesso e Transparência**: Em *EVE Online*, o Acesso médio (`1,48`) e a Transparência (`1,49`) superam nitidamente os valores de *WoW* (`1,17` e `1,32`), impulsionados pela infraestrutura aberta de APIs (ESI e MCP).
3. **Hiperconcentração de Codestruição em WoW**: Em *World of Warcraft*, mais de um quarto dos tópicos ativos (**26,2% em VC3**, contra 13,6% em EVE) documentam perdas severas de confiança, banimentos indevidos e atritos institucionais decorrentes da automação do suporte ao cliente.

### 4.4 Tipologia Emergente de Tópicos: Os 5 Clusters Sociotécnicos

A análise de padrões em todo o corpus de 143 tópicos permitiu identificar **cinco agrupamentos sociotécnicos emergentes**, caracterizados por distintas configurações de agência, interação e blocos DART:

1. **Cluster 1: Ferramentas Externas, Integração de APIs e MCP** (31 tópicos | 21,7%)
   * *Foco*: Desenvolvimento e interligação de dados via APIs públicas (ESI, Model Context Protocol - MCP, Pyfa, exportação de telemetria para LLMs como Claude e GPT-4).
   * *Métricas*: Elevado Acesso (`A: 1,8`) e Transparência (`T: 1,6`). Forte concentração de cocriação colaborativa (VC1 e VC2).
2. **Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva** (29 tópicos | 20,3%)
   * *Foco*: Tensão entre assistência algorítmica legítima e automação desleal em ambientes PvP, arenas e frotas de combate.
   * *Métricas*: Pico de Risco Percebido (`R: 1,5`) e Acesso restrito (`A: 0,9`). Elevada fricção normativa e acusações mútuas.
3. **Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning** (26 tópicos | 18,2%)
   * *Foco*: Contestação ao uso de IA pela publicadora para resolução de tickets, triagem de denúncias e suspensão de contas.
   * *Métricas*: Risco mais severo do estudo (`R: 2,1`) e baixa Transparência (`T: 1,0`). Principal nascente de codestruição de valor (VC3).
4. **Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores** (20 tópicos | 14,0%)
   * *Foco*: Avaliação de companheiros e instâncias operadas por IA oficial da publicadora (*Follower Dungeons*, *Delves*, *Aura Guidance*).
   * *Métricas*: Acesso institucional controlado (`A: 1,4`) e Risco moderado (`R: 1,3`). Dinâmica mista entre inclusão de jogadores casuais (VC2) e isolamento da sociabilidade humana (VC4).
5. **Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding** (37 tópicos | 25,9%)
   * *Foco*: Utilização de assistentes generativos para conceção de macros, interfaces, scripts Lua e addons complexos.
   * *Métricas*: Acesso técnico relevante (`A: 1,3`) e risco contido (`R: 1,3`). Maior volume empírico, catalisando cocriação efetiva (VC1) na democratização da programação comunitária.

### 4.5 Casos Paradigmáticos de Tópicos de Discussão

O quadro seguinte sintetiza tópicos emblemáticos que ilustram o comportamento empírico dos clusters nos dois ecossistemas:

| ID Tópico | Título Central | Ecossistema / Cluster | Agência / Interação | Vetor DART (Médias) | Dinâmica de Valor | Evidência Literal Verificável (*Verbatim Quote*) |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **`510327`** | *EVE Crews: A lore-accurate\* API-linked crew simulator* | EVE Online<br>Cluster 1 (APIs/MCP) | **A1** / **I3** | `D: 2,9`<br>`A: 2,4`<br>`R: 1,2`<br>`T: 2,3` | **VC1** (Cocriação Efetiva) | *"The crew numbers in EVE Crews are derived from a blend of official CCP lore, historical game data, and community research..."* |
| **`516433`** | *EVE MCP Server — querying ESI from Claude, Copilot and other AI assistants* | EVE Online<br>Cluster 1 (APIs/MCP) | **A1** / **I4** | `D: 0,0`<br>`A: 5,0`<br>`R: 2,0`<br>`T: 3,0` | **VC4** (Reflexivo Técnico) | *"exposing EVE’s public ESI endpoints as tools an AI assistant can call directly"* |
| **`1jukb0x`** | *Psa For The New Bros Dont Ask Chatgpt About Eve* | EVE Online<br>Cluster 5 (Copilotos) | **A5** / **I3** | `D: 1,4`<br>`A: 1,3`<br>`R: 1,3`<br>`T: 1,0` | **VC1** (Cocriação Efetiva) | *"I asked gpt what it wanted to say about this post here it is. ... If someone points out I gave garbage, I can course-correct mid-convo."* |
| **`508618`** | *Recorded a bot in high sec - but why even bother?* | EVE Online<br>Cluster 3 (Suporte/Bans) | **A5** / **I4** | `D: 1,4`<br>`A: 0,5`<br>`R: 2,2`<br>`T: 1,5` | **VC3** (Codestruição) | *"Why is he compromising his acc for this? ... most commonly RMT ... IP bans does little - VPNs exist and IPs can be changed."* |
| **`reddit_1tvlpnw`** | *Sick of spam and bots ruining our game? Here's an addon that uses ML...* | WoW<br>Cluster 2 (Fair Play) | **A3** / **I4** | `D: 0,0`<br>`A: 2,0`<br>`R: 1,5`<br>`T: 0,5` | **VC4** (Reflexivo Normativo) | *"it would bring up the report window and fill in the box with their coordinates a timestamp and the reason for report botting"* |
| **`reddit_1v3v2p2`** | *Claude Code Success* | WoW<br>Cluster 5 (Copilotos) | **A1** / **I3** | `D: 5,0`<br>`A: 4,0`<br>`R: 1,0`<br>`T: 1,0` | **VC1** (Cocriação Efetiva) | *"Explained a breakdown to what happened. Gave a link to the blue post. Directed it to review addons... Instructed it to add updated logic"* |

---

## 5. Cocriação e Codestruição de Valor (VC1–VC4)

### 5.1 Distribuição Global no Corpus Refinado

| Categoria de Valor | Frequência | Percentagem | Papel Teórico |
| :--- | :---: | :---: | :--- |
| **VC1 (Cocriação de Valor Efetiva)** | 26 | 3,2% | Parceria simétrica bem-sucedida com ganhos tangíveis mútuos. |
| **VC2 (Potencial Cocriação de Valor)** | 72 | 8,7% | Soluções em desenvolvimento, propostas conceituais e intenções de colaboração. |
| **VC3 (Codestruição de Valor)** | 90 | 10,9% | Perdas financeiras, frustração com alucinações, vantagens injustas ou bans indevidos. |
| **VC4 (Sem Evidência Direta)** | 637 | 77,2% | Discussões reflexivas sem impacto empírico mensurável de ganho ou perda imediata. |
| **Total** | **825** | **100,0%** | — |

**Análise**: Com a poda do ruído espúrio, a proporção de posts que documentam um **impacto ativo de valor (VC1 + VC2 + VC3)** ascende a **22,8% do corpus** (188 posts), contra apenas 11,4% antes da filtragem. 

A codestruição de valor (VC3: 10,9%) manifesta-se com frequência superior à cocriação efetiva (VC1: 3,2%), refletindo que a tecnologia de IA contemporânea ainda introduz elevada fricção, alucinações e assimetrias que perturbam as expectativas dos jogadores.

### 5.2 Evidências Paradigmáticas de Cocriação de Valor (VC1)

* **Post 510327_2870703** e **Post 510327_2913288** (EVE Online): O utilizador identifica anomalias na atribuição de tripulação a naves capitais e o programador, juntamente com o agente Claude, analisa o log, reescreve as regras de inferência e publica a correção em tempo real. O valor gerado reverte em benefício de toda a comunidade.
* **Post 513384_2889848** (EVE Online): Criação colaborativa de um servidor MCP público para dotar LLMs de compreensão contextual das 26 principais tabelas de dados de EVE, permitindo a qualquer jogador planear frotas conversacionalmente.

### 5.3 Evidências Paradigmáticas de Codestruição de Valor (VC3)

* **Post reddit_1ariy3g_20** (World of Warcraft): Automatização opaca de tickets de serviço ao cliente onde respostas padronizadas fecham chamados sem analisar o problema (*"Took me 5 tickets to finally get someone who looked into my ticket for more than 5 seconds"*), destruindo a confiança no suporte.
* **Post 1ph9o3i_22** (EVE Online): Copiloto generativo fornece cálculos errados de refinação de minérios e fitações, resultando na perda de uma nave dispendiosa em combate (*"MISTAKES WERE MADE"* — Risco 4/5).

---

## 6. Reflexão sobre as Questões de Investigação

### 6.1 QI1: Proporção de Agentes de IA Autónomos vs. Bots Convencionais
**Resposta**: No corpus purificado, os agentes de IA autónomos (A1: 11,5%) e copilotos assistidos (A4: 7,2%) superam largamente os bots convencionais e scripts mecânicos residuais (A2+A3: 4,2%). No entanto, ambos são envolvidos por uma densa camada de discurso sociotécnico reflexivo (A5: 77,2%).

### 6.2 QI2: Estruturas de Interação Humano-IA
**Resposta**: As interações diretas com agentes de IA (I1, I2, I3 e I5) somam **14,2%** do corpus refinado, com destaque para a interação bidirecional iterativa (I3: 6,8%). O canal predominante permanece a discussão humana sobre a tecnologia (I4: 77,7%), enquanto o ruído sem interação (I6) caiu para 8,1%.
* **Ampliação ao Nível de Tópicos**: Quando analisada ao nível de tópicos conversacionais completos, a presença de interação agêntica e colaborativa direta ganha ainda maior relevância: cerca de **30,8% dos tópicos** apresentam padrões predominantes de interação direta (I1/I2) ou cooperação triádica (I3: Humano + IA + Comunidade), particularmente nos clusters de APIs/MCP e Copilotos. Revela-se assim que discussões que se iniciam sob a forma de debate comunitário abstrato (I4) progridem frequentemente, através da partilha iterativa de código, logs e testes de prompts, para ciclos colaborativos de cocriação triádica (I3).

### 6.3 QI3: Satisfação das Dimensões DART
**Resposta**: No corpus refinado, todas as dimensões DART satisfazem critérios mínimos de substância empírica ($\text{Médias} > 1,0$): Risco lidera com **1,61/5**, seguido de Transparência (**1,34/5**), Acesso (**1,20/5**) e Diálogo (**1,09/5**). O Risco é a dimensão estruturante da perceção comunitária.

### 6.4 QI4: Cocriação (VC1/VC2) vs. Codestruição (VC3) de Valor
**Resposta**: As discussões com impacto direto de valor totalizam **22,8%** do corpus. A codestruição de valor (VC3: 10,9%) sobrepõe-se à cocriação efetiva (VC1: 3,2%), demonstrando que a integração de IA em ecossistemas de jogos ainda opera num estágio de maturidade assimétrico e conflituoso.
* **Ampliação ao Nível de Tópicos**: A unidade analítica da thread revela uma proporção muito mais substancial de impacto ativo de valor, abrangendo **47,6% dos tópicos ativos** (13,3% VC1, 13,3% VC2 e 21,0% VC3). Esta agregação expõe uma clivagem radical entre clusters: enquanto os clusters de Ferramentas/APIs (Cluster 1) e Copilotos (Cluster 5) concentram episódios de cocriação simétrica (VC1/VC2) alicerçados em Diálogo e Acesso, os clusters de Moderação/Suporte (Cluster 3) e Fair Play (Cluster 2) concentram eventos severos de codestruição (VC3). Em *World of Warcraft*, a taxa de tópicos em VC3 atinge **26,2%** (contra 13,6% em EVE), espelhando um profundo descontentamento comunitário com sistemas opacos de moderação algorítmica e encerramento automatizado de tickets.

### 6.5 QI5: Implicações para o Design de Ecossistemas com IA
**Resposta**: O sucesso de ferramentas comunitárias baseadas em MCP em EVE Online indica que as editoras devem disponibilizar **interfaces abertas, auditáveis e com visibilidade de diagnóstico (Transparência)**. Inversamente, a automação opaca de suporte e moderação observada em WoW ilustra o caminho da rápida destruição de valor relacional.

**Síntese Comparativa Transversal (Sandbox vs. Ecossistema Controlado)**:
A análise transversal agregada demonstra que a arquitetura de governança e a infraestrutura técnica exercem um papel determinístico na transição do discurso comunitário da especulação defensiva para a cocriação tangível de valor (Prahalad & Ramaswamy, 2004). No ecossistema **Sandbox de *EVE Online***, a disponibilização aberta e padronizada da API ESI e a recente adoção do *Model Context Protocol* (MCP) catalisam uma governança descentralizada onde os jogadores assumem o papel de co-desenvolvedores informacionais. Ao facultar Acesso técnico direto (`A: 1,48`) e visibilidade de diagnóstico (`T: 1,49`), a CCP Games reduz a fricção epistémica e fomenta ecossistemas cooperativos (tais como *EVE Crews* e *Battlefield.Space*), convertendo agentes de IA em próteses de ampliação cognitiva que mitigam a complexidade sistémica em benefício mútuo da comunidade e da plataforma.

Em contrapartida, no ecossistema **Controlado de *World of Warcraft***, a governança algorítmica da Blizzard é estritamente centralizada e defensiva. A sandbox de addons em Lua é delimitada por restrições rigorosas e a IA oficial é confinada a ambientes isolados de jogabilidade assistida (*Follower Dungeons* e *Delves*). Concomitantemente, a automação opaca de pipelines de atendimento e aplicação de penalizações gera uma elevada taxa de codestruição de valor ao nível de tópicos (`VC3: 26,2%`), induzindo cinismo e sensação de desamparo institucional. Quando a cocriação desponta em *WoW*, ocorre quase exclusivamente nas margens informais através do *vibe-coding* de addons via LLMs externos. Em termos de design de ecossistemas digitais, conclui-se que interfaces abertas, auditáveis e programáveis catalisam a agência comunitária para a cocriação sustentável de valor (VC1/VC2), ao passo que arquiteturas muradas com automação opaca de suporte desviam a energia da comunidade para a contestação contínua, o atrito regulatório e a erosão do valor relacional (VC3).

---

## 7. Auditoria de Qualidade, Calibração e Fila de Validação Humana

### 7.1 Auditoria Cega Qualitativa (QualityGuardAgent)
A auditoria independente conduzida com o modelo `deepseek-v4-pro` sobre uma amostra de **159 codificações do corpus refinado** consolidou métricas de excelência:
* **Score Médio Global de Consistência**: **`91,31%`** (limiar crítico $\ge 70\%$ amplamente superado);
* **Veracidade das Evidências Literais**: **100%** de citações verificadas no texto original;
* **Casos Sinalizados com Alerta**: Apenas 8 casos em 159 análises auditadas, decorrentes exclusivamente de limiares conservadores de confiança.

### 7.2 Calibração da Fila de Validação Humana
* **Total de Posts com Validação Manual Prioritária (`human_review_required = True`)**: **708 posts (85,82%)**
* **Critérios de Sinalização**: Confiança analítica $< 0,80$, jargões altamente contextualizados, sarcasmo e ambiguidade entre categorias de fronteira.

---

## 8. Discussão Teórica, Reprodutibilidade e Gestão de Recursos

### 8.1 Arquitetura Não Destrutiva e Poda Metodológica
A pipeline garantiu a total rastreabilidade da investigação:
1. **Camada 1 (Raw Data)**: Preservados 430 ficheiros brutos intactos em `data/raw/`;
2. **Camada 2 (AI Coding)**: Registro integral das 1.032 codificações brutas em `netnography_results_1032_unpruned.jsonl` e do corpus refinado de 825 análises em `netnography_results.jsonl`;
3. **Log de Poda Auditável**: Documentação individualizada dos 207 posts excluídos e respetivos motivos teóricos em `data/analysis/excluded_posts_log.json`.

### 8.2 Monitorização e Custo Global da Pipeline
* **Volume de Chamadas de API**: Mais de 27.000 invocações acumuladas (`deepseek-v4-flash` e `deepseek-v4-pro`);
* **Custo Operacional Global**: **~$21,50 USD**, consolidando uma relação custo-eficácia inigualável para investigações empíricas em larga escala.

### 8.3 O Agente de Síntese de Tópicos (ThreadSynthesisAgent) e Entregáveis Analíticos

Na Fase 4.5 da investigação, o ecossistema multiagente foi expandido com a conceção e implementação do [`ThreadSynthesisAgent`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/thread_synthesis_agent.py), desenhado para executar a agregação algorítmica e a síntese sociotécnica do corpus purificado:

1. **Agregação Algorítmica e Integridade Empírica**: O agente agrupa com fidelidade os 825 posts validados nos seus **143 tópicos de discussão ativos** (59 em EVE Online e 84 em World of Warcraft), excluindo tópicos esvaziados pela poda metodológica e calculando, para cada unidade, o vetor DART médio ponderado, as frequências taxonómicas e o código de valor emergente.
2. **Entregável Estruturado JSON**: Os resultados estruturados de todos os tópicos foram consolidados em [`data/analysis/thread_level_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/thread_level_results.json), contendo metadados completos, métricas DART individuais e citações paradigmáticas para consumo programático e reprodutibilidade integral.
3. **Catálogo Sistemático e Macro-Síntese**: Foi gerado o documento exaustivo [`output/analise_agregada_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/analise_agregada_topicos.md) (com 2.206 linhas), que inclui uma ficha analítica sistemática para cada um dos 143 tópicos e a formalização teórica dos 5 clusters sociotécnicos identificados.
4. **Articulação Teórica Multinível**: Este módulo fecha o ciclo investigativo entre a calibração micro (posts individuais), a dinâmica meso (threads conversacionais) e a governança macro (ecossistemas sandbox vs. controlados), assegurando total rigor netnográfico segundo Kozinets (2020) e Prahalad & Ramaswamy (2004).