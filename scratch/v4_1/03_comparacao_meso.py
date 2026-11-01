"""DART-NET v4.1 — comparação micro vs. meso sobre a mesma base: regra 'basta um post', leitura holística e modelo nulo."""
import json, os, random
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda f: os.path.join(ROOT, "data", "analysis", f)
VCS = ["VC1", "VC2", "VC3", "VC4"]
CL = {"c1_api_mcp": 1, "c2_fairplay": 2, "c3_support": 3, "c4_followers": 4, "c5_vibecoding": 5}

posts = [json.loads(l) for l in open(A("netnography_results_v4_1.jsonl"))]
hol = {k: v for k, v in json.load(open(A("topic_holistic_coding_v4_1.json"))).items() if "erro" not in v}
old_threads = {x["thread_id"]: x for x in json.load(open(A("thread_level_results.json")))}

th = defaultdict(list)
for p in posts:
    th[p["thread_id"]].append(p)
game = {t: v[0]["game"] for t, v in th.items()}


def rule(labels):
    c = Counter(labels)
    if c["VC1"]:
        return "VC1"
    if c["VC3"] > c["VC2"] and c["VC3"]:
        return "VC3"
    if c["VC2"]:
        return "VC2"
    return "VC4"


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


tids = sorted(t for t in th if t in hol)
rule_vc = {t: rule([p["value_type"] for p in th[t]]) for t in tids}
hol_vc = {t: hol[t]["vc_principal"] for t in tids}

res = {"N_posts": len(posts), "N_topicos": len(th), "N_topicos_codificados_holistico": len(tids)}
res["micro_posts"] = dist([p["value_type"] for p in posts])
rel = [p for p in posts if p["ai_type"] != "A6" and p.get("relevance") != "IRRELEVANT"]
res["micro_posts_sem_A6_irrelevantes"] = dist([p["value_type"] for p in rel])
res["meso_regra_basta_um"] = dist(list(rule_vc.values()))
res["meso_holistico_llm"] = dist(list(hol_vc.values()))
res["concordancia_regra_vs_holistico"] = {
    "acordo_pct": round(100 * sum(rule_vc[t] == hol_vc[t] for t in tids) / len(tids), 1),
    "kappa": kappa([rule_vc[t] for t in tids], [hol_vc[t] for t in tids], VCS),
    "matriz": {r: {h: sum(1 for t in tids if rule_vc[t] == r and hol_vc[t] == h) for h in VCS} for r in VCS},
}

rng = random.Random(2026)
labels = [p["value_type"] for t in tids for p in th[t]]
sizes = [len(th[t]) for t in tids]
sims = []
for _ in range(5000):
    rng.shuffle(labels)
    i, agg = 0, []
    for s in sizes:
        agg.append(rule(labels[i:i + s]))
        i += s
    sims.append(100 * sum(a != "VC4" for a in agg) / len(agg))
sims.sort()
obs = res["meso_regra_basta_um"]["impacto_ativo_pct"]
res["modelo_nulo_regra"] = {
    "media_impacto_ativo_pct": round(sum(sims) / len(sims), 1),
    "ic95": [round(sims[int(0.025 * len(sims))], 1), round(sims[int(0.975 * len(sims))], 1)],
    "observado_regra_pct": obs,
    "p_observado_maior_ou_igual": round(sum(s >= obs for s in sims) / len(sims), 4),
}

by_game = {}
for g in ["EVE Online", "World of Warcraft"]:
    gt = [t for t in tids if game[t] == g]
    gp = [p for p in posts if p["game"] == g]
    by_game[g] = {"topicos": len(gt), "posts": len(gp),
                  "micro": dist([p["value_type"] for p in gp]),
                  "meso_regra": dist([rule_vc[t] for t in gt]),
                  "meso_holistico": dist([hol_vc[t] for t in gt])}
res["por_jogo"] = by_game

reg_cl = {}
for t in tids:
    src = old_threads.get(t) or old_threads.get("3000003" if t == "2248893" else t)
    if src:
        reg_cl[t] = CL[src["cluster_key"]]
ct = [t for t in tids if t in reg_cl]
res["cluster"] = {
    "regex_pipeline": dict(Counter(reg_cl[t] for t in ct)),
    "holistico_llm": dict(Counter(hol[t]["cluster"] for t in tids)),
    "acordo_regex_vs_llm_pct": round(100 * sum(reg_cl[t] == hol[t]["cluster"] for t in ct) / len(ct), 1),
    "kappa_regex_vs_llm": kappa([reg_cl[t] for t in ct], [hol[t]["cluster"] for t in ct], [1, 2, 3, 4, 5]),
}
res["holistico_qualidade"] = {
    "evidencia_verbatim_pct": round(100 * sum(1 for t in tids if hol[t].get("evidencia_verbatim")) / len(tids), 1),
    "confianca": dict(Counter(hol[t]["confianca"] for t in tids)),
    "ironia_satira": dict(Counter(hol[t]["ironia_satira"] for t in tids)),
    "truncados": [t for t in tids if hol[t].get("truncado")],
}


def dart_means(ps, strict):
    out = {}
    for d in ["dialogue", "access", "risk", "transparency"]:
        vals = []
        for p in ps:
            x = p["dart"][d]
            s = x.get("score", 0) or 0
            if strict and x.get("evidencia_verificada") not in ("verbatim", "nao_aplicavel"):
                s = 0
            vals.append(s)
        out[d] = round(sum(vals) / len(vals), 2)
    return out


res["dart_micro"] = {g: {"todas": dart_means([p for p in posts if p["game"] == g], False),
                         "so_evidencia_verbatim": dart_means([p for p in posts if p["game"] == g], True)}
                     for g in ["EVE Online", "World of Warcraft"]}
res["dart_micro"]["Total"] = {"todas": dart_means(posts, False), "so_evidencia_verbatim": dart_means(posts, True)}

json.dump(res, open(A("comparacao_meso_v4_1.json"), "w"), indent=2, ensure_ascii=False)
print(json.dumps(res, indent=1, ensure_ascii=False))
