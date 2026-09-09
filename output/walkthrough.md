# Walkthrough: Conclusão da Reexecução do Estudo DART-NET v3.0

O estudo netnográfico DART-NET foi **integralmente reexecutado, auditado e consolidado com sucesso** com base no corpus canónico de **303 tópicos de discussão** e na aplicação estrita do **filtro temporal delimitado a partir de janeiro de 2024** (`created_at >= '2024-01-01'`).

---

## 1. Síntese do Corpus e Filtro Temporal Estrito

1. **Unificação do Corpus Canónico (303 Discussões)**:
   - Fusão deduplicada do catálogo de discussões curadas A1–A5 com as novas fontes da consulta avançada booleana (234 tópicos únicos).
   - Base canónica consolidada e persistida em [`data/target_corpus_303.json`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/data/target_corpus_303.json).
2. **Ingestão em Bruto (Camada 1 — Raw Data)**:
   - Volume total em `data/raw/` expandido para **430 ficheiros**.
   - Descarregados 87 tópicos Discourse Blizzard WoW, 62 tópicos Discourse CCP EVE Online, 125 tópicos Reddit 2024+ (via Arctic Shift API) e 11 tópicos Steam Community.
3. **Filtro Temporal Rigoroso (Jan 2024 – 2026)**:
   - Todas as mensagens criadas antes de 01/01/2024 foram sumariamente excluídas em todas as fases da pipeline.
   - De 8.999 mensagens identificadas, 1.248 mensagens pré-2024 e 1.266 posts com comprimento insuficiente (<50 carateres) foram descartados no `ScraperAgent`, resultando num corpus de **6.485 posts elegíveis**.
   - A triagem com o `SemanticValidatorAgent` validou **1.034 posts** relevantes (1.032 IDs únicos), 100% dos quais com carimbo temporal compreendido entre **22 de janeiro de 2024 e 08 de setembro de 2026**.

---

## 2. Métricas Globais da Codificação DART-NET (Camada 2 — AI Coding)

O conjunto dos 1.032 posts anonimizados foi codificado e auditado sob a taxonomia DART-NET:

### A. Distribuição dos Tipos de IA (A1–A6)
| Código | Classificação | Total | Percentagem |
| :--- | :--- | :---: | :---: |
| **A1** | Agente de IA Autónomo / LLM Integrado | 87 | 8,4% |
| **A2** | Bot Convencional (Regras determinísticas) | 100 | 9,7% |
| **A3** | Script / Automação simples | 14 | 1,4% |
| **A4** | Humano Assistido por IA (Copilotos/Addons) | 52 | 5,0% |
| **A5** | Discussão Reflexiva sobre IA | 511 | 49,5% |
| **A6** | Contexto de Fundo / Ruído residual | 268 | 26,0% |
| **Total** | **Corpus Validado** | **1.032** | **100,0%** |

### B. Estruturas de Interação Humano-IA (I1–I6)
| Código | Estrutura | Total | Percentagem |
| :--- | :--- | :---: | :---: |
| **I1** | Humano → IA (Comando / Prompt) | 43 | 4,2% |
| **I2** | IA → Humano (Recomendação / Ação) | 5 | 0,5% |
| **I3** | Humano ↔ IA (Bidirecional / Cocriação) | 51 | 4,9% |
| **I4** | Humano → Humano sobre IA (Discurso social) | 578 | 56,0% |
| **I5** | Humano → Ambiente mediado por IA | 4 | 0,4% |
| **I6** | Sem interação significativa identificável | 351 | 34,0% |

### C. Cocriação e Codestruição de Valor (VC1–VC4)
| Código | Tipologia de Valor | Total | Percentagem |
| :--- | :--- | :---: | :---: |
| **VC1** | Cocriação de Valor Efetiva | 23 | 2,2% |
| **VC2** | Potencial Cocriação de Valor | 50 | 4,8% |
| **VC3** | Codestruição de Valor (Frustração, desequilíbrio) | 45 | 4,4% |
| **VC4** | Sem evidência direta de impacto de valor | 914 | 88,6% |

### D. Médias das Dimensões DART (Escala 0 a 5)
- **Diálogo (D)**: 0,70 / 5
- **Acesso (A)**: 0,79 / 5
- **Risco (R)**: 1,16 / 5 (dimensão mais saliente no discurso empírico)
- **Transparência (T)**: 0,79 / 5

---

## 3. Resultados do Controlo de Qualidade e Custos

1. **Auditoria Científica (`QualityGuardAgent`)**:
   - Amostra probabilística de **20% (206 análises)** auditada cegamente com o modelo de alta capacidade `deepseek-v4-pro`.
   - **Score Médio de Consistência Qualitativa**: **84,41%** (aprovado com distinção face ao limiar mínimo de 70,0%).
   - **Veracidade das Citações**: 100% de conformidade com o texto original (ausência de alucinações).
2. **Fila de Validação Humana (`human_review_required`)**:
   - **803 posts (77,81%)** sinalizados para revisão manual prioritária com `⚠️ Sim` (confiança < 0,80 ou presença de gíria/sarcasmo).
   - **229 posts (22,19%)** com aceitação automática de confiança muito elevada.
3. **Consumo de Recursos e Custos da API**:
   - **Modelo `deepseek-v4-flash`**: 24.674 chamadas ($11,27 USD).
   - **Modelo `deepseek-v4-pro`**: 1.942 chamadas ($9,77 USD).
   - **Custo Global Consolidado**: **$21,05 USD** (26.616 chamadas de API, ~28 milhões de tokens processados).

---

## 4. Catálogo dos Entregáveis Finais no Repositório

Todos os ficheiros de saída estão atualizados, validados e versionados no Git:

| Ficheiro de Saída | Conteúdo / Finalidade | Estado |
| :--- | :--- | :---: |
| [`output/lista_links.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.md) | Catálogo unificado com 303 discussões canónicas por comunidade e índice temático A1 a A5. | ✅ Concluído |
| [`output/lista_links.txt`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/lista_links.txt) | Inventário canónico de URLs em formato texto simples. | ✅ Concluído |
| [`output/tabela_resumos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_resumos.md) | Matriz completa dos 1.032 posts (DART, A1-A6, I1-I6, VC1-VC4, resumos de 50 palavras, temas de 8 palavras, links e Rev. Humana). | ✅ Concluído |
| [`output/leitura_netnography_results.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/leitura_netnography_results.md) | Relatório legível de codificação qualitativa das 1.032 mensagens com 1.032 fichas analíticas detalhadas. | ✅ Concluído |
| [`output/leitura_quality_audit_results.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/leitura_quality_audit_results.md) | Relatório legível da auditoria cega de 206 análises com justificação de cada critério. | ✅ Concluído |
| [`output/relatorio_netnografia.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/relatorio_netnografia.md) | Relatório científico integral de 8 secções em português de Portugal, respondendo às questões de investigação (QI1 a QI5). | ✅ Concluído |
| [`output/fluxograma_implementacao.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/fluxograma_implementacao.md) | Fluxograma arquitetural completo em formato Mermaid e detalhe metodológico das 6 fases da pipeline DART-NET v3.0. | ✅ Concluído |
| [`output/visualizar_fluxograma.html`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/visualizar_fluxograma.html) | Aplicação web local interativa para navegação gráfica com zoom/pan do fluxograma. | ✅ Concluído |
| [`output/tabela_custos.md`](file:///Users/jpaulo/Documents/AntiGravity_Agents/Interação%20Humano-IA%20e%20Cocriação%20de%20Valor%20em%20Ecossistemas%20de%20Videojogos/output/tabela_custos.md) | Auditoria financeira e registo de tokens consumidos pelas 26.616 chamadas de API. | ✅ Concluído |
