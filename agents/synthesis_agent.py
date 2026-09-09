import os
import json
import logging
import re
import config
import api_client

logger = logging.getLogger("pipeline.synthesis_agent")

class SynthesisAgent:
    def __init__(self):
        self.processed_dir = config.DATA_PROCESSED_DIR
        self.analysis_dir = config.DATA_ANALYSIS_DIR
        self.output_dir = config.OUTPUT_DIR
        
    def _compile_metrics(self):
        # Load netnography results
        results_file = os.path.join(self.analysis_dir, "netnography_results.jsonl")
        if not os.path.exists(results_file):
            raise FileNotFoundError(f"Netnography results file not found at {results_file}")
            
        analyses = []
        with open(results_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    analyses.append(json.loads(line))
                    
        # Load quality audit results
        audit_file = os.path.join(self.analysis_dir, "quality_audit_results.json")
        audit_data = {}
        if os.path.exists(audit_file):
            try:
                with open(audit_file, "r", encoding="utf-8") as f:
                    audit_data = json.load(f)
            except Exception as e:
                logger.error(f"Failed to read audit results: {e}")
                
        # Load cost tracking
        cost_file = os.path.join(config.DATA_INTERIM_DIR, "custos_pipeline.json")
        total_cost = 0.0
        if os.path.exists(cost_file):
            try:
                with open(cost_file, "r", encoding="utf-8") as f:
                    total_cost = json.load(f).get("total_cost_usd", 0.0)
            except Exception:
                pass
                
        # Compile counts
        total_analyzed = len(analyses)
        eve_count = sum(1 for a in analyses if (a.get("game") or a.get("jogo")) == "EVE Online")
        wow_count = sum(1 for a in analyses if (a.get("game") or a.get("jogo")) == "World of Warcraft")
        
        # Calculate Discourse metadata statistics
        avg_likes_eve = sum(a.get("likes", 0) for a in analyses if (a.get("game") or a.get("jogo")) == "EVE Online") / eve_count if eve_count else 0.0
        avg_likes_wow = sum(a.get("likes", 0) for a in analyses if (a.get("game") or a.get("jogo")) == "World of Warcraft") / wow_count if wow_count else 0.0
        
        avg_trust_eve = sum(a.get("trust_level", 0) for a in analyses if (a.get("game") or a.get("jogo")) == "EVE Online") / eve_count if eve_count else 0.0
        avg_trust_wow = sum(a.get("trust_level", 0) for a in analyses if (a.get("game") or a.get("jogo")) == "World of Warcraft") / wow_count if wow_count else 0.0
        
        avg_edits = sum(a.get("edits", 1) for a in analyses) / total_analyzed if total_analyzed else 1.0
        
        # DART-NET: AI Type distribution (A1-A6)
        ai_type_dist = {"A1": 0, "A2": 0, "A3": 0, "A4": 0, "A5": 0, "A6": 0}
        for a in analyses:
            atype = a.get("ai_type", "A2")
            if atype in ai_type_dist:
                ai_type_dist[atype] += 1
                
        # DART-NET: Interaction structure distribution (I1-I6)
        interaction_dist = {"I1": 0, "I2": 0, "I3": 0, "I4": 0, "I5": 0, "I6": 0}
        for a in analyses:
            itype = a.get("interaction_type", "I4")
            if itype in interaction_dist:
                interaction_dist[itype] += 1
                
        # DART-NET: Value co-creation distribution (VC1-VC4)
        value_dist = {"VC1": 0, "VC2": 0, "VC3": 0, "VC4": 0}
        for a in analyses:
            vtype = a.get("value_type", "VC4")
            if vtype in value_dist:
                value_dist[vtype] += 1
                
        # DART-NET: DART 0-5 score averages
        d_scores = [a.get("dart", {}).get("dialogue", {}).get("score", 0) for a in analyses]
        a_scores = [a.get("dart", {}).get("access", {}).get("score", 0) for a in analyses]
        r_scores = [a.get("dart", {}).get("risk", {}).get("score", a.get("score_risco_percebido", 0)) for a in analyses]
        t_scores = [a.get("dart", {}).get("transparency", {}).get("score", 0) for a in analyses]
        
        avg_d = sum(d_scores) / total_analyzed if total_analyzed else 0.0
        avg_a = sum(a_scores) / total_analyzed if total_analyzed else 0.0
        avg_r = sum(r_scores) / total_analyzed if total_analyzed else 0.0
        avg_t = sum(t_scores) / total_analyzed if total_analyzed else 0.0
        
        # DART-NET: Human review required count
        human_review_count = sum(1 for a in analyses if a.get("human_review_required", False))
        human_review_pct = (human_review_count / total_analyzed * 100) if total_analyzed else 0.0
        
        # Legacy Co-creation distribution (simetrica, assimetrica, parasitaria)
        cocreation_dist = {"simetrica": 0, "assimetrica": 0, "parasitaria": 0}
        for a in analyses:
            typ = (a.get("tipologia_cocriacao") or a.get("tipologia_criacao") or "parasitaria").lower()
            if typ in cocreation_dist:
                cocreation_dist[typ] += 1
                
        # Legacy Dominant dimension
        dim_dist = {"dialogo": 0, "acesso": 0, "risco": 0, "transparencia": 0}
        for a in analyses:
            dim = (a.get("dimensao_dominante") or "risco").lower()
            if dim in dim_dist:
                dim_dist[dim] += 1
                
        metrics = {
            "total_analyzed": total_analyzed,
            "eve_count": eve_count,
            "wow_count": wow_count,
            "ai_type_distribution": ai_type_dist,
            "interaction_distribution": interaction_dist,
            "value_distribution": value_dist,
            "dart_averages": {
                "dialogue": avg_d,
                "access": avg_a,
                "risk": avg_r,
                "transparency": avg_t
            },
            "human_review_count": human_review_count,
            "human_review_pct": human_review_pct,
            "cocreation_distribution": cocreation_dist,
            "dimension_distribution": dim_dist,
            "average_risk_global": avg_r,
            
            # Discourse metrics
            "average_likes_eve": avg_likes_eve,
            "average_likes_wow": avg_likes_wow,
            "average_trust_eve": avg_trust_eve,
            "average_trust_wow": avg_trust_wow,
            "average_edits": avg_edits,
            
            "average_quality_score": audit_data.get("average_consistency_score", 0.0),
            "total_cost_usd": total_cost,
            "analyses": analyses
        }
        
        return metrics

    def run(self):
        logger.info("SynthesisAgent starting report compilation...")
        cost_file = os.path.join(config.DATA_INTERIM_DIR, "custos_pipeline.json")
        try:
            metrics = self._compile_metrics()
        except Exception as e:
            logger.error(f"Failed to compile metrics for synthesis: {e}")
            raise e
            
        # Structure the prompt with statistics and representative analyses summaries
        analyses = metrics["analyses"]
        import random
        random.seed(42)
        sample_analyses = random.sample(analyses, min(80, len(analyses))) if analyses else []
        
        analyses_summary = []
        for index, a in enumerate(sample_analyses):
            # Summarize each analysis for the writer LLM
            dart = a.get("dart", {})
            dialogue_pres = "Sim" if (a.get("dialogo", {}).get("presente") or dart.get("dialogue", {}).get("score", 0) > 0) else "Não"
            access_pres = "Sim" if (a.get("acesso", {}).get("presente") or dart.get("access", {}).get("score", 0) > 0) else "Não"
            risk_pres = "Sim" if (a.get("risco", {}).get("presente") or dart.get("risk", {}).get("score", 0) > 0) else "Não"
            trans_pres = "Sim" if (a.get("transparencia", {}).get("presente") or dart.get("transparency", {}).get("score", 0) > 0) else "Não"
            
            ai_type = a.get("ai_type", "A2")
            inter_type = a.get("interaction_type", "I4")
            val_type = a.get("value_type", "VC4")
            
            summary = (
                f"- Post ID: {a.get('post_id')} | Jogo: {a.get('jogo') or a.get('game')}\n"
                f"  Classificação DART-NET: Tipo IA={ai_type}, Interação={inter_type}, Valor={val_type}\n"
                f"  Dimensões - Diálogo: {dialogue_pres}, Acesso: {access_pres}, Risco: {risk_pres}, Transparência: {trans_pres}\n"
                f"  Dominante: {a.get('dimensao_dominante', 'risco')} | Risco: {a.get('score_risco_percebido', 1)}/5 | Cocriação: {a.get('tipologia_cocriacao') or a.get('tipologia_criacao') or 'parasitaria'}\n"
                f"  Metadados: Likes={a.get('likes', 0)}, Confiança Autor={a.get('trust_level', 0)}, Edições={a.get('edits', 1)}\n"
                f"  Evidência/Fundamentação: {a.get('fundamentacao_risco') or a.get('classification_notes', '')}\n"
            )
            analyses_summary.append(summary)
            
        analyses_text = "\n".join(analyses_summary)
        
        system_prompt = (
            "És um cientista de computação e sociólogo digital especializado em netnografia e ecossistemas virtuais.\n"
            "O teu objetivo é redigir um relatório académico de alto nível, profundo e formal, em português de Portugal.\n"
            "O relatório analisa a interação entre humanos e agentes de IA e a cocriação de valor em ecossistemas de videojogos, "
            "aplicando o Framework DART-NET (Prahalad & Ramaswamy, 2004; DART-NET 2026).\n\n"
            "O relatório deve ser estruturado em Markdown com exatamente estas 8 secções:\n"
            "1. Sumário Metodológico e Framework DART-NET (descrever a metodologia, a distinção entre IA e automação convencional A1-A6, e listar as 5 Questões de Investigação: QI1 a QI5)\n"
            "2. Taxonomia de Agentes de IA e Interações (A1-A6 e I1-I6: proporção de agentes autónomos vs bots/scripts convencionais e estruturas de interação)\n"
            "3. Análise por Dimensão DART (avaliação independente de Diálogo, Acesso, Risco e Transparência na escala 0 a 5 com evidências empíricas)\n"
            "4. Análise Comparativa de Jogos (Sandbox vs. Controlado: EVE Online vs. World of Warcraft)\n"
            "5. Cocriação e Codestruição de Valor (VC1 a VC4: análise da distribuição de valor entre jogadores e sistemas automatizados)\n"
            "6. Reflexão sobre as Questões de Investigação (QI1 a QI5 fundamentadas em evidências empíricas concretas e IDs de posts)\n"
            "7. Auditoria de Qualidade, Calibração e Fila de Validação Humana (desempenho da auditoria deepseek-v4-pro e percentagem de human_review_required)\n"
            "8. Discussão Teórica, Reprodutibilidade e Limitações (separação em 3 camadas, ética e caminhos futuros)\n\n"
            "Instruções Específicas de Linguagem:\n"
            "- Escreve estritamente em português de Portugal (ex: 'videojogos', 'utilizadores', 'ficheiros', 'equipa', 'análise', 'dados').\n"
            "- Mantém um tom académico formal, rigoroso, transparente e analítico.\n\n"
            "Não adicione notas fora do Markdown do relatório."
        )
        
        user_prompt = (
            f"Por favor, redige o relatório com base nas seguintes estatísticas e resumos recolhidos pela pipeline DART-NET:\n\n"
            f"[ESTATÍSTICAS GLOBAIS DART-NET]\n"
            f"- Total de posts analisados: {metrics['total_analyzed']}\n"
            f"  - EVE Online (Sandbox): {metrics['eve_count']}\n"
            f"  - World of Warcraft (Controlado / Theme Park): {metrics['wow_count']}\n"
            f"- Distribuição de Tipos de IA (A1-A6):\n"
            f"  - A1 (AI Agent): {metrics['ai_type_distribution']['A1']}\n"
            f"  - A2 (Conventional Bot): {metrics['ai_type_distribution']['A2']}\n"
            f"  - A3 (Script/Automation): {metrics['ai_type_distribution']['A3']}\n"
            f"  - A4 (AI-Assisted Human): {metrics['ai_type_distribution']['A4']}\n"
            f"  - A5 (Discussion About AI): {metrics['ai_type_distribution']['A5']}\n"
            f"  - A6 (Irrelevant): {metrics['ai_type_distribution']['A6']}\n"
            f"- Estrutura de Interação Humano-IA (I1-I6):\n"
            f"  - I1 (Humano -> IA): {metrics['interaction_distribution']['I1']}\n"
            f"  - I2 (IA -> Humano): {metrics['interaction_distribution']['I2']}\n"
            f"  - I3 (Humano <-> IA Bidirecional): {metrics['interaction_distribution']['I3']}\n"
            f"  - I4 (Humano -> Humano sobre IA): {metrics['interaction_distribution']['I4']}\n"
            f"  - I5 (Humano -> Ambiente mediado por IA): {metrics['interaction_distribution']['I5']}\n"
            f"  - I6 (Sem interação significativa): {metrics['interaction_distribution']['I6']}\n"
            f"- Cocriação de Valor (VC1-VC4):\n"
            f"  - VC1 (Cocriação de Valor): {metrics['value_distribution']['VC1']}\n"
            f"  - VC2 (Potencial Cocriação): {metrics['value_distribution']['VC2']}\n"
            f"  - VC3 (Codestruição de Valor): {metrics['value_distribution']['VC3']}\n"
            f"  - VC4 (Sem evidência de criação/destruição): {metrics['value_distribution']['VC4']}\n"
            f"- Médias das Dimensões DART (Escala 0 a 5):\n"
            f"  - Diálogo: {metrics['dart_averages']['dialogue']:.2f}/5\n"
            f"  - Acesso: {metrics['dart_averages']['access']:.2f}/5\n"
            f"  - Risco: {metrics['dart_averages']['risk']:.2f}/5\n"
            f"  - Transparência: {metrics['dart_averages']['transparency']:.2f}/5\n"
            f"- Fila de Validação Humana (Human Review Required):\n"
            f"  - Posts sinalizados para revisão humana: {metrics['human_review_count']} ({metrics['human_review_pct']:.1f}%)\n"
            f"- Metadados Médios da API do Discourse:\n"
            f"  - Média de Gostos (EVE Online): {metrics['average_likes_eve']:.1f}\n"
            f"  - Média de Gostos (World of Warcraft): {metrics['average_likes_wow']:.1f}\n"
            f"  - Média do Nível de Confiança do Autor (EVE Online): {metrics['average_trust_eve']:.1f}\n"
            f"  - Média do Nível de Confiança do Autor (World of Warcraft): {metrics['average_trust_wow']:.1f}\n"
            f"  - Média do Histórico de Edições: {metrics['average_edits']:.1f}\n"
            f"- Auditoria de Qualidade e Custos:\n"
            f"  - Score Médio de Consistência da Auditoria: {metrics['average_quality_score']:.1f}%\n"
            f"  - Custo total da pipeline em API: ${metrics['total_cost_usd']:.4f} USD\n\n"
            f"[AMOSTRA DE RESUMOS DAS ANÁLISES DOS POSTS]\n"
            f"{analyses_text}\n"
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        try:
            # SynthesisAgent: deepseek-v4-pro, thinking enabled (reasoning model)
            report_content, _ = api_client.call_llm(
                model=config.MODEL_PRO,
                messages=messages,
                thinking_enabled=True,
                temperature=0.3,
                max_tokens=8000
            )
            
            output_file = os.path.join(self.output_dir, "relatorio_netnografia.md")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(report_content)
                
            # Create a markdown cost summary table and remove raw json cost log
            try:
                if os.path.exists(cost_file):
                    with open(cost_file, "r", encoding="utf-8") as cf:
                        cost_data = json.load(cf)
                    
                    # Group costs by model
                    model_stats = {}
                    for call in cost_data.get("calls", []):
                        m = call.get("model", "unknown")
                        if m not in model_stats:
                            model_stats[m] = {"calls": 0, "prompt": 0, "completion": 0, "cost": 0.0}
                        model_stats[m]["calls"] += 1
                        model_stats[m]["prompt"] += call.get("prompt_tokens", 0)
                        model_stats[m]["completion"] += call.get("completion_tokens", 0)
                        model_stats[m]["cost"] += call.get("cost_usd", 0.0)
                    
                    # Build markdown
                    md_lines = [
                        "# Tabela de Custos do Pipeline",
                        "",
                        "Resumo detalhado dos custos de chamadas de API acumulados durante a execução do pipeline netnográfico.",
                        "",
                        "| Modelo | Chamadas | Tokens de Prompt | Tokens de Conclusão | Custo Total (USD) |",
                        "| :--- | :---: | :---: | :---: | :---: |"
                    ]
                    for m, stat in model_stats.items():
                        md_lines.append(f"| `{m}` | {stat['calls']} | {stat['prompt']:,} | {stat['completion']:,} | ${stat['cost']:.6f} USD |")
                    
                    md_lines.append(f"| **Total Acumulado** | **{sum(s['calls'] for s in model_stats.values())}** | **{sum(s['prompt'] for s in model_stats.values()):,}** | **{sum(s['completion'] for s in model_stats.values()):,}** | **${cost_data.get('total_cost_usd', 0.0):.6f} USD** |")
                    
                    cost_table_path = os.path.join(self.output_dir, "tabela_custos.md")
                    with open(cost_table_path, "w", encoding="utf-8") as ctf:
                        ctf.write("\n".join(md_lines) + "\n")
                    logger.info(f"Cost summary table compiled and saved to {cost_table_path}.")
            except Exception as ce:
                logger.error(f"Failed to generate cost table: {ce}")
                
            logger.info(f"SynthesisAgent complete. Academic report saved to {output_file}.")
            return report_content
            
        except Exception as e:
            logger.error(f"Failed to generate synthesis report: {e}")
            raise e

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = SynthesisAgent()
    agent.run()
