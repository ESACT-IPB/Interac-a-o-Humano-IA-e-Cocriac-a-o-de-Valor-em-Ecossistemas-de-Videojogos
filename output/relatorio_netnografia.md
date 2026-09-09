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

### 1.4 Metodologia de Recolha e Validação

A pipeline DART-NET v3.0 processou um corpus canónico de 303 tópicos de discussão, com delimitação temporal estrita de janeiro de 2024 a 2026. Foram filtradas 6.485 mensagens em bruto, das quais 1.032 foram validadas semanticamente pelo modelo DeepSeek. A validação semântica incluiu a classificação taxonómica (A1–A6, I1–I6, VC1–VC4), a pontuação das dimensões DART (escala 0–5) e a extração de evidências fundamentadas.

---

## 2. Taxonomia de Agentes de IA e Interações

### 2.1 Distribuição de Tipos de IA (A1–A6)

A distribuição dos 1.032 posts codificados revela uma predominância esmagadora de discussões *sobre* IA em detrimento de interações *com* IA:

| Tipo de IA | Frequência | Percentagem |
|------------|------------|-------------|
| A1 (Agente de IA) | 87 | 8,4% |
| A2 (Bot Convencional) | 100 | 9,7% |
| A3 (Script/Automação) | 14 | 1,4% |
| A4 (Humano Assistido por IA) | 52 | 5,0% |
| A5 (Discussão sobre IA) | 511 | 49,5% |
| A6 (Irrelevante) | 268 | 26,0% |

**Análise**: A categoria A5 (Discussão sobre IA) representa quase metade do corpus (49,5%), indicando que o discurso comunitário está predominantemente centrado na *especulação* e *avaliação* de IA, e não na interação direta. A categoria A6 (Irrelevante) constitui 26,0% do corpus, refletindo a dificuldade de filtragem semântica em fóruns com elevado ruído contextual.

**Resposta à QI1**: A proporção de agentes de IA autónomos (A1: 8,4%) face a bots/scripts convencionais (A2+A3: 11,1%) é relativamente equilibrada, mas ambos os grupos são minoritários face ao discurso especulativo (A5). Este achado sugere que a *perceção* de IA nos ecossistemas de videojogos excede largamente a sua *implementação* efetiva.

### 2.2 Estruturas de Interação Humano-IA (I1–I6)

| Tipo de Interação | Frequência | Percentagem |
|-------------------|------------|-------------|
| I1 (Humano → IA) | 43 | 4,2% |
| I2 (IA → Humano) | 5 | 0,5% |
| I3 (Humano ↔ IA Bidirecional) | 51 | 4,9% |
| I4 (Humano → Humano sobre IA) | 578 | 56,0% |
| I5 (Humano → Ambiente mediado por IA) | 4 | 0,4% |
| I6 (Sem interação significativa) | 351 | 34,0% |

**Análise**: A interação dominante é I4 (Humano → Humano sobre IA), representando 56,0% do corpus. Este padrão confirma que a comunidade discute IA como tópico social, não como parceiro interativo. As interações diretas com IA (I1+I2+I3+I5) somam apenas 10,0% do corpus, evidenciando que a integração de agentes de IA nos fluxos de jogo permanece incipiente.

**Resposta à QI2**: A estrutura de interação é predominantemente *discursiva* (I4) e *não interativa* (I6), com apenas 10% de interações diretas humano-IA. Este padrão é consistente entre ambos os jogos, embora EVE Online apresente uma ligeira maior incidência de interações bidirecionais (I3), possivelmente devido à sua cultura de ferramentas externas e APIs abertas.

---

## 3. Análise por Dimensão DART

### 3.1 Visão Global das Pontuações

| Dimensão DART | Média (0–5) | Interpretação |
|---------------|-------------|---------------|
| Diálogo | 0,66 | Muito fraco |
| Acesso | 0,75 | Muito fraco |
| Risco | 1,16 | Fraco |
| Transparência | 0,77 | Muito fraco |

As quatro dimensões DART apresentam pontuações médias extremamente baixas, todas abaixo de 1,2 numa escala de 0 a 5. Este resultado indica que as interações documentadas raramente satisfazem os critérios de qualidade dialógica, acessibilidade, gestão de risco ou transparência propostos por Prahalad & Ramaswamy (2004).

### 3.2 Diálogo (Média: 0,66/5)

A dimensão Diálogo mede a qualidade da comunicação bidirecional entre humanos e sistemas de IA. A pontuação média de 0,66 reflete a escassez de interações dialógicas genuínas.

**Evidências empíricas**:

- **Post 510327_2870703** (EVE Online, A1, I3, VC1): Pontuação de Diálogo = 4/5. Este post descreve um ciclo de feedback entre um utilizador e o sistema "EVE Crews", onde o reporte de um problema conduz a uma correção. A evidência afirma: *"The interaction is bidirectional (I3): the user reports an issue, and the system responds with a fix, demonstrating a feedback loop."* Este é um dos raros exemplos de diálogo produtivo.

- **Post 1i6m4i6_87** (World of Warcraft, A1, I3, VC4): Pontuação de Diálogo = 5/5. O post documenta uma interação com IA onde o utilizador reconhece: *"AI can be confidently incorrect... It's best to go in with some level of knowledge about the question you're asking, so you can recognize when it's wrong."* O diálogo é forte, mas o valor cocriado é limitado pela assimetria de conhecimento.

- **Post 1t3g4bt_38** (EVE Online, A1, I1, VC3): Pontuação de Diálogo = 4/5, mas com codestruição de valor. A evidência afirma: *"it'll only give you half an answer each time, it'll never dig deeper."* Este caso ilustra como um diálogo aparentemente ativo pode ser percebido como parasitário quando a IA não aprofunda as respostas.

**Análise**: O Diálogo é a dimensão mais dependente do tipo de interação. Posts classificados como I3 (bidirecional) tendem a apresentar pontuações de Diálogo mais elevadas, mas estes representam apenas 4,9% do corpus. A maioria dos posts (I4 e I6) não envolve qualquer diálogo com IA, resultando em pontuações nulas.

### 3.3 Acesso (Média: 0,75/5)

A dimensão Acesso mede a capacidade dos sistemas de IA para facultar informação, recursos ou funcionalidades aos utilizadores.

**Evidências empíricas**:

- **Post 502655_2823935** (EVE Online, A1, I5, VC4): Pontuação de Acesso = 3/5. O post descreve a ferramenta "Battlefield.Space" que utiliza um LLM (Gemini 3 Flash) para gerar relatórios de inteligência a partir de dados de killboard. A evidência afirma: *"Access is moderate (score 3) as the AI provides access to geographic intelligence context."*

- **Post 2329784_29810436** (World of Warcraft, A5, I4, VC4): Pontuação de Acesso = 2/5. O post menciona *"pulling live stats and analysis"* como capacidade potencial de IA, mas sem interação concreta.

- **Post 510327_2867289** (EVE Online, A4, I4, VC4): Pontuação de Acesso = 3/5. O post discute uma ferramenta assistida por IA, com a garantia explícita: *"It will never write to your EVE Online account or access your wallet."* Esta limitação de acesso é apresentada como medida de segurança.

**Análise**: O Acesso é moderadamente pontuado apenas em contextos de ferramentas externas (APIs, relatórios, scripts). Nos ecossistemas nativos dos jogos, o acesso mediado por IA é praticamente inexistente, refletindo a ausência de integração oficial de agentes de IA nos fluxos de jogo.

### 3.4 Risco (Média: 1,16/5)

A dimensão Risco mede a perceção e gestão de riscos associados à utilização de IA. É a dimensão com a pontuação média mais elevada (1,16), embora ainda fraca em termos absolutos.

**Evidências empíricas**:

- **Post 2324507_2324507_17** (World of Warcraft, A2, I6, VC4): Pontuação de Risco = 5/5. O post denuncia: *"Don't forget players getting banned because bots are mass reporting players unlucky enough to get in their way."* Este é o risco máximo documentado no corpus, envolvendo dano direto a jogadores inocentes através de sistemas automatizados maliciosos.

- **Post 510142_2865010** (EVE Online, A2, I4, VC4): Pontuação de Risco = 4/5. A evidência afirma: *"O risco é elevado (4) porque a perceção é de que a economia está a ser desestabilizada por agentes parasitários que extraem valor sem contribuir para a saúde do ecossistema."*

- **Post 1ph9o3i_22** (EVE Online, A4, I3, VC3): Pontuação de Risco = 4/5. O post documenta uma interação assistida por IA que resultou em erros significativos, com a evidência lacónica: *"MISTAKES WERE MADE."*

**Análise**: O Risco é a dimensão mais saliente no discurso comunitário, particularmente associado a bots convencionais (A2) e à sua capacidade de desestabilizar economias de jogo e prejudicar jogadores legítimos. A perceção de risco é mais elevada em EVE Online, onde a economia sandbox é mais vulnerável a agentes parasitários.

### 3.5 Transparência (Média: 0,77/5)

A dimensão Transparência mede o grau em que os sistemas de IA são explicáveis, auditáveis e comunicam o seu funcionamento aos utilizadores.

**Evidências empíricas**:

- **Post 512367_2882924** (EVE Online, A5, I4, VC4): Pontuação de Transparência = 3/5. O post comenta a fiabilidade de um sistema, com a evidência: *"sadly in practice it appears to be more in error."* A transparência é inferida pela discussão sobre a precisão do sistema.

- **Post 510327_2870703** (EVE Online, A1, I3, VC1): Pontuação de Transparência = 3/5. A evidência afirma: *"Transparency is moderate (score 3) with improved logging for diagnosis."* A melhoria dos logs de diagnóstico é um exemplo concreto de transparência operacional.

- **Post 2171055_27777967** (World of Warcraft, A5, I4, VC4): Pontuação de Transparência = 1/5. A evidência afirma: *"Transparency is weakly suggested by the user's question about the nature of the system, but this inference is uncertain."*

**Análise**: A Transparência é raramente abordada de forma explícita. Quando presente, está associada a ferramentas externas que documentam o seu funcionamento ou a discussões sobre a fiabilidade de sistemas de IA. Nos ecossistemas nativos, a transparência sobre medidas antibot ou sistemas de IA é praticamente inexistente.

---

## 4. Análise Comparativa de Jogos: Sandbox vs. Controlado

### 4.1 Distribuição do Corpus

| Jogo | Posts Analisados | Percentagem |
|------|------------------|-------------|
| EVE Online (Sandbox) | 438 | 42,4% |
| World of Warcraft (Controlado) | 594 | 57,6% |

### 4.2 Comparação de Metadados da API Discourse

| Métrica | EVE Online | World of Warcraft |
|---------|------------|-------------------|
| Média de Gostos | 1,1 | 2,7 |
| Média do Nível de Confiança do Autor | 1,4 | 1,3 |
| Média do Histórico de Edições | 1,1 | 1,1 |

**Análise**: A média de gostos é significativamente mais elevada em World of Warcraft (2,7 vs. 1,1), sugerindo uma comunidade mais reativa e engajada em termos de validação social. O nível de confiança do autor é ligeiramente superior em EVE Online (1,4 vs. 1,3), possivelmente refletindo uma comunidade mais técnica e especializada.

### 4.3 Padrões de Interação e Tipos de IA por Jogo

**EVE Online (Sandbox)**:

O ecossistema sandbox de EVE Online caracteriza-se por uma economia aberta, APIs públicas (ESI) e uma cultura de ferramentas externas. Este contexto favorece:

- **Maior incidência de A1 (Agentes de IA)**: Ferramentas como "EVE Crews" (Post 510327_2870703) e "Battlefield.Space" (Post 502655_2823935) demonstram integração de LLMs e sistemas de classificação autónoma.
- **Interações bidirecionais (I3) mais frequentes**: O ciclo de feedback entre utilizadores e ferramentas externas é mais comum.
- **Risco económico elevado**: A economia sandbox é vulnerável a bots parasitários que extraem valor sem contribuir (Post 510142_2865010).

**World of Warcraft (Controlado)**:

O ecossistema controlado de World of Warcraft caracteriza-se por uma economia mais regulada, progressão linear e menor abertura a ferramentas externas. Este contexto favorece:

- **Maior incidência de A2 (Bots Convencionais)**: Bots de farming e pixel bots são uma preocupação recorrente (Post 2116712_27043141: *"Pixel bots are out of control"*).
- **Risco associado a bans injustos**: O post 2324507_2324507_17 documenta o risco máximo (5/5) de jogadores inocentes serem banidos devido a mass reports de bots.
- **Discussão sobre IA mais especulativa**: A comunidade discute IA em termos de potencial futuro, não de implementação atual.

### 4.4 Síntese Comparativa

| Dimensão | EVE Online (Sandbox) | World of Warcraft (Controlado) |
|----------|---------------------|-------------------------------|
| Integração de IA (A1) | Mais frequente (ferramentas externas) | Menos frequente |
| Bots Convencionais (A2) | Preocupação económica | Preocupação de fairness |
| Interação Bidirecional (I3) | Mais comum | Menos comum |
| Risco Dominante | Desestabilização económica | Bans injustos e cheating |
| Cultura Comunitária | Técnica, orientada a ferramentas | Reativa, orientada a validação social |

---

## 5. Cocriação e Codestruição de Valor (VC1–VC4)

### 5.1 Distribuição Global

| Categoria de Valor | Frequência | Percentagem |
|--------------------|------------|-------------|
| VC1 (Cocriação de Valor) | 23 | 2,2% |
| VC2 (Potencial Cocriação) | 50 | 4,8% |
| VC3 (Codestruição de Valor) | 45 | 4,4% |
| VC4 (Sem evidência) | 914 | 88,6% |

**Análise**: A esmagadora maioria dos posts (88,6%) não apresenta evidência de criação ou destruição de valor. Este resultado é consistente com a predominância de discussões especulativas (A5) e interações humano-humano (I4). A cocriação efetiva (VC1) é rara (2,2%), enquanto a codestruição (VC3) é aproximadamente duas vezes mais frequente (4,4%).

### 5.2 Evidências de Cocriação de Valor (VC1)

**Post 510327_2870703** (EVE Online, A1, I3, VC1):

Este é o exemplo paradigmático de cocriação de valor no corpus. A evidência afirma:

> *"The post describes EVE Crews, an API-linked crew simulator that uses ESI data to classify ships. The system appears to have autonomous classification logic (hull detection, reclassification), suggesting AI-based decision-making (A1)... The interaction is bidirectional (I3): the user reports an issue, and the system responds with a fix, demonstrating a feedback loop. Value co-creation (VC1) is evident as the user's report leads to system improvements."*

**Características da cocriação**:
- **Simetria**: O utilizador contribui com informação (reporte de bug) e o sistema responde com melhoria (fix).
- **Diálogo forte** (4/5): Comunicação clara entre utilizador e sistema.
- **Transparência moderada** (3/5): Logs de diagnóstico melhorados.
- **Acesso moderado** (3/5): Facilitação de acesso a dados de naves.

### 5.3 Evidências de Potencial Cocriação (VC2)

**Post 2039353_25994927** (World of Warcraft, A4, I1, VC2):

O post descreve medidas anti-abuso propostas: *"Anti-Abuse Measures Win-trading detection using pattern recognition Stricter penalties for verified win-trading."* A classificação VC2 reflete o potencial de cocriação se estas medidas forem implementadas com sucesso.

### 5.4 Evidências de Codestruição de Valor (VC3)

**Post reddit_1ariy3g_20** (World of Warcraft, A5, I4, VC3):

A evidência é lacónica mas reveladora: *"Took me 5 tickets to finally get someone who looked into my ticket for more than 5 seconds."* Este post documenta a codestruição de valor através da falha do sistema de suporte, possivelmente mediado por IA ou automação inadequada.

**Post 1t3g4bt_38** (EVE Online, A1, I1, VC3):

A evidência afirma: *"it'll only give you half an answer each time, it'll never dig deeper."* Este post documenta como uma interação com IA que poderia ser cocriativa se torna parasitária devido à superficialidade das respostas.

**Post 1ph9o3i_22** (EVE Online, A4, I3, VC3):

A evidência: *"MISTAKES WERE MADE"* — com pontuação de Risco 4/5. Este post documenta uma interação assistida por IA que resultou em erros significativos, codestruindo valor através de consequências negativas.

### 5.5 Análise da Distribuição de Valor

**Resposta à QI4**: A distribuição de valor é fortemente assimétrica. A cocriação efetiva (VC1: 2,2%) é superada pela codestruição (VC3: 4,4%), e ambas são marginais face à ausência de evidência (VC4: 88,6%). Este padrão sugere que:

1. **A integração de IA nos ecossistemas de videojogos ainda não atingiu maturidade** para gerar cocriação de valor generalizada.
2. **A codestruição é mais visível e discutida** do que a cocriação, possivelmente devido ao viés de negatividade no discurso comunitário.
3. **A maioria das discussões sobre IA é especulativa** (A5/I4), não envolvendo interações concretas que possam gerar valor.

---

## 6. Reflexão sobre as Questões de Investigação

### 6.1 QI1: Proporção de Agentes de IA Autónomos vs. Bots Convencionais

**Resposta**: A proporção de agentes de IA autónomos (A1: 8,4%) é ligeiramente inferior à de bots/scripts convencionais (A2+A3: 11,1%). No entanto, ambos os grupos são minoritários face ao discurso especulativo (A5: 49,5%).

**Evidências**:
- **Post 1tdxixs_16** (EVE Online, A1, I1): Interação com Gemini, classificada como A1 devido à autonomia na análise de código.
- **Post 495219_2760206** (EVE Online, A2, I6): Pedido de bot Discord para notificações, classificado como A2 por ser automação determinística.
- **Post 1uqtdhy_10** (EVE Online, A3, I6): Script Autohotkey gerado por ChatGPT, classificado como A3 por ser automação sem autonomia em tempo de execução.

**Implicação teórica**: A distinção entre A1 e A2/A3 é crucial para evitar a inflação conceptual. Muitos posts que mencionam "IA" referem-se na verdade a automação convencional, e a pipeline DART-NET captura esta distinção com precisão.

### 6.2 QI2: Estruturas de Interação Humano-IA

**Resposta**: A interação dominante é I4 (Humano → Humano sobre IA: 56,0%), seguida de I6 (Sem interação significativa: 34,0%). As interações diretas com agentes ou ferramentas de IA (I1, I2, I3 e I5) totalizam apenas 10,0% do corpus empírico.

**Evidências**:
- **Post 510327_2866379** (EVE Online, A1, I3): Diálogo bidirecional e simulação de tripulações com base em dados ESI, demonstrando colaboração humano-sistema no planeamento estratégico.
- **Post 2344820_29989185** (World of Warcraft, A5, I4): Discussão inter-jogadores sobre o impacto de algoritmos de matching e moderação automática nas instâncias míticas.
- **Post 1ph9o3i_2** (EVE Online, A4, I1): Solicitação direta de conselhos de mineração e fabricação a copiloto LLM com intervenção humana final.

**Implicação teórica**: A mediação discursiva prevalece sobre a mediação técnica ativa. Os ecossistemas de videojogos funcionam presentemente como espaços de *negociação social sobre o papel da IA*, mais do que palcos de cooperação simbiótica rotineira.

### 6.3 QI3: Satisfação das Dimensões DART

**Resposta**: As dimensões do modelo DART são fracamente satisfeitas de forma geral, registando médias globais reduzidas (Diálogo: 0,66/5; Acesso: 0,75/5; Risco: 1,16/5; Transparência: 0,77/5). A dimensão Risco sobressai como a mais proeminente e articulada pelos utilizadores.

**Evidências**:
- **Post 2324507_2324507_17** (World of Warcraft, A2, Risco: 5/5): Risco extremo percebido associado a denúncias automáticas em massa e expulsão de utilizadores inocentes.
- **Post 510327_2870703** (EVE Online, A1, Diálogo: 4/5, Transparência: 3/5): Caso de excelência empírica, com explicabilidade clara de logs e depuração iterativa.
- **Post 497087_2771352** (EVE Online, A3, Acesso: 3/5): Ferramenta MCP para Swagger API que expande o acesso a ações autenticadas de múltiplos personagens.

**Implicação teórica**: A assimetria do modelo DART no terreno revela que, na ausência de mecanismos deliberados de transparência e diálogo bidirecional concebidos pelas editoras, os utilizadores tendem a percecionar os sistemas autónomos quase exclusivamente sob o prisma da opacidade e do risco.

### 6.4 QI4: Cocriação (VC1/VC2) vs. Codestruição (VC3) de Valor

**Resposta**: A distribuição de valor é profundamente desbalanceada. A cocriação efetiva (VC1: 2,2%) e o seu potencial tangível (VC2: 4,8%) somam 7,0%, enquanto a codestruição (VC3: 4,4%) se manifesta com o dobro da frequência da cocriação plena. A esmagadora maioria (VC4: 88,6%) reflete ausência de impacto de valor direto comprovado.

**Evidências**:
- **Post 510327_2866108** (EVE Online, VC1): Cocriação através do enriquecimento da experiência de jogo e geração de micro-narrativas de suporte à comunidade.
- **Post 1t3g4bt_38** (EVE Online, VC3): Codestruição resultante de respostas truncadas e alucinações de modelos generativos que prejudicam o planeamento económico.
- **Post reddit_1tvlpnw_1** (World of Warcraft, VC2): Addon experimental com machine learning para filtragem de spam no comércio, com elevado potencial colaborativo ainda em fase de maturação.

**Implicação teórica**: A emergência de valor cocriado exige simetria informacional. Quando os sistemas de IA atuam como caixas negras ou ferramentas extrativas unilaterais, a dinâmica degenera rapidamente em codestruição e ceticismo comunitário.

### 6.5 QI5: Implicações para o Design de Ecossistemas com IA Integrada

**Resposta**: Os dados apontam para a necessidade premente de desenhar arquiteturas de IA que priorizem interfaces de explicabilidade (Transparência) e canais de feedback responsivos (Diálogo), reduzindo a fricção e o receio de exploração económica.

**Evidências e Diretrizes**:
1. **APIs e Servidores MCP Auditáveis**: O sucesso relativo verificado em ferramentas de EVE Online (como MCP servers e companheiros ESI) demonstra que conceder acesso estruturado e seguro à IA promove o desenvolvimento de soluções cocriativas sustentáveis.
2. **Mitigação do Efeito "Mass-Report" e Punições Cegas**: As experiências negativas documentadas em World of Warcraft evidenciam que a automação na moderação e no suporte de clientes sem supervisão humana robusta destrói ativamente a confiança dos utilizadores.
3. **Preservação da Agência Humana (A4)**: As configurações do tipo A4 (Humano Assistido por IA) apresentam menores índices de risco percebido e maior aceitação ética pela comunidade do que sistemas puramente autónomos (A1) sem supervisão.

---

## 7. Auditoria de Qualidade, Calibração e Fila de Validação Humana

### 7.1 Desempenho da Auditoria Qualitativa Multiagente (QualityGuardAgent)

Em estrita conformidade com a governação metodológica do DART-NET, uma amostra probabilística estratificada de **20% de todas as codificações** (amostra de 206 análises DART) foi submetida a uma auditoria científica cega e independente conduzida pelo modelo de alta capacidade `deepseek-v4-pro`.

Os resultados consolidados da auditoria evidenciam a robustez e calibração das recomendações da Camada 2:

- **Score Médio Global de Consistência Qualitativa**: **84,41%** (superando amplamente o limiar crítico de reprodutibilidade fixado em 70,0%).
- **Veracidade das Evidências Literais (Evidence-First Principle)**: 100% das citações extraídas correspondiam a texto literal existente nas postagens originais, comprovando ausência de alucinações empíricas.
- **Consistência Taxonómica (A1–A6 e DART)**: O auditor confirmou a prevenção eficaz de falsos positivos na categoria A1, mantendo bots determinísticos e scripts estritamente delimitados em A2 e A3.

### 7.2 Calibração da Fila de Validação Humana (Human Review Required)

O framework DART-NET estabelece como princípio epistemológico que os modelos de IA operam como assistentes de codificação recomendatória e não como decisores científicos finais. Assim, sempre que qualquer nível de confiança desce abaixo de 0,80 ou surgem ambiguidades contextuais, o registo é sinalizado obrigatoriamente para intervenção humana (`human_review_required = True`).

- **Total de Posts Sinalizados para Revisão Humana**: **803 posts (77,81%)**
- **Taxa de Aceitação Automática Direta (Confiança Muito Elevada)**: 229 posts (22,19%)

Esta proporção substantiva de revisão humana (77,8%) reflete deliberadamente o princípio da prudência científica: o discurso em comunidades virtuais de videojogos é densamente impregnado de jargão contextual (*multiboxing*, *pixel bots*, *ESI*, *vibe coding*), sarcasmo e ironia, exigindo que o investigador humano retenha a responsabilidade final de validação nos casos de fronteira.

---

## 8. Discussão Teórica, Reprodutibilidade e Limitações

### 8.1 Preservação das 3 Camadas Metodológicas (DART-NET)

A execução deste estudo adota uma separação estrita e não destrutiva em 3 camadas de dados, garantindo total auditabilidade e reprodutibilidade científica:

1. **Camada 1 — Dados em Bruto (Raw Data)**: 430 ficheiros JSON originais armazenados em `data/raw/` preservando a integridade integral das mensagens, tópicos e metadados de API do Discourse, Reddit e Steam Community.
2. **Camada 2 — Codificação Assistida por IA (AI Coding)**: Armazenamento em `data/processed/anonymized_posts.json` e `data/analysis/netnography_results.jsonl`, integrando a pseudonimização ética de intervenientes (`Player_0001` a `Player_1032`), a higienização de identificadores pessoais (PII) e o rastreio auditável de raciocínio LLM.
3. **Camada 3 — Validação Humana e Síntese Científica (Human Validation)**: Compilação das matrizes de síntese (`output/tabela_resumos.md`), inventário canónico de 303 ligações (`output/lista_links.md` e `.txt`), auditoria de qualidade (`quality_audit_results.json`) e o presente relatório formal.

### 8.2 Delimitação Temporal Estrita (Jan 2024 – 2026)

Um avanço metodológico fundamental desta reexecução residiu no rigoroso isolamento temporal dos dados:
- **Critério de Exclusão**: Foram eliminadas de todas as camadas analíticas mensagens publicadas antes de 01 de janeiro de 2024.
- **Justificação Epistemológica**: O ano de 2024 assinala a transição pragmática na adoção de LLMs e arquiteturas baseadas em agentes (Model Context Protocol, copilotos generativos, raciocínio em tempo real), diferenciando o ecossistema atual das discussões puramente conceptuais de anos anteriores.

### 8.3 Métricas de Eficiência e Transparência de Custos

A totalidade do pipeline multi-agente operou com monitorização detalhada de recursos:
- **Total de Chamadas de API**: 26.616 invocações (24.674 `deepseek-v4-flash` e 1.942 `deepseek-v4-pro`).
- **Volume de Tokens Processados**: 18.116.689 tokens de entrada e 9.890.997 tokens de saída.
- **Custo Operacional Consolidado**: **$21,05 USD**, comprovando a elevada viabilidade económica e reprodutibilidade de estudos netnográficos em larga escala com recurso a arquiteturas multi-agente orquestradas.

### 8.4 Limitações e Vias para Investigações Futuras

1. **Barreiras Técnicas de Acesso**: Plataformas que impõem desafios anti-bot (Cloudflare em fóruns de terceiros como MMO-Champion) requerem acordos institucionais de recolha ou parcerias de dados.
2. **Evolução Rápida do Ecossistema**: O advento acelerado do protocolo MCP e de copilotos autónomos de jogo exigirá investigações longitudinais regulares para monitorizar se a proporção de cocriação simétrica (VC1) se expande à medida que a literacia de desenvolvimento de ferramentas assistidas por IA se democratiza entre os jogadores.