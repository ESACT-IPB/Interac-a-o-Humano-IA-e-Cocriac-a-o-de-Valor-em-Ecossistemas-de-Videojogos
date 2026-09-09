# Fluxograma do Plano de Implementação da Pipeline Netnográfica DART-NET v2.0

Este documento apresenta o fluxograma metodológico e arquitetural completo da pipeline multiagente de análise netnográfica baseada no Framework **DART-NET** (Prahalad & Ramaswamy, 2004; DART-NET 2026), integrando desde a extração de dados brutos até a validação inter-codificadores via Kappa de Cohen.

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
    subgraph FASE1 ["Camada 1: Ingestão de Dados Brutos (RAW DATA)"]
        RAW_WOW["Fóruns Blizzard WoW<br/>(Comunidades e Tópicos)"]:::source
        RAW_EVE["Fóruns CCP EVE Online<br/>(Economia e Mecânicas)"]:::source
        RAW_REDDIT["Reddit & Média Externa<br/>(Subreddits e Discussões)"]:::source
        
        SCRAPER["ScraperAgent<br/>(Extração integral, preservação de contexto e keywords)"]:::agent
        RAW_WOW --> SCRAPER
        RAW_EVE --> SCRAPER
        RAW_REDDIT --> SCRAPER
        SCRAPER --> SCRAPED_POSTS[("scraped_posts.json<br/>(RAW DATA Preservado)")]
    end

    %% CAMADA 2: Triagem e Anonimização Ética
    subgraph FASE2 ["Fase 2: Triagem em 2 Etapas e Pseudonimização"]
        SCRAPED_POSTS --> VALIDATOR["SemanticValidatorAgent<br/>(deepseek-v4-flash)"]:::agent
        VCACHE[("validation_cache.json")] <--> VALIDATOR
        
        VALID_CHECK{"Classificação de Relevância<br/>(Secção 6)"}:::decision
        VALIDATOR --> VALID_CHECK
        VALID_CHECK -- "IRRELEVANT" --> DISCARD["Descartado da Análise"]
        VALID_CHECK -- "RELEVANT / POSSIBLY RELEVANT" --> VALID_POSTS[("validated_posts.json")]
        
        ANON["AnonymizerAgent<br/>(Preservação das 3 camadas e<br/>atribuição de Player_XXX)"]:::agent
        VALID_POSTS --> ANON
        ANON --> ANON_POSTS[("anonymized_posts.json<br/>(Texto integral preservado)")]
    end

    %% CAMADA 2: Codificação Qualitativa DART-NET
    subgraph FASE3 ["Camada 2: Codificação Científica DART-NET"]
        ANON_POSTS --> NETNO["NetnographyAgent<br/>(deepseek-v4-flash em thinking mode)"]:::agent
        
        subgraph DART_CODING ["Classificação Multi-Taxonómica DART-NET"]
            AI_TAX["Tipo de IA (A1–A6)<br/>(AI Agent, Bot, Script, Assisted, etc.)"]
            INTERACTION["Estrutura de Interação (I1–I6)<br/>(Humano-IA, Bidirecional, Mediado)"]
            VALUE_TAX["Cocriação de Valor (VC1–VC4)<br/>(Co-criação vs Co-destruição)"]
            DART_DIM["Dimensões DART (0 a 5)<br/>(Diálogo, Acesso, Risco, Transparência)"]
            CONFIDENCE["Calibração de Confiança & Flag<br/>(human_review_required se < 0.80)"]
        end
        
        NETNO --> DART_CODING
        DART_CODING --> NETNO_RESULTS[("netnography_results.jsonl<br/>(Esquema Padronizado Secção 13)")]
    end

    %% CAMADA 2: Auditoria de Qualidade
    subgraph FASE4 ["Fase 4: Controlo de Qualidade Interno"]
        NETNO_RESULTS --> AUDIT_SAMPLE["Amostragem Aleatória de 20%<br/>(Seed 42)"]
        AUDIT_SAMPLE --> QUALITY_GUARD["QualityGuardAgent<br/>(deepseek-v4-pro em thinking mode)"]:::agent
        
        QUALITY_CHECK{"Índice de Concordância<br/>Global >= 70%?"}:::decision
        QUALITY_GUARD --> QUALITY_CHECK
        QUALITY_CHECK -- "Não" --> ABORT["Abortar Pipeline"]
        QUALITY_CHECK -- "Sim" --> AUDIT_REPORT[("quality_audit_results.json")]
    end

    %% CAMADA 2 & 3: Síntese e Entregáveis Finais
    subgraph FASE5 ["Fase 5: Síntese e Entregáveis Finais"]
        NETNO_RESULTS --> SYNTHESIS["SynthesisAgent<br/>(deepseek-v4-pro)"]:::agent
        AUDIT_REPORT --> SYNTHESIS
        
        SYNTHESIS --> REPORT_FINAL["relatorio_netnografia.md<br/>(Relatório Académico DART-NET)"]:::output
        
        ANON_POSTS --> TABLE_GEN["SummaryTableGenerator<br/>(Resumos + Codificação DART-NET)"]:::agent
        NETNO_RESULTS --> TABLE_GEN
        TABLE_GEN --> TABLE_RESUMOS["tabela_resumos.md<br/>(Tabela com Links e Classificações)"]:::output
        
        COST_LOG["Registo de Tokens"] --> TABELA_CUSTOS["tabela_custos.md<br/>(Auditoria de Custos de API)"]:::output
    end

    %% CAMADA 3: Validação Metodológica Externa
    subgraph FASE6 ["Camada 3: Validação Humana e Reprodutibilidade"]
        NETNO_RESULTS --> KAPPA_SAMPLE["Amostragem para Revisão Humana"]:::agent
        KAPPA_SAMPLE --> CSV_HUMAN["amostra_codificacao_humana.csv<br/>(Fila de Revisão Humana)"]:::validation
        
        HUMAN_CODING["Codificação Cega por Investigador Humano<br/>(DART-NET: A1-A6, I1-I6, VC1-VC4, DART)"]:::validation
        CSV_HUMAN --> HUMAN_CODING
        
        HUMAN_CODING --> CALC_KAPPA["calculate_kappa.py<br/>(Cálculo do Kappa de Cohen)"]:::agent
        CALC_KAPPA --> KAPPA_REPORT["relatorio_concordancia_kappa.md<br/>(Índice de Fiabilidade Científica)"]:::output
    end
```

---

## Descrição das Fases da Pipeline DART-NET v2.0

1. **Fase 1: Ingestão e Preservação de Dados Brutos (RAW DATA)**
   * **Agente:** `ScraperAgent`
   * **Fontes:** Publicações de fóruns Discourse (WoW e EVE Online), subreddits e plataformas externas.
   * **Ação:** Extração preservando o texto original, contexto conversacional e identificando as palavras-chave desencadeadoras de descoberta (`keywords_triggered`).
   * **Saída:** `data/interim/scraped_posts.json` (Camada 1 preservada integralmente).

2. **Fase 2: Triagem Semântica e Sanitização Ética**
   * **Agentes:** `SemanticValidatorAgent` e `AnonymizerAgent`
   * **Ação:** Triagem de relevância tripartida (`RELEVANT`, `POSSIBLY RELEVANT`, `IRRELEVANT`) com calibração de confiança. Pseudonimização ética de autores (`author_id` -> `Player_XXX`) garantindo a não-exclusão dos ficheiros brutos conforme a regra de três camadas (Secção 14).
   * **Saída:** `data/processed/anonymized_posts.json`.

3. **Fase 3: Codificação Qualitativa DART-NET**
   * **Agente:** `NetnographyAgent`
   * **Ação:** Codificação teórica com `deepseek-v4-flash` (*thinking mode*):
     * **Tipologia de IA (`A1` a `A6`)**: Distinção estrita de agentes de IA vs bots convencionais e scripts.
     * **Estrutura de Interação (`I1` a `I6`)**: Identificação de fluxos unidirecionais, bidirecionais (`I3`) e mediados.
     * **Cocriação de Valor (`VC1` a `VC4`)**: Mapeamento de criação, potencial cocriação e codestruição de valor.
     * **Dimensões DART (0 a 5)**: Avaliação independente de Diálogo, Acesso, Risco e Transparência com citação literal (máx. 40 palavras).
     * **Calibração de Confiança e Flag Humana**: Atribuição automática de `human_review_required: true` se confiança `< 0.80` ou ambiguidade.
   * **Saída:** Base de dados incremental em `data/analysis/netnography_results.jsonl` (Esquema da Secção 13).

4. **Fase 4: Controlo de Qualidade Interno**
   * **Agente:** `QualityGuardAgent`
   * **Ação:** Amostragem cega de 20% avaliada por `deepseek-v4-pro` (*thinking mode*) validando a veracidade das citações literais, consistência concetual de A1-A6 e I1-I6, calibração DART (0-5) e sinalização da revisão humana. Limiar mínimo de aprovação $\ge 70\%$.
   * **Saída:** `data/analysis/quality_audit_results.json`.

5. **Fase 5: Síntese e Entregáveis Finais**
   * **Agentes:** `SynthesisAgent` e `SummaryTableGenerator`
   * **Entregáveis:**
     * `output/relatorio_netnografia.md`: Relatório científico formal incorporando as taxonomias DART-NET.
     * `output/tabela_resumos.md`: Tabela cruzada com posts, classificações DART-NET, flags de revisão humana, resumos e links diretos.
     * `output/tabela_custos.md`: Auditoria financeira de consumo da API DeepSeek.

6. **Fase 6: Validação Inter-Codificadores (Kappa de Cohen)**
   * **Ação:** Extração de amostra de auditoria humana cega para cálculo estatístico do coeficiente Kappa de Cohen ($\kappa$) comparando a codificação da IA com o investigador humano.
   * **Saída:** `output/relatorio_concordancia_kappa.md`.

