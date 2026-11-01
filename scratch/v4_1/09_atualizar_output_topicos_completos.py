"""DART-NET v4.1 — passa os resultados dos tópicos completos para os ficheiros de output/ (aprovado pelo investigador).

Etapa 2: Emmanoel, Roger e Gomide (ainda por preencher) recebem o resumo novo em Resumo_IA.
         JPaulo (já avaliou os resumos antigos) mantém tudo e ganha colunas K–P para avaliar o resumo novo.
Chave:   colunas holísticas passam para a leitura dos tópicos completos; nova coluna com o nº de posts do tópico completo.
"""
import copy, json, os
from collections import Counter

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = lambda f: os.path.join(ROOT, "output", f)
A = lambda f: os.path.join(ROOT, "data", "analysis", f)

res = json.load(open(A("topic_discussions_insights_v4_1_completos.json")))
hol = json.load(open(A("topic_holistic_coding_v4_1_completos.json")))
n_posts = Counter(json.loads(l)["thread_id"] for l in open(os.path.join(ROOT, "data", "processed", "topicos_completos_v4_1.jsonl")))
resolve = lambda x: x if x in hol else ("reddit_" + x if "reddit_" + x in hol else x.replace("reddit_", ""))

INSTR_RESUMO = ("Resumo_IA — resumo gerado pela pipeline a partir do tópico completo (todos os posts recolhidos, por ordem "
                "cronológica, incluindo o post de abertura). Não alterar.")


def etapa2(coder):
    f = OUT(f"etapa_2_Avaliacao_Resumos_{coder}.xlsx")
    wb = openpyxl.load_workbook(f)
    ws, ins = wb["Avaliacao_Resumos"], wb["Instrucoes"]
    ins["A22"].value = INSTR_RESUMO
    if coder != "JPaulo":
        for r in range(2, ws.max_row + 1):
            if ws.cell(r, 1).value:
                ws.cell(r, 5).value = res[str(ws.cell(r, 1).value)]["resumo_extenso_discussao"]
        wb.save(f)
        return
    # JPaulo: a avaliação dos resumos antigos fica como registo; acrescentam-se colunas para o resumo novo
    heads = ["Resumo_IA_v2 (tópico completo)", "JPaulo_Fidelidade_Sintese_v2 (1-5)", "JPaulo_Erros_Factuais_v2",
             "JPaulo_Omissoes_Relevantes_v2", "JPaulo_Leitura_Tom_Retorico_v2", "JPaulo_Notas_v2"]
    last = max(r for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value)
    for i, h in enumerate(heads):
        src, dst = 5 + i, 11 + i  # E..J -> K..P
        for r in range(1, last + 1):
            s, d = ws.cell(r, src), ws.cell(r, dst)
            d._style = copy.copy(s._style)
            d.value = h if r == 1 else (res[str(ws.cell(r, 1).value)]["resumo_extenso_discussao"] if i == 0 else None)
        L = lambda c: openpyxl.utils.get_column_letter(c)
        ws.column_dimensions[L(dst)].width = ws.column_dimensions[L(src)].width
    for dv in list(ws.data_validations.dataValidation):
        col = str(dv.sqref).split(":")[0].rstrip("0123456789")
        new = DataValidation(type=dv.type, formula1=dv.formula1, allow_blank=dv.allow_blank, showErrorMessage=dv.showErrorMessage,
                             errorTitle=dv.errorTitle, error=dv.error)
        nc = openpyxl.utils.get_column_letter(openpyxl.utils.column_index_from_string(col) + 6)
        new.add(f"{nc}2:{nc}{last}")
        ws.add_data_validation(new)
    row = ins.max_row + 2
    lines = ["7. REAVALIAÇÃO DOS RESUMOS NOVOS (colunas K–P)",
             "Os resumos das colunas E–J foram gerados a partir dos posts filtrados por relevância (em média 6 de cada tópico) e "
             "sem o texto do post de abertura do Reddit. A sua avaliação desses resumos fica registada e não deve ser alterada.",
             "Os resumos da coluna K (Resumo_IA_v2) foram gerados com o mesmo agente e o mesmo modelo, mas a partir do tópico completo. "
             "Avalie-os nas colunas L–P com as mesmas regras e a mesma escala (secções 4 e 5)."]
    for k, t in enumerate(lines):
        c = ins.cell(row + k, 1, t)
        c._style = copy.copy(ins["A19" if k == 0 else "A20"]._style)
    wb.save(f)


def chave():
    f = OUT("Chave_Analise_NAO_PARTILHAR_com_codificadores.xlsx")
    wb = openpyxl.load_workbook(f)
    ws = wb["Chave_Analise"]
    h = {c.value: c.column for c in ws[1]}
    cols = {"vc": h["VC_Holistico_v4_1 (deepseek-v4-pro, regra secundário VC1-VC3)"], "sec": h["VC_Secundario_Holistico_v4_1"],
            "cl": h["Cluster_Holistico_v4_1"], "conf": h["Confianca_Holistico_v4_1 (1-3)"], "iro": h["Ironia_Holistico_v4_1"],
            "llm": h["VC_LLM_Holistico (TopicDiscussionAnalyst)"]}
    ws.cell(1, cols["vc"]).value = "VC_Holistico_v4_1 (deepseek-v4-pro, tópico completo)"
    ws.cell(1, cols["llm"]).value = "VC_LLM_Holistico (TopicDiscussionAnalyst, tópico completo)"
    npc = ws.max_column + 1
    ws.cell(1, npc).value = "N_Posts_Topico_Completo"
    ws.cell(1, npc)._style = copy.copy(ws.cell(1, cols["iro"])._style)
    ws.column_dimensions[openpyxl.utils.get_column_letter(npc)].width = 14
    for r in range(2, ws.max_row + 1):
        tid = ws.cell(r, 1).value
        if not tid:
            continue
        t, x = resolve(str(tid)), str(tid)
        d = hol[t]
        for k, v in [("vc", d["vc_principal"]), ("sec", d["vc_secundario"]), ("cl", d["cluster"]), ("conf", d["confianca"]),
                     ("iro", d["ironia_satira"])]:
            ws.cell(r, cols[k]).value = v
        if x in res:
            ws.cell(r, cols["llm"]).value = res[x]["dinamicas_valor"]["tipo_dominante"]
        ws.cell(r, npc).value = n_posts[t]
        ws.cell(r, npc)._style = copy.copy(ws.cell(r, cols["iro"])._style)
    wb.save(f)


for c in ["JPaulo", "Emmanoel", "Roger", "Gomide"]:
    etapa2(c)
chave()
print("ok")
