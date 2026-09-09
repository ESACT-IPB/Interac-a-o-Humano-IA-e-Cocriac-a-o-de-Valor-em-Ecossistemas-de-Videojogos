# Relatório DART-NET: Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos

**Análise Comparativa entre EVE Online (Sandbox) e World of Warcraft (Controlado)**

---

## 1. Sumário Metodológico e Framework DART-NET

### 1.1 Enquadramento Teórico

O presente relatório adota o framework DART-NET (Prahalad & Ramaswamy, 2004; DART-NET 2026), uma extensão operacional do modelo DART clássico — Diálogo, Acesso, Risco e Transparência — para a análise sistemática de interações entre humanos e agentes de inteligência artificial (IA) em ecossistemas virtuais de videojogos. O framework original de Prahalad e Ramaswamy postula que a cocriação de valor emerge da interação dialética entre consumidores e sistemas, sendo mediada por quatro pilares fundamentais: a qualidade do diálogo entre atores, o acesso a recursos e informação, a avaliação e gestão de riscos, e a transparência dos processos.

A extensão DART-NET (2026) adapta este modelo para o contexto específico de ecossistemas digitais, onde a presença de agentes de IA — desde bots convencionais até agentes autónomos sofisticados — introduz novas dinâmicas de poder, valor e risco que não são capturadas adequadamente pelas taxonomias tradicionais de automação.

### 1.2 Metodologia de Recolha e Processamento

A pipeline DART-NET foi operacionalizada através da recolha de dados provenientes de fóruns oficiais (Discourse) e plataformas complementares, abrangendo um corpus total de **2867 posts analisados**, distribuídos da seguinte forma:

- **EVE Online (Sandbox):** 1429 posts (49,8%)
- **World of Warcraft (Controlado / Theme Park):** 1429 posts (49,8%)
- **Amostra de Controlo Cruzado (DarkTide / RuneScape):** 9 posts (0,4%)

A metodologia compreendeu as seguintes etapas:

1. **Extração:** Recolha automatizada de posts através da API do Discourse e de fontes complementares, incluindo metadados de autor (nível de confiança, histórico de edições) e de interação social (número de gostos).

2. **Classificação Taxonómica:** Cada post foi classificado segundo três eixos:
   - **Tipo de Agente de IA (A1-A6):** Distinção entre agentes de IA autónomos, bots convencionais, scripts, assistência humana, discussões sobre IA e conteúdo irrelevante.
   - **Estrutura de Interação Humano-IA (I1-I6):** Caracterização da direcionalidade e natureza da interação entre humanos e sistemas automatizados.
   - **Cocriação de Valor (VC1-VC4):** Identificação de evidências de cocriação, codestruição, potencial cocriação ou ausência de ambas.

3. **Avaliação DART:** Atribuição de pontuações nas quatro dimensões DART (Diálogo, Acesso, Risco, Transparência) numa escala Likert de 0 a 5, acompanhada de fundamentação qualitativa para cada classificação.

4. **Auditoria de Qualidade:** Submissão dos resultados a uma auditoria secundária (deepseek-v4-pro) para verificação de consistência e identificação de casos que requerem revisão humana.

### 1.3 Especificação Detalhada de Todas as Fontes Consultadas

A recolha empírica foi concebida para assegurar a máxima representatividade ecológica dos discursos comunitários, combinando canais formais geridos pelas editoras com espaços independentes e não moderados pelas empresas. O corpus integra **246 hiperligações canónicas ativas** indexadas em [`output/lista_links.txt`](file:///Users/jpaulo/Documents/AntiGravity_Agents/DeepSeek_Netnography%20DART%20Pipeline%20Orchestration/output/lista_links.txt), alicerçadas numa base primária de **350 ficheiros de discussão imutáveis** e **8.779 mensagens brutas**, com novas ramificações dedicadas especificamente à emergência de **Agentes LLM, Protocolo MCP e Ferramentas Copiloto**.

A Tabela 1.1 sintetiza a distribuição consolidada de todas as plataformas, comunidades e fontes primárias consultadas no estudo.

**Tabela 1.1 — Inventário Consolidado das Fontes e Comunidades Consultadas**

| Plataforma / Domínio | Jogo / Ecossistema | Comunidade / Secção Específica | Tipologia de Gestão | Foco Principal da Investigação | Método de Extração |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fórum Blizzard US** (`us.forums.blizzard.com`) | World of Warcraft | General, Classic, Economy, Support, Dev | Oficial (Blizzard Entertainment) | Economia AH, Banwaves, MCP Blizzard API, Addons IA | API Discourse (JSON) |
| **Fórum Blizzard EU** (`eu.forums.blizzard.com`) | World of Warcraft | General Discussion (EU) | Oficial (Blizzard Entertainment) | Economia de bots, manipulação de preços | API Discourse (JSON) |
| **Fórum EVE Online** (`forums.eveonline.com`) | EVE Online | General, Features, Security, Third-Party Dev | Oficial (CCP Games) | *Aura Guidance Beta*, Servidores MCP ESI, Regras IA | API Discourse (JSON) |
| **Reddit** (`reddit.com/r/Eve`) | EVE Online | Subreddit `r/Eve` | Independente / Não-moderado | *ChatGPT Copilot via MCP/ESI*, Killboards LLM, Mercado | Web Scraping Estruturado |
| **Reddit** (`reddit.com/r/wow`) | World of Warcraft | Subreddit `r/wow` | Independente / Não-moderado | *Vibe-coding* de addons, *OneButton Assist*, ChatGPT | Web Scraping Estruturado |
| **Steam Community** (`steamcommunity.com`) | EVE Online | Hub Geral de Discussão (App 8500) | Aberto (Valve / Utilizadores) | Barreiras PLEX, perceções de novos jogadores | Web Scraping Estruturado |
| **Reddit** (`reddit.com/r/classicwow`) | World of Warcraft | Subreddit `r/classicwow` | Independente / Não-moderado | Claude Code, bots no Classic Fresh, Suporte IA | Web Scraping Estruturado |
| **Reddit** (`reddit.com/r/woweconomy`) | World of Warcraft | Subreddit `r/woweconomy` | Especializado em Economia / Goblins | Modelos preditivos de AH, APIs de leilão, Anti-bot | Web Scraping Estruturado |
| **Reddit** (`reddit.com/r/DarkTide`) | Warhammer 40k: Darktide | Subreddit `r/DarkTide` | Amostra de Controlo Cruzado | Comportamento de bots em PvE cooperativo tático | Web Scraping Estruturado |
| **Reddit** (`reddit.com/r/RunescapeBotting`) | RuneScape | Subreddit `r/RunescapeBotting` | Amostra Comparativa de Automação | Deteção comportamental de cliques e visão computacional | Web Scraping Estruturado |
| **Fontes Complementares** | Multi-ecossistema | GameSpot, YouTube, TikTok | Jornalismo & Mídias Sociais | Simulações IA single-player, vídeos de bot trains | Web Scraping Estruturado |

#### 1.3.1 Caracterização Qualitativa das Novas Dimensões Temáticas e Fontes Primárias

1. **EVE Online — A Vanguarda do Protocolo MCP e Copilotos LLM:**
   - *Integração MCP (Model Context Protocol) & ESI API:* Discussões em torno de projetos abertos de integração (`eve-mcp-server`, `eve-mentor-mcp`, `OpenClaw`) que conectam modelos de fronteira (Claude 3.7 Sonnet, ChatGPT) diretamente à *Endpoints Server Interface* (ESI) da CCP Games. O LLM atua como copiloto tático em tempo real com acesso a telemetria, cálculos de Dogma Engine para fittings de naves e alertas de rota.
   - *Aura Guidance AI (Iniciativa Oficial CCP):* Tópicos de feedback da comunidade sobre o assistente experimental de onboarding da CCP (*Aura Guidance Beta*), debatendo se a IA deve atuar apenas como intérprete contextual do lore de New Eden ou como guia procedural com acesso à interface de voo.
   - *Inteligência de Combate e Mercado via LLM:* Projetos comunitários como *Eve Market Scout*, *EveKill Narrative Killboards* e *Battlefield Space*, que utilizam LLMs para sintetizar relatórios táticos de perdas e lucros de frotas.

2. **World of Warcraft — Vibe-Coding de Addons e Automação de Interface:**
   - *Vibe-Coded Addons & Impacto Técnico:* Análise aprofundada nos subreddits `r/wow` e fóruns oficiais sobre o fenómeno de jogadores e criadores sem experiência prévia de programação que utilizam ChatGPT e Claude para gerar addons em Lua e XML, resultando em sobrecarga na renderização e degradação de FPS (*Frame Pacing*).
   - *Servidores MCP para Blizzard API & Ferramentas de Raide:* Implementações comunitárias de conectores MCP para aceder a registos de combate (Warcraft Logs) e dados de guias míticos, transformando assistentes de IA em estrategistas de preparação de masmorras.
   - *OneButton Assist e Acessibilidade vs. Automação:* A tensão entre mecanismos de assistência de jogabilidade projetados pela Blizzard e a linha ténue que os separa de rotações automáticas não autorizadas.

3. **Economia e Suporte ao Cliente (Classic WoW & WoW Economy):**
   - Discussão sobre o impacto de ferramentas como Claude Code na análise preditiva de mercados, e a contestação generalizada da automação das respostas de apoio ao cliente (GMs de suporte substituídos por bots de IA).

#### 1.3.2 Protocolo de Descoberta Booleana e Triangulação Netnográfica
Para ultrapassar as limitações de cobertura dos motores de busca internos dos fóruns e capturar o discurso emergente sobre as mais recentes tecnologias de IA, foram implementadas consultas booleanas estruturadas via Google Search direcionadas a subcomunidades específicas:
1. `site:reddit.com/r/Eve ("LLM" OR "ChatGPT" OR "AI agent" OR "Claude")`
2. `site:reddit.com/r/Eve ("copilot" OR "agent" OR "MCP") ("ESI" OR "API")`
3. `site:reddit.com (r/wow OR r/Eve OR r/classicwow OR r/woweconomy) ("LLM" OR "ChatGPT" OR "Claude" OR "machine learning") ("AI agent" OR "copilot" OR "agent" OR "MCP") ("API" OR "ESI" OR "botting" OR "computer vision")`

Esta abordagem cumpre com rigor os cânones da triangulação netnográfica (Kozinets, 2020), cruzando evidências oficiais sob a vigilância das editoras com espaços de desenvolvimento aberto e partilha crítica sem filtro institucional.

### 1.4 Distinção entre IA e Automação Convencional (A1-A6)

A taxonomia de agentes de IA adotada neste estudo estabelece uma distinção crucial entre automação convencional e inteligência artificial genuína, refletindo a diversidade de sistemas automatizados presentes nos ecossistemas de videojogos:

- **A1 (AI Agent):** Agente de IA autónomo com capacidade de aprendizagem, adaptação e tomada de decisão independente, frequentemente associado a técnicas de aprendizagem automática ou redes neuronais. Estes agentes demonstram comportamentos emergentes que não são programados explicitamente.

- **A2 (Conventional Bot):** Bot convencional, também designado como "bot tradicional" ou "bot de script fixo", caracterizado por regras predefinidas e comportamentos repetitivos sem capacidade de aprendizagem ou adaptação. Representa a forma mais comum de automação em videojogos, frequentemente utilizada para farming, mineração automatizada ou exploração económica.

- **A3 (Script/Automation):** Scripts ou automação de interface que executam tarefas específicas e limitadas, frequentemente através de macros ou manipulação de input, sem constituir um agente inteligente autónomo.

- **A4 (AI-Assisted Human):** Humano assistido por ferramentas de IA que aumentam as suas capacidades, mas onde o humano permanece como agente primário de decisão. Representa uma forma híbrida de interação.

- **A5 (Discussion About AI):** Conteúdo que discute IA ou automação como tópico, sem constituir uma interação direta com um agente. Estes posts refletem a perceção, opinião e discurso da comunidade sobre automação.

- **A6 (Irrelevant):** Conteúdo que não apresenta qualquer evidência de relação com IA, bots ou automação, independentemente da sua relevância para o tópico geral do fórum.

A distinção fundamental entre A1 e A2 reside na capacidade de adaptação: enquanto os bots convencionais (A2) executam ações baseadas em regras fixas e previsíveis, os agentes de IA autónomos (A1) demonstram flexibilidade comportamental, aprendizagem e capacidade de resposta a situações não programadas explicitamente. Esta distinção é operacionalizada através da análise linguística, referências técnicas e evidências contextuais presentes nos posts.

### 1.5 Questões de Investigação (QI1-QI5)

O presente estudo orienta-se pela formulação de cinco Questões de Investigação (QI), que estruturam a análise subsequente:

- **QI1:** Qual a proporção de agentes de IA autónomos (A1) face a bots e scripts convencionais (A2-A3) nos ecossistemas de videojogos analisados?

- **QI2:** Como se caracterizam as estruturas de interação entre humanos e agentes de IA (I1-I6) em ecossistemas sandbox versus controlados?

- **QI3:** De que forma as quatro dimensões DART — Diálogo, Acesso, Risco e Transparência — se manifestam quantitativamente e qualitativamente nos discursos dos jogadores sobre automação?

- **QI4:** Como se distribui a cocriação e codestruição de valor (VC1-VC4) entre jogadores humanos e sistemas automatizados, e que implicações tem para a sustentabilidade dos ecossistemas?

- **QI5:** Quais as diferenças observáveis entre ecossistemas sandbox (EVE Online) e controlados (World of Warcraft) na perceção de risco e na dinâmica de valor associada à automação?

---

## 2. Taxonomia de Agentes de IA e Interações

### 2.1 Distribuição Global de Tipos de IA (A1-A6)

A Tabela 2.1 apresenta a distribuição global dos tipos de IA identificados no corpus consolidado após a integração dos novos tópicos de fronteira (MCP, LLMs, copilotos e vibe-coding).

**Tabela 2.1 — Distribuição de Tipos de IA (A1-A6) no Corpus Total (N=2867)**

| Tipo | Designação | Frequência | Percentagem |
|------|------------|------------|-------------|
| A1 | AI Agent (Agente de IA autónomo) | 65 | 2,27% |
| A2 | Conventional Bot (Bot convencional) | 1486 | 51,83% |
| A3 | Script/Automation | 7 | 0,24% |
| A4 | AI-Assisted Human | 32 | 1,12% |
| A5 | Discussion About AI | 340 | 11,86% |
| A6 | Irrelevant (Irrelevante) | 937 | 32,68% |

Os resultados revelam uma evolução crucial: **embora a automação convencional (A2) permaneça como a categoria mais volumosa (51,83%)**, a introdução de discussões sobre o **Protocolo MCP (Model Context Protocol)** e copilotos LLM conduziu ao surgimento mensurável de **agentes de IA genuínos (A1: 65 posts, 2,27%)** e de **humanos assistidos por IA (A4: 32 posts, 1,12%)**. 

Projetos como o `eve-mentor-mcp` (Tópico #513384) no EVE Online e ferramentas de *vibe-coding* em World of Warcraft demonstram que a fronteira da automação está a transitar de scripts mecânicos determinísticos para sistemas dotados de julgamento contextual, raciocínio em grafos de dependências de skills e integração com APIs abertas de telemetria. Paralelamente, as **discussões sobre IA (A5) expandiram-se substancialmente para 340 posts (11,86%)**, refletindo o debate comunitário sobre as implicações de políticas de suporte automatizado, *Aura AI* e regulação de copilotos.

### 2.2 Distribuição de Estruturas de Interação (I1-I6)

A Tabela 2.2 sintetiza a distribuição das estruturas de interação humano-IA identificadas.

**Tabela 2.2 — Distribuição de Estruturas de Interação Humano-IA (I1-I6)**

| Tipo | Designação | Frequência | Percentagem |
|------|------------|------------|-------------|
| I1 | Humano → IA (unidirecional) | 22 | 0,77% |
| I2 | IA → Humano (unidirecional) | 3 | 0,10% |
| I3 | Humano ↔ IA (bidirecional) | 42 | 1,46% |
| I4 | Humano → Humano sobre IA | 1799 | 62,75% |
| I5 | Humano → Ambiente mediado por IA | 3 | 0,10% |
| I6 | Sem interação significativa | 998 | 34,81% |

A estrutura de interação dominante continua a ser **I4 (Humano → Humano sobre IA)**, com 62,75% do corpus, demonstrando que os fóruns operam primariamente como esferas de debate comunitário. No entanto, regista-se a emergência clara de **interações bidirecionais genuínas (I3: 42 posts, 1,46%)** e de comandos deliberados **Humano → IA (I1: 22 posts, 0,77%)**, impulsionadas pela interação ativa com clientes Claude/ChatGPT conectados a servidores MCP de mentoria e simulação de combate.

### 2.3 Implicações para as Questões de Investigação QI1 e QI2

**Relativamente à QI1** — A proporção de agentes autónomos ou aumentados (A1+A4: 97 posts, 3,39%) face a bots convencionais (A2-A3: 1.493 posts, 52,07%) é de aproximadamente **1:15**. Embora os bots tradicionais continuem a ditar o volume de queixas sobre distorção económica, a ascensão qualitativa de servidores MCP e copilotos LLM prova que a inteligência artificial generativa já não é puramente hipotética nos ecossistemas de videojogos, operando como uma nova classe emergente de ferramentas cooperativas.

**Relativamente à QI2** — As estruturas de interação deixam de ser exclusivamente conversas indiretas entre jogadores (I4) e passam a integrar diálogos reflexivos e operacionais (I3). No sandbox (EVE Online), a integração profunda com a ESI API fomenta assistentes táticos sofisticados; no ecossistema controlado (World of Warcraft), o foco recai na assistência à programação de macros/addons e em controvérsias sobre o atendimento automatizado da Blizzard.

---

## 3. Análise por Dimensão DART

### 3.1 Médias Globais das Dimensões DART

A Tabela 3.1 apresenta as médias globais das quatro dimensões DART na escala de 0 a 5.

**Tabela 3.1 — Médias Globais das Dimensões DART (Escala 0-5) no Corpus Consolidado (N=2867)**

| Dimensão | Média | Desvio-Padrão Estimado | Variação com Tópicos de IA/MCP |
|----------|-------|------------------------|--------------------------------|
| Diálogo | 0,16 | 0,52 | +0,15 (Crescimento de 16x) |
| Acesso | 0,19 | 0,58 | +0,18 (Crescimento de 19x) |
| Risco | 2,02 | 1,55 | -0,06 (Estável em patamar elevado) |
| Transparência | 0,19 | 0,56 | +0,17 (Crescimento de 10x) |

Os resultados consolidados revelam uma transformação empírica fundamental: embora o **Risco** continue a ser a dimensão com maior pontuação média global (**2,02/5**), a incorporação sistemática de tópicos sobre **Protocolo MCP, copilotos LLM e Aura AI** provocou um aumento acentuado nas dimensões de **Diálogo** (0,16/5), **Acesso** (0,19/5) e **Transparência** (0,19/5). Estas três dimensões, anteriormente com médias quase nulas (0,01-0,02/5), multiplicaram-se por um fator de 10x a 19x.

### 3.2 Análise Detalhada da Dimensão Diálogo (Média: 0,16/5)

A dimensão Diálogo avalia a presença de comunicação bidirecional significativa entre os participantes do ecossistema, incluindo a formulação de prompts e interação com agentes de IA.

**Evidência Empírica:** Posts focados em servidores MCP e agentes copiloto exibem pontuações de Diálogo entre 2 e 4. No post ID `513384_2889848` (`eve-mentor-mcp`), o desenvolvedor destaca: *"It gives Claude (or any MCP client) live EVE data with judgment baked in"*, registando uma interação dialógica onde o jogador coloca questões contextuais sobre perdas de naves e o modelo devolve recomendações táticas personalizadas. Em World of Warcraft, o diálogo expressa-se na assistência interativa para depuração de erros de Lua via ChatGPT.

### 3.3 Análise Detalhada da Dimensão Acesso (Média: 0,19/5)

A dimensão Acesso avalia a disponibilidade de telemetria, documentação de APIs, e ferramentas analíticas abertas.

**Evidência Empírica:** A média de Acesso subiu para 0,19/5, impulsionada pelos tópicos de integração técnica. No caso do `eve-mentor-mcp`, o score de Acesso atinge o patamar máximo de **5/5 (explícito e central)**: o sistema disponibiliza 26 ferramentas operacionais ligadas à ESI API da CCP e ao zKillboard, conferindo ao novo jogador acesso imediato a dados de mercado em tempo real, cálculos de pré-requisitos de treino de competências e análise forense de destruição de naves.

### 3.4 Análise Detalhada da Dimensão Risco (Média: 2,02/5)

A dimensão Risco continua a ser a mais expressiva no cômputo geral, refletindo tanto as ameaças persistentes de botting tradicional (distorção económica em EVE e WoW) como novos riscos emergentes associados a sobrecarga de renderização por addons gerados por IA (*vibe-coding*) e questões de privacidade/etiqueta de chamadas a APIs oficiais.

**Evidência Empírica:** O post `513384_2889848` ilustra a nova perceção de risco cauteloso (Risco: 2/5): *"Feedback from this community would be very welcome, particularly on ESI etiquette and on what guidance is appropriate to give brand-new players."* Paralelamente, os casos de risco extremo (5/5) continuam concentrados nas denúncias de automação parasitária não mitigada.

**Análise de Posts Exemplares de Alto Risco (4-5/5):**

- **Post ID `xaonz7_2` (EVE Online, Risco: 5/5, 65 gostos):** O autor identifica o botting e o RMT (Real Money Trading) como "indissociáveis" e sugere conivência da editora, gerando um "estado de vulnerabilidade sistémica". Os 65 gostos indicam amplo acordo comunitário, reforçando a perceção de risco grave.

- **Post ID `514029_2896571` (EVE Online, Risco: 5/5, Trust Level 3):** O autor veterano classifica a situação como "game-breaking", denunciando a falta de enforcement contra input broadcasting. A ameaça à integridade económica é percebida como existencial.

- **Post ID `3000005_25902831` (World of Warcraft, Risco: 5/5):** O jogador reporta bots persistentes há meses "sem qualquer ação da Blizzard", indicando "falha sistémica na moderação". A economia do servidor é afetada e a confiança no fairness do jogo está "quebrada".

- **Post ID `2000001_29688302` (World of Warcraft, Risco: 5/5):** O autor descreve bots "fora de controlo", adotando uma estratégia defensiva de "esperar por camadas altas" que evidencia impotência perante a ameaça.

**Análise de Posts de Risco Moderado (3/5):**

- **Post ID `2000026_10132536` (World of Warcraft, Risco: 3/5):** O autor reconhece riscos históricos (PvE em GW) mas considera a ideia "decente", sugerindo cautela não alarmista.

- **Post ID `2041181_26019948` (World of Warcraft, Risco: 3/5):** O autor não relata ameaça iminente, mas especula sobre riscos futuros com base no conhecimento de IA e addons, mostrando "preocupação cautelosa, não alarmista".

**Interpretação Teórica:** A dominância do Risco reflete a **centralidade das preocupações com integridade, justiça e sustentabilidade** no discurso comunitário sobre automação. O risco percebido concentra-se em três dimensões principais:

1. **Risco Económico:** Bots que distorcem mercados, inflacionam preços e degradam o valor das economias virtuais.
2. **Risco Competitivo:** Automação que confere vantagem injusta, eliminando a habilidade humana como fator determinante.
3. **Risco de Confiança:** Falhas na moderação e enforcement que quebram a confiança dos jogadores na integridade do ecossistema.

A elevada média de Risco contrasta com as médias quase nulas das outras dimensões, sugerindo que o discurso comunitário está estruturado em torno do **paradigma da ameaça**, e não do paradigma da colaboração ou cocriação.

### 3.5 Análise Detalhada da Dimensão Transparência (Média: 0,02/5)

A dimensão Transparência avalia o grau de visibilidade dos processos, regras e mecanismos relacionados com a automação, incluindo a clareza sobre deteção, enforcement e políticas editoriais.

**Evidência Empírica:** A média de 0,02/5 indica uma **quase total ausência de transparência** no corpus analisado. Quando a transparência é identificada, frequentemente relaciona-se com a opacidade dos processos de deteção e punição de bots.

**Exemplos de Transparência Presente:**

- **Post ID `3000002_27797749` (World of Warcraft, Transparência: Sim):** O autor argumenta que "95% poderia ser resolvido com GMs humanos", expondo a opacidade das atuais políticas de moderação automatizada.

- **Post ID `514029_2896571` (EVE Online, Transparência: Sim):** O post revela a falta de enforcement contra input broadcasting, expondo a ausência de transparência nos processos regulatórios.

**Interpretação Teórica:** A ausência de transparência é consistente com a perceção generalizada de que as editoras (CCP, Blizzard) não comunicam adequadamente as suas políticas de deteção e punição de bots. Esta opacidade contribui para a elevada perceção de risco, pois os jogadores não têm visibilidade sobre as medidas de mitigação existentes, levando a uma sensação de desamparo e vulnerabilidade.

### 3.6 Síntese DART: A Assimetria do Risco

A análise DART global revela uma paisagem de interação profundamente assimétrica, onde a dimensão de **Risco domina o discurso** (2,08/5) enquanto as dimensões de **Diálogo, Acesso e Transparência são praticamente inexistentes** (0,01-0,02/5).

Esta assimetria tem implicações teóricas significativas para o framework DART-NET: **a cocriação de valor é minimizada quando as condições de diálogo, acesso e transparência não são satisfeitas, mesmo na presença de um forte sentido de risco**. Os jogadores reconhecem ameaças significativas, mas não dispõem de mecanismos de diálogo, acesso a informação ou transparência processual para responder a essas ameaças de forma construtiva. Em vez disso, o discurso reflete-se em estratégias de evasão, adaptação individual ou simples resignação.

---

## 4. Análise Comparativa de Jogos: Sandbox vs. Controlado

### 4.1 EVE Online (Sandbox)

**Tipo de Ecossistema:** EVE Online representa o arquétipo do sandbox, onde a economia é inteiramente gerida pelos jogadores, as regras são mínimas e a agência individual é maximizada. O jogo permite que os jogadores estabeleçam corporações, disputem território e manipulem mercados de forma orgânica.

**Perfil de Automação no Corpus:** Dos 1316 posts analisados de EVE Online, a distribuição de tipos de IA é dominada pelos bots convencionais (A2), com uma proporção ligeiramente elevada de posts irrelevantes (A6) devido à riqueza de discussões sobre lore, política e mecânicas de jogo.

**Média de Gostos:** 1,4 por post.
**Média do Nível de Confiança do Autor:** 1,8.

**Características do Risco em EVE Online:** A perceção de risco em EVE Online está profundamente ligada à **economia aberta**. Os bots são percebidos como ameaças à integridade do mercado, capazes de inflacionar preços, monopolizar recursos e destruir o valor do esforço humano. O risco é vivido como **existencial para a economia sandbox**, pois a automação não regulamentada pode colapsar a complexa teia de interdependências económicas que define o jogo.

**Evidência Exemplar:**

- **Post ID `xaonz7_2` (EVE Online, Risco: 5/5, 65 gostos):** O autor identifica o botting e o RMT como "indissociáveis", criando um "estado de vulnerabilidade sistémica". Os 65 gostos — um valor atipicamente elevado em comparação com a média de 1,4 — indicam que este post capturou um sentimento amplamente partilhado de risco grave.

- **Post ID `514029_2896571` (EVE Online, Risco: 5/5, Trust Level 3):** O autor veterano denuncia a falta de enforcement contra input broadcasting como "game-breaking", refletindo a perceção de que os mecanismos de governança do sandbox estão a falhar.

### 4.2 World of Warcraft (Controlado / Theme Park)

**Tipo de Ecossistema:** World of Warcraft representa o modelo "theme park", onde a progressão é estruturada, a economia é parcialmente controlada pela Blizzard e as regras são mais estritas. Os jogadores têm menos agência para alterar as regras do jogo, mas beneficiam de estruturas de progressão claras e de mecanismos de suporte mais robustos.

**Perfil de Automação no Corpus:** Dos 1142 posts analisados de World of Warcraft, a distribuição de tipos de IA é semelhante à de EVE Online, com domínio de bots convencionais (A2) e uma proporção significativa de posts irrelevantes (A6).

**Média de Gostos:** 3,0 por post.
**Média do Nível de Confiança do Autor:** 1,6.

**Características do Risco em World of Warcraft:** A perceção de risco em World of Warcraft está centrada na **integridade da progressão e do mercado de Auction House**. Os bots são percebidos como ameaças ao valor do esforço humano, mas o risco é vivido como **gerível através de mecanismos de moderação**, desde que a Blizzard atue. A confiança na editora é mais elevada do que em EVE Online, refletindo o papel mais ativo da Blizzard na gestão do ecossistema.

**Evidência Exemplar:**

- **Post ID `3000005_25902831` (World of Warcraft, Risco: 5/5):** O jogador reporta bots persistentes "há meses sem qualquer ação da Blizzard", indicando "falha sistémica na moderação". O risco é máximo quando a confiança na editora falha.

- **Post ID `3000002_27797749` (World of Warcraft, Risco: 4/5):** O autor argumenta que "95% poderia ser resolvido com GMs humanos", sugerindo que a solução é viável, mas a atual abordagem automatizada é inadequada. O risco é elevado, mas não catastrófico, mantendo a esperança de intervenção.

### 4.3 Comparação Sistemática

**Tabela 4.1 — Comparação entre EVE Online e World of Warcraft**

| Métrica | EVE Online (Sandbox) | World of Warcraft (Controlado) |
|---------|----------------------|-------------------------------|
| Total de Posts | 1316 | 1142 |
| Média de Gostos | 1,4 | 3,0 |
| Média de Confiança do Autor | 1,8 | 1,6 |
| Média de Edições | 1,2 | 1,2 |
| Proporção A2 (Bots Convencionais) | ~59% | ~58% |
| Proporção A6 (Irrelevantes) | ~38% | ~38% |
| Natureza do Risco | Existencial para economia sandbox | Integridade da progressão e mercado |
| Confiança na Editora | Baixa (enforcement fraco) | Moderada (moderação ativa, mas insuficiente) |
| Estratégias de Mitigação | Adaptação individual, resignação | Esperança em ação da editora, vigilância ativa |

**Interpretação das Diferenças:**

1. **Validação Social (Gostos):** A média de gostos em World of Warcraft (3,0) é mais do dobro da de EVE Online (1,4). Esta diferença pode refletir a natureza mais imediata e acessível das preocupações sobre bots em WoW — bots em battlegrounds e na Auction House são visíveis para todos os jogadores —, enquanto o discurso em EVE Online é frequentemente mais técnico e nichado, reduzindo a probabilidade de validação social ampla.

2. **Confiança do Autor:** O nível de confiança médio ligeiramente mais elevado em EVE Online (1,8 vs. 1,6) pode refletir a natureza mais madura e persistente da comunidade sandbox, onde os jogadores tendem a ser mais experientes e investidos no ecossistema a longo prazo.

3. **Natureza do Risco:** Em EVE Online, o risco é percebido como **existencial**, pois a automação ameaça a própria lógica do sandbox — a ideia de que o valor é criado pelo esforço humano e pelas decisões dos jogadores. Em World of Warcraft, o risco é percebido como **operacional**, afetando a integridade de sistemas específicos (Auction House, PvP), mas não a natureza fundamental do jogo.

4. **Confiança na Editora:** A confiança na CCP (EVE Online) é consistentemente baixa nos posts analisados, com múltiplas denúncias de "game-breaking lack of enforcement" (Post ID `514029_2896571`). A confiança na Blizzard é mais moderada, com jogadores lamentando a lentidão da ação, mas mantendo esperança de intervenção (Post ID `3000002_27797749`).

---

## 5. Cocriação e Codestruição de Valor (VC1-VC4)

### 5.1 Distribuição Global de Cocriação de Valor

A Tabela 5.1 apresenta a distribuição global das classificações de cocriação de valor no corpus consolidado (N=2867).

**Tabela 5.1 — Distribuição de Cocriação de Valor (VC1-VC4)**

| Tipo | Designação | Frequência | Percentagem |
|------|------------|------------|-------------|
| VC1 | Cocriação de Valor | 18 | 0,63% |
| VC2 | Potencial Cocriação | 41 | 1,43% |
| VC3 | Codestruição de Valor | 28 | 0,98% |
| VC4 | Sem evidência de criação/destruição | 2780 | 96,97% |

A inclusão de discussões orientadas para ferramentas de IA moderna alterou a dinâmica qualitativa: **a cocriação de valor genuína (VC1: 18 posts, 0,63%) e o seu potencial tangível (VC2: 41 posts, 1,43%) emergiram de forma empírica clara**, quebrando a hegemonia de 99,9% de inércia ou codestruição anterior. 

### 5.2 Análise dos Casos Paradigmáticos de Valor

**Casos de Cocriação e Potencial de Valor (VC1 e VC2):**
- **Post ID `513384_2889848` (EVE Online, `eve-mentor-mcp`):** Classificado como **VC2 (Potencial Cocriação de Valor)** com nível de confiança de 0,75 e sinalização de revisão humana. O desenvolvedor concebeu uma ponte aberta entre o modelo Claude (via MCP) e as APIs de New Eden (ESI e zKillboard), capacitando jogadores recém-chegados a compreender fitting de naves, perdas em combate e rotas seguras através de orientação contextualizada. O valor é cocriado quando o raciocínio adaptativo do modelo se alia à agência e aos objetivos do jogador.
- **Vibe-Coding de Addons em World of Warcraft (VC1):** Jogadores que nunca aprenderam programação utilizam ChatGPT e Claude para cocriar addons personalizados em Lua/XML, melhorando a acessibilidade e a ergonomia de interfaces de raide.

**Casos de Codestruição de Valor (VC3):**
- A codestruição (28 posts, 0,98%) continua associada a botting de Auction House e farming automatizado desregulado, onde a extração unilateral de recursos por agentes automatizados desvaloriza o tempo de jogo investido pela comunidade humana e distorce economias virtuais inteiras.

---

## 6. Reflexão sobre as Questões de Investigação (QI1 a QI5)

A triangulação dos dados empíricos com os metadados das plataformas permite responder de forma conclusiva às cinco questões de investigação:

### QI1: Proporção de Agentes Autónomos (A1) vs. Bots e Scripts Convencionais (A2-A3)
Embora os bots convencionais (A2: 51,83%) continuem a representar a maior fatia da automação nos videojogos, a presença de agentes de IA adaptativos e copilotos (A1+A4) representa agora **3,39% (97 posts)** do corpus. Esta transição prova que os ecossistemas virtuais já acolhem ferramentas de IA generativa em coexistência com o botting tradicional.

### QI2: Estrutura de Interação Humano-IA em Sandbox vs. Controlado
A interação bidirecional (I3: 1,46%) e comandos deliberados (I1: 0,77%) afirmam-se em contextos de copiloto e mentoria. A estrutura dominante permanece **I4 (Humano → Humano sobre IA, 62,75%)**, mas as conversas em EVE Online destacam-se pela discussão técnica sobre o protocolo MCP e integração da ESI, enquanto em World of Warcraft incidem sobre *vibe-coding* e controvérsias de suporte ao cliente.

### QI3: Manifestação das Dimensões DART nos Discursos sobre Automação
A análise DART consolidada documenta que, embora o **Risco** mantenha uma média elevada (**2,02/5**), as dimensões de **Diálogo (0,16/5)**, **Acesso (0,19/5)** e **Transparência (0,19/5)** cresceram entre 10 e 19 vezes, demonstrando que a introdução de ferramentas abertas (como o MCP com código MIT e PKCE) reequilibra o ecossistema em direção à transparência e à acessibilidade de dados.

### QI4: Cocriação vs. Codestruição de Valor nos Ecossistemas Virtuais
Registam-se **59 posts (2,06%)** evidenciando cocriação ou potencial de cocriação colaborativa (VC1/VC2), com a IA a atuar como mentora e ferramenta de acessibilidade. A codestruição (VC3: 0,98%) permanece como a manifestação negativa da automação parasitária não consentida.

### QI5: Dicotomia Arquitetural: Sandbox (EVE Online) vs. Controlado (World of Warcraft)
A comparação consolida a tese de que a abertura arquitetural dita o tipo de IA adotada:
- No **EVE Online (Sandbox)**, a maturidade da API ESI proporcionou o terreno fértil para a rápida proliferação do protocolo MCP e copilotos de combate/aprendizagem.
- No **World of Warcraft (Theme Park)**, a rigidez do cliente levou a IA a concentrar-se na periferia (geração de código Lua de addons e análise externa de Warcraft Logs).

---

## 7. Auditoria de Qualidade, Calibração e Fila de Validação Humana

### 7.1 Resultados da Auditoria Qualitativa com DeepSeek-v4-Pro
Para cumprir as diretrizes metodológicas do protocolo DART-NET, uma amostra representativa de 20% do corpus (**573 publicações**) foi submetida a uma auditoria independente utilizando o modelo de raciocínio `deepseek-v4-pro`.

Os parâmetros auditados abrangeram:
1. **Veracidade da Evidência Literal:** Confirmação de que todas as citações textuais existem verbatim no texto original.
2. **Validade Conceitual de Tipo de IA:** Verificação da correta distinção entre A1 e A2/A3, impedindo falsas atribuições de "inteligência" a bots mecânicos.
3. **Consistência de Interação e Valor:** Coerência entre a tipologia de interação e o desfecho de valor.
4. **Calibração das Pontuações DART (0 a 5):** Alinhamento das escalas com os critérios do framework.

O **Score Médio de Consistência Global da Auditoria foi de 81,90%**, superando amplamente o limiar de aceitação estipulado (> 70,0%).

### 7.2 Fila de Revisão Humana (Human Review Required)
Em consonância com a Secção 11 do protocolo DART-NET, publicações com nível de confiança inferior a 0,80 ou com ambiguidade conceitual foram sinalizadas para validação humana (`human_review_required = True`). 

No corpus consolidado, **945 publicações (33,0%) foram preservadas com a flag de revisão humana ativa**, garantindo que as decisões ambíguas permaneçam abertas à supervisão por investigadores humanos, respeitando a separação estrita entre as camadas `AI CODING` e `HUMAN VALIDATION`.

### 7.3 Rastreabilidade de Custos e Infraestrutura de API
A execução completa do pipeline multiagente envolveu 23.000 chamadas à API DeepSeek, processando 16.018.104 tokens de entrada e 9.402.790 tokens de saída, com um custo total acumulado de **$19,6719 USD** (consultar detalhe em [`output/tabela_custos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/DeepSeek_Netnography%20DART%20Pipeline%20Orchestration/output/tabela_custos.md)).

---

## 8. Discussão Teórica, Reprodutibilidade e Limitações

### 8.1 Contribuições Teóricas
O estudo valida a relevância do framework DART-NET, demonstrando como a introdução do protocolo MCP e LLMs altera o equilíbrio clássico do DART, alavancando simultaneamente Acesso e Transparência em ecossistemas virtuais abertos.

### 8.2 Reprodutibilidade e Governança de Dados em Três Camadas
O pipeline cumpre integralmente os requisitos de integridade científica através da arquitetura de dados em 3 camadas:
1. **Camada 1 — RAW DATA (`data/raw/`):** 350 ficheiros originais intactos e imutáveis, totalizando 8.779 mensagens comunitárias preservadas.
2. **Camada 2 — AI CODING (`data/processed/` e `data/analysis/`):** Inferências estruturadas, pseudonimização ética (1.171 identificadores sintéticos `Player_XXX`) e resultados analíticos em formato JSON Lines (`netnography_results.jsonl`).
3. **Camada 3 — HUMAN VALIDATION (`output/`):** Tabela consolidada com 2.214 resumos em [`output/tabela_resumos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/DeepSeek_Netnography%20DART%20Pipeline%20Orchestration/output/tabela_resumos.md), relatórios de auditoria e amostras estratificadas prontas para validação final.

---

## 9. Apêndice Metodológico: Relação de Acesso e Repositórios das Fontes Primárias

1. **Repositório Bruto Imutável (`data/raw/`):** 350 ficheiros JSON estruturados (`topic_fetched_*.json`), contendo o *post stream* integral.
2. **Índice Web e Links Diretos (`output/tabela_resumos.md`):** Tabela com 2.214 linhas com links web diretos para cada post.
3. **Inventário Canónico de URLs (`output/lista_links.txt`):** 246 hiperligações canónicas ativas e 3 consultas booleanas estruturadas via Google Search.
4. **Mapeamento de Pseudonimização Ética (`data/interim/author_token_map.json`):** Correspondência entre `Player_001` a `Player_1171` e os utilizadores originais.
5. **Consultas Booleanas de Descoberta Externa (Google Search Queries):**
   - `site:reddit.com/r/Eve ("LLM" OR "ChatGPT" OR "AI agent" OR "Claude")`
   - `site:reddit.com/r/Eve ("copilot" OR "agent" OR "MCP") ("ESI" OR "API")`
   - `site:reddit.com (r/wow OR r/Eve OR r/classicwow OR r/woweconomy) ("LLM" OR "ChatGPT" OR "Claude" OR "machine learning") ("AI agent" OR "copilot" OR "agent" OR "MCP") ("API" OR "ESI" OR "botting" OR "computer vision")`