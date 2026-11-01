"""DART-NET v4.1 — estatísticas usadas na atualização do relatório (corte de contraste, jogos, clusters)."""
import json, os
from collections import Counter, defaultdict
from statistics import mean

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda f: os.path.join(ROOT, "data", "analysis", f)
posts = [json.loads(l) for l in open(A("netnography_results_v4_1.jsonl"))]
hol = json.load(open(A("topic_holistic_coding_v4_1.json")))
old = {x["thread_id"]: x for x in json.load(open(A("thread_level_results.json")))}
log = json.load(open(A("correcoes_v4_1_log.json")))
exc = json.load(open(A("excluded_posts_log.json")))["excluded_posts"]
ren = dict(log["fusao_topico"]["posts_fundidos"])
exc_ids = {ren.get(e["post_id"], e["post_id"]) for e in exc}
D = ["dialogue", "access", "risk", "transparency"]
pct = lambda a, b: round(100 * a / b, 1)
r = {}

cut = [p for p in posts if p["post_id"] not in exc_ids]
r["corte"] = {"N": len(cut), "excluidos_presentes": len(posts) - len(cut),
              "jogo": dict(Counter(p["game"] for p in cut)),
              "ai": {k: [v, pct(v, len(cut))] for k, v in Counter(p["ai_type"] for p in cut).most_common()},
              "inter": {k: [v, pct(v, len(cut))] for k, v in Counter(p["interaction_type"] for p in cut).most_common()},
              "vc": {k: [v, pct(v, len(cut))] for k, v in sorted(Counter(p["value_type"] for p in cut).items())},
              "dart": {d: round(mean(p["dart"][d]["score"] or 0 for p in cut), 2) for d in D},
              "dart_verbatim": {d: round(mean((p["dart"][d]["score"] or 0) if p["dart"][d].get("evidencia_verificada") in ("verbatim", "nao_aplicavel") else 0 for p in cut), 2) for d in D},
              "review": [sum(1 for p in cut if p.get("human_review_required")), pct(sum(1 for p in cut if p.get("human_review_required")), len(cut))]}

th = defaultdict(list)
for p in posts:
    th[p["thread_id"]].append(p)
game = {t: v[0]["game"] for t, v in th.items()}
tdart = {t: {d: mean(p["dart"][d]["score"] or 0 for p in v) for d in D} for t, v in th.items()}
reg = {t: int(old.get(t, old.get("3000003"))["cluster_key"][1]) for t in th}
hcl = {t: hol[t]["cluster"] for t in th}
hvc = {t: hol[t]["vc_principal"] for t in th}
r["jogo_meso"] = {}
for g in ["EVE Online", "World of Warcraft"]:
    ts = [t for t in th if game[t] == g]
    r["jogo_meso"][g] = {"topicos": len(ts), "posts": sum(len(th[t]) for t in ts),
                         "posts_por_topico": round(sum(len(th[t]) for t in ts) / len(ts), 2),
                         "dart_topico": {d: round(mean(tdart[t][d] for t in ts), 2) for d in D}}
r["jogo_meso"]["Total"] = {"dart_topico": {d: round(mean(tdart[t][d] for t in th), 2) for d in D},
                           "posts_por_topico": round(len(posts) / len(th), 2)}
for name, cl in [("regex", reg), ("holistico", hcl)]:
    out = {}
    for c in range(1, 6):
        ts = [t for t in th if cl[t] == c]
        out[c] = {"n": len(ts), "pct": pct(len(ts), len(th)),
                  "dart": {d: round(mean(tdart[t][d] for t in ts), 2) for d in D},
                  "vc_holistico": dict(sorted(Counter(hvc[t] for t in ts).items())),
                  "jogo": dict(Counter(game[t] for t in ts))}
    r["cluster_" + name] = out
    n145 = sum(1 for t in th if cl[t] in (1, 4, 5))
    r["cluster_" + name]["c1_c4_c5"] = [n145, pct(n145, len(th))]
# interação direta ao nível do tópico: maioria/predominante I1/I2/I3/I5 vs qualquer post
r["topicos_interacao_direta"] = {
    "algum_post_I1_I2_I3": [sum(1 for t in th if any(p["interaction_type"] in ("I1", "I2", "I3") for p in th[t])),
                            pct(sum(1 for t in th if any(p["interaction_type"] in ("I1", "I2", "I3") for p in th[t])), len(th))]}
old_any = sum(1 for t, x in old.items() if any(x["inter_counts"].get(i, 0) for i in ("I1", "I2", "I3")))
r["topicos_interacao_direta"]["antigo_mesma_definicao"] = [old_any, pct(old_any, len(old))]
json.dump(r, open(A("estatisticas_relatorio_v4_1.json"), "w"), indent=2, ensure_ascii=False)
print(json.dumps(r, indent=1, ensure_ascii=False))
