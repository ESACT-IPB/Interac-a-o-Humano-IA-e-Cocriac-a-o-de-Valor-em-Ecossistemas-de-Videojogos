import os
import json
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def convert_netnography_results():
    print("Processando netnography_results.jsonl...")
    input_file = os.path.join(BASE_DIR, "data", "analysis", "netnography_results.jsonl")
    output_file = os.path.join(OUTPUT_DIR, "leitura_netnography_results.md")
    
    if not os.path.exists(input_file):
        print(f"Aviso: {input_file} não encontrado.")
        return

    records = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
                
    total = len(records)
    games = Counter(r.get("jogo", "Desconhecido") for r in records)
    dart_dims = Counter(r.get("dimensao_dominante", "N/A") for r in records)
    cocreation = Counter(r.get("tipologia_cocriacao", "N/A") for r in records)
    risks = [r.get("score_risco_percebido", 0) for r in records if isinstance(r.get("score_risco_percebido"), (int, float))]
    avg_risk = sum(risks) / len(risks) if risks else 0.0

    lines = []
    lines.append("# Análise Netnográfica DART - Leitura Humana dos Resultados")
    lines.append("")
    lines.append("Este documento apresenta de forma legível e estruturada os dados codificados pelo agente netnográfico a partir do ficheiro bruto `data/analysis/netnography_results.jsonl`.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Sumário Executivo das Codificações")
    lines.append("")
    lines.append(f"* **Total de Posts Codificados:** {total}")
    lines.append(f"* **Média Global de Risco Percebido:** `{avg_risk:.2f} / 5.0`")
    lines.append("")
    lines.append("### Distribuição por Jogo")
    for game, count in games.most_common():
        lines.append(f"* **{game}:** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("### Distribuição por Dimensão DART Dominante")
    for dim, count in dart_dims.most_common():
        lines.append(f"* **{dim.capitalize()}:** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("### Distribuição por Tipologia de Cocriação")
    for tip, count in cocreation.most_common():
        lines.append(f"* **{tip.capitalize()}:** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Catálogo Detalhado das Análises Netnográficas")
    lines.append("")
    lines.append("| # | ID do Post | Jogo | Dimensão DART | Tipologia | Risco (1-5) | QIs Mapeadas |")
    lines.append("| :--- | :--- | :--- | :--- | :--- | :---: | :--- |")
    
    # First write a quick reference table for the first 100 posts (or full summary)
    for idx, r in enumerate(records[:150], 1):
        qis = ", ".join(r.get("questoes_investigacao", []))
        lines.append(f"| {idx} | `{r.get('post_id')}` | {r.get('jogo', 'N/A')} | **{r.get('dimensao_dominante', 'N/A').capitalize()}** | {r.get('tipologia_cocriacao', 'N/A').capitalize()} | {r.get('score_risco_percebido', 'N/A')} | {qis} |")
        
    if total > 150:
        lines.append(f"\n*(Tabela resumida com os primeiros 150 de {total} posts. Seguem abaixo as fichas detalhadas completas de cada post.)*\n")
        
    lines.append("\n---\n")
    lines.append("## 3. Fichas Qualitativas Individuais (DART e Evidências)\n")

    for idx, r in enumerate(records, 1):
        pid = r.get("post_id", "N/A")
        jogo = r.get("jogo", "N/A")
        dim = r.get("dimensao_dominante", "N/A").capitalize()
        tip = r.get("tipologia_cocriacao", "N/A").capitalize()
        score = r.get("score_risco_percebido", "N/A")
        qis = ", ".join(r.get("questoes_investigacao", []))
        fund_risco = r.get("fundamentacao_risco", "N/A")
        
        lines.append(f"### Post #{idx}: `{pid}` ({jogo})")
        lines.append(f"* **Dimensão Dominante:** {dim} | **Cocriação:** {tip} | **Score de Risco:** {score}/5 | **QIs:** `{qis}`")
        lines.append(f"* **Metadados:** Likes: {r.get('likes', 0)} | Nível de Confiança: {r.get('trust_level', 0)} | Edições: {r.get('edits', 0)}")
        lines.append(f"* **Fundamentação Teórica do Risco:** {fund_risco}")
        lines.append("")
        
        # DART dimensions detail
        lines.append("**Dimensões DART Analisadas:**")
        has_dims = False
        for d in ["dialogo", "acesso", "risco", "transparencia"]:
            d_obj = r.get(d)
            if isinstance(d_obj, dict) and d_obj.get("presente"):
                has_dims = True
                evid = d_obj.get("evidencia_literal", "").strip()
                interp = d_obj.get("interpretacao_teorica", "").strip()
                ctx = d_obj.get("contexto_jogo", "").strip()
                lines.append(f"- **{d.capitalize()} (Presente):**")
                if evid:
                    lines.append(f"  - *Evidência Literal:* \"{evid}\"")
                if interp:
                    lines.append(f"  - *Interpretação:* {interp}")
                if ctx:
                    lines.append(f"  - *Contexto:* {ctx}")
        if not has_dims:
            lines.append("- *(Nenhuma dimensão secundária assinalada como explicitamente ativa)*")
            
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))
    print(f"Sucesso: {output_file} criado com {total} análises.")


def convert_quality_audit_results():
    print("Processando quality_audit_results.json...")
    input_file = os.path.join(BASE_DIR, "data", "analysis", "quality_audit_results.json")
    output_file = os.path.join(OUTPUT_DIR, "leitura_quality_audit_results.md")

    if not os.path.exists(input_file):
        print(f"Aviso: {input_file} não encontrado.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    audited_at = data.get("audited_at", "N/A")
    total_analyses = data.get("total_analyses", 0)
    sample_size = data.get("sample_size", 0)
    avg_score = data.get("average_consistency_score", 0.0)
    failed = data.get("failed_audits", [])
    details = data.get("details", [])

    lines = []
    lines.append("# Relatório Legível de Auditoria de Qualidade (QualityGuard)")
    lines.append("")
    lines.append("Este documento apresenta a leitura humana dos resultados da auditoria de controlo de qualidade realizada pelo `QualityGuardAgent` (`deepseek-v4-pro` com modo pensamento) sobre a codificação netnográfica.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Sumário Executivo da Auditoria")
    lines.append("")
    lines.append(f"* **Data da Auditoria:** {audited_at}")
    lines.append(f"* **Universo Total de Análises:** {total_analyses} posts")
    lines.append(f"* **Tamanho da Amostra Auditada:** {sample_size} posts ({sample_size/total_analyses*100:.1f}%)")
    lines.append(f"* **Score Médio de Consistência Global:** **`{avg_score:.2f}%`** (Limiar mínimo de aprovação: 70.0%)")
    lines.append(f"* **Classificação Final:** **{'APROVADO' if avg_score >= 70.0 else 'REPROVADO'}**")
    lines.append(f"* **Auditorias com Alertas/Pontuação Baixa:** {len(failed)}")
    lines.append("")
    
    # Calculate criteria pass rates
    valid_details = [d for d in details if not d.get("api_error")]
    if valid_details:
        n_valid = len(valid_details)
        pass_literal = sum(1 for d in valid_details if d.get("evidencia_literal_existe", False)) / n_valid * 100
        pass_concept = sum(1 for d in valid_details if d.get("consistencia_conceitual", False)) / n_valid * 100
        pass_risk = sum(1 for d in valid_details if d.get("fundamentacao_risco_valida", False)) / n_valid * 100
        pass_meta = sum(1 for d in valid_details if d.get("coerencia_metadados", False)) / n_valid * 100

        lines.append("### Taxa de Aprovação por Critério Teórico")
        lines.append(f"* **Existência Literal da Evidência:** `{pass_literal:.1f}%` de conformidade (evidência existe no texto)")
        lines.append(f"* **Consistência Conceptual DART:** `{pass_concept:.1f}%` de conformidade teórica")
        lines.append(f"* **Fundamentação Válida do Risco:** `{pass_risk:.1f}%` de lógica de risco consistente")
        lines.append(f"* **Coerência de Metadados e QIs:** `{pass_meta:.1f}%` de conformidade de metadados")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 2. Auditorias com Alerta ou Falha Registada")
    lines.append("")
    if not failed:
        lines.append("Nenhuma falha detetada na amostra auditada.")
    else:
        lines.append("| ID do Post | Score | Motivo / Justificação da Auditoria |")
        lines.append("| :--- | :---: | :--- |")
        for item in failed[:30]:
            pid = item.get("post_id", "N/A")
            sc = item.get("score", 0)
            reason = item.get("reason", "Sem motivo especificado.").replace("\n", " ")
            lines.append(f"| `{pid}` | **{sc}** | {reason} |")
        if len(failed) > 30:
            lines.append(f"\n*(Exibindo as primeiras 30 de {len(failed)} ocorrências com alertas/erros)*\n")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Registo Detalhado da Amostra Auditada")
    lines.append("")

    for idx, d in enumerate(details, 1):
        pid = d.get("post_id", "N/A")
        score = d.get("score_auditoria", 0)
        literal = "SIM" if d.get("evidencia_literal_existe") else "NÃO"
        concept = "SIM" if d.get("consistencia_conceitual") else "NÃO"
        risk = "SIM" if d.get("fundamentacao_risco_valida") else "NÃO"
        meta = "SIM" if d.get("coerencia_metadados") else "NÃO"
        just = d.get("justificacao_auditoria", "Sem notas.")

        lines.append(f"### Post Auditado #{idx}: `{pid}` — Score: **{score}/100**")
        lines.append(f"* **Critérios:** Evidência Literal: **{literal}** | Conceito DART: **{concept}** | Risco Válido: **{risk}** | Metadados Coerentes: **{meta}**")
        lines.append(f"* **Justificação do Auditor Académico:** {just}")
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))
    print(f"Sucesso: {output_file} criado com {len(details)} auditorias detalhadas.")


def convert_quality_audit_interim():
    print("Processando data/interim/quality_audit.json...")
    input_file = os.path.join(BASE_DIR, "data", "interim", "quality_audit.json")
    output_file = os.path.join(OUTPUT_DIR, "leitura_quality_audit_interim.md")

    if not os.path.exists(input_file):
        print(f"Aviso: {input_file} não encontrado.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    audits = data.get("audits", [])

    lines = []
    lines.append("# Auditoria de Qualidade Inicial (Fase Intercalar / Protótipo)")
    lines.append("")
    lines.append("> [!NOTE]")
    lines.append("> Este documento reflete os dados do ficheiro de teste histórico `data/interim/quality_audit.json`, gerado durante os primeiros testes de prototipagem da pipeline (1 de julho de 2026). Para os resultados de produção completos e ativos, consulte `output/leitura_quality_audit_results.md`.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## 1. Registos Auditados no Protótipo ({len(audits)} posts de teste)")
    lines.append("")
    lines.append("| # | ID Auditado | Correspondência Literal | Consistência Score | Tipo Apropriado | QIs Corretas | Aprovado |")
    lines.append("| :--- | :--- | :---: | :---: | :---: | :---: | :---: |")
    for idx, a in enumerate(audits, 1):
        aid = a.get("audit_id", "N/A")
        lm = "SIM" if a.get("literal_match") else "NÃO"
        sc = "SIM" if a.get("score_consistency") else "NÃO"
        ta = "SIM" if a.get("type_appropriateness") else "NÃO"
        rq = "SIM" if a.get("rq_correctness") else "NÃO"
        acc = "**SIM**" if a.get("accepted") else "NÃO"
        lines.append(f"| {idx} | `{aid}` | {lm} | {sc} | {ta} | {rq} | {acc} |")

    lines.append("")
    lines.append("## 2. Notas Detalhadas de Cada Auditoria")
    lines.append("")
    for idx, a in enumerate(audits, 1):
        aid = a.get("audit_id", "N/A")
        notes = a.get("audit_notes", "Sem notas.")
        lines.append(f"### Teste #{idx}: `{aid}`")
        lines.append(f"* **Estado de Aceitação:** {'Aprovado' if a.get('accepted') else 'Rejeitado'}")
        lines.append(f"* **Notas da Auditoria:** {notes}")
        lines.append("")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))
    print(f"Sucesso: {output_file} criado com {len(audits)} registos.")

if __name__ == "__main__":
    convert_netnography_results()
    convert_quality_audit_results()
    convert_quality_audit_interim()
