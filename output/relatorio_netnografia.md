# Relatório DART-NET v4.0: Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos

**Análise Comparativa Multinível Incorporada entre EVE Online (Sandbox) e World of Warcraft (Controlado)**

> [!IMPORTANT]
> **Revisão de dados v4.1 (1 de novembro de 2026)**: os valores deste relatório foram recalculados sobre o corpus corrigido `data/analysis/netnography_results_v4_1.jsonl`. As correções, registadas em `data/analysis/correcoes_v4_1_log.json`, foram:
> * **Jogo**: 14 tópicos do subreddit r/Eve estavam atribuídos a *World of Warcraft* (confirmado na API Arctic Shift). Passaram para *EVE Online*, o que altera todas as comparações entre ecossistemas.
> * **Duplicado**: o tópico `3000003` era uma cópia parcial do `2248893`; foi fundido (15 posts movidos, 3 duplicados removidos).
> * **Pseudonimização**: 20 nomes de utilizador que ainda apareciam no texto dos posts foram substituídos por *tokens*.
> * **Evidência DART**: cada citação foi verificada contra o texto original do post.
>
> O corpus ativo passa de 1.032 posts / 152 tópicos para **1.029 posts / 151 tópicos** (79 EVE Online, 72 World of Warcraft), e o corte de contraste passa de 825 para **824 posts**. Foi ainda acrescentada uma **codificação holística cega dos 151 tópicos** (`deepseek-v4-pro`, sem acesso aos rótulos dos posts) e um **modelo nulo** para a comparação micro vs. meso (`data/analysis/comparacao_meso_v4_1.json`). Os scripts estão em `scratch/v4_1/`.

---

## 1. Sumário Metodológico e Framework DART-NET v4.0 (Arquitetura Multinível Incorporada)

### 1.1 Enquadramento Teórico e Mudança de Paradigma Analítico

O presente relatório formaliza e aplica a framework **DART-NET v4.0** (Prahalad & Ramaswamy, 2004; Vargo & Lusch, 2016; Kozinets, 2020; DART-NET 2026) à análise da interação entre humanos e agentes de inteligência artificial (IA) em ecossistemas de videojogos. O modelo DART original — **Diálogo, Acesso, Risco e Transparência** — constitui a matriz conceptual para avaliar a qualidade das interações sociotécnicas. A versão **DART-NET v4.0** operacionaliza este referencial para ambientes digitais mediados por IA através de uma **Arquitetura Metodológica Multinível Incorporada (*Embedded Multilevel Design*)**, na qual o **Tópico de Discussão (*Thread*, Nível Meso, $N=151$)** assume o estatuto de **Unidade Primária de Análise, Sentido, Codificação Relacional e Teorização**, enquanto os **Posts Individuais (Nível Micro, $N=1.029$ posts ativos / $824$ no corte de contraste)** são integralmente preservados e incorporados dentro dos respetivos tópicos como **Unidade de Ancoragem Empírica (*Verbatim Grounding*) e Controlo Forense Anti-Alucinação**.

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
  * **QI1a** *(antiga QI1)*: Qual é a proporção de agentes de IA autónomos face a bots e scripts convencionais?
  * **QI1b** *(antiga QI2)*: Como se estruturam as interações humano-IA e que padrões emergem entre o ecossistema sandbox e o controlado?
* **QI2. Em que medida essas interações cocriam ou codestroem valor, e que papel desempenham as dimensões do modelo DART?**
  * **QI2a** *(antiga QI3)*: Em que medida se verificam as dimensões Diálogo, Acesso, Risco e Transparência nas interações documentadas?
  * **QI2b** *(antiga QI4)*: Que evidências empíricas sustentam a ocorrência de cocriação (VC1/VC2) face à codestruição (VC3) de valor?
* **QI3. Como é que a arquitetura de governança de cada ecossistema condiciona a cocriação de valor com IA, e que implicações daí decorrem?**
  * **QI3a**: Que diferenças sistemáticas existem entre EVE Online (sandbox aberto) e World of Warcraft (ecossistema controlado) na configuração DART e na dinâmica de valor?
  * **QI3b** *(antiga QI5)*: Que implicações teóricas e práticas emergem para o desenho de ecossistemas de videojogos com IA integrada?

### 1.5 Metodologia de Recolha e Ingestão Inicial

A pipeline DART-NET v3.0 processou um corpus canónico de 303 tópicos de discussão, com delimitação temporal estrita de janeiro de 2024 a 2026. Foram filtradas 6.485 mensagens em bruto, das quais 1.032 foram inicialmente validadas semanticamente e codificadas pelo modelo DeepSeek sob o protocolo DART-NET, garantindo conformidade com a taxonomia A1–A6, I1–I6, VC1–VC4 e as quatro dimensões de Prahalad & Ramaswamy (2004).

### 1.6 Protocolo de Refinamento Epistémico e Critérios de Poda Metodológica

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

### 1.7 Arquitetura Metodológica Multinível Incorporada (*Embedded Multilevel Design* — DART-NET v4.0)

À luz da teoria de **Interação Humano-Computador (HCI / CSCW)**, da **Lógica Dominante do Serviço (*Service-Dominant Logic* / Cocriação de Valor)** e dos **Estudos de Videojogos (*Game Studies*)**, a análise isolada de posts atómicos sofre de limitações epistemológicas severas que apenas uma arquitetura centrada no **Tópico de Discussão (*Thread*) com incorporação dos seus posts constituintes** permite superar:

1. **Princípio da Indexicalidade Conversacional e *Common Ground* (HCI / CSCW)**: Em plataformas assíncronas como *Reddit* e *Discourse* (Blizzard / CCP Forums), um post individual não é um documento autónomo, mas um **turno conversacional** (*conversational turn*; Clark & Brennan, 1991; Bakhtin, 1986) cujo significado semântico depende das mensagens antecedentes, do post de abertura (*Original Post* — OP) e das respostas subsequentes.
2. **Natureza Relacional e Temporal do Valor (Cocriação e Codestruição de Valor)**: Segundo Prahalad & Ramaswamy (2004), Vargo & Lusch (2016) e Plé & Chumpitaz Cáceres (2010), a cocriação (`VC1`/`VC2`) e a codestruição (`VC3`) de valor são **processos relacionais e temporais** que emergem na trajetória dialética (proposta ou queixa inicial $\rightarrow$ escrutínio técnico comunitário $\rightarrow$ iteração com o agente de IA $\rightarrow$ estabilização ou rutura). Quando o processo é fatiado em posts isolados, turnos intermédios de diagnóstico ou pergunta surgem artificialmente como "neutros" (`VC4`).
3. **Pragmática Subcultural Situada e Descodificação de Sátira/Ironia (*Game Studies* e Netnografia)**: Comunidades de MMORPGs (*EVE Online* e *World of Warcraft*) operam com elevado capital subcultural (Consalvo, 2007; Kozinets, 2020), recorrendo sistematicamente a ironia, sarcasmo, *shitposting* e paródia corporativa. Fora do enquadramento completo do tópico, codificadores automatizados incorrem em alucinação literal; quando o post é confrontado com a totalidade do tópico, a intenção figurativa torna-se empiricamente transparente (permitindo demarcar com rigor **238 posts** com tags explícitas de `[Sátira/Ironia]` ou `[Humor/Piada]` e **383 posts** com enquadramento retórico contextualizado em `output/tabela_resumos.md`).

#### 1.7.1 Contribuição Metodológica Central: A Comparação Micro vs. Meso

Estabelecer o **Tópico de Discussão ($N=151$)** como **Unidade Primária de Sentido, Análise e Teorização** e manter o **Post Individual ($N=1.029$ ativos / $824$ no corte de contraste)** como **Unidade Incorporada de Ancoragem Empírica (*Verbatim Grounding*) e Contraste Crítico** é uma das contribuições metodológicas do estudo. A revisão v4.1 testou esta comparação de três formas: (i) com a mesma base de posts nos dois níveis; (ii) contra um modelo nulo; (iii) com uma codificação holística independente dos tópicos.

| Dimensão de Valor | Micro: corte de contraste ($N=824$ posts) | Micro: corpus ativo ($N=1.029$ posts) | Meso — regra de agregação ($N=151$ tópicos) | Meso — leitura holística cega ($N=151$ tópicos) |
| :--- | :---: | :---: | :---: | :---: |
| **VC1 (Cocriação Efetiva)** | `3,2%` (26) | `2,5%` (26) | `12,6%` (19) | **`17,2%` (26)** |
| **VC2 (Potencial de Cocriação)** | `8,7%` (72) | `7,2%` (74) | `12,6%` (19) | **`13,2%` (20)** |
| **VC3 (Codestruição)** | `10,9%` (90) | `11,3%` (116) | `23,2%` (35) | **`15,9%` (24)** |
| **VC4 (Sem Evidência Direta)** | `77,2%` (636) | `79,0%` (813) | `51,7%` (78) | **`53,6%` (81)** |
| **Impacto Ativo ($\text{VC1}+\text{VC2}+\text{VC3}$)** | **`22,8%`** (188) | **`21,0%`** (216) | **`48,3%`** (73) | **`46,4%`** (70) |

**Leitura dos resultados**:
1. **A regra de agregação, por si só, não demonstra o ganho meso.** A pipeline classifica um tópico como VC1 se pelo menos um dos seus posts for VC1, e como VC3 se tiver mais posts VC3 do que VC2. Pela mesma lógica, quanto mais posts um tópico tem, mais provável é que fique com impacto ativo. Para medir esse efeito, os rótulos dos posts foram baralhados aleatoriamente entre tópicos, mantendo o tamanho de cada tópico (5.000 simulações). Com rótulos baralhados, a mesma regra produz em média **57,7%** de tópicos com impacto ativo (IC95%: 52,3–62,9%). O valor observado (48,3%) fica **abaixo** desse intervalo. O salto de ~21–23% para ~48% resulta, portanto, da regra e não constitui evidência empírica de cocriação ao nível do tópico.
2. **A leitura holística independente chega a uma proporção semelhante por outra via.** O `deepseek-v4-pro` leu cada tópico completo, por ordem cronológica, sem ver os rótulos dos posts, e aplicou as mesmas instruções dadas aos codificadores humanos. Resultado: **46,4%** de impacto ativo, com 150 das 151 citações de evidência verificadas literalmente no texto. Isto sustenta que perto de metade das discussões tem uma dinâmica de valor ativa. A leitura holística é estável: numa segunda corrida, em que só mudou a regra do VC secundário (Secção 7.3.1), manteve o VC principal em 142 dos 151 tópicos ($\kappa = 0,91$ teste-reteste).
3. **As duas leituras meso não identificam os mesmos tópicos.** O acordo entre a regra e a leitura holística é de apenas **49,0%** ($\kappa = 0,21$, acordo fraco). A leitura holística atribui mais cocriação efetiva (VC1: 26 vs. 19 tópicos) e menos codestruição (VC3: 24 vs. 35). Por exemplo, 20 dos 35 tópicos que a regra marca como VC3 são, na leitura holística, VC4: queixas genéricas sem dano concreto relatado.
4. **Conclusão operacional**: a proporção agregada (~48%) é robusta às duas leituras, mas a distribuição entre VC1, VC2 e VC3 depende do método. As conclusões substantivas sobre cocriação vs. codestruição devem apoiar-se na leitura holística e ser confirmadas pela codificação humana cega em curso (Secção 7.3).

Consequentemente, a **Framework Final DART-NET v4.0** estrutura-se em **três níveis analíticos incorporados** (preservando integralmente os posts de todos os tópicos e os respetivos campos analíticos):

1. **Nível Meso — Unidade Primária de Análise, Sentido e Teorização (O Tópico de Discussão — $N=151$ discussões ativas)**: Constitui o centro gravitacional do estudo e a base substantiva para responder às Questões de Investigação (QI1, QI2 e QI3). É a este nível que se determinam a **Trajetória Relacional de Valor (`VC1–VC4`)**, o **Vetor DART Agregado ($D, A, R, T$)**, o **Enquadramento Sociotécnico nos 5 Clusters** (aplicando a regra de fronteira entre o Cluster 1 e o Cluster 5) e o **Registo Pragmático/Retórico** (deteção de sátira, ironia e humor via `TopicDiscussionAnalystAgent` e `ThreadSynthesisAgent`).
2. **Nível Micro Incorporado — Unidade de Ancoragem Empírica e Evidência Forense (Os Posts do Tópico — $N=1.029$ ativos / $824$ no corte de contraste)**: Cada tópico mantém vinculados todos os seus posts constituintes e respetivos campos (`Post_ID`, `Texto_Real_Verbatim`, `Tema`, `Resumo <= 60 palavras`, `A1–A5`, `I1–I6`, `VC1–VC4`, `DART`). O post individual cumpre três funções indispensáveis:
   * **Ancoragem Anti-Alucinação (*Verbatim Grounding*)**: Nenhuma inferência de nível Meso é aceite sem citação literal verificável nos posts constituintes (ex.: citações exatas de código, mensagens de erro e respostas de suporte);
   * **Granularidade de Agência e Interação**: Fornece as contagens de micro-atos comunicativos (`A1–A5` e `I1–I6`) e a dispersão intra-tópico (consenso vs. polarização);
   * **Contraste Crítico e Auditoria Bidirecional Post-Tópico**: Permite confrontar a leitura atómica com a leitura holística, auditando a fidelidade factual do resumo do tópico.
3. **Nível Macro — Unidade Comparativa de Governança (O Ecossistema — Sandbox vs. Controlado)**: Contrasta como a arquitetura institucional aberta de *EVE Online* (API ESI, servidores MCP) versus a arquitetura regulada de *World of Warcraft* (sandbox Lua restrita, instâncias nativas fechadas) condiciona a emergência de valor sociotécnico.

---

## 2. Taxonomia de Agentes de IA e Interações

> **Nota Metodológica de Enquadramento (Abordagem Multinível Incorporada)**:  
> As contagens e frequências apresentadas nesta secção e na Secção 3 ($N=824$ posts) representam a **camada micro-empírica atomizada**, funcionando como um inventário descritivo dos turnos comunicativos e linha de base granular. Em estrito cumprimento da metodologia DART-NET v4.0, estes números **não devem ser interpretados como conclusões substantivas isoladas sobre o valor do ecossistema**, mas sim como a matéria-prima empírica cuja significação teórica plena se consolida ao nível dos **151 tópicos de discussão** (Secções 4, 6 e 7).

### 2.1 Distribuição de Tipos de IA (A1–A5 no Corpus Refinado)

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

**Resposta à QI1a (Proporção de Agentes Autónomos vs. Bots)**: A proporção de agentes de IA autónomos (A1: 11,5%) e de assistência híbrida (A4: 7,2%) supera substancialmente a presença de bots e scripts convencionais residuais (A2+A3: 4,1%). Este resultado demonstra que, ao expurgar o ruído e o farming mecânico do século passado, o ecossistema atual encontra-se fortemente polarizado entre o **discurso sociotécnico reflexivo (A5)** e a **experimentação ativa com agentes e copilotos modernos (A1/A4)**.

### 2.2 Estruturas de Interação Humano-IA (I1–I6)

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

**Resposta à QI1b (Estruturas de Interação Humano-IA)**: Embora o discurso social comunitário (I4: 77,7%) continue a ser a forma dominante de circulação de sentido em torno da IA, o corpus refinado revela uma camada técnica viva de interações diretas (14,2%), liderada por fluxos bidirecionais (I3) e de comando direto (I1).

---

## 3. Análise por Dimensão DART

> **Nota Metodológica de Enquadramento (Abordagem Multinível Incorporada)**:  
> As pontuações DART apresentadas nesta secção avaliam a intensidade dos micro-atos comunicativos contidos em cada um dos **824 posts refinados**. Servem como uma aferição de sensibilidade granular e inventário de referências textuais imediatas. A configuração sistémica completa do vetor DART — que traduz a maturidade sociotécnica real do ambiente lúdico — consolida-se através da ponderação agregada ao nível dos **151 tópicos de discussão** (Secção 4.3).

### 3.1 Visão Global das Pontuações no Corpus Refinado

| Dimensão DART | Média no Corpus Refinado (0–5) | Média só com Evidência Verbatim (0–5) | Interpretação Metodológica |
| :--- | :---: | :---: | :--- |
| **Diálogo (D)** | **1,09** | 1,08 | Presença ativa em canais de feedback, loops de copilotos e comandos iterativos. |
| **Acesso (A)** | **1,21** | 1,19 | Disponibilização de inteligência de jogo, endpoints de API e copilotos de dados. |
| **Risco (R)** | **1,62** | 1,54 | Dimensão mais saliente: apreensão com desequilíbrio competitivo, assimetria e dependência. |
| **Transparência (T)** | **1,34** | 1,28 | Reivindicação de explicabilidade técnica, rotulagem de IA e diagnóstico auditável. |

Com a exclusão dos 172 posts "Zero DART", todas as quatro dimensões apresentam valores médios superiores a 1,0, e todas as mensagens retidas têm pontuação em pelo menos uma dimensão. Esta propriedade decorre do próprio critério de exclusão e não constitui, por si só, evidência adicional de substância empírica.

**Verificação da evidência (v4.1)**: cada pontuação DART acima de zero vem acompanhada de uma citação justificativa produzida pelo LLM. A revisão v4.1 confirmou se essa citação existe literalmente no post. A coluna "só com evidência verbatim" atribui zero às pontuações cuja citação não foi encontrada no texto (total ou parcialmente). As médias descem no máximo 0,08 pontos (Risco), e a ordem das dimensões mantém-se.

### 3.2 Diálogo (Média: 1,09/5)

A dimensão Diálogo avalia a capacidade de comunicação bidirecional, reciprocidade e negociação entre utilizadores humanos e instâncias de IA.

**Evidências empíricas no corpus refinado**:

- **Post 510327_2912893** (EVE Online, A1, I3, VC1): Pontuação de Diálogo = **5/5**. Interação direta e aberta onde o próprio modelo é integrado na mediação comunitária: *"I’m Claude — the AI assistant he works with on EVE Crews... it’s more honest — it reflects how the tool is actually made."* O diálogo atinge o nível máximo de reciprocidade entre programador, comunidade e agente.
- **Post 510327_2913288** (EVE Online, A1, I3, VC1): Pontuação de Diálogo = **5/5**. Demonstração de ciclo iterativo de suporte: *"Here’s a more detailed response from Claude regarding your issues, for your info... we tweaked the classification rules."*
- **Post 1i6m4i6_87** (World of Warcraft, A1, I3, VC4): Pontuação de Diálogo = **5/5**. Reflexão crítica sobre a calibração do diálogo humano-máquina: *"AI can be confidently incorrect... It's best to go in with some level of knowledge about the question you're asking, so you can recognize when it's wrong."*

**Análise**: O Diálogo floresce com particular intensidade nos ecossistemas com ferramentas abertas e assistentes integrados, onde a IA não opera como um oráculo passivo, mas como um interlocutor interativo de cocriação.

### 3.3 Acesso (Média: 1,21/5)

A dimensão Acesso investiga como os sistemas de IA facilitam, democratizam ou restringem o acesso a recursos, conhecimento tático e capacidades computacionais no jogo.

**Evidências empíricas no corpus refinado**:

- **Post 513384_2889848** (EVE Online, A1, I1, VC1): Pontuação de Acesso = **5/5**. O utilizador documenta a expansão radical de acesso através de servidores MCP: *"It gives Claude (or any MCP client) live EVE data with judgment baked in. 26 tools available for market, fittings, navigation."*
- **Post 516433_2913324** (EVE Online, A1, I1, VC1): Pontuação de Acesso = **5/5**. Acesso programático a dados do jogo: *"exposing EVE’s public ESI endpoints as tools an AI assistant can call directly."*
- **Post 492935_2751948** (EVE Online, A5, I4, VC2): Pontuação de Acesso = **5/5**. Democratização linguística e cognitiva: *"It is not about replacing English, but about expanding access and participation."*

**Análise**: O Acesso surge como o pilar mais funcionalmente transformador do DART: a IA quebra a barreira de entrada da extrema complexidade de folhas de cálculo e dados de API em jogos sandbox.

### 3.4 Risco (Média: 1,62/5)

A dimensão Risco constitui a faceta mais proeminente e articulada no discurso empírico dos jogadores (1,62/5), englobando preocupações de justiça distributiva (*fair play*), exploração económica e perda de agência.

**Evidências empíricas no corpus refinado**:

- **Post reddit_1ormrc6_1** (EVE Online, A5, I4, VC3): Pontuação de Risco = **5/5**. Preocupação explícita com assimetria económica e vantagens indevidas: *"Unfair advantage. Will players using a paid AI assistant for market analysis or crafting get an edge that free-to-play users cannot match?"*
- **Post 2116712_27042848** (World of Warcraft, A5, I4, VC3): Pontuação de Risco = **5/5**. Dano à integridade do ambiente competitivo de PvP: *"This is an epidemic, and feel I see AT LEAST one of these in each lobby. When are proactive algorithmic bans coming?"*
- **Post 1ph9o3i_22** (EVE Online, A4, I3, VC3): Pontuação de Risco = **4/5**. Alucinações de modelos generativos que causam perdas de ativos espaciais: *"MISTAKES WERE MADE."*

**Análise**: Ao contrário da visão tecnicista que associa o risco apenas à batota mecânica, os utilizadores no corpus refinado articulam riscos epistémicos sofisticados: a emergência de "vibe-cheating", a opacidade dos modelos proprietários e a dependência psicológica ou técnica de copilotos de decisão rápida.

### 3.5 Transparência (Média: 1,34/5)

A dimensão Transparência mensura a visibilidade das regras algorítmicas, a rotulagem de conteúdo gerado por IA e a explicabilidade das decisões dos agentes.

**Evidências empíricas no corpus refinado**:

- **Post 510327_2913288** (EVE Online, A1, I3, VC1): Pontuação de Transparência = **5/5**. Disponibilização de instrumentação direta para auditoria: *"The diagnostics panel exists because you couldn’t reach a browser console — and provides complete visibility into AI decisions."*
- **Post 2318118_29656965** (World of Warcraft, A5, I4, VC3): Pontuação de Transparência = **5/5**. Exigência de rotulagem e escrutínio público das editoras: *"they say they didn’t use AI, but the devs could’ve at some point especially for generative texture work, we demand disclosure."*
- **Post 510327_2866379** (EVE Online, A1, I3, VC1): Pontuação de Transparência = **5/5**. Documentação explícita de parâmetros analíticos: *"The crew numbers in EVE Crews are derived from a blend of official CCP lore, historical documentation and ship volume metrics."*

**Análise**: Com o jogo corrigido (v4.1), a Transparência média por post é **mais alta em World of Warcraft** (1,26) do que em EVE Online (1,06), no corpus ativo de 1.029 posts. A diferença está sobretudo na natureza da transparência: em EVE Online é construída pelos criadores de ferramentas comunitárias (logs e diagnósticos abertos); em World of Warcraft é sobretudo **reivindicada** contra a opacidade das políticas corporativas da Blizzard, o que faz subir a pontuação sem que haja transparência efetiva.

---

## 4. Análise Comparativa de Jogos: Sandbox vs. Controlado

### 4.1 Distribuição do Corpus Refinado

| Jogo | Posts Analisados no Corpus Refinado | Percentagem |
| :--- | :---: | :---: |
| **World of Warcraft (Ambiente Controlado)** | 453 | 55,0% |
| **EVE Online (Ambiente Sandbox)** | 371 | 45,0% |
| **Total Refinado** | **824** | **100,0%** |

*Nota v4.1*: antes da correção, 14 tópicos do r/Eve estavam contados como World of Warcraft (73 posts no corpus ativo, 67 no corte de contraste). A distribuição antiga era 521 WoW / 304 EVE.

### 4.2 Comparação de Padrões e Culturas Comunitárias

1. **EVE Online (Sandbox — 371 posts)**:
   * **Cultura Construtiva e Extensível**: O acesso aberto à API ESI e a introdução do protocolo MCP catalisam a criação de agentes autónomos (A1) e copilotos avançados (A4). 
   * **Cocriação Dialógica**: Concentra os casos mais proeminentes de cocriação efetiva (VC1: ex. ferramentas EVE Crews e Battlefield.Space).
   * **Risco Centrado na Economia**: Preocupação predominante com a distorção do mercado financeiro e a desestabilização de nós de produção espacial por agentes algorítmicos.

2. **World of Warcraft (Controlado — 453 posts)**:
   * **Cultura Protetiva e Regulada**: Foco nas instâncias de combate (míticas e raids), onde a autonomia externa é encarada com desconfiança e severamente punida pelo código de conduta da editora.
   * **Codestruição e Frustração (VC3)**: Forte saliência de queixas sobre moderação automática cega de tickets de suporte e desconfiança quanto à presença de bots inteligentes nas arenas competitivas.
   * **Inovação Oficial**: Acolhimento positivo mas cauteloso de instâncias geridas por IA nativa (*Follower Dungeons*), vistas como oportunidade de treino sem pressão tóxica de outros jogadores.

### 4.3 Agregação ao Nível de Tópicos de Discussão (151 Threads Ativas) — A Unidade Primária de Sentido

Na perspetiva meso-sociotécnica da framework **DART-NET v4.0**, o agrupamento dos posts nos seus respetivos **151 tópicos de discussão (*threads*) ativos** constitui a **unidade substantiva primária** para captar os ciclos deliberativos e a evolução temporal das dinâmicas de cocriação de valor. A tabela apresenta as duas leituras meso: a regra de agregação da pipeline e a leitura holística cega (Secção 1.7.1).

| Dimensão Analítica / Ecossistema | EVE Online (Sandbox Aberto) | World of Warcraft (Ambiente Controlado) | Total Consolidado (Nível Meso) |
| :--- | :---: | :---: | :---: |
| **Número de Tópicos Ativos** | **79 tópicos** (52,3%) | **72 tópicos** (47,7%) | **151 tópicos** (100,0%) |
| **Volume de Posts Analisados** | 511 posts (49,7%) | 518 posts (50,3%) | 1.029 posts (100,0%) |
| **Média de Posts por Tópico** | `6,47` posts/tópico | `7,19` posts/tópico | `6,81` posts/tópico |
| **Vetor DART Médio por Tópico** | `D: 0,87 | A: 1,47 | R: 1,44 | T: 1,27` | `D: 0,91 | A: 1,05 | R: 1,54 | T: 1,35` | `D: 0,89 | A: 1,27 | R: 1,49 | T: 1,31` |
| **VC1 (Cocriação Efetiva)** — holística / regra | **24,1%** (19) / 11,4% (9) | **9,7%** (7) / 13,9% (10) | **17,2%** (26) / 12,6% (19) |
| **VC2 (Potencial de Cocriação)** — holística / regra | **16,5%** (13) / 11,4% (9) | **9,7%** (7) / 13,9% (10) | **13,2%** (20) / 12,6% (19) |
| **VC3 (Codestruição)** — holística / regra | **12,7%** (10) / 15,2% (12) | **19,4%** (14) / 31,9% (23) | **15,9%** (24) / 23,2% (35) |
| **VC4 (Sem Evidência Direta)** — holística / regra | **46,8%** (37) / 62,0% (49) | **61,1%** (44) / 40,3% (29) | **53,6%** (81) / 51,7% (78) |
| **Impacto Ativo** — holística / regra | **53,2%** / 38,0% | **38,9%** / 59,7% | **46,4%** / 48,3% |

**Interpretação Teórica**:
1. **As duas leituras meso invertem o contraste entre jogos.** Pela regra de agregação, *World of Warcraft* teria mais impacto ativo (59,7% vs. 38,0%). Pela leitura holística, é *EVE Online* que o tem (53,2% vs. 38,9%), com mais do dobro da proporção de cocriação efetiva (VC1: 24,1% vs. 9,7%). A regra é sensível ao número de posts por tópico e ao rótulo de um único post, e os tópicos de WoW são em média mais longos (7,19 vs. 6,47 posts). Por isso, a comparação entre ecossistemas deve basear-se na leitura holística, a confirmar pela codificação humana cega.
2. **Assimetria estrutural de Acesso**: em *EVE Online*, o Acesso médio por tópico (`1,47`) supera claramente o de *WoW* (`1,05`), em linha com a infraestrutura aberta de APIs (ESI e MCP). A Transparência é ligeiramente mais alta em *WoW* (`1,35` vs. `1,27`), sobretudo por reivindicação contra a opacidade da editora (ver Secção 3.5).
3. **Codestruição mais frequente em WoW**: em ambas as leituras, a proporção de tópicos VC3 é maior em *World of Warcraft* (19,4% holística / 31,9% regra) do que em *EVE Online* (12,7% / 15,2%). Os tópicos VC3 de WoW concentram-se em queixas sobre suporte automatizado, moderação e bots em PvP. A magnitude da diferença depende do método.
4. **Antes da correção do jogo**, a versão anterior deste relatório reportava 65 tópicos EVE / 87 WoW e VC1 de 7,7% em EVE contra 16,1% em WoW. Esse resultado devia-se em parte aos 14 tópicos do r/Eve contados como WoW. Pela regra de agregação, 4 deles eram VC1 (por exemplo, `reddit_1vdomcq`, sobre ferramentas de trading e indústria em EVE).

### 4.4 Tipologia Emergente de Tópicos: Os 5 Clusters Sociotécnicos

A análise de padrões na totalidade dos **151 tópicos ativos** (calibrada pela aplicação rigorosa da Regra de Fronteira Operacional da Secção 4.4.1 para desambiguar falsos positivos lexicais entre os estratos iniciais de amostragem `[30, 35, 32, 25, 30]` e a arquitetura real de integração) consolida **cinco agrupamentos sociotécnicos emergentes**. As contagens e métricas DART abaixo usam o cluster atribuído pela pipeline (regras por palavras-chave em `ThreadSynthesisAgent`). A distribuição de valor usa a leitura holística.

1. **Cluster 1: Ferramentas Externas, Integração de APIs e MCP** (22 tópicos | 14,6% — *Estrato inicial: 30 tópicos*; 21 EVE / 1 WoW)
   * *Foco*: Desenvolvimento e interligação programática de dados vivos do jogo via APIs públicas (ESI, *Model Context Protocol* - MCP, Pyfa, exportação de telemetria para LLMs como Claude e GPT-4).
   * *Métricas DART*: Maior Acesso de todo o estudo (`A: 2,36`) e mais elevada Transparência (`T: 1,46`; `D: 0,92`; `R: 1,36`). Maior concentração de cocriação: 12 dos 22 tópicos são VC1 na leitura holística (e 6 VC2).
2. **Cluster 2: Fair Play, Deteção Algorítmica e Integridade Competitiva** (32 tópicos | 21,2% — *Estrato inicial: 35 tópicos*; 21 EVE / 11 WoW)
   * *Foco*: Tensão entre assistência algorítmica permitida e automação desleal em ambientes PvP (*pixel bots* em arenas), mercados e frotas de mineração/combate.
   * *Métricas DART*: Elevado Risco Percebido (`R: 1,59`) e Acesso restrito (`A: 0,82`; `D: 0,39`; `T: 1,08`). Predomínio de debate normativo (20 VC4) com 5 tópicos VC3 na leitura holística.
3. **Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning** (25 tópicos | 16,6% — *Estrato inicial: 32 tópicos*; 6 EVE / 19 WoW)
   * *Foco*: Contestação ao uso de IA pela publicadora para resolução de tickets (*"ChatGPT GM"*), triagem automatizada de denúncias, despedimentos (*layoffs*) e suspensão de contas.
   * *Métricas DART*: Risco mais severo de todo o estudo (`R: 2,11`), menor Acesso (`A: 0,75`) e forte reivindicação de Transparência (`T: 1,40`; `D: 0,69`). Principal foco de codestruição: 9 dos 25 tópicos são VC3 na leitura holística.
4. **Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores** (21 tópicos | 13,9% — *Estrato inicial: 25 tópicos*; 11 EVE / 10 WoW)
   * *Foco*: Avaliação de companheiros, assistentes e instâncias operadas por IA oficial da publicadora (*Follower Dungeons*, *Delves* com Brann Bronzebeard, *Aura AI* e *Ask Aura*).
   * *Métricas DART*: Acesso institucional controlado (`A: 1,14`), menor Risco percebido (`R: 1,09`; `D: 0,89`; `T: 1,29`). Predomínio de avaliação reflexiva (15 VC4), com 3 tópicos VC2 e 2 VC3.
5. **Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding** (51 tópicos | 33,8% — *Estrato inicial: 30 tópicos*; 20 EVE / 31 WoW)
   * *Foco*: Utilização de assistentes generativos (Claude, ChatGPT, Gemini, Copilot) mediante mediação humana manual (sem ligação API direta em tempo real) para conceção e reparação de *addons* em Lua, *WeakAuras*, macros e sessões de *brainstorming* ou planeamento tático.
   * *Métricas DART*: Maior volume empírico do corpus (`33,8%`) e mais alto índice de Diálogo (`D: 1,28`), aliado a Acesso técnico relevante (`A: 1,40`; `R: 1,35`; `T: 1,35`). Dinâmica mista: 9 VC1, 5 VC2, 7 VC3 e 30 VC4 na leitura holística.

**Fiabilidade da atribuição de clusters (v4.1)**: a leitura holística cega atribuiu também um cluster a cada tópico. O acordo com o cluster da pipeline é de **56,3%** ($\kappa = 0,43$, acordo moderado). As maiores diferenças:
* a leitura holística põe muito mais tópicos no Cluster 4 (43 vs. 21), sobretudo tópicos que a pipeline tinha posto em Fair Play (12) e em Copilotos (8);
* põe muito menos no Cluster 3 (11 vs. 25): 9 dos 25 tópicos que a pipeline pôs em Suporte/Moderação passam para Fair Play (Cluster 2).

As proporções por cluster devem, por isso, ser lidas como indicativas até à validação humana.

#### 4.4.1 Critério Operacional de Fronteira: Distinção entre o Cluster 1 e o Cluster 5

Dado que tanto o **Cluster 1** como o **Cluster 5** envolvem a utilização de modelos de linguagem (Claude, ChatGPT, Gemini, GitHub Copilot), programação comunitária e dinâmicas de cocriação de valor (`VC1` e `VC2`), o protocolo estabelece um **critério de fronteira estrito** baseado na arquitetura de ligação aos dados do jogo:

* **Cluster 1 (Integração de Sistemas, APIs e MCP)**: A ferramenta ou o agente de IA **comunica programaticamente com endpoints de dados vivos do jogo via API** (ex.: API pública *ESI* de *EVE Online*, servidores *Model Context Protocol* — MCP ou telemetria de *killboards*). O foco incide sobre uma aplicação externa, plataforma web ou servidor que extrai dados estruturados do ecossistema em tempo real.
* **Cluster 5 (Copilotos, Addons e *Vibe-Coding*)**: O jogador interage com um LLM externo como **assistente ou copiloto pessoal**, sem ligação direta por API entre a IA e o servidor do jogo. **O utilizador humano atua como ponte manual**: copia mensagens de erro, documentação (*blue posts*) ou descrições funcionais para o chat da IA, gera ou depura código local (ex.: *Addons* em Lua ou *WeakAuras* para o cliente de *World of Warcraft*) ou realiza sessões de *brainstorming*, planeamento e consulta sobre mecânicas do jogo.

| Dimensão de Contraste | **Cluster 1: Ferramentas Externas, APIs e MCP** | **Cluster 5: Copilotos, Addons e *Vibe-Coding*** |
| :--- | :--- | :--- |
| **Papel da IA** | Motor integrado numa aplicação ou ligado diretamente a *endpoints* de dados do jogo (**Agente A1**). | Assistente/copiloto pessoal de programação local ou consulta conversacional (**Copiloto A4 / Discussão A5**). |
| **Fluxo de Dados** | **Automatizado via API** (Servidor do Jogo $\leftrightarrow$ API ESI / MCP $\leftrightarrow$ Agente IA). | **Mediado Manualmente pelo Humano** (Jogador copia/cola *prompt* ou código $\leftrightarrow$ LLM externo). |
| **Artefacto Principal** | Aplicações web comunitárias, servidores MCP, painéis de telemetria e simuladores ligados à API oficial. | *Addons* locais em Lua, *WeakAuras*, macros de interface ou consultas de planeamento/*brainstorming*. |
| **Indicadores Empíricos no Corpus** | `API`, `ESI`, `MCP Server`, `Endpoint`, `Telemetry`, `Live Data`, `zKillboard`. | `Vibe-coding`, `Lua`, `Addon`, `WeakAura`, `Claude Code`, `OnUpdate`, `FPS`, `Brainstorm`. |
| **Casos Verificados no Corpus** | • **`510327`** (*EVE Crews*: simulador web ligado à API ESI com regras calibradas via Claude);<br>• **`516433`** (*EVE MCP Server*: exposição de *endpoints* ESI para consulta direta por assistentes de IA). | • **`reddit_1v3v2p2`** (*Claude Code Success*: reparação de *addon* Lua pós-*patch* via *blue post*);<br>• **`reddit_1r1dd9i`** (*Vibe Coded AddOns*: impacto de performance em Lua e uso de `OnUpdate`);<br>• **`1mctiz6`** e **`1i6m4i6`** (uso do Gemini/ChatGPT para *brainstorming* e rotas de navegação). |

### 4.5 Casos Paradigmáticos de Tópicos de Discussão e Ancoragem Literal (*Verbatim Grounding*)

Em conformidade com o princípio de **ancoragem empírica (*verbatim grounding*)** da metodologia DART-NET v4.0, cada tópico de nível Meso é estritamente sustentado pelas falas exatas e inalteradas dos jogadores nos posts constituintes, eliminando qualquer risco de alucinação analítica. O quadro seguinte sintetiza tópicos emblemáticos que ilustram o comportamento empírico dos clusters nos dois ecossistemas:

| ID Tópico | Título Central | Ecossistema / Cluster | Agência / Interação | Vetor DART (Médias) | Dinâmica de Valor (Regra / Holística v4.1) | Evidência Literal Verificável (*Verbatim Quote* de Ancoragem Micro) |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **`510327`** | *EVE Crews: A lore-accurate\* API-linked crew simulator* | EVE Online<br>Cluster 1 (APIs/MCP) | **A1** / **I3** | `D: 2,9`<br>`A: 2,4`<br>`R: 1,2`<br>`T: 2,3` | **VC1** / **VC1** (Cocriação Efetiva) | *"The crew numbers in EVE Crews are derived from a blend of official CCP lore, historical game data, and community research..."* |
| **`516433`** | *EVE MCP Server — querying ESI from Claude, Copilot and other AI assistants* | EVE Online<br>Cluster 1 (APIs/MCP) | **A1** / **I4** | `D: 0,0`<br>`A: 5,0`<br>`R: 2,0`<br>`T: 3,0` | **VC4** / **VC1** (holística: ferramenta funcional partilhada) | *"exposing EVE’s public ESI endpoints as tools an AI assistant can call directly"* |
| **`1jukb0x`** | *Psa For The New Bros Dont Ask Chatgpt About Eve* | EVE Online<br>Cluster 5 (Copilotos) | **A5** / **I3** | `D: 1,4`<br>`A: 1,3`<br>`R: 1,3`<br>`T: 1,0` | **VC1** / **VC4** (holística: aviso reflexivo sobre alucinações) | *"I asked gpt what it wanted to say about this post here it is. ... If someone points out I gave garbage, I can course-correct mid-convo."* |
| **`508618`** | *Recorded a bot in high sec - but why even bother?* | EVE Online<br>Cluster 3 (Suporte/Bans)<br>*(holística: C2)* | **A5** / **I4** | `D: 1,4`<br>`A: 0,5`<br>`R: 2,2`<br>`T: 1,5` | **VC3** / **VC4** (holística: debate sem dano concreto relatado) | *"Why is he compromising his acc for this? ... most commonly RMT ... IP bans does little - VPNs exist and IPs can be changed."* |
| **`reddit_1tvlpnw`** | *Sick of spam and bots ruining our game? Here's an addon that uses ML...* | WoW (r/woweconomy)<br>Cluster 2 (Fair Play)<br>*(holística: C5)* | **A3** / **I4** | `D: 0,0`<br>`A: 2,0`<br>`R: 1,5`<br>`T: 0,5` | **VC4** / **VC2** (holística: addon proposto, benefício por confirmar) | *"it would bring up the report window and fill in the box with their coordinates a timestamp and the reason for report botting"* |
| **`reddit_1v3v2p2`** | *Claude Code Success* | WoW<br>Cluster 5 (Copilotos) | **A1** / **I3** | `D: 5,0`<br>`A: 4,0`<br>`R: 1,0`<br>`T: 1,0` | **VC1** / **VC1** (Cocriação Efetiva) | *"Explained a breakdown to what happened. Gave a link to the blue post. Directed it to review addons... Instructed it to add updated logic"* |

---

## 5. Cocriação e Codestruição de Valor (VC1–VC4)

### 5.1 O Nível Micro como Contraste Crítico e Inventário Atomizado

> **Nota Epistemológica Central**:  
> A distribuição de frequências abaixo ($N=824$ posts) constitui um **inventário descritivo da camada micro-empírica** e funciona como **contraste** para a leitura ao nível do tópico (Secção 1.7.1).

| Categoria de Valor | Frequência Micro ($N=824$) | Percentagem Micro | Papel na Arquitetura Multinível DART-NET v4.0 |
| :--- | :---: | :---: | :--- |
| **VC1 (Cocriação de Valor Efetiva)** | 26 | 3,2% | Turnos onde a solução finalizada é partilhada pontualmente. *(Meso: 17,2% holística / 12,6% regra)* |
| **VC2 (Potencial Cocriação de Valor)** | 72 | 8,7% | Ideias, propostas e intenções comunicadas em mensagens únicas. *(Meso: 13,2% holística / 12,6% regra)* |
| **VC3 (Codestruição de Valor)** | 90 | 10,9% | Denúncias pontuais, queixas de bans ou relatos de alucinações. *(Meso: 15,9% holística / 23,2% regra)* |
| **VC4 (Sem Evidência Direta / Reflexão)** | 636 | 77,2% | Turnos intermédios de debate, perguntas e diálogo exploratório. *(Meso: 53,6% holística / 51,7% regra)* |
| **Total** | **824** | **100,0%** | **Linha de Base Micro-Empírica de Contraste** |

**Análise do Contraste Teórico**:  
Ao nível do post, as mensagens com impacto ativo de valor (VC1 + VC2 + VC3) são **22,8%** (188 posts), contra 77,2% em VC4. A codestruição (VC3: 10,9%) é mais frequente do que a cocriação efetiva (VC1: 3,2%). Ao nível do tópico, perto de metade das discussões tem impacto ativo (46,4% na leitura holística). Estas duas proporções medem coisas diferentes: a primeira, a fração de turnos com valor explícito; a segunda, a fração de discussões cujo desfecho global é de cocriação ou codestruição. A diferença entre elas não deve ser lida como um "ganho" do nível meso (ver o modelo nulo na Secção 1.7.1). Ao nível do tópico, e na leitura holística, a ordem inverte-se: a cocriação efetiva (17,2%) supera a codestruição (15,9%).

### 5.2 Evidências Paradigmáticas de Cocriação de Valor (VC1)

* **Post 510327_2870703** e **Post 510327_2913288** (EVE Online): O utilizador identifica anomalias na atribuição de tripulação a naves capitais e o programador, juntamente com o agente Claude, analisa o log, reescreve as regras de inferência e publica a correção em tempo real. O valor gerado reverte em benefício de toda a comunidade.
* **Post 513384_2889848** (EVE Online): Criação colaborativa de um servidor MCP público para dotar LLMs de compreensão contextual das 26 principais tabelas de dados de EVE, permitindo a qualquer jogador planear frotas conversacionalmente.

### 5.3 Evidências Paradigmáticas de Codestruição de Valor (VC3)

* **Post reddit_1ariy3g_20** (World of Warcraft): Automatização opaca de tickets de serviço ao cliente onde respostas padronizadas fecham chamados sem analisar o problema (*"Took me 5 tickets to finally get someone who looked into my ticket for more than 5 seconds"*), destruindo a confiança no suporte.
* **Post 1ph9o3i_22** (EVE Online): Copiloto generativo fornece cálculos errados de refinação de minérios e fitações, resultando na perda de uma nave dispendiosa em combate (*"MISTAKES WERE MADE"* — Risco 4/5).

---

## 6. Reflexão sobre as Questões de Investigação

> **Enquadramento Epistémico DART-NET v4.0**:  
> Em estrita conformidade com a Arquitetura Metodológica Multinível Incorporada, as **respostas substantivas às Questões de Investigação (QI1, QI2 e QI3)** assentam primariamente na dinâmica deliberativa, relacional e temporal do **Tópico de Discussão ($N=151$, Nível Meso)**. Os dados e frequências dos posts individuais ($N=824$, Nível Micro) cumprem a função de **ancoragem empírica (*verbatim grounding*)**, rastreabilidade de citações inalteradas e linha de base granular de micro-atos comunicativos.

### 6.1 QI1: Tipologia de Agentes de IA e Formas de Interação Humano-IA
*Pergunta Central: Que tipos de agentes de IA e que formas de interação humano-IA caracterizam os MMORPG analisados?*

#### 6.1.1 QI1a: Proporção de Agentes de IA Autónomos face a Bots e Scripts Convencionais
**Resposta (Consolidada no Nível Meso com Suporte Micro)**:
A análise multinível revela que os ecossistemas contemporâneos superaram a era dos bots mecânicos repetitivos. Na linha de base atómica ($N=824$ posts), os agentes autónomos (A1: 11,5%) e a assistência híbrida por IA generativa (A4: 7,2%) superam largamente os bots e scripts convencionais residuais (A2+A3: 4,1%), embora 77,2% dos turnos sejam dedicados ao debate reflexivo (A5). 
Quando avaliada ao **Nível Meso dos 151 tópicos completos**, esta proporção ganha relevo estrutural: **62,3% dos tópicos ativos** (94 tópicos nos Clusters 1, 4 e 5 da pipeline; 74,8% na leitura holística) centram-se em ferramentas ligadas por API, agentes oficiais de IA e *vibe-coding* assistido por LLMs (Claude, GPT-4, Gemini). Apenas 21,2% (Cluster 2; 17,9% na leitura holística) debatem fair play, automação ilícita ou bots. *(A versão anterior indicava 48,1% / 73 tópicos, mas a soma dos Clusters 1, 4 e 5 já era então de 94 tópicos.)* O fenómeno central dos MMORPGs atuais é a integração de inteligência contextual e modelos generativos.

#### 6.1.2 QI1b: Estruturas de Interação Humano-IA e Padrões entre Sandbox e Controlado
**Resposta (Consolidada no Nível Meso com Suporte Micro)**:
Embora na contagem isolada de mensagens a discussão entre humanos pareça hegemónica (I4: 77,7%), a **análise ao nível de tópicos conversacionais completos** demonstra que **29,8% dos tópicos** (45 de 151, com pelo menos um post I1, I2 ou I3) materializam padrões ativos de interação direta (I1/I2) ou cooperação triádica contínua (**I3: Humano $\leftrightarrow$ IA $\leftrightarrow$ Comunidade**), especialmente nos clusters de APIs/MCP e Copilotos. 
* **Padrões por Ecossistema**:
  * Em **EVE Online (Sandbox Aberto)**: A governança técnica da API ESI e servidores MCP propicia interações agênticas abertas (I1/I3), onde jogadores conversam diretamente com LLMs que consultam dados do jogo em tempo real (ex.: tópicos `510327` e `516433`).
  * Em **World of Warcraft (Ambiente Controlado)**: As interações diretas são confinadas pela Blizzard a NPCs aliados nativos (*Follower Dungeons*, I5) ou ocorrem externamente via copilotos de *vibe-coding* para criação e reparação de addons em Lua (Cluster 5, I3, ex.: `reddit_1v3v2p2`).

---

### 6.2 QI2: Cocriação, Codestruição de Valor e o Papel das Dimensões DART
*Pergunta Central: Em que medida essas interações cocriam ou codestroem valor, e que papel desempenham as dimensões do modelo DART?*

#### 6.2.1 QI2a: Verificação das Dimensões Diálogo, Acesso, Risco e Transparência
**Resposta (Consolidada no Nível Meso com Suporte Micro)**:
Todas as quatro dimensões DART têm médias superiores a 1,0 na base granular de 824 posts, com o Risco a liderar (**1,62/5**), seguido da Transparência (**1,34/5**), Acesso (**1,21/5**) e Diálogo (**1,09/5**). A ordem mantém-se quando só se contam pontuações com evidência verificada literalmente (1,54 / 1,28 / 1,19 / 1,08).
* **Papel Sistémico das Dimensões no Nível Meso**: A análise agregada por cluster comprova que o **Acesso técnico programável** e o **Diálogo bidirecional** são as condições propulsoras da cocriação de valor (Clusters 1 e 5). Por outro lado, o **Défice de Transparência algorítmica** e a perceção de **Risco assimétrico** (ameaça competitiva, perdas económicas e moderação cega por IA) funcionam como gatilhos primários de codestruição de valor (VC3 nos Clusters 2 e 3).

#### 6.2.2 QI2b: Evidências Empíricas de Cocriação (VC1/VC2) vs. Codestruição (VC3) de Valor
**Resposta (Consolidada no Nível Meso com Suporte Micro)**:
* **Na leitura atómica por post ($N=824$)**: 3,2% atingem VC1 e 10,9% VC3, com 77,2% em VC4. A maioria dos turnos isolados não relata, por si, ganho ou perda.
* **Na leitura holística ao Nível do Tópico ($N=151$)**: **46,4% das discussões têm uma dinâmica de valor ativa** (**`17,2% VC1`**, **`13,2% VC2`** e **`15,9% VC3`**). A regra de agregação da pipeline dá uma proporção global semelhante (48,3%), mas outra distribuição (12,6% VC1, 12,6% VC2, 23,2% VC3) e acordo fraco com a leitura holística ($\kappa = 0,21$). O modelo nulo mostra que a subida de ~22% para ~48% é esperada pela própria regra (Secção 1.7.1).
* **Distribuição entre Clusters**: a cocriação efetiva concentra-se nos clusters de Ferramentas/APIs (Cluster 1: 12 de 22 tópicos VC1) e Copilotos (Cluster 5: 9 VC1 e 5 VC2 em 51). A codestruição concentra-se em Suporte/Moderação (Cluster 3: 9 de 25 tópicos VC3) e Fair Play (Cluster 2: 5 de 32). É mais frequente em *World of Warcraft* (**19,4%** dos tópicos na leitura holística; 31,9% pela regra) do que em *EVE Online* (12,7% / 15,2%).
* **Estado da evidência**: estes resultados vêm de codificação automática (DeepSeek). A codificação humana cega de 37 tópicos (Secção 7.3) servirá para validar quer a leitura holística quer a regra de agregação.

---

### 6.3 QI3: Governança do Ecossistema e Implicações para o Design com IA
*Pergunta Central: Como é que a arquitetura de governança de cada ecossistema condiciona a cocriação de valor com IA, e que implicações daí decorrem?*

#### 6.3.1 QI3a: Diferenças Sistemáticas entre EVE Online e World of Warcraft na Configuração DART e Dinâmica de Valor
**Resposta (Síntese Comparativa Transversal)**:
A análise transversal agregada demonstra que a arquitetura de governança e a infraestrutura técnica exercem um papel determinístico na transição do discurso comunitário da especulação defensiva para a cocriação tangível de valor (Prahalad & Ramaswamy, 2004). 

No ecossistema **Sandbox de *EVE Online***, a disponibilização aberta e padronizada da API ESI e a recente adoção do *Model Context Protocol* (MCP) catalisam uma governança descentralizada onde os jogadores assumem o papel de co-desenvolvedores informacionais. O Acesso técnico direto é claramente superior (`A: 1,47` por tópico, contra `1,05` em *WoW*). A plataforma fomenta assim ecossistemas cooperativos (tais como *EVE Crews* e *Battlefield.Space*), convertendo agentes de IA em próteses de ampliação cognitiva que mitigam a complexidade sistémica. Na leitura holística, **24,1% dos tópicos de EVE são de cocriação efetiva (VC1)**, contra 9,7% em *WoW*. Desses 19 tópicos, 9 pertencem ao Cluster 1 (ferramentas ligadas por API) e 10 ao Cluster 5 (copilotos).

Em contrapartida, no ecossistema **Controlado de *World of Warcraft***, a governança algorítmica da Blizzard é estritamente centralizada e defensiva. A sandbox de addons em Lua é delimitada por restrições rigorosas e a IA oficial é confinada a ambientes isolados de jogabilidade assistida (*Follower Dungeons* e *Delves*). Concomitantemente, a automação opaca de pipelines de atendimento e aplicação de penalizações está associada a uma taxa de codestruição de valor mais elevada ao nível de tópicos (`VC3: 19,4%` na leitura holística, contra 12,7% em *EVE*; 31,9% pela regra de agregação), induzindo cinismo e sensação de desamparo institucional. A Transparência média é ligeiramente mais alta em *WoW* (`1,35` vs. `1,27`), mas reflete sobretudo exigências de transparência dirigidas à Blizzard e não transparência efetiva. Quando a cocriação desponta em *WoW*, ocorre quase exclusivamente nas margens informais: 6 dos 7 tópicos VC1 de *WoW* são *vibe-coding* de addons ou uso de LLMs externos (Cluster 5).

> **Nota de cautela**: antes da correção do jogo, a regra de agregação dava mais cocriação a *WoW* (VC1 16,1% vs. 7,7%). Com o jogo corrigido e a leitura holística, o resultado inverte-se e fica coerente com a hipótese sandbox vs. controlado. Como as duas leituras automáticas divergem, esta conclusão deve ser confirmada pela codificação humana cega antes de ser apresentada como resultado final.

#### 6.3.2 QI3b: Implicações Teóricas e Práticas para o Desenho de Ecossistemas de Videojogos com IA Integrada
**Resposta**: 
1. **Implicações Teóricas**: A operacionalização do modelo DART-NET em ambientes lúdicos demonstra que o Risco e a Transparência funcionam como variáveis moderadoras cruciais: sem transparência algorítmica, o aumento de acesso técnico não fomenta cocriação, antes precipita atritos de codestruição (VC3). Ademais, a análise multinível mostra que a leitura do valor depende da unidade de análise: 22,8% dos posts têm impacto ativo de valor, contra 46,4% dos tópicos na leitura holística. A forma de agregação, porém, condiciona fortemente o resultado: uma regra do tipo "basta um post" produz este salto mesmo com rótulos aleatórios (modelo nulo: 57,7%). Para estudos netnográficos assistidos por LLM, a lição metodológica é que a codificação ao nível do tópico deve ser feita de forma independente e não derivada da soma dos posts.
2. **Implicações Práticas para Estúdios e Designers**: O sucesso de ferramentas comunitárias baseadas em MCP em *EVE Online* indica que as publicadoras devem disponibilizar **interfaces abertas, programáveis e auditáveis (Transparência)**. Inversamente, a automação opaca de suporte ao cliente e moderação por "caixa negra", tal como observado em *WoW*, ilustra o caminho da rápida degradação do valor relacional. Recomenda-se a adoção de salvaguardas contra alucinações, explicabilidade nas regras algorítmicas e a garantia imperativa de intervenção humana no circuito (*human-in-the-loop*) para decisões sancionatórias.

---

## 7. Auditoria de Qualidade, Calibração e Fila de Validação Humana

### 7.1 Auditoria Cega Qualitativa (QualityGuardAgent)
A auditoria independente conduzida com o modelo `deepseek-v4-pro` sobre uma amostra de **159 codificações do corpus refinado** consolidou métricas de excelência:
* **Score Médio Global de Consistência**: **`91,31%`** (limiar crítico $\ge 70\%$ amplamente superado);
* **Veracidade das Evidências Literais**: **100%** de citações verificadas no texto original;
* **Casos Sinalizados com Alerta**: Apenas 8 casos em 159 análises auditadas, decorrentes exclusivamente de limiares conservadores de confiança.

### 7.2 Calibração da Fila de Validação Humana
* **Total de Posts com Validação Manual Prioritária (`human_review_required = True`)**: **707 posts (85,8% do corte de 824)**
* **Critérios de Sinalização**: Confiança analítica $< 0,80$, jargões altamente contextualizados, sarcasmo e ambiguidade entre categorias de fronteira.

### 7.3 Codificação Humana Cega ao Nível do Tópico (Protocolo v4.1)

O protocolo anterior (Track B, Rondas 1 e 2) foi **substituído**. Os codificadores tinham acesso aos resumos e às classificações da pipeline, o que impedia uma validação independente; por isso, o acordo reportado nessa fase ($\kappa = 0,916$ em clusters e $\kappa = 1,00$ em trajetórias de valor) não pode ser usado como medida de fiabilidade. Os ficheiros `Protocolo_Auditoria_Humana_Formatado*.xlsx` foram retirados. O protocolo atual decorre em duas etapas, com quatro ficheiros por etapa (um por codificador) em `output/`:

**Amostra ($N=37$ tópicos, 24,5% dos 151)**: seleção reprodutível (semente 2026) composta por:
* os 15 tópicos já analisados pelo Prof. JPaulo;
* 15 novos tópicos estratificados por cluster e jogo;
* 7 tópicos que o LLM anterior classificara como VC1, sobreamostrados para testar a categoria mais rara.

| Par de Codificadores | Tópicos | Composição | Jogo (EVE / WoW) |
| :--- | :---: | :--- | :---: |
| **Prof. JPaulo & Prof. Emmanoel** | 18 | 15 do bloco inicial + 3 VC1 sobreamostrados | 8 / 10 |
| **Prof. Roger & Prof. Gomide** | 19 | 15 estratificados novos + 4 VC1 sobreamostrados | 12 / 7 |
| **Total** | **37** | | **20 / 17** |

**Etapa 1 — Codificação cega** (`etapa_1_Codificacao_Topicos_<nome>.xlsx`): cada codificador lê o tópico original através de uma hiperligação e preenche, sem ver resumos nem rótulos automáticos, os campos Cluster (1–5), VC principal e secundário, Confiança (1–3), Evidência (citação literal), Ironia/Sátira e Notas. As instruções de preenchimento são as mesmas dadas à leitura holística automática.

**Etapa 2 — Avaliação dos resumos da IA** (`etapa_2_Avaliacao_Resumos_<nome>.xlsx`): só depois de concluída a Etapa 1, cada codificador avalia o resumo longo da pipeline quanto à Fidelidade da Síntese (1–5), Erros Factuais, Omissões Relevantes e Leitura do Tom Retórico.

**Análise prevista**: a chave `Chave_Analise_NAO_PARTILHAR_com_codificadores.xlsx` (não partilhada com os codificadores) reúne, para cada tópico, a regra de agregação, a classificação holística antiga e a leitura holística v4.1. A análise vai calcular três medidas: o acordo entre codificadores de cada par (κ de Cohen), o acordo de cada codificador com a regra de agregação e o acordo com a leitura holística v4.1. Na amostra, a leitura holística v4.1 dá 18 VC4, 9 VC1, 4 VC2 e 6 VC3.

**Estado (1 de novembro de 2026)**: o Prof. JPaulo já preencheu o Cluster de 15 dos 18 tópicos e o VC principal de 8; os restantes codificadores ainda não começaram. Ainda não há resultados de acordo.

#### 7.3.1 VC Principal e VC Secundário: Regra e Justificação Metodológica

A codificação regista, para cada tópico, um **VC principal** (obrigatório) e um **VC secundário** (opcional). As duas colunas têm papéis diferentes:

| | VC Principal | VC Secundário |
| :--- | :--- | :--- |
| **Estatuto** | Obrigatório; uma única categoria (VC1–VC4) | Opcional; só VC1, VC2 ou VC3, diferente do principal |
| **Quando se usa** | Sempre: dinâmica que melhor descreve a discussão no seu conjunto | Só quando há um episódio concreto de outra dinâmica, apontável num post |
| **Uso na análise** | κ de Cohen entre codificadores; comparação com a regra de agregação e com a leitura holística; conclusões sobre a QI2b e a QI3a | Descrição da ambivalência (por exemplo, tópicos que combinam VC1 e VC3) e cálculo do acordo parcial |

**Justificação**:
1. **O κ exige categorias mutuamente exclusivas.** A fiabilidade entre codificadores e a comparação com a codificação automática só podem ser calculadas sobre uma única categoria por tópico. Por isso, todas as conclusões assentam no VC principal.
2. **O valor é muitas vezes ambivalente.** Cocriação e codestruição podem ocorrer na mesma discussão: é a formação interativa de valor (Echeverri & Skålén, 2011; Plé & Chumpitaz Cáceres, 2010). Na primeira leitura do Prof. JPaulo, 7 dos 15 tópicos receberam duas categorias. O secundário preserva essa informação sem a misturar com a medida principal.
3. **Permite medir acordo parcial.** Se o principal de um codificador for o secundário do outro, o caso conta como acordo parcial e não como desacordo total. Isso distingue desacordos de fronteira de desacordos substantivos.
4. **O VC4 não pode ser secundário.** VC4 significa ausência de evidência direta de valor, por isso não é uma dinâmica que esteja presente no tópico. Combinações como "VC2 + VC4" não acrescentam informação: na primeira corrida da leitura holística, 7 dos 19 secundários eram VC4.
5. **O secundário não serve para registar dúvidas.** Se fosse usado assim, o acordo parcial ficaria artificialmente inflacionado. A dúvida regista-se na Confiança (1–3) e nas Notas.

**Efeito da regra na codificação automática**: a leitura holística foi repetida com esta regra, para usar exatamente o mesmo critério que os codificadores humanos.
* Com a regra estrita, o modelo passou a atribuir secundário a apenas **2 dos 151 tópicos** (antes eram 19).
* O VC principal manteve-se em 142 tópicos ($\kappa = 0,91$).
* Ou seja, para o LLM o secundário contribui pouco. Na corrida anterior também explicava apenas 2 dos 73 desacordos entre a regra de agregação e a leitura holística.
* O uso do secundário pelos codificadores humanos será reportado de forma descritiva e não entra no cálculo do κ.

> **Limitação conhecida da Etapa 2**: os resumos avaliados foram gerados pela pipeline antes da revisão v4.1. Nalguns tópicos, os posts foram lidos fora da ordem cronológica (ordenados pelo ID em texto); em 4 tópicos da amostra, o resumo foi gerado com o jogo errado. Estes problemas devem ser tidos em conta na avaliação da fidelidade.

---

## 8. Discussão Teórica, Reprodutibilidade e Gestão de Recursos

### 8.1 Arquitetura Não Destrutiva e Poda Metodológica
A pipeline garantiu a total rastreabilidade da investigação:
1. **Camada 1 (Raw Data)**: Preservados 430 ficheiros brutos intactos em `data/raw/`;
2. **Camada 2 (AI Coding)**: Registo integral das 1.032 codificações validadas em `data/analysis/netnography_results.jsonl` (organizadas nos 152 tópicos ativos de discussão) e preservação do arquivo não podado em `data/analysis/netnography_results_1032_unpruned.jsonl`;
3. **Log de Poda Auditável**: Documentação individualizada dos 207 posts avaliados no experimento preliminar de poda da Fase 3.5 em `data/analysis/excluded_posts_log.json`;
4. **Camada v4.1 (Correções)**: corpus corrigido com 1.029 posts / 151 tópicos em `data/analysis/netnography_results_v4_1.jsonl`, sem alterar os ficheiros anteriores (Secção 8.5).

### 8.2 Monitorização e Custo Global da Pipeline
* **Volume de Chamadas de API**: Mais de 27.000 invocações acumuladas (`deepseek-v4-flash` e `deepseek-v4-pro`);
* **Custo Operacional Global**: **~$21,50 USD**, consolidando uma relação custo-eficácia inigualável para investigações empíricas em larga escala. As duas corridas da codificação holística v4.1 dos 151 tópicos acrescentaram ~0,52 USD.

### 8.3 O Agente de Síntese de Tópicos (ThreadSynthesisAgent) e Entregáveis Analíticos

Na Fase 4.5 da investigação, o ecossistema multiagente foi expandido com a conceção e implementação do [`ThreadSynthesisAgent`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/thread_synthesis_agent.py), atualizado para a versão **DART-NET v4.0** para operacionalizar a Arquitetura Multinível Incorporada:

1. **Agregação Algorítmica com Preservação dos Posts Constituintes**: O agente agrupa com fidelidade os posts validados nos seus **152 tópicos de discussão ativos** (65 em EVE Online e 87 em World of Warcraft na versão original; **151 tópicos, 79 EVE / 72 WoW** após a revisão v4.1), mantendo em cada ficha de tópico a lista explícita dos seus `post_ids` constituintes (*Ancoragem Micro*), o cluster sociotécnico calibrado, o vetor DART médio ponderado, as frequências taxonómicas e o código de valor emergente.
2. **Entregável Estruturado JSON**: Os resultados estruturados de todos os tópicos foram consolidados em [`data/analysis/thread_level_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/thread_level_results.json), contendo metadados completos, lista de posts incorporados, métricas DART individuais, dinâmicas de valor e citações paradigmáticas.
3. **Catálogo Sistemático e Macro-Síntese**: Foi gerado o documento exaustivo [`output/analise_agregada_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/analise_agregada_topicos.md) (com 3.928 linhas), que inclui uma ficha analítica sistemática para cada um dos 152 tópicos (com os seus posts e campos preservados) e a formalização teórica dos 5 clusters sociotécnicos calibrados.
4. **Articulação Teórica Multinível**: Este módulo fecha o ciclo investigativo entre o nível Meso (tópico como unidade primária de sentido), o nível Micro incorporado (post como evidência literal verificável) e o nível Macro (ecossistemas sandbox vs. controlados), assegurando total rigor netnográfico segundo Kozinets (2020) e Prahalad & Ramaswamy (2004).

### 8.4 O Agente Analista de Discussões (TopicDiscussionAnalystAgent), Deteção de Sátira e Alinhamento Anti-Alucinação

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

### 8.5 Revisão v4.1: Correções, Leitura Holística e Modelo Nulo

A revisão v4.1 foi feita sem alterar os ficheiros originais. Todos os resultados novos estão em ficheiros com o sufixo `_v4_1`:

| Ficheiro | Conteúdo |
| :--- | :--- |
| `scratch/v4_1/01_corrigir_dados.py` | Correção do jogo (14 tópicos), dos subreddits (3 tópicos), fusão do duplicado `3000003`, pseudonimização de 20 nomes, verificação literal da evidência DART |
| `data/analysis/netnography_results_v4_1.jsonl` | Corpus corrigido: 1.029 posts, 151 tópicos |
| `data/target_corpus_v4_1.json` | Catálogo de tópicos corrigido (303 → 291 entradas) |
| `data/analysis/correcoes_v4_1_log.json` | Registo de todas as correções |
| `scratch/v4_1/02_codificacao_holistica_topicos.py` | Codificação holística cega dos 151 tópicos com `deepseek-v4-pro` (posts por ordem cronológica, sem rótulos micro, evidência verificada literalmente, VC secundário limitado a VC1–VC3; ~0,26 USD por corrida) |
| `data/analysis/topic_holistic_coding_v4_1.json` | Resultados da codificação holística definitiva (151/151 tópicos, 0 erros, 150/151 citações verificadas), usados neste relatório |
| `data/analysis/topic_holistic_coding_v4_1_run1_sec_livre.json` | Primeira corrida, com o secundário sem restrições; guardada para o teste-reteste (Secção 7.3.1) |
| `scratch/v4_1/03_comparacao_meso.py` → `data/analysis/comparacao_meso_v4_1.json` | Comparação micro vs. meso, modelo nulo (5.000 permutações), resultados por jogo e por cluster |
| `scratch/v4_1/04_estatisticas_relatorio.py` → `data/analysis/estatisticas_relatorio_v4_1.json` | Estatísticas do corte de contraste (824 posts) e das métricas DART por jogo e por cluster usadas neste relatório |

**Principais consequências para as conclusões**:
1. O contraste entre ecossistemas inverte-se quando se corrige o jogo e se usa a leitura holística: *EVE Online* tem mais cocriação efetiva (VC1 24,1% vs. 9,7%) e menos codestruição (VC3 12,7% vs. 19,4%) do que *World of Warcraft* (Secções 4.3 e 6.3.1).
2. O "salto" micro → meso obtido pela regra de agregação é um efeito mecânico da regra (modelo nulo, Secção 1.7.1). A proporção de ~48% de tópicos com impacto ativo é, ainda assim, corroborada pela leitura holística independente (46,4%).
3. A atribuição de clusters por palavras-chave tem acordo moderado com a leitura holística ($\kappa = 0,43$); as proporções por cluster são indicativas.
4. As médias DART são robustas à verificação literal da evidência (variação máxima de −0,08).
5. A leitura holística é estável entre corridas (VC principal: $\kappa = 0,91$; cluster: $\kappa = 0,85$). As conclusões assentam no VC principal; o VC secundário é descritivo (Secção 7.3.1).
