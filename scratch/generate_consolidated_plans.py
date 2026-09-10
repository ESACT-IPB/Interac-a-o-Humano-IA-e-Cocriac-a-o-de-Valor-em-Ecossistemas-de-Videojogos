import os
import json

def generate_consolidated_plans():
    plans = []
    transcript_path = '/Users/jpaulo/.gemini/antigravity/brain/9f22e362-5007-4bb4-862f-3fab8ae596ee/.system_generated/logs/transcript_full.jsonl'
    
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'implementation_plan.md' in line and 'write_to_file' in line:
                data = json.loads(line)
                for tc in data.get('tool_calls', []):
                    if tc.get('name') == 'write_to_file' and 'implementation_plan.md' in str(tc.get('args', {})):
                        plans.append({
                            'step': data.get('step_index'),
                            'date': data.get('created_at'),
                            'content': tc['args'].get('CodeContent', '')
                        })

    meta = [
        {
            "id": "Plano 1",
            "titulo": "Arquitetura Fundacional da Framework DART-NET v2.0",
            "data": "2026-09-04",
            "solicitacao": "Conceção da pipeline multiagente para investigação científica sobre Interação Humano-IA e Cocriação de Valor em videojogos MMO (World of Warcraft e EVE Online).",
            "escopo": "Criação da taxonomia teórica DART-NET (A1-A6, I1-I6, VC1-VC4), dimensões DART, orquestração de 7 agentes e geração de relatórios.",
            "resultado": "Pipeline multiagente estabelecida, agentes configurados com API DeepSeek e primeiro ciclo de testes executado."
        },
        {
            "id": "Plano 2",
            "titulo": "Expansão Temática e Ingestão de Novas Fontes (MCP, Copilotos, Vibe-Coding)",
            "data": "2026-09-08",
            "solicitacao": "Inclusão de um novo lote de discussões da comunidade cobrindo tópicos emergentes de IA generativa em jogos.",
            "escopo": "Integração de fontes sobre Model Context Protocol (MCP), agentes autónomos de jogo, copilotos ChatGPT/Claude para WoW e EVE Online, e 'vibe coding'.",
            "resultado": "Inventário de discussões expandido, catálogo temático A1-A5 construído e novos scrapers desenvolvidos."
        },
        {
            "id": "Plano 3",
            "titulo": "Reexecução Integral DART-NET v3.0 com Filtro Temporal Estrito (Jan 2024 – 2026)",
            "data": "2026-09-09",
            "solicitacao": "Refazer integralmente o estudo unificando 303 tópicos canónicos e restringindo temporalmente os dados a janeiro de 2024 em diante.",
            "escopo": "Aplicação do corte `created_at >= 2024-01-01`, ingestão de 8.999 mensagens brutas, validação semântica de 1.034 posts (1.032 IDs únicos), recodificação qualitativa integral e auditoria de qualidade cega (206 amostras).",
            "resultado": "Corpus canónico de 1.032 posts temporalmente puros gerado, com auditoria de qualidade a 84,41% e relatórios científicos sintetizados."
        },
        {
            "id": "Plano 4",
            "titulo": "Parsing Guard, Reprocessamento de Falhas de API e Resiliência Sintática",
            "data": "2026-09-10 (14:34)",
            "solicitacao": "Identificar e reprocessar todas as mensagens que sofreram falhas de delimitador/parsing da API DeepSeek, atualizando o fluxograma com essa etapa.",
            "escopo": "Desenvolvimento do motor de recuperação e reparação recursiva de JSON (Parsing Guard), reprocessamento determinístico de todos os posts pendentes e reexecução da auditoria de qualidade.",
            "resultado": "Zero erros remanescentes no corpus de 1.032 posts, pontuação da auditoria de qualidade elevada para 91,20% e inclusão do self-healing loop no fluxograma."
        },
        {
            "id": "Plano 5",
            "titulo": "Poda Metodológica Epistémica (Exclusão de A6, Zero-DART e Queixas Mecânicas)",
            "data": "2026-09-10 (15:32)",
            "solicitacao": "Remover do corpus as categorias A6 (Não-IA), Zero DART (D:0, A:0, R:0, T:0) e queixas mecânicas clássicas de farming em A2, atualizando fluxograma e relatório.",
            "escopo": "Script de poda determinístico (`prune_dataset_methodological.py`), backup salvaguardado do corpus de 1.032, exclusão líquida de 207 posts sem perda de A1/A4/VC1/VC2, e consolidação do corpus refinado de 825 posts.",
            "resultado": "Médias DART todas elevadas acima de 1,0 (D=1.09, A=1.20, R=1.61, T=1.34), proporção de cocriação ativa subiu para 22,8%, auditoria refinada para 91,31% e atualização de todas as tabelas e relatórios."
        }
    ]

    out = []
    out.append("# Compilação Histórica dos Planos de Implementação — DART-NET v1.0 a v3.5")
    out.append("")
    out.append("Este documento reúne e consolida **todos os planos de implementação formais** concebidos, aprovados e executados ao longo do desenvolvimento do projeto de investigação científica:")
    out.append("")
    out.append("> **Título do Projeto:** *Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos*  ")
    out.append("> **Enquadramento Teórico:** Framework DART-NET (Prahalad & Ramaswamy, 2004; Vargo & Lusch, 2004; Kozinets, 2020)  ")
    out.append("> **Ambiente Empírico:** MMORPGs (*World of Warcraft* e *EVE Online*) — Período: Janeiro de 2024 a Setembro de 2026  ")
    out.append("> **Modelo Computacional de Codificação:** Multiagente autónomo orquestrado com LLMs (`deepseek-v4-flash` para codificação e `deepseek-v4-pro` para auditoria cega).")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Índice Cronológico dos Planos de Implementação")
    out.append("")
    out.append("| # | Plano de Implementação | Data de Aprovação | Foco Epistémico Principal | Corpus Resultante |")
    out.append("| :-: | :--- | :---: | :--- | :---: |")
    out.append("| **1** | [Plano 1: Arquitetura Fundacional DART-NET v2.0](#1-plano-1-arquitetura-fundacional-da-framework-dart-net-v20) | 04/09/2026 | Estruturação teórica DART-NET e orquestração multiagente inicial | Amostra piloto |")
    out.append("| **2** | [Plano 2: Expansão de Fontes e Tecnologias Emergentes](#2-plano-2-expansão-temática-e-ingestão-de-novas-fontes-mcp-copilotos-vibe-coding) | 08/09/2026 | Ingestão de MCP, copilotos ChatGPT/Claude e vibe-coding | Corpus expandido |")
    out.append("| **3** | [Plano 3: Reexecução com Filtro Temporal Estrito (Jan 2024+)](#3-plano-3-reexecução-integral-dart-net-v30-com-filtro-temporal-estrito-jan-2024--2026) | 09/09/2026 | 303 tópicos canónicos, corte temporal $\\ge$ 2024, Camadas 1-3 | 1.032 posts |")
    out.append("| **4** | [Plano 4: Parsing Guard e Resiliência Sintática](#4-plano-4-parsing-guard-reprocessamento-de-falhas-de-api-e-resiliência-sintática) | 10/09/2026 | Recuperação determinística de falhas de parsing JSON/delimitadores | 1.032 posts (0 erros) |")
    out.append("| **5** | [Plano 5: Poda Metodológica e Refinamento Epistémico (Fase 3.5)](#5-plano-5-poda-metodológica-epistémica-exclusão-de-a6-zero-dart-e-queixas-mecânicas) | 10/09/2026 | Exclusão de A6 (Não-IA), Zero-DART e queixas mecânicas arcaicas | **825 posts refinados** |")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Matriz Comparativa de Evolução Metodológica")
    out.append("")
    out.append("A tabela seguinte sintetiza como cada plano de implementação transformou a precisão dos dados e a solidez teórica do estudo:")
    out.append("")
    out.append("| Dimensão / Indicador | Plano 1 & 2 (Fase Exploratória) | Plano 3 (Reexecução Canónica) | Plano 4 (Parsing Guard) | Plano 5 (Corpus Refinado Final) |")
    out.append("| :--- | :---: | :---: | :---: | :---: |")
    out.append("| **Tópicos Canónicos** | 69 tópicos iniciais | 303 discussões unificadas | 303 discussões unificadas | **303 discussões unificadas** |")
    out.append("| **Filtro Temporal** | Sem corte estrito (histórico) | $\\ge$ 01/01/2024 rigoroso | $\\ge$ 01/01/2024 rigoroso | **$\\ge$ 01/01/2024 rigoroso** |")
    out.append("| **Universo de Mensagens** | Variável | 1.032 posts validados | 1.032 posts validados | **825 posts purificados** |")
    out.append("| **Erros de Delimitador/Parsing** | Ocorrências pontuais | 224 posts com erro/truncamento | 0 erros remanescentes (100% recuperados) | **0 erros** |")
    out.append("| **Score da Auditoria de Qualidade** | N/A | 84,41% (206 auditorias) | 91,20% (206 auditorias) | **91,31% (159 auditorias)** |")
    out.append("| **Veracidade Literal de Citações** | N/A | 98,5% | 100,0% | **100,0% (0 alucinações)** |")
    out.append("| **Média Diálogo (D) [0-5]** | N/A | 0,88 | 0,88 | **1,09** (+23,9%) |")
    out.append("| **Média Acesso (A) [0-5]** | N/A | 0,98 | 0,98 | **1,20** (+22,4%) |")
    out.append("| **Média Risco (R) [0-5]** | N/A | 1,38 | 1,38 | **1,61** (+16,7%) |")
    out.append("| **Média Transparência (T) [0-5]** | N/A | 1,09 | 1,09 | **1,34** (+22,9%) |")
    out.append("| **Discussões com Cocriação Ativa (VC1-VC3)** | N/A | 11,4% (118 posts) | 11,4% (118 posts) | **22,8% (188 posts)** |")
    out.append("| **Preservação de Agentes Autónomos (A1)** | — | 95 posts | 95 posts | **95 posts (100% preservados)** |")
    out.append("| **Preservação de Copilotos Humanos (A4)** | — | 59 posts | 59 posts | **59 posts (100% preservados)** |")
    out.append("")
    out.append("---")
    out.append("")

    for idx, p in enumerate(plans):
        m = meta[idx]
        out.append(f"## {idx+1}. {m['id']}: {m['titulo']}")
        out.append("")
        out.append(f"* **Data de Criação e Aprovação:** `{p['date']}` (Step `{p['step']}` no registo)")
        out.append(f"* **Contexto / Solicitação do Utilizador:** {m['solicitacao']}")
        out.append(f"* **Escopo e Intervenções Centrais:** {m['escopo']}")
        out.append(f"* **Resultado Final e Impacto:** {m['resultado']}")
        out.append("")
        out.append("### Transcrição Integral do Plano Executado:")
        out.append("")
        out.append("> [!NOTE]")
        out.append(f"> O texto abaixo corresponde ao documento original `{m['id']}` tal como submetido para validação do utilizador e executado pela equipa de agentes.")
        out.append("")
        
        # Format the plan content slightly indented or within blockquote/subsections
        content_lines = p['content'].splitlines()
        # Adjust header levels so the document maintains correct hierarchical outline
        adjusted_lines = []
        for cl in content_lines:
            if cl.startswith('# '):
                adjusted_lines.append('#### ' + cl[2:])
            elif cl.startswith('## '):
                adjusted_lines.append('##### ' + cl[3:])
            elif cl.startswith('### '):
                adjusted_lines.append('###### ' + cl[4:])
            else:
                adjusted_lines.append(cl)
                
        out.append("\n".join(adjusted_lines))
        out.append("")
        out.append("---")
        out.append("")

    out.append("## Síntese de Rastreabilidade e Reprodutibilidade")
    out.append("")
    out.append("A execução sequencial e cumulativa destes cinco planos de implementação assegurou:")
    out.append("1. **Transparência Epistémica Total**: Nenhuma alteração de dados ocorreu sem plano prévio aprovado, registo determinístico em script e salvaguarda do estado anterior em ficheiros `unpruned`.")
    out.append("2. **Supervisão Humana Contínua (*Human-in-the-Loop*)**: A pipeline sinalizou 708 posts para validação humana prioritária (`human_review_required: true`), e a taxa de consistência da auditoria algorítmica atingiu **91,31%**.")
    out.append("3. **Conformidade Metodológica Estrita**: O corpus refinado de **825 posts** responde diretamente às questões de investigação QI1 a QI5 sem o viés de mensagens pré-2024, queixas de bots mecânicos ou posts periféricos sem ligação a IA.")
    out.append("")

    dest_file = '/Users/jpaulo/Documents/AntiGravity_Agents/Interação Humano-IA e Cocriação de Valor em Ecossistemas de Videojogos/output/planos_implementacao_consolidados.md'
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(out))
        
    print(f"Sucesso: {dest_file} gerado com {len(out)} linhas ({os.path.getsize(dest_file)} bytes).")

if __name__ == '__main__':
    generate_consolidated_plans()
