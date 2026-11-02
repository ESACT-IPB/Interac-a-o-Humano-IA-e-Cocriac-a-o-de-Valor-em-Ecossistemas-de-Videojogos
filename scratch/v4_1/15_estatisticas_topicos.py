"""DART-NET v4.1 — estatísticas do relatório ao nível do tópico (151 tópicos completos).

Junta a leitura holística (02: cluster, VC, ironia) e a codificação de tipo de IA, interação e DART (13).
Saída: data/analysis/estatisticas_topicos_v4_1.json
"""
import json, os
from collections import Counter
from statistics import mean

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda f: os.path.join(ROOT, "data", "analysis", f)
hol = json.load(open(A("topic_holistic_coding_v4_1_completos.json")))
aid = json.load(open(A("topic_coding_ai_interacao_dart_v4_1_completos.json")))
titles = {}
for l in open(os.path.join(ROOT, "data", "processed", "topicos_completos_v4_1.jsonl")):
    p = json.loads(l)
    titles.setdefault(p["thread_id"], p["title"])
D = ["dialogo", "acesso", "risco", "transparencia"]
JOGOS = {"Total": None, "EVE Online": "EVE Online", "World of Warcraft": "World of Warcraft"}
pct = lambda a, b: round(100 * a / b, 1) if b else 0.0
dist = lambda vals, cats: {c: [Counter(vals)[c], pct(Counter(vals)[c], len(vals))] for c in cats}


def perfil(ts):
    n = len(ts)
    return {
        "n": n,
        "ia_principal": dist([aid[t]["ia_principal"] for t in ts], ["A1", "A2", "A3", "A4", "A5", "A6"]),
        "ia_presente": {c: [k := sum(c in aid[t]["ia_presentes"] for t in ts), pct(k, n)] for c in ["A1", "A2", "A3", "A4"]},
        "algum_A1_A4": [k := sum(bool({"A1", "A4"} & set(aid[t]["ia_presentes"])) for t in ts), pct(k, n)],
        "algum_A2_A3": [k := sum(bool({"A2", "A3"} & set(aid[t]["ia_presentes"])) for t in ts), pct(k, n)],
        "interacao_principal": dist([aid[t]["interacao_principal"] for t in ts], ["I1", "I2", "I3", "I4", "I5", "I6"]),
        "interacao_presente": {c: [k := sum(c in aid[t]["interacoes_presentes"] for t in ts), pct(k, n)] for c in ["I1", "I2", "I3", "I5"]},
        "alguma_interacao_direta": [k := sum(bool(aid[t]["interacoes_presentes"]) for t in ts), pct(k, n)],
        "dart_media": {d: round(mean(aid[t]["dart"][d]["score"] for t in ts), 2) for d in D},
        "dart_forte_3mais": {d: [k := sum(aid[t]["dart"][d]["score"] >= 3 for t in ts), pct(k, n)] for d in D},
        "vc": dist([hol[t]["vc_principal"] for t in ts], ["VC1", "VC2", "VC3", "VC4"]),
        "impacto_ativo": [k := sum(hol[t]["vc_principal"] != "VC4" for t in ts), pct(k, n)],
        "cluster": dist([hol[t]["cluster"] for t in ts], [1, 2, 3, 4, 5]),
        "ironia": dist([hol[t]["ironia_satira"] for t in ts], ["Sim", "Parcial", "Não"]),
        "jogo": dict(Counter(hol[t]["game"] for t in ts)),
    }


assert set(hol) == set(aid) and len(hol) == 151
excluidos = [t for t in hol if aid[t]["ia_principal"] == "A6"]  # tópicos sem IA, fora do corpus final (16_corpus_final_sem_A6.py)
tids = sorted(t for t in hol if t not in excluidos)
r = {"por_jogo": {k: perfil([t for t in tids if g is None or hol[t]["game"] == g]) for k, g in JOGOS.items()},
     "por_cluster": {c: perfil([t for t in tids if hol[t]["cluster"] == c]) for c in range(1, 6)},
     "dart_por_vc": {v: {d: round(mean(aid[t]["dart"][d]["score"] for t in tids if hol[t]["vc_principal"] == v), 2) for d in D}
                     for v in ["VC1", "VC2", "VC3", "VC4"]},
     "ia_x_vc": {f"{a}|{v}": n for (a, v), n in Counter((aid[t]["ia_principal"], hol[t]["vc_principal"]) for t in tids).items()},
     "qualidade": {"vc_citacao_verbatim": sum(bool(hol[t].get("evidencia_verbatim")) for t in tids),
                   "dart_citacoes_verbatim_falhadas": sum(not aid[t]["dart"][d]["verbatim"] for t in tids for d in D),
                   "confianca_vc": dict(Counter(hol[t]["confianca"] for t in tids)),
                   "confianca_ia_dart": dict(Counter(aid[t]["confianca"] for t in tids)),
                   "truncados": [t for t in tids if aid[t]["truncado"]]}}
# exemplos com pontuação 5 por dimensão (citação verificada) e exemplos de VC1/VC3 com confiança alta
r["exemplos_dart5"] = {d: [{"topico": t, "titulo": titles[t], "jogo": hol[t]["game"], "post": aid[t]["dart"][d]["post_id"],
                            "citacao": aid[t]["dart"][d]["citacao"]}
                           for t in tids if aid[t]["dart"][d]["score"] == 5 and aid[t]["dart"][d]["verbatim"]] for d in D}
r["exemplos_vc"] = {v: [{"topico": t, "titulo": titles[t], "jogo": hol[t]["game"], "cluster": hol[t]["cluster"],
                         "ia": aid[t]["ia_principal"], "interacao": aid[t]["interacao_principal"],
                         "dart": [aid[t]["dart"][d]["score"] for d in D], "post": hol[t]["post_ancora_id"],
                         "citacao": hol[t]["evidencia_citacao"], "justificacao": hol[t]["justificacao"]}
                        for t in tids if hol[t]["vc_principal"] == v and hol[t]["confianca"] == 3 and hol[t].get("evidencia_verbatim")]
                    for v in ["VC1", "VC3"]}
r["topicos_A6_excluidos"] = [{"topico": t, "titulo": titles[t], "jogo": hol[t]["game"], "vc": hol[t]["vc_principal"],
                               "justificacao": aid[t]["justificacao"]} for t in sorted(excluidos)]
r["n_posts_completos"] = {g: sum(1 for l in open(os.path.join(ROOT, "data", "processed", "topicos_completos_v4_1.jsonl"))
                                 if (p := json.loads(l))["thread_id"] in tids and (g == "Total" or p["game"] == g)) for g in JOGOS}
json.dump(r, open(A("estatisticas_topicos_v4_1.json"), "w"), indent=2, ensure_ascii=False)
for k in ["Total", "EVE Online", "World of Warcraft"]:
    p = r["por_jogo"][k]
    print(k, p["n"], "IA", {a: v[0] for a, v in p["ia_principal"].items()}, "I", {a: v[0] for a, v in p["interacao_principal"].items()},
          "direta", p["alguma_interacao_direta"], "DART", p["dart_media"], "forte", {d: v[0] for d, v in p["dart_forte_3mais"].items()})
print("exemplos DART5:", {d: len(v) for d, v in r["exemplos_dart5"].items()}, "VC:", {v: len(x) for v, x in r["exemplos_vc"].items()})
