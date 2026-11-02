"""DART-NET v4.1 — leitura holística: posts filtrados por relevância vs. tópicos completos."""
import json, os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda f: os.path.join(ROOT, "data", "analysis", f)
VCS = ["VC1", "VC2", "VC3", "VC4"]

filt = {k: v for k, v in json.load(open(A("topic_holistic_coding_v4_1.json"))).items() if "erro" not in v}
comp = {k: v for k, v in json.load(open(A("topic_holistic_coding_v4_1_completos.json"))).items() if "erro" not in v}
cmp_meso = json.load(open(A("comparacao_meso_v4_1.json")))
tids = sorted(set(filt) & set(comp))


def kappa(a, b, cats):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[c] * cb[c] for c in cats) / n ** 2
    return round((po - pe) / (1 - pe), 3) if pe < 1 else 1.0


def dist(vals):
    c, n = Counter(vals), len(vals)
    d = {k: {"n": c[k], "pct": round(100 * c[k] / n, 1)} for k in VCS}
    d["impacto_ativo_pct"] = round(100 * (n - c["VC4"]) / n, 1)
    d["N"] = n
    return d


res = {"N_topicos": len(tids), "erros_completos": [k for k, v in json.load(open(A("topic_holistic_coding_v4_1_completos.json"))).items() if "erro" in v]}
for nome, src in [("filtrado", filt), ("completos", comp)]:
    res[nome] = {"total": dist([src[t]["vc_principal"] for t in tids])}
    for g in ["EVE Online", "World of Warcraft"]:
        res[nome][g] = dist([src[t]["vc_principal"] for t in tids if src[t]["game"] == g])
    res[nome]["cluster"] = dict(sorted(Counter(src[t]["cluster"] for t in tids).items()))
    res[nome]["secundario"] = dict(Counter(src[t]["vc_secundario"] for t in tids if src[t]["vc_secundario"]))
    res[nome]["evidencia_verbatim_pct"] = round(100 * sum(bool(src[t].get("evidencia_verbatim")) for t in tids) / len(tids), 1)
    res[nome]["confianca"] = dict(sorted(Counter(src[t]["confianca"] for t in tids).items()))
    res[nome]["truncados"] = [t for t in tids if src[t].get("truncado")]

a, b = [filt[t]["vc_principal"] for t in tids], [comp[t]["vc_principal"] for t in tids]
res["vc_filtrado_vs_completos"] = {
    "acordo_pct": round(100 * sum(x == y for x, y in zip(a, b)) / len(tids), 1), "kappa": kappa(a, b, VCS),
    "matriz": {f: {c: sum(1 for x, y in zip(a, b) if x == f and y == c) for c in VCS} for f in VCS}}
ca, cb = [filt[t]["cluster"] for t in tids], [comp[t]["cluster"] for t in tids]
res["cluster_filtrado_vs_completos"] = {"acordo_pct": round(100 * sum(x == y for x, y in zip(ca, cb)) / len(tids), 1),
                                        "kappa": kappa(ca, cb, [1, 2, 3, 4, 5])}

# Concordância com a regra de agregação (que só existe sobre os posts filtrados, porque precisa dos rótulos micro)
posts = [json.loads(l) for l in open(A("netnography_results_v4_1.jsonl"))]
lab = {}
for p in posts:
    lab.setdefault(p["thread_id"], []).append(p["value_type"])


def rule(ls):
    c = Counter(ls)
    return "VC1" if c["VC1"] else "VC3" if c["VC3"] > c["VC2"] and c["VC3"] else "VC2" if c["VC2"] else "VC4"


r = [rule(lab[t]) for t in tids]
res["regra_vs_completos"] = {"acordo_pct": round(100 * sum(x == y for x, y in zip(r, b)) / len(tids), 1),
                             "kappa": kappa(r, b, VCS)}
res["regra_vs_filtrado"] = cmp_meso["concordancia_regra_vs_holistico"]["acordo_pct"], cmp_meso["concordancia_regra_vs_holistico"]["kappa"]

json.dump(res, open(A("comparacao_topicos_completos_v4_1.json"), "w"), indent=2, ensure_ascii=False)
print(json.dumps(res, indent=1, ensure_ascii=False))
