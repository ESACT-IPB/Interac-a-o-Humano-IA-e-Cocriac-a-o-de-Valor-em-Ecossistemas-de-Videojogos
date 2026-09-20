# Resumo Executivo: O Que Foi Feito Até Agora no Projeto DART-NET

Este documento sintetiza a evolução integral, metodológica e computacional do projeto de investigação científica:

> **Título da Investigação:** *Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos*  
> **Framework Teórica:** DART-NET 2026 (alicerçada na Cocriação de Valor de Prahalad & Ramaswamy, 2004; Lógica do Serviço Dominante de Vargo & Lusch, 2004; Netnografia de Kozinets, 2020)  
> **Ecossistemas Empíricos:** *World of Warcraft* (Blizzard — Ambiente Controlado) e *EVE Online* (CCP Games — Sandbox Aberto)  
> **Recorte Temporal Rigoroso:** Janeiro de 2024 a Setembro de 2026 (`created_at >= '2024-01-01'`)  
> **Arquitetura Multiagente:** LLMs coordenados autonomamente (`deepseek-v4-flash` para codificação qualitativa; `deepseek-v4-pro` para auditoria cega de rigor científico).

---

## 1. Quadro Sinóptico da Evolução das Quatro Versões do Walkthrough

Ao longo do desenvolvimento do estudo, o documento **`walkthrough.md`** atravessou quatro grandes versões no controlo de versões (Git), refletindo cada uma um marco metodológico decisivo:

| Versão | Commit Git | Data / Hora | Título do Marco | Foco Metodológico e Intervenções Técnicas | Volume Analítico | DART Médio Global | Auditoria de Qualidade |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: | :---: |
| **V1** | [`52e9984`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 09/09/2026 *(17:44)* | **Reexecução Canónica DART-NET v3.0** | Unificação de 303 tópicos canónicos; aplicação do filtro temporal rigoroso $\ge$ Jan 2024; ingestão de 8.999 mensagens brutas e triagem de 1.032 posts; primeira codificação DART-NET. | 1.032 posts | D: 0,88 \| A: 0,98<br/>R: 1,38 \| T: 1,09 | 84,41% (206 amostras) |
| **V2** | [`36c816b`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 10/09/2026 *(15:41)* | **Parsing Guard & Resiliência Sintática** | Reparação determinística de 224 falhas de delimitador/parsing da API DeepSeek (`extract_and_repair_json`); 0 erros residuais; autorrecuperação integrada no fluxograma. | 1.032 posts | D: 0,88 \| A: 0,98<br/>R: 1,38 \| T: 1,09 | **91,20%** (206 amostras) |
| **V3** | [`95f63e1`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 10/09/2026 *(16:37)* | **Poda Metodológica Epistémica (Fase 3.5)** | Remoção de ruído Não-IA (A6), posts "Zero DART" e queixas de bots mecânicos (207 posts excluídos com log auditável); salvaguarda do corpus original; médias DART todas $> 1,0$. | **825 posts refinados** | D: 1,09 \| A: 1,20<br/>R: 1,61 \| T: 1,34 | **91,31%** (159 amostras) |
| **V4** *(Atual)* | [`6bd0666`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md) | 15/09/2026 *(16:05)* | **Análise Agregada de Tópicos (Fase 4.5)** | Implementação do `ThreadSynthesisAgent`; agregação dos 825 posts em 143 tópicos ativos; catálogo de 143 fichas sistemáticas; macro-síntese transversal Sandbox vs. Controlado. | **143 tópicos** (825 posts) | D: 0,96 \| A: 1,29<br/>R: 1,56 \| T: 1,39 | **91,31%** (Auditado) |

---

## 2. Detalhe da Evolução Metodológica: O Que Foi Feito em Cada Fase

### Fase 1: Reexecução Canónica com Filtro Temporal Estrito (Walkthrough V1)
* **Objetivo:** Refazer o estudo netnográfico garantindo purificação temporal total, unificando os tópicos curados das tipologias A1–A5 com os resultados de uma consulta booleana avançada de IA generativa (`LLM`, `ChatGPT`, `Claude`, `Copilot`, `MCP`, `machine learning`, etc.).
* **Ações Executadas:**
  1. Consolidação do catálogo canónico de **303 discussões únicas** em [`data/target_corpus_303.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/target_corpus_303.json) e [`output/lista_links.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.md).
  2. Ingestão em bruto de 8.999 mensagens através de scrapers especializados (`ScraperAgent`) para Discourse (WoW e EVE), Reddit (via Arctic Shift API) e Steam Community.
  3. Aplicação do filtro temporal rígido `created_at >= '2024-01-01T00:00:00Z'` e eliminação de mensagens com $< 50$ carateres, resultando em 6.485 posts elegíveis.
  4. Triagem semântica via `SemanticValidatorAgent` e pseudonimização ética via `AnonymizerAgent` (`Player_0001` a `Player_1032`), gerando **1.032 posts validados únicos**.
  5. Codificação qualitativa multiagente com `NetnographerAgent` sob a taxonomia DART-NET:
     * Tipologia de IA: A1 a A6;
     * Estrutura de Interação: I1 a I6;
     * Tipologia de Valor: VC1 a VC4;
     * Escores DART: Diálogo, Acesso, Risco e Transparência (escala 0 a 5);
     * Sinalização de revisão humana (`human_review_required: true` para confiança $< 0,80$).
  6. Primeira auditoria cega independente pelo `QualityGuardAgent` (amostra de 206 posts), obtendo **84,41%** de consistência inicial.

---

### Fase 2: Parsing Guard, Resiliência Sintática e Reprocessamento (Walkthrough V2)
* **Objetivo:** Resolver falhas pontuais de delimitador e truncamento JSON ocorridas na inferência em larga escala da API DeepSeek, garantindo resiliência e integridade a 100% dos registos.
* **Ações Executadas:**
  1. Diagnóstico de 224 posts afetados por formatação Markdown inconsistente da API (`Processing error encountered`).
  2. Construção do módulo **Parsing Guard** com motor de extração e reparação recursiva de JSON (`extract_and_repair_json`) e controlo estrito de payload no prompt ($\le 8.000$ carateres).
  3. Reprocessamento determinístico através do script `scratch/reprocess_parsing_failures.py`, alcançando **zero erros residuais** no universo de 1.032 análises.
  4. Reauditoria científica cega (`QualityGuardAgent`) da amostra atualizada:
     * O score médio de consistência qualitativa subiu de 84,41% para **91,20%**;
     * Os casos com alertas foram reduzidos de 31 para apenas 12;
     * Veracidade literal de citações atingiu 100% (ausência total de alucinações).
  5. Integração formal do ciclo de autorrecuperação (*self-healing loop*) no fluxograma arquitetural.

---

### Fase 3: Poda Metodológica e Refinamento Epistémico (Walkthrough V3 — Fase 3.5)
* **Objetivo:** Eliminar dados espúrios e pré-paradigmáticos sem relevância para a cocriação de valor humano-IA, elevando a validade interna do estudo conforme preconizado por Prahalad & Ramaswamy (2004) e Kozinets (2020).
* **Ações Executadas:**
  1. Criação do script determinístico [`scratch/prune_dataset_methodological.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/scratch/prune_dataset_methodological.py) e aplicação de 3 critérios de exclusão:
     * **Critério 1 — Categoria A6 ("Não-IA / Ruído Residual")**: 51 posts eliminados (discussões periféricas de jogabilidade padrão sem menção a IA);
     * **Critério 2 — Posts com "Zero DART" (D=0, A=0, R=0, T=0)**: 172 posts eliminados (48 partilhados com A6), por manifestarem ausência total de experiência agêntica ou cocriação;
     * **Critério 3 — Queixas Antigas de Bots Mecânicos / Farming Tradicional em A2**: 33 posts eliminados (queixas genéricas de bots de pesca ou RMT dos anos 2000 sem relevância para IA generativa/adaptativa moderna).
  2. **Salvaguarda Integral e Rastreabilidade**:
     * O dataset original de 1.032 posts foi preservado intacto em [`data/analysis/netnography_results_1032_unpruned.jsonl`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/netnography_results_1032_unpruned.jsonl);
     * Foi gerado o ficheiro de auditoria [`data/analysis/excluded_posts_log.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/excluded_posts_log.json) catalogando cada um dos 207 posts excluídos com os respetivos motivos;
     * Preservação integral de 100% dos Agentes Autónomos (**A1: 95 posts**), Copilotos Humanos (**A4: 59 posts**) e episódios de Cocriação Efetiva (**VC1: 26 posts**) e Potencial (**VC2: 72 posts**).
  3. **Consolidação do Corpus Refinado de 825 Posts**:
     * As médias dimensionais DART passaram todas a superar 1,0: Diálogo: **`1,09`** (+23,9%); Acesso: **`1,20`** (+22,4%); Risco: **`1,61`** (+16,7%); Transparência: **`1,34`** (+22,9%);
     * As discussões refletindo impacto ativo de valor (VC1 + VC2 + VC3) duplicaram de 11,4% para **22,8%** (188 posts);
     * A auditoria cega reajustou-se para **91,31% de consistência média** (159 amostras; apenas 8 alertas contextuais).
  4. Redação da **Secção 1.5** no relatório científico ([`output/relatorio_netnografia.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/relatorio_netnografia.md)) com a justificação epistémica detalhada de cada exclusão e recálculo de todas as tabelas downstream.

---

### Fase 4: Análise Agregada ao Nível de Tópicos e Evolução DART-NET v3.6 (Walkthrough V4 — Atual)
* **Objetivo:** Elevar a unidade de análise da granularidade atómica de posts para a **agregação ao nível de tópicos de discussão (*threads*)**, capturando o ciclo de vida deliberativo, as controvérsias coletivas e as dinâmicas sociotécnicas entre *EVE Online* (Sandbox) e *World of Warcraft* (Controlado).
* **Ações Executadas:**
  1. Criação e execução do **`ThreadSynthesisAgent`** ([`agents/thread_synthesis_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/thread_synthesis_agent.py)).
  2. Agrupamento dos 825 posts validados em exatamente **143 tópicos ativos de discussão** (excluindo tópicos que ficaram com 0 posts retidos pós-poda):
     * **World of Warcraft**: **84 tópicos** (521 posts | média de `6,20` posts/tópico);
     * **EVE Online**: **59 tópicos** (304 posts | média de `5,15` posts/tópico).
  3. Geração do catálogo exaustivo de **143 fichas sistemáticas estruturadas**, contendo metadados de volume (retidos/originais), perfis dominantes de agência (`A1–A5`) e interação (`I1–I5`), médias dimensionais DART, dinâmica de valor dominante (`VC1–VC4`), resumos analíticos densos (4–5 linhas) e citações literais paradigmáticas.
  4. Elaboração da **Macro-Síntese Transversal**:
     * **Tabela Comparativa Global por Ecossistema**: Demonstra que *EVE Online* apresenta índices de Acesso (`1,48`) e Transparência (`1,49`) muito superiores a *WoW* (`A: 1,17`, `T: 1,32`), enquanto *World of Warcraft* exibe maior índice de codestruição de valor e atrito institucional (VC3: `26,2%` em WoW vs. `13,6%` em EVE);
     * **Tipologia Emergente em 5 Clusters**:
       1. *Cluster 1: Ferramentas Externas, Integração de APIs e MCP* (31 tópicos | 21,7%);
       2. *Cluster 2: Fair Play, Deteção Algorítmica e Integridade no PvP* (29 tópicos | 20,3%);
       3. *Cluster 3: Suporte ao Cliente, Moderação Automatizada e Banning* (26 tópicos | 18,2%);
       4. *Cluster 4: Agentes Oficiais In-Game e Masmorras de Seguidores* (20 tópicos | 14,0%);
       5. *Cluster 5: Copilotos de Desenvolvimento, Addons e Vibe-Coding* (37 tópicos | 25,9%).
     * **Ensaio Transversal Sandbox vs. Controlado**: Análise de como a governança algorítmica aberta (ESI/MCP em EVE) canaliza a comunidade para a cocriação tangível de ferramentas (`A1/A4/I3/VC1`), ao passo que ambientes fechados e controlados (*WoW*) direcionam a agência dos jogadores para a contestação normativa de riscos (`A5/I4/VC3`).
  5. Publicação do relatório consolidado [`output/analise_agregada_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/analise_agregada_topicos.md), do dataset [`data/analysis/thread_level_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/thread_level_results.json), e atualização do fluxograma de implementação.

---

## 3. Principais Descobertas Científicas Acumuladas

1. **A Dimensão Hegemónica do Risco no Discurso dos Jogadores**:
   Em ambos os videojogos, o **Risco Percebido ($R=1,61$)** é a dimensão mais saliente. Contudo, a natureza do risco difere substancialmente: em *EVE*, o risco é primariamente operacional e de perda de ativos na economia aberta (*full-loot*); em *WoW*, o risco é ético, de perda de identidade social e de punição injusta por sistemas automatizados de moderação.
2. **O Papel Determinístico da Arquitetura do Jogo na Cocriação de Valor**:
   O contraste entre a sandbox aberta de *EVE* (com APIs públicas ESI e suporte comunitário a MCP) e o ambiente regulado de *WoW* prova que a disponibilidade de infraestruturas de dados públicas dita a transição da comunidade de simples debate reativo (A5) para a cocriação ativa de ferramentas e agentes copilotos (A1/A4).
3. **Emergência do Fenómeno do *Vibe-Coding* nos Jogos**:
   Identificou-se uma vaga substancial de jogadores casuais e semi-técnicos (Cluster 5, 25,9% dos tópicos) que recorrem a assistentes LLM (Claude, ChatGPT) para programar addons complexos em Lua e ferramentas analíticas em Python sem formação prévia em engenharia de software, democratizando a cocriação de valor.
4. **Resistência Comunitária à Substituição Social**:
   Tanto em funcionalidades oficiais (*Follower Dungeons* em WoW) como em companheiros com IA (*Aura* em EVE), a comunidade aceita a IA como muleta de acessibilidade ou ferramenta assíncrona, mas resiste energicamente à substituição da interação humana em instâncias de prestígio social e liderança de guildas.

---

## 4. Inventário Geral dos Entregáveis no Repositório

Todos os artefactos produzidos ao longo destas fases encontram-se consolidados, validados e versionados no Git:

### A. Relatórios Analíticos e Sínteses Académicas (`output/`)
- [`output/analise_agregada_topicos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/analise_agregada_topicos.md): Análise agregada dos **143 tópicos ativos**, catálogo de 143 fichas DART e macro-síntese transversal.
- [`output/relatorio_netnografia.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/relatorio_netnografia.md): Relatório científico completo com fundamentação das 3 Macro-Questões de Investigação (QI1 a QI3 e subquestões a/b), abordagem multinível e Secção 1.5 sobre a poda metodológica.
- [`output/planos_implementacao_consolidados.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/planos_implementacao_consolidados.md): Compilação histórica exaustiva dos 5 planos de implementação executados no projeto.
- [`output/tabela_resumos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_resumos.md): Matriz de dados com exatamente **825 linhas ativas**, classificações, resumos ($\le$ 50 palavras), temas ($\le$ 8 palavras) e links diretos.
- [`output/leitura_netnography_results.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/leitura_netnography_results.md): Relatório legível com as 825 fichas analíticas detalhadas do corpus.
- [`output/leitura_quality_audit_results.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/leitura_quality_audit_results.md): Relatório legível da auditoria cega com as 159 análises do `QualityGuardAgent`.
- [`output/fluxograma_implementacao.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/fluxograma_implementacao.md) e [`output/visualizar_fluxograma.html`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/visualizar_fluxograma.html): Fluxograma arquitetural completo e visualizador HTML interativo (zoom/pan) atualizados com a Fase 4.5.
- [`output/lista_links.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.md) e [`output/lista_links.txt`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.txt): Catálogo unificado das 303 discussões canónicas por comunidade e índice temático A1 a A5.
- [`output/tabela_custos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_custos.md): Auditoria financeira com registo de ~27.000 chamadas de API com custo total de **~$21,50 USD**.
- [`output/walkthrough.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/walkthrough.md): O registo canónico e atualizado do projeto na versão DART-NET v3.6.

### B. Datasets e Ficheiros de Análise (`data/analysis/` e `data/processed/`)
- [`data/analysis/thread_level_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/thread_level_results.json): Dataset estruturado com as variáveis agregadas dos **143 tópicos ativos**.
- [`data/analysis/netnography_results.jsonl`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/netnography_results.jsonl): Dataset ativo purificado de **825 posts validados**.
- [`data/analysis/netnography_results_1032_unpruned.jsonl`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/netnography_results_1032_unpruned.jsonl): Backup canónico do corpus não podado de 1.032 posts.
- [`data/analysis/excluded_posts_log.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/excluded_posts_log.json): Registo de auditoria detalhado dos 207 posts excluídos com os respetivos motivos.
- [`data/analysis/quality_audit_results.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/analysis/quality_audit_results.json): Registo das 159 auditorias cegas realizadas com consistência de 91,31%.
- [`data/processed/anonymized_posts.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/processed/anonymized_posts.json): Posts com texto integral e anonimização de identificadores de utilizadores.
- [`data/target_corpus_303.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/target_corpus_303.json): Inventário JSON com as 303 URLs e metadados dos tópicos canónicos.

### C. Módulos da Pipeline Multiagente (`agents/`)
- [`agents/thread_synthesis_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/thread_synthesis_agent.py): Agente de agregação ao nível de tópicos e geração de fichas DART.
- [`agents/netnography_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/netnography_agent.py): Agente de codificação qualitativa DART-NET com módulo *Parsing Guard* integrado.
- [`agents/quality_guard_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/quality_guard_agent.py): Auditor independente cego baseado no modelo `deepseek-v4-pro`.
- [`agents/semantic_validator_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/semantic_validator_agent.py): Triagem semântica de mensagens brutas com base em léxico expandido.
- [`agents/anonymizer_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/anonymizer_agent.py): Pseudonimização ética e proteção de dados pessoais (PII).
- [`agents/scraper_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/scraper_agent.py): Ingestão automatizada de mensagens nas plataformas Discourse, Reddit e Steam.
- [`agents/synthesis_agent.py`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/agents/synthesis_agent.py): Síntese académica e redação das respostas às Questões de Investigação.
