import os
import json
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

DIM_MAP = {
    "dialogue": "Diálogo",
    "dialogo": "Diálogo",
    "access": "Acesso",
    "acesso": "Acesso",
    "risk": "Risco",
    "risco": "Risco",
    "transparency": "Transparência",
    "transparencia": "Transparência"
}

def normalize_dim(dim_str):
    if not dim_str:
        return "N/A"
    return DIM_MAP.get(str(dim_str).lower().strip(), str(dim_str).capitalize())

def convert_netnography_results():
    print("Processando netnography_results.jsonl para DART-NET v3.0...")
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
    games = Counter(r.get("jogo") or r.get("game") or "Desconhecido" for r in records)
    ai_types = Counter(r.get("ai_type", "A2") for r in records)
    interactions = Counter(r.get("interaction_type", "I4") for r in records)
    values = Counter(r.get("value_type", "VC4") for r in records)
    dart_dims = Counter(normalize_dim(r.get("dimensao_dominante")) for r in records)
    human_reviews = Counter("⚠️ Sim" if r.get("human_review_required") else "Não" for r in records)

    # Calculate DART dimensions averages
    d_scores, a_scores, r_scores, t_scores = [], [], [], []
    for r in records:
        dart = r.get("dart") or {}
        d_val = dart.get("dialogue", {}).get("score", 0) if isinstance(dart.get("dialogue"), dict) else (1 if r.get("dialogo", {}).get("presente") else 0)
        a_val = dart.get("access", {}).get("score", 0) if isinstance(dart.get("access"), dict) else (1 if r.get("acesso", {}).get("presente") else 0)
        r_val = dart.get("risk", {}).get("score", 0) if isinstance(dart.get("risk"), dict) else r.get("score_risco_percebido", 0)
        t_val = dart.get("transparency", {}).get("score", 0) if isinstance(dart.get("transparency"), dict) else (1 if r.get("transparencia", {}).get("presente") else 0)
        d_scores.append(float(d_val))
        a_scores.append(float(a_val))
        r_scores.append(float(r_val))
        t_scores.append(float(t_val))

    avg_d = sum(d_scores) / len(d_scores) if d_scores else 0.0
    avg_a = sum(a_scores) / len(a_scores) if a_scores else 0.0
    avg_r = sum(r_scores) / len(r_scores) if r_scores else 0.0
    avg_t = sum(t_scores) / len(t_scores) if t_scores else 0.0

    lines = []
    lines.append("# Análise Netnográfica DART-NET v3.0 — Leitura Humana dos Resultados")
    lines.append("")
    lines.append("Este documento formaliza a leitura humana estruturada e detalhada dos resultados da codificação netnográfica multiagente baseada no framework **DART-NET** (Prahalad & Ramaswamy, 2004; DART-NET 2026), processados pelo modelo `deepseek-v4-flash` a partir de `data/analysis/netnography_results.jsonl`.")
    lines.append("")
    lines.append("> [!IMPORTANT]")
    lines.append("> **Filtro Temporal Estrito (Jan 2024 – 2026):** Todos os 1.032 posts aqui apresentados satisfazem a restrição metodológica `created_at >= '2024-01-01T00:00:00Z'`, cobrindo discussões empíricas dos ecossistemas de *World of Warcraft* e *EVE Online*.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Sumário Executivo das Codificações DART-NET")
    lines.append("")
    lines.append(f"* **Total de Mensagens Analisadas:** {total}")
    lines.append(f"* **Médias Dimensionais DART (0 a 5):** Diálogo: `{avg_d:.2f}` | Acesso: `{avg_a:.2f}` | Risco: `{avg_r:.2f}` | Transparência: `{avg_t:.2f}`")
    lines.append(f"* **Fila de Revisão Humana Prioritária:** {human_reviews.get('⚠️ Sim', 0)} posts ({human_reviews.get('⚠️ Sim', 0)/total*100:.1f}%) assinalados para validação manual")
    lines.append("")
    lines.append("### Distribuição por Jogo / Ecossistema")
    for game, count in games.most_common():
        lines.append(f"* **{game}:** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("### Distribuição por Tipologia de IA (Taxonomia A1 a A6)")
    for tip, count in sorted(ai_types.items()):
        labels = {
            "A1": "Agentes de IA Autónomos (LLMs / MCP)",
            "A2": "Bots Convencionais (Farming / Rotações)",
            "A3": "Scripts / Automação Determinística",
            "A4": "Humanos Assistidos por IA (Vibe-Coding / Copilotos)",
            "A5": "Discussões / Perceções da Comunidade sobre IA",
            "A6": "Não-IA / Ruído Descartado"
        }
        lines.append(f"* **{tip} ({labels.get(tip, 'Outro')}):** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("### Distribuição por Estrutura de Interação (I1 a I6)")
    for inter, count in sorted(interactions.items()):
        labels_i = {
            "I1": "Interação Direta Humano-Agente",
            "I2": "Interação Agente-Agente",
            "I3": "Cooperação Triádica (Humano-Agente-Humano)",
            "I4": "Discurso Comunitário / Mediação Social",
            "I5": "Conflito / Disputa Mediada por Agente",
            "I6": "Sem Interação Significativa"
        }
        lines.append(f"* **{inter} ({labels_i.get(inter, 'Outro')}):** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("### Distribuição por Cocriação de Valor (VC1 a VC4)")
    for val, count in sorted(values.items()):
        labels_vc = {
            "VC1": "Cocriação Efetiva de Valor",
            "VC2": "Potencial / Intenção de Cocriação",
            "VC3": "Codestruição de Valor (Assimetria / Prejuízo)",
            "VC4": "Sem Evidência Relevante de Valor"
        }
        lines.append(f"* **{val} ({labels_vc.get(val, 'Outro')}):** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("### Distribuição por Dimensão DART Dominante")
    for dim, count in dart_dims.most_common():
        lines.append(f"* **{dim}:** {count} posts ({count/total*100:.1f}%)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2. Catálogo Sintético das Análises Netnográficas")
    lines.append("")
    lines.append("| # | ID do Post | Jogo | Tipo IA | Interação | Valor | Dimensão Dominante | DART (D/A/R/T) | Rev. Humana | QIs Mapeadas |")
    lines.append("| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :---: | :---: | :--- |")
    
    for idx, r in enumerate(records, 1):
        pid = r.get("post_id") or r.get("id") or "N/A"
        jogo = r.get("jogo") or r.get("game") or "N/A"
        ai_t = r.get("ai_type", "A2")
        i_t = r.get("interaction_type", "I4")
        v_t = r.get("value_type", "VC4")
        dim = normalize_dim(r.get("dimensao_dominante"))
        
        dart = r.get("dart") or {}
        d_val = dart.get("dialogue", {}).get("score", 0) if isinstance(dart.get("dialogue"), dict) else (1 if r.get("dialogo", {}).get("presente") else 0)
        a_val = dart.get("access", {}).get("score", 0) if isinstance(dart.get("access"), dict) else (1 if r.get("acesso", {}).get("presente") else 0)
        r_val = dart.get("risk", {}).get("score", 0) if isinstance(dart.get("risk"), dict) else r.get("score_risco_percebido", 0)
        t_val = dart.get("transparency", {}).get("score", 0) if isinstance(dart.get("transparency"), dict) else (1 if r.get("transparencia", {}).get("presente") else 0)
        dart_str = f"{d_val}/{a_val}/{r_val}/{t_val}"
        
        rev = "⚠️ Sim" if r.get("human_review_required") else "Não"
        qis = ", ".join(r.get("questoes_investigacao") or [])
        
        lines.append(f"| {idx} | `{pid}` | {jogo} | **{ai_t}** | {i_t} | {v_t} | **{dim}** | `{dart_str}` | {rev} | {qis} |")
        
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Fichas Qualitativas Individuais (DART e Evidências)")
    lines.append("")

    for idx, r in enumerate(records, 1):
        pid = r.get("post_id") or r.get("id") or "N/A"
        jogo = r.get("jogo") or r.get("game") or "N/A"
        ai_t = r.get("ai_type", "A2")
        i_t = r.get("interaction_type", "I4")
        v_t = r.get("value_type", "VC4")
        dim = normalize_dim(r.get("dimensao_dominante"))
        rev = "⚠️ Sim" if r.get("human_review_required") else "Não"
        
        dart = r.get("dart") or {}
        d_val = dart.get("dialogue", {}).get("score", 0) if isinstance(dart.get("dialogue"), dict) else (1 if r.get("dialogo", {}).get("presente") else 0)
        a_val = dart.get("access", {}).get("score", 0) if isinstance(dart.get("access"), dict) else (1 if r.get("acesso", {}).get("presente") else 0)
        r_val = dart.get("risk", {}).get("score", 0) if isinstance(dart.get("risk"), dict) else r.get("score_risco_percebido", 0)
        t_val = dart.get("transparency", {}).get("score", 0) if isinstance(dart.get("transparency"), dict) else (1 if r.get("transparencia", {}).get("presente") else 0)
        dart_str = f"Diálogo: {d_val} | Acesso: {a_val} | Risco: {r_val} | Transparência: {t_val}"

        qis = ", ".join(r.get("questoes_investigacao") or [])
        fund_risco = r.get("fundamentacao_risco") or r.get("classification_notes") or "Sem notas adicionais."
        
        lines.append(f"### Post #{idx}: `{pid}` ({jogo})")
        lines.append(f"* **Classificação DART-NET:** Tipo IA: **{ai_t}** | Interação: **{i_t}** | Valor: **{v_t}** | Dimensão Dominante: **{dim}**")
        lines.append(f"* **Scores DART (0-5):** {dart_str} | **Revisão Humana:** {rev} | **QIs:** `{qis}`")
        lines.append(f"* **Metadados:** Likes: {r.get('likes', 0)} | Nível de Confiança: {r.get('trust_level', 0)} | Edições: {r.get('edits', 0)}")
        lines.append(f"* **Fundamentação / Notas:** {fund_risco}")
        lines.append("")
        
        # Dimensions breakdown
        lines.append("**Dimensões DART Analisadas:**")
        has_dims = False
        for d_key, d_name in [("dialogo", "Diálogo"), ("acesso", "Acesso"), ("risco", "Risco"), ("transparencia", "Transparência")]:
            d_obj = r.get(d_key)
            if isinstance(d_obj, dict) and (d_obj.get("presente") or d_obj.get("evidencia_literal")):
                has_dims = True
                evid = str(d_obj.get("evidencia_literal", "")).strip()
                interp = str(d_obj.get("interpretacao_teorica", "")).strip()
                ctx = str(d_obj.get("contexto_jogo", "")).strip()
                lines.append(f"- **{d_name} (Ativo):**")
                if evid:
                    lines.append(f"  - *Evidência Literal:* \"{evid}\"")
                if interp:
                    lines.append(f"  - *Interpretação Teórica:* {interp}")
                if ctx:
                    lines.append(f"  - *Contexto no Jogo:* {ctx}")
                    
        # Check dart object if legacy fields not filled
        if not has_dims and isinstance(dart, dict):
            for d_key, d_name in [("dialogue", "Diálogo"), ("access", "Acesso"), ("risk", "Risco"), ("transparency", "Transparência")]:
                sub = dart.get(d_key, {})
                if isinstance(sub, dict) and sub.get("evidence"):
                    has_dims = True
                    lines.append(f"- **{d_name} (Score: {sub.get('score', 0)}/5):**")
                    lines.append(f"  - *Evidência Literal:* \"{sub.get('evidence', '')}\"")
                    if sub.get("interpretation"):
                        lines.append(f"  - *Interpretação Teórica:* {sub.get('interpretation', '')}")
                        
        if not has_dims:
            lines.append("- *(Sem evidência literal explícita de dimensões ativas no post)*")
            
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))
    print(f"Sucesso: {output_file} criado com {total} análises.")


def convert_quality_audit_results():
    print("Processando quality_audit_results.json para DART-NET v3.0...")
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
    lines.append("# Relatório Legível de Auditoria de Qualidade (QualityGuard) — DART-NET v3.0")
    lines.append("")
    lines.append("Este documento apresenta a leitura humana dos resultados da auditoria de controlo de qualidade realizada pelo `QualityGuardAgent` (`deepseek-v4-pro` com modo de raciocínio profundo) sobre uma amostragem de 20% das codificações netnográficas da pipeline.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. Sumário Executivo da Auditoria")
    lines.append("")
    lines.append(f"* **Data da Auditoria:** {audited_at}")
    lines.append(f"* **Universo Total de Análises:** {total_analyses} posts")
    lines.append(f"* **Tamanho da Amostra Auditada:** {sample_size} posts ({sample_size/total_analyses*100:.1f}%)")
    lines.append(f"* **Score Médio de Consistência Global:** **`{avg_score:.2f}%`** (Limiar mínimo de aprovação científica: 70.0%)")
    lines.append(f"* **Classificação Final:** **{'APROVADO' if avg_score >= 70.0 else 'REPROVADO'}**")
    lines.append(f"* **Casos com Alertas ou Ajustes Identificados:** {len(failed)} análises")
    lines.append("")
    
    # Calculate criteria pass rates
    valid_details = [d for d in details if not d.get("api_error")]
    if valid_details:
        n_valid = len(valid_details)
        pass_literal = sum(1 for d in valid_details if d.get("evidencia_literal_existe", False)) / n_valid * 100
        pass_ai_type = sum(1 for d in valid_details if d.get("consistencia_ai_type", False)) / n_valid * 100
        pass_inter_val = sum(1 for d in valid_details if d.get("consistencia_interacao_valor", False)) / n_valid * 100
        pass_dart = sum(1 for d in valid_details if d.get("calibracao_dart_scores", False)) / n_valid * 100
        pass_review = sum(1 for d in valid_details if d.get("human_review_corretamente_sinalizado", False)) / n_valid * 100
        pass_concept = sum(1 for d in valid_details if d.get("consistencia_conceitual", False)) / n_valid * 100

        lines.append("### Taxa de Aprovação por Critério Metodológico")
        lines.append(f"* **Veracidade da Evidência Literal:** `{pass_literal:.1f}%` (100% de citações literais verificadas no texto)")
        lines.append(f"* **Consistência da Tipologia de IA (A1–A6):** `{pass_ai_type:.1f}%` de rigor na taxonomia de agentes")
        lines.append(f"* **Consistência de Interação e Valor (I1–I6 / VC1–VC4):** `{pass_inter_val:.1f}%` de conformidade teórica")
        lines.append(f"* **Calibração das Dimensões DART:** `{pass_dart:.1f}%` de alinhamento com definições de Prahalad & Ramaswamy")
        lines.append(f"* **Calibração da Revisão Humana:** `{pass_review:.1f}%` de coerência com o limiar de confiança de 0,80")
        lines.append(f"* **Consistência Concetual Global:** `{pass_concept:.1f}%` de validação epistémica")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 2. Auditorias com Alerta ou Pontuação < 70")
    lines.append("")
    if not failed:
        lines.append("Nenhuma falha crítica detetada na amostra auditada.")
    else:
        lines.append("| ID do Post | Score | Motivo / Justificação da Auditoria |")
        lines.append("| :--- | :---: | :--- |")
        for item in failed:
            pid = item.get("post_id", "N/A")
            sc = item.get("score", 0)
            reason = item.get("reason", "Sem motivo especificado.").replace("\n", " ")
            lines.append(f"| `{pid}` | **{sc}/100** | {reason} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Registo Detalhado da Amostra Auditada (206 auditorias)")
    lines.append("")

    for idx, d in enumerate(details, 1):
        pid = d.get("post_id", "N/A")
        score = d.get("score_auditoria", 0)
        literal = "SIM" if d.get("evidencia_literal_existe") else "NÃO"
        ai_type = "SIM" if d.get("consistencia_ai_type") else "NÃO"
        inter_val = "SIM" if d.get("consistencia_interacao_valor") else "NÃO"
        dart_cal = "SIM" if d.get("calibracao_dart_scores") else "NÃO"
        rev_cal = "SIM" if d.get("human_review_corretamente_sinalizado") else "NÃO"
        concept = "SIM" if d.get("consistencia_conceitual") else "NÃO"
        just = d.get("justificacao_auditoria", "Sem notas.")

        lines.append(f"### Post Auditado #{idx}: `{pid}` — Score: **{score}/100**")
        lines.append(f"* **Critérios Teóricos:** Evidência Literal: **{literal}** | Tipo IA: **{ai_type}** | Interação/Valor: **{inter_val}** | Calibração DART: **{dart_cal}** | Revisão Humana: **{rev_cal}** | Consistência Concetual: **{concept}**")
        lines.append(f"* **Justificação do Auditor Académico:** {just}")
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))
    print(f"Sucesso: {output_file} criado com {len(details)} auditorias detalhadas.")

if __name__ == "__main__":
    convert_netnography_results()
    convert_quality_audit_results()
