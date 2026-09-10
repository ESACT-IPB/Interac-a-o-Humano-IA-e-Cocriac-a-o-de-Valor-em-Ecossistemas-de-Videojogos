# Fluxograma da Pipeline Netnográfica DART-NET v3.0
## Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos

Este documento apresenta o fluxograma metodológico e arquitetural completo da pipeline multiagente de análise netnográfica baseada no Framework **DART-NET** (Prahalad & Ramaswamy, 2004; DART-NET 2026), integrando desde a extração de dados brutos pós-2024 até à validação inter-codificadores via Kappa de Cohen.

---

## Diagrama de Fluxo (Mermaid)

```mermaid
flowchart TD
    %% Estilos Globais
    classDef source fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef agent fill:#ede7f6,stroke:#512da8,stroke-width:2px;
    classDef decision fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef output fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef validation fill:#fce4ec,stroke:#c2185b,stroke-width:2px;

    %% CAMADA 1: Ingestão de Dados Brutos
    subgraph FASE1 ["Camada 1: Ingestão de Dados Brutos (RAW DATA) — Jan 2024 a 2026"]
        CORPUS["Corpus Canónico de 303 Tópicos Únicos<br/>(A1-A5 curados + Query Booleana IA/LLM/MCP)"]:::source
        
        RAW_WOW["Fóruns Blizzard WoW<br/>(87 tópicos Discourse JSON)"]:::source
        RAW_EVE["Fóruns CCP EVE Online<br/>(62 tópicos Discourse JSON)"]:::source
        RAW_REDDIT["Reddit r/wow & r/Eve<br/>(125 tópicos Arctic Shift API)"]:::source
        RAW_STEAM["Steam Community<br/>(11 tópicos 2026)"]:::source
        
        CORPUS --> RAW_WOW
        CORPUS --> RAW_EVE
        CORPUS --> RAW_REDDIT
        CORPUS --> RAW_STEAM
        
        SCRAPER["ScraperAgent<br/>(Filtro Temporal Estrito: created_at >= 2024-01-01<br/>Comprimento mínimo >= 50 carateres)"]:::agent
        RAW_WOW --> SCRAPER
        RAW_EVE --> SCRAPER
        RAW_REDDIT --> SCRAPER
        RAW_STEAM --> SCRAPER
        
        SCRAPER --> SCRAPED_POSTS[("scraped_posts.json<br/>(6.485 posts pós-2024 preservados)")]
    end

    %% CAMADA 2: Triagem e Anonimização Ética
    subgraph FASE2 ["Fase 2: Triagem Semântica e Pseudonimização Ética"]
        SCRAPED_POSTS --> VALIDATOR["SemanticValidatorAgent<br/>(deepseek-v4-flash com léxico expandido)"]:::agent
        VCACHE[("validation_cache.json<br/>(12.429 validações em cache)")] <--> VALIDATOR
        
        VALID_CHECK{"Classificação de Relevância<br/>(RELEVANT / POSSIBLY RELEVANT)?"}:::decision
        VALIDATOR --> VALID_CHECK
        VALID_CHECK -- "IRRELEVANT" --> DISCARD["Descartado da Análise"]
        VALID_CHECK -- "Válido (2024-2026)" --> VALID_POSTS[("validated_posts.json<br/>(1.034 posts qualificados)")]
        
        ANON["AnonymizerAgent<br/>(Preservação das 3 camadas, sanitização de PII<br/>e pseudonimização Player_0001 a Player_1032)"]:::agent
        VALID_POSTS --> ANON
        ANON --> ANON_POSTS[("anonymized_posts.json<br/>(1.032 posts únicos com texto integral)")]
    end

    %% CAMADA 2: Codificação Qualitativa DART-NET
    subgraph FASE3 ["Camada 2: Codificação Científica DART-NET (AI CODING)"]
        ANON_POSTS --> NETNO["NetnographyAgent<br/>(deepseek-v4-flash, 30 workers concorrentes)"]:::agent
        
        NETNO --> PARSE_GUARD{"Validação Sintática & Guardião JSON<br/>(Deteta JSON malformado / truncado)?"}:::decision
        PARSE_GUARD -- "Erro de Delimitador / Truncamento" --> REPROCESS["Parsing Guard & Reprocessamento<br/>(extract_and_repair_json + controlo de payload)"]:::agent
        REPROCESS -. "Ciclo de Auto-Reparação" .-> NETNO
        PARSE_GUARD -- "Sintaxe Válida" --> DART_CODING
        
        subgraph DART_CODING ["Classificação Multi-Taxonómica DART-NET"]
            AI_TAX["Tipo de IA (A1–A6)<br/>(Taxonomia Adaptativa vs Determinística)"]
            INTERACTION["Estrutura de Interação (I1–I6)<br/>(Fluxos Diretos, Discurso e Mediação)"]
            VALUE_TAX["Cocriação de Valor (VC1–VC4)<br/>(Simétrica, Assimétrica e Parasitária)"]
            DART_DIM["Dimensões DART (0 a 5)<br/>(Diálogo, Acesso, Risco, Transparência)"]
            CONFIDENCE["Calibração de Confiança & Flag<br/>(human_review_required = True se conf < 0,80)"]
        end
        
        DART_CODING --> NETNO_RESULTS[("netnography_results.jsonl<br/>(1.032 análises científicas validadas sem erros)")]
    end

    %% CAMADA 2: Auditoria de Qualidade Interna
    subgraph FASE4 ["Fase 4: Controlo de Qualidade Interno Multiagente"]
        NETNO_RESULTS --> AUDIT_SAMPLE["Amostragem Aleatória de 20%<br/>(206 análises, Seed 42)"]
        AUDIT_SAMPLE --> QUALITY_GUARD["QualityGuardAgent<br/>(deepseek-v4-pro auditor independente)"]:::agent
        
        QUALITY_CHECK{"Índice de Concordância<br/>Global >= 70%?"}:::decision
        QUALITY_GUARD --> QUALITY_CHECK
        QUALITY_CHECK -- "Não" --> ABORT["Abortar Pipeline"]
        QUALITY_CHECK -- "Aprovado: 91,20%" --> AUDIT_REPORT[("quality_audit_results.json<br/>(Score 91,20% | 100% citações literais | 12 alertas)")]
    end

    %% CAMADA 2 & 3: Síntese e Entregáveis Finais
    subgraph FASE5 ["Fase 5: Síntese e Entregáveis Principais"]
        NETNO_RESULTS --> SYNTHESIS["SynthesisAgent<br/>(deepseek-v4-pro com amostragem estratificada)"]:::agent
        AUDIT_REPORT --> SYNTHESIS
        
        SYNTHESIS --> REPORT_FINAL["relatorio_netnografia.md<br/>(Relatório Académico de 8 Secções — QI1 a QI5)"]:::output
        
        ANON_POSTS --> TABLE_GEN["SummaryTableGenerator<br/>(deepseek-v4-flash para resumos <= 50 palavras)"]:::agent
        NETNO_RESULTS --> TABLE_GEN
        TABLE_GEN --> TABLE_RESUMOS["tabela_resumos.md<br/>(1.032 posts com DART, resumos e links diretos)"]:::output
        
        CORPUS --> LISTA_LINKS_MD["lista_links.md / lista_links.txt<br/>(Catálogo das 303 URLs Canónicas)"]:::output
        COST_LOG["Registo de Tokens<br/>(~27.000 chamadas API)"] --> TABELA_CUSTOS["tabela_custos.md<br/>(Auditoria de Custos: ~$21,50 USD)"]:::output
    end

    %% CAMADA 3: Validação Metodológica Externa
    subgraph FASE6 ["Camada 3: Validação Humana e Reprodutibilidade (HUMAN VALIDATION)"]
        NETNO_RESULTS --> HUMAN_QUEUE["Fila de Validação Humana Prioritária<br/>(799 posts com '⚠️ Sim' em Rev. Humana)"]:::validation
        
        NETNO_RESULTS --> KAPPA_SAMPLE["Amostragem para Revisão Humana"]:::agent
        KAPPA_SAMPLE --> CSV_HUMAN["amostra_codificacao_humana.csv<br/>(Amostra para teste cego)"]:::validation
        
        HUMAN_CODING["Codificação Cega por Investigador Humano<br/>(DART-NET: A1-A6, I1-I6, VC1-VC4, DART)"]:::validation
        CSV_HUMAN --> HUMAN_CODING
        
        HUMAN_CODING --> CALC_KAPPA["calculate_kappa.py<br/>(Cálculo do Coeficiente Kappa de Cohen)"]:::agent
        CALC_KAPPA --> KAPPA_REPORT["relatorio_concordancia_kappa.md<br/>(Índice de Fiabilidade Científica)"]:::output
    end
```

---

## Descrição das Fases da Pipeline DART-NET v3.0

1. **Fase 1: Ingestão Canónica e Filtro Temporal Estrito (RAW DATA)**
   * **Agente:** `ScraperAgent`
   * **Fontes:** 303 discussões canónicas catalogadas (Discourse WoW e EVE Online, Reddit `r/wow` e `r/Eve`, Steam Community).
   * **Regra Temporal:** `POST_MIN_DATE = "2024-01-01T00:00:00Z"`. Foram filtradas 8.999 mensagens, excluindo 1.248 posts pré-2024 e 1.266 posts curtos (< 50 carateres).
   * **Saída:** `data/interim/scraped_posts.json` (6.485 posts pós-2024 preservados na íntegra).

2. **Fase 2: Triagem Semântica e Sanitização Ética**
   * **Agentes:** `SemanticValidatorAgent` e `AnonymizerAgent`
   * **Ação:** Triagem semântica de relevância suportada pelo modelo `deepseek-v4-flash` com léxico expandido (LLM, MCP, Copilot, etc.). Pseudonimização ética (`Player_0001` a `Player_1032`) e sanitização de dados privados (PII), preservando as 3 camadas metodológicas intactas (Secção 14).
   * **Saída:** `data/processed/anonymized_posts.json` (1.032 posts únicos estritamente pós-2024).

3. **Fase 3: Codificação Qualitativa DART-NET e Parsing Guard (AI CODING)**
   * **Agente:** `NetnographyAgent` com módulo integrado `Parsing Guard & Reprocessing`
   * **Mecanismo de Tolerância a Falhas:** Incorporação da camada de reparação estrutural de JSON (`extract_and_repair_json`), proteção contra estouro de contexto para posts volumosos (truncamento de segurança no prompt a $\le 8.000$ carateres, preservando o texto original no ficheiro final) e rotina automática de reprocessamento em ciclo fechado. Recuperou **100% dos 224 posts afetados**, garantindo zero falhas residuais (`0` erros remanescentes) e integridade analítica total dos 1.032 posts.
   * **Ação Analítica:** Codificação multi-taxonómica via `deepseek-v4-flash`:
     * **Tipologia de IA (`A1` a `A6`)**: Distinção estrita de agentes de IA autónomos (A1) vs bots convencionais (A2), scripts (A3), humanos assistidos (A4) e discussões reflexivas (A5).
     * **Estrutura de Interação (`I1` a `I6`)**: Identificação dos fluxos direto (I1), agente-humano (I2), bidirecional (I3) e discurso social (I4).
     * **Cocriação de Valor (`VC1` a `VC4`)**: Mapeamento de cocriação simétrica (VC1), potencial cocriação assimétrica (VC2) e codestruição parasitária (VC3).
     * **Dimensões DART (0 a 5)**: Avaliação independente de Diálogo, Acesso, Risco e Transparência com evidência literal.
     * **Calibração de Confiança e Flag Humana**: Sinalização automática de `human_review_required: true` para casos com confiança < 0,80 ou ambiguidade.
   * **Saída:** `data/analysis/netnography_results.jsonl` (1.032 análises científicas validadas sem falhas de processamento).

4. **Fase 4: Controlo de Qualidade Interno Multiagente**
   * **Agente:** `QualityGuardAgent`
   * **Ação:** Amostragem cega e probabilística de 20% (206 análises) auditada pelo modelo de raciocínio `deepseek-v4-pro`. Validação da autenticidade literal de 100% das citações, coerência taxonómica e calibração DART.
   * **Resultado:** **Score Médio de 91,20%** (limiar crítico de $\ge 70\%$ superado amplamente; apenas 12 casos com alertas estritos de confiança).
   * **Saída:** `data/analysis/quality_audit_results.json`.

5. **Fase 5: Síntese e Entregáveis Finais**
   * **Agentes:** `SynthesisAgent` e `SummaryTableGenerator`
   * **Entregáveis:**
     * `output/relatorio_netnografia.md`: Relatório académico formal de 8 secções em português de Portugal, respondendo às 5 Questões de Investigação (QI1 a QI5) fundamentadas empiricamente.
     * `output/tabela_resumos.md`: Matriz com 1.032 registos (DART scores, Tipos IA, Interação, Valor, resumos $\le$ 50 palavras, temas $\le$ 8 palavras, links diretos e flag de revisão humana).
     * `output/lista_links.md` e `output/lista_links.txt`: Inventário canónico das 303 discussões catalogadas.
     * `output/tabela_custos.md`: Auditoria financeira de ~27.000 chamadas de API com custo consolidado de **~$21,50 USD**.

6. **Fase 6: Validação Humana e Reprodutibilidade (HUMAN VALIDATION)**
   * **Fila de Revisão Humana**: 799 posts (77,42%) priorizados para validação humana através da flag `⚠️ Sim`.
   * **Concordância Inter-Codificadores**: Amostra de validação para teste cego e cálculo estatístico do coeficiente Kappa de Cohen ($\kappa$).
   * **Saída:** `output/relatorio_concordancia_kappa.md`.


