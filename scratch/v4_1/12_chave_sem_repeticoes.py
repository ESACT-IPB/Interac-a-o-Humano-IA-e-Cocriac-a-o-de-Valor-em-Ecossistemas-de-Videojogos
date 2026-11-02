"""DART-NET v4.1 — refaz a chave de análise para a amostra sem repetições (48 tópicos, um codificador por tópico)."""
import copy, json, os
from collections import Counter, defaultdict

import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda *p: os.path.join(ROOT, "data", *p)
F = os.path.join(ROOT, "output", "Chave_Analise_NAO_PARTILHAR_com_codificadores.xlsx")

amostra = json.load(open(A("analysis", "amostra_auditoria_v4_1_sem_repeticoes.json")))["amostra"]
res = json.load(open(A("analysis", "topic_discussions_insights_v4_1_completos.json")))
hol = json.load(open(A("analysis", "topic_holistic_coding_v4_1_completos.json")))
old = {x["thread_id"]: x for x in json.load(open(A("analysis", "thread_level_results.json")))}
n_full = Counter(json.loads(l)["thread_id"] for l in open(A("processed", "topicos_completos_v4_1.jsonl")))
labels = defaultdict(list)
for l in open(A("analysis", "netnography_results_v4_1.jsonl")):
    p = json.loads(l)
    labels[p["thread_id"]].append(p["value_type"])


def rule(ls):
    c = Counter(ls)
    return "VC1" if c["VC1"] else "VC3" if c["VC3"] > c["VC2"] and c["VC3"] else "VC2" if c["VC2"] else "VC4"


wb = openpyxl.load_workbook(F)
ws = wb["Chave_Analise"]
origem = {str(r[0]): r[3] for r in ws.iter_rows(min_row=2, values_only=True) if r[0]}
estilo = [copy.copy(ws.cell(2, c)._style) for c in range(1, ws.max_column + 1)]
ws.cell(1, 3).value = "Codificador"
ws.delete_rows(2, ws.max_row)
r = 2
for coder, tids in amostra.items():
    for t in tids:
        h = hol[t]
        src = old.get(t) or old.get("3000003" if t == "2248893" else t)
        row = [t, h["game"], coder, origem.get(t, "Estratificada_sem_repeticoes") if coder == "JPaulo" else "Estratificada_sem_repeticoes",
               src["cluster_key"], rule(labels[t]), res[t]["dinamicas_valor"]["tipo_dominante"],
               bool(res[t]["tom_e_retorica"].get("contem_satira_ironia")), len(labels[t]), h["vc_principal"],
               h["vc_secundario"], h["cluster"], h["confianca"], h["ironia_satira"], n_full[t]]
        for c, v in enumerate(row, 1):
            ws.cell(r, c).value = v
            ws.cell(r, c)._style = copy.copy(estilo[c - 1])
        r += 1
wb.save(F)
print("linhas:", r - 2, dict(Counter(ws.cell(i, 3).value for i in range(2, r))),
      "VC holístico:", dict(sorted(Counter(ws.cell(i, 10).value for i in range(2, r)).items())))
