# Resumo Executivo: O Que Foi Feito Até Agora no Projeto DART-NET

Este documento sintetiza a evolução integral, metodológica e computacional do projeto de investigação científica:

> **Título da Investigação:** *Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos*  
> **Framework Teórica:** DART-NET v4.0 (alicerçada na Cocriação de Valor de Prahalad & Ramaswamy, 2004; Lógica do Serviço Dominante de Vargo & Lusch, 2016; Netnografia de Kozinets, 2020)  
> **Ecossistemas Empíricos:** *World of Warcraft* (Blizzard — Ambiente Controlado) e *EVE Online* (CCP Games — Sandbox Aberto)  
> **Recorte Temporal Rigoroso:** Janeiro de 2024 a Outubro de 2026 (`created_at >= '2024-01-01'`)  
> **Arquitetura Multiagente:** LLMs coordenados autonomamente (`deepseek-v4-flash` para codificação qualitativa; `deepseek-v4-pro` para auditoria cega de rigor científico; `TopicDiscussionAnalystAgent` para análise conversacional profunda).

---

## 1. Quadro Sinóptico da Evolução das Versões do Projeto e Walkthrough

Ao longo do desenvolvimento do estudo, a arquitetura metodológica atravessou seis grandes versões no controlo de versões (Git), refletindo cada uma um salto epistemológico e operacional:

| Versão | Commit Git | Data | Título do Marco | Foco Metodológico e Intervenções Técnicas | Volume Analítico | DART Médio Global | Auditoria e Validação |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: | :---: |
| **V1** | [`52e9984`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 09/09/2026 | **Reexecução Canónica DART-NET v3.0** | Unificação de 303 tópicos canónicos; filtro temporal $\ge$ Jan 2024; triagem de 1.032 posts únicos validados; primeira codificação DART-NET. | 1.032 posts | D: 0,88 \| A: 0,98<br/>R: 1,38 \| T: 1,09 | 84,41% (206 amostras) |
| **V2** | [`36c816b`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 10/09/2026 | **Parsing Guard & Resiliência Sintática** | Reparação determinística de 224 falhas de delimitador JSON na API DeepSeek (`extract_and_repair_json`); 0 erros residuais; autorrecuperação integrada. | 1.032 posts | D: 0,88 \| A: 0,98<br/>R: 1,38 \| T: 1,09 | **91,20%** (206 amostras) |
| **V3** | [`95f63e1`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 10/09/2026 | **Poda Metodológica Epistémica (Fase 3.5)** | Remoção atomizada de 207 posts de ruído (A6, zero DART e farming convencional); catálogo de exclusão em `excluded_posts_log.json`. | 825 posts refinados | D: 1,09 \| A: 1,20<br/>R: 1,61 \| T: 1,34 | **91,31%** (159 amostras) |
| **V4** | [`6bd0666`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 15/09/2026 | **Análise Agregada Preliminar (Fase 4.5)** | Implementação do `ThreadSynthesisAgent`; agrupamento preliminar dos 825 posts em 143 tópicos ativos (9 tópicos ficaram sem posts pós-poda). | 143 tópicos (825 posts) | D: 0,96 \| A: 1,29<br/>R: 1,56 \| T: 1,39 | **91,31%** (Auditado) |
| **V5** | [`0ac7111`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/resumos_discussoes_topicos.md) | 14/10/2026 | **Análise Conversacional & Deteção de Sátira** | Implementação do `TopicDiscussionAnalystAgent`; reintegração dos posts para restaurar os diálogos completos; expansão para **152 tópicos ativos** e **1.032 posts** em `netnography_results.jsonl`; deteção de sátira/ironia em 308 posts. | **152 tópicos** (1.032 posts) | D: 0,93 \| A: 1,06<br/>R: 1,51 \| T: 1,16 | Mapeamento de Sátira em 100 Tópicos |
| **V6** *(Atual)* | [`6ef6689`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/Protocolo_Auditoria_Humana_Formatado.xlsx) | 29/10/2026 | **DART-NET v4.0: Embedded Multilevel Design & Auditoria Humana Track B em 2 Blocos** | Formalização do Tópico ($N=152$) como Unidade Primária de Análise e Teorização e do Post ($N=1.032$) como Ancoragem Verbatim e Contraste Crítico (resolução da diluição atómica); remoção de `Track_A_Posts`; auditoria humana em duplo-cego expandida para **30 tópicos e 355 posts constituintes** (Bloco 1: JPaulo & Emmanoel; Bloco 2: Roger & Gomide). | **152 tópicos** (1.032 posts ativos) | Nível Meso: D: 1,2 \| A: 1,5<br/>R: 1,6 \| T: 1,5 | **Convergência Inter-Auditores: $\kappa=0,916$ / $\kappa=1,00$** |

---

## 2. Detalhe da Evolução Metodológica: O Que Foi Feito em Cada Fase

### Fase 1: Reexecução Canónica com Filtro Temporal Estrito (Walkthrough V1)
* **Objetivo:** Refazer o estudo netnográfico garantindo purificação temporal total ($\ge$ Jan 2024), unificando as tipologias A1–A5 com termos booleanos de IA generativa moderna (`LLM`, `ChatGPT`, `Claude`, `Copilot`, `MCP`, `machine learning`, etc.).
* **Ações Executadas:**
  1. Consolidação do catálogo canónico de **303 discussões únicas** em [`data/target_corpus_303.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/target_corpus_303.json) e [`output/lista_links.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.md).
  2. Ingestão em bruto de 8.999 mensagens via scrapers especializados (`ScraperAgent`) para Discourse (WoW e EVE), Reddit (Arctic Shift API) e Steam Community.
  3. Aplicação do filtro temporal rígido `created_at >= '2024-01-01T00:00:00Z'` e eliminação de mensagens com $< 50$ carateres, resultando em 6.485 posts elegíveis.
  4. Triagem semântica via `SemanticValidatorAgent` e pseudonimização ética via `AnonymizerAgent` (`Player_0001` a `Player_1032`), gerando **1.032 posts validados únicos**.
  5. Codificação qualitativa multiagente com `NetnographerAgent` sob a taxonomia DART-NET (`A1–A6`, `I1–I6`, `VC1–VC4`, `DART`).
  6. Primeira auditoria cega independente pelo `QualityGuardAgent` (amostra de 206 posts), obtendo **84,41%** de consistência inicial.

---

### Fase 2: Parsing Guard, Resiliência Sintática e Reprocessamento (Walkthrough V2)
* **Objetivo:** Resolver falhas pontuais de delimitador e truncamento JSON ocorridas na inferência em larga escala da API DeepSeek, garantindo resiliência e integridade a 100% dos registos.
* **Ações Executadas:**
  1. Diagnóstico de 224 posts afetados por formatação Markdown inconsistente da API.
  2. Construção do módulo **Parsing Guard** com motor de extração e reparação recursiva de JSON (`extract_and_repair_json`) e controlo estrito de payload no prompt ($\le 8.000$ carateres).
  3. Reprocessamento determinístico através do script `scratch/reprocess_parsing_failures.py`, alcançando **zero erros residuais** no universo de 1.032 análises.
  4. Reauditoria científica cega (`QualityGuardAgent`) da amostra atualizada:
     * O score médio de consistência qualitativa subiu de 84,41% para **91,20%**;
     * Os casos com alertas foram reduzidos de 31 para apenas 12;
     * Veracidade literal de citações atingiu 100% (ausência total de alucinações).

---

### Fase 3: O Experimento da Poda Metodológica Atomizada (Walkthrough V3 — Fase 3.5)
* **Objetivo:** Testar se a remoção de ruído atomizado e mensagens desprovidas de DART clarificava a perceção de valor ao nível do post individual.
* **Ações Executadas:**
  1. Criação do script determinístico [`scratch/prune_dataset_methodological.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/scratch/prune_dataset_methodological.py) e aplicação de 3 critérios de exclusão:
     * **Critério 1 — Categoria A6 ("Não-IA / Ruído Residual")**: 51 posts eliminados;
     * **Critério 2 — Posts com "Zero DART" (D=0, A=0, R=0, T=0)**: 172 posts eliminados (48 partilhados com A6);
     * **Critério 3 — Queixas Antigas de Bots Mecânicos em A2**: 33 posts eliminados.
  2. **Registo de Auditoria**: Criação do ficheiro [`data/analysis/excluded_posts_log.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/excluded_posts_log.json) catalogando os 207 posts excluídos e backup do ficheiro não podado em [`data/analysis/netnography_results_1032_unpruned.jsonl`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/netnography_results_1032_unpruned.jsonl).
  3. **Descoberta Crítica**: Mesmo após expurgar 207 posts e reter apenas **825 posts refinados**, a neutralidade isolada (`VC4`) continuava massiva (**77,2%**), demonstrando empiricamente que a atomização do post gera uma distorção analítica incontornável ("Falácia da Diluição Atómica").

---

### Fase 4: Análise Agregada Preliminar ao Nível de Tópicos (Walkthrough V4 — Fase 4.5)
* **Objetivo:** Elevar a unidade de análise da granularidade atómica de posts para a agregação ao nível de tópicos de discussão (*threads*).
* **Ações Executadas:**
  1. Execução do `ThreadSynthesisAgent` sobre os 825 posts da Fase 3.5.
  2. Identificação de uma limitação estrutural da poda: **9 tópicos de discussão ficaram com 0 posts retidos** (como o tópico `481937` *"A win for bots?"* em EVE Online, cujos únicos 2 posts tinham sido classificados como queixa A2 e réplica A5), reduzindo artificialmente o universo para **143 tópicos**.
  3. Elaboração da tipologia preliminar em 5 clusters temáticos e constatação de que a amputação de turnos conversacionais impedia a compreensão do ciclo dialético completo.

---

### Fase 5: Análise Profunda de Discussões, Deteção de Sátira e Reintegração dos 1.032 Posts (Walkthrough V5 — Commit `0ac7111`)
* **Objetivo:** Recuperar a integridade conversacional de todo o ecossistema, permitindo analisar discussões completas sem perda de turnos de fala e descodificar marcadores de ironia e sátira comunitária.
* **Ações Executadas:**
  1. Criação e execução do **`TopicDiscussionAnalystAgent`** ([`agents/topic_discussion_analyst_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/topic_discussion_analyst_agent.py)), gerando análises extensas e contínuas em [`output/resumos_discussoes_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/resumos_discussoes_topicos.md) (4.877 linhas) e [`data/analysis/topic_discussions_insights.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/topic_discussions_insights.json).
  2. **Reintegração Conversacional Integral**:
     * Para que nenhuma discussão ficasse mutilada, o ficheiro ativo [`data/analysis/netnography_results.jsonl`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/netnography_results.jsonl) foi reunificado com a totalidade dos **1.032 posts validados**, restaurando os 9 tópicos anteriormente excluídos e estabilizando a base em **152 tópicos ativos de discussão** (65 em EVE Online e 87 em World of Warcraft) em [`data/analysis/thread_level_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/thread_level_results.json).
     * Refatoração do `SummaryTableGenerator` para atualizar [`output/tabela_resumos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_resumos.md) com todas as **1.032 mensagens** (1.034 linhas na tabela) e sinalização explícita de `[Sátira/Ironia]` e `[Humor/Piada]` em 308 posts.

---

### Fase 6: Framework DART-NET v4.0 e Auditoria Humana Track B Unificada (Walkthrough V6 — Atual)
* **Objetivo:** Formalizar a **Arquitetura Metodológica Multinível Incorporada (*Embedded Multilevel Design*)**, estabelecer o **Tópico de Discussão ($N=152$)** como Unidade Primária de Análise, Sentido e Teorização e o **Post ($N=1.032$)** como Ancoragem Verbatim Forense, implementando um protocolo de auditoria humana em duplo-cego independente.
* **Ações Executadas:**
  1. **Remoção de `Track_A_Posts`**: A auditoria isolada de posts foi permanentemente eliminada, unificando a avaliação humana no nível Meso (o Tópico) com os posts constituintes integrados como evidência literal (*verbatim grounding*).
  2. **Desenho em Dois Blocos Independentes no Excel ([`output/Protocolo_Auditoria_Humana_Formatado.xlsx`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/Protocolo_Auditoria_Humana_Formatado.xlsx))**:
     * **Bloco 1 (Prof. JPaulo & Prof. Emmanoel)**: 15 tópicos estratificados e os seus 104 posts constituintes, calibrados em duas rondas com concordância quase perfeita ($\kappa = 0,916$ em clusters temáticos e $\kappa = 1,00$ em valor relacional);
     * **Bloco 2 (Prof. Roger & Prof. Gomide)**: 15 novas discussões estratificadas (3 por cluster nos dois jogos) e os seus 251 posts constituintes, estruturadas com dados empíricos preenchidos e colunas limpas para votação em duplo-cego independente;
     * **Total Consolidado da Auditoria**: **30 discussões completas** (~20% do corpus de 152 tópicos) e **355 posts constituintes** (34,4% dos 1.032 posts ativos / 43,0% do corte refinado de 825 posts).
  3. **Formalização Teórica da Falácia da Diluição Atómica**: Comprovação de que, enquanto a leitura de posts isolados sugere 77,2% a 78,9% de neutralidade inerte (`VC4`), a dinâmica conversacional dos 152 tópicos revela que **48,7% das discussões produzem impacto ativo de valor** (12,5% cocriação efetiva `VC1`, 13,8% potencial `VC2` e 22,4% codestruição `VC3`).

---

## 3. Principais Descobertas Científicas e Metodológicas Acumuladas

1. **A Superação da Falácia da Diluição Atómica (Contributo Metodológico Central)**:
   A unidade de sentido em comunidades online é o **tópico de discussão** e não o post atómico. Ao avaliar conversas completas, o impacto real de cocriação e codestruição de valor salta de 3,2% para 48,7%, provando que métodos ingénuos de NLP baseados em posts isolados produzem imagens artificialmente estéreis dos ecossistemas digitais.
2. **A Dimensão Hegemónica do Risco no Discurso dos Jogadores**:
   Em ambos os videojogos, o **Risco Percebido ($R=1,61$)** é a dimensão mais saliente. Em *EVE*, o risco é financeiro, tático e de perda de ativos na economia aberta (*full-loot*); em *WoW*, o risco é ético, de perda de identidade comunitária e de injustiça por moderação automatizada.
3. **O Papel Determinístico da Arquitetura do Jogo na Cocriação de Valor**:
   A infraestrutura de dados abertos de *EVE* (APIs ESI e suporte a Model Context Protocol — MCP) canaliza os jogadores para a cocriação tangível de software e copilotos (`A1/A4/VC1`), enquanto a arquitetura fechada de *WoW* canaliza a agência dos jogadores para a contestação normativa de riscos (`A5/VC3`).
4. **Emergência do Fenómeno do *Vibe-Coding* nos Jogos**:
   Identificou-se uma vaga expressiva de jogadores (Cluster 5, ~25% dos tópicos) que recorrem a LLMs (Claude Code, ChatGPT) para programar addons complexos em Lua e ferramentas de mercado sem formação prévia em engenharia de software, desencadeando debates sobre qualidade de código e autoria comunitária.
5. **Resistência Comunitária à Substituição Social**:
   Tanto em funcionalidades oficiais (*Follower Dungeons* em WoW) como em companheiros com IA (*Aura* em EVE), a comunidade aceita a IA como muleta de acessibilidade, mas resiste categoricamente à substituição da socialização humana em atividades de prestígio.

---

## 4. Inventário Geral dos Entregáveis no Repositório

Todos os artefactos produzidos ao longo do projeto encontram-se consolidados, validados e versionados no Git:

### A. Livro de Cálculo e Protocolo de Auditoria Humana (`output/`)
- [`output/Protocolo_Auditoria_Humana_Formatado.xlsx`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/Protocolo_Auditoria_Humana_Formatado.xlsx): Livro de cálculo com **7 folhas integradas** contendo as instruções metodológicas, exemplos canónicos, o Bloco 1 calibrado (15 tópicos / 104 posts; Prof. JPaulo & Prof. Emmanoel) e o Bloco 2 para duplo-cego (15 tópicos / 251 posts; Prof. Roger & Prof. Gomide).
- [`output/Protocolo_Auditoria_Humana_Formatado_JPaulo.xlsx`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/Protocolo_Auditoria_Humana_Formatado_JPaulo.xlsx): Cópia personalizada de auditoria do investigador principal.

### B. Relatórios Analíticos e Sínteses Académicas (`output/`)
- [`output/relatorio_netnografia.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/relatorio_netnografia.md): Relatório científico completo formalizando a framework **DART-NET v4.0**, com a resposta substantiva às 3 Macro-Questões de Investigação (QI1 a QI3), contraste micro vs. meso, fundamentação teórica e tabelas consolidadas da Track B.
- [`output/analise_agregada_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/analise_agregada_topicos.md): Análise agregada dos **152 tópicos ativos de discussão** (65 em EVE e 87 em WoW), catálogo de fichas sistemáticas e macro-síntese transversal.
- [`output/resumos_discussoes_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/resumos_discussoes_topicos.md): Documento de 4.877 linhas com resumos analíticos densos e descodificação de ironia/sátira em todos os 152 tópicos.
- [`output/tabela_resumos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_resumos.md): Matriz de dados com **1.032 posts** (1.034 linhas na tabela), classificações, resumos ($\le 50$ palavras), temas e tags contextuais de sátira/humor.
- [`output/planos_implementacao_consolidados.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/planos_implementacao_consolidados.md): Compilação histórica dos planos de implementação executados.
- [`output/leitura_netnography_results.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/leitura_netnography_results.md): Relatório legível das fichas analíticas detalhadas de codificação dos posts.
- [`output/leitura_quality_audit_results.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/leitura_quality_audit_results.md): Relatório legível da auditoria cega independente do `QualityGuardAgent`.
- [`output/fluxograma_implementacao.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/fluxograma_implementacao.md) e [`output/visualizar_fluxograma.html`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/visualizar_fluxograma.html): Diagrama arquitetural completo e visualizador HTML interativo.
- [`output/lista_links.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.md) e [`output/lista_links.txt`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.txt): Catálogo unificado das 303 URLs canónicas.
- [`output/tabela_custos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_custos.md): Auditoria financeira com registo de ~27.000 chamadas de API com custo total de ~$21,50 USD.

### C. Datasets Estruturados (`data/analysis/` e `data/processed/`)
- [`data/analysis/thread_level_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/thread_level_results.json): Dataset principal estruturado contendo as variáveis agregadas, vetores DART, perfis e resumos dos **152 tópicos ativos de discussão**.
- [`data/analysis/netnography_results.jsonl`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/netnography_results.jsonl): Dataset ativo contendo os **1.032 posts validados** que constituem os turnos conversacionais dos 152 tópicos.
- [`data/analysis/netnography_results_1032_unpruned.jsonl`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/netnography_results_1032_unpruned.jsonl): Cópia canónica original de segurança dos 1.032 posts.
- [`data/analysis/excluded_posts_log.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/excluded_posts_log.json): Registo de auditoria dos 207 posts avaliados no experimento preliminar de poda da Fase 3.5.
- [`data/analysis/topic_discussions_insights.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/topic_discussions_insights.json): Insights de discussão e mapeamento de sátira/ironia em 152 tópicos.
- [`data/analysis/quality_audit_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/quality_audit_results.json): Registo das auditorias cegas realizadas com consistência de 91,31%.
- [`data/processed/anonymized_posts.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/processed/anonymized_posts.json): Posts com texto integral e anonimização ética.
- [`data/target_corpus_303.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/target_corpus_303.json): Inventário JSON com as 303 URLs e metadados.

### D. Módulos da Pipeline Multiagente (`agents/`)
- [`agents/topic_discussion_analyst_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/topic_discussion_analyst_agent.py): Agente de análise conversacional profunda, síntese ilimitada e deteção contextual de sátira em 152 tópicos.
- [`agents/thread_synthesis_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/thread_synthesis_agent.py): Agente de agregação ao nível de tópicos e geração de fichas DART.
- [`agents/netnography_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/netnography_agent.py): Agente de codificação qualitativa com módulo *Parsing Guard* integrado.
- [`agents/quality_guard_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/quality_guard_agent.py): Auditor independente cego baseado no modelo `deepseek-v4-pro`.
- [`agents/semantic_validator_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/semantic_validator_agent.py): Triagem semântica de mensagens brutas com base em léxico expandido.
- [`agents/anonymizer_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/anonymizer_agent.py): Pseudonimização ética e proteção de dados pessoais (PII).
- [`agents/scraper_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/scraper_agent.py): Ingestão automatizada de mensagens nas plataformas Discourse, Reddit e Steam.
- [`agents/synthesis_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/synthesis_agent.py): Síntese académica e redação das respostas às Questões de Investigação.
