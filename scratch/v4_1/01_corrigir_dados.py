"""DART-NET v4.1 — correções determinísticas das etapas 1-3 (não altera ficheiros originais)."""
import json, re, os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = lambda *a: os.path.join(ROOT, *a)

# Subreddit real confirmado na API Arctic Shift (posts/ids) em 2026-11-01.
EVE_THREADS_MISLABELED = ["reddit_1t939or", "reddit_1spdcd4", "reddit_1r77r09", "reddit_1u0bxq6", "reddit_1ormrc6",
                          "reddit_1q7m0sl", "reddit_1usj0hv", "reddit_1vdomcq", "reddit_1phwb0r", "reddit_1pftbpi",
                          "reddit_1d8nm29", "reddit_1r3mzvw", "reddit_1sq7b1r", "reddit_1vy3jwo"]
WOW_SUBREDDIT_FIX = {"reddit_1tvlpnw": "r/woweconomy", "reddit_1ariy3g": "r/classicwow", "reddit_1v3v2p2": "r/classicwow"}
DUP_THREAD, CANON_THREAD = "3000003", "2248893"
NOT_USERNAMES = {"system", "EVE Online", "Solutions", "Aaron"}
STAFF = {"CCP_Swift": "CCP_Staff", "CCP_Bee": "CCP_Staff", "CCP_Dopamine": "CCP_Staff", "Kaivax": "Blizzard_Staff"}

log = {"versao": "4.1", "jogo_corrigido": [], "subreddit_corrigido": [], "fusao_topico": {}, "pseudonimizacao": {},
       "post_vazio_assinalado": [], "evidencia": {}, "catalogo": {}}

posts = [json.loads(l) for l in open(P("data", "analysis", "netnography_results.jsonl"))]

for p in posts:
    if p["thread_id"] in EVE_THREADS_MISLABELED:
        if p["game"] != "EVE Online":
            log["jogo_corrigido"].append(p["post_id"])
        p["game"], p["community"] = "EVE Online", "r/Eve"
    elif p["thread_id"] in WOW_SUBREDDIT_FIX:
        p["community"] = WOW_SUBREDDIT_FIX[p["thread_id"]]
        log["subreddit_corrigido"].append(p["post_id"])

canon_nums = {p["post_id"].split("_", 1)[1] for p in posts if p["thread_id"] == CANON_THREAD}
merged, dropped = [], []
kept = []
for p in posts:
    if p["thread_id"] == DUP_THREAD:
        num = p["post_id"].split("_", 1)[1]
        if num in canon_nums:
            dropped.append(p["post_id"])
            continue
        old = p["post_id"]
        p["post_id"], p["thread_id"] = f"{CANON_THREAD}_{num}", CANON_THREAD
        merged.append([old, p["post_id"]])
    kept.append(p)
posts = kept
log["fusao_topico"] = {"de": DUP_THREAD, "para": CANON_THREAD, "posts_fundidos": merged, "duplicados_removidos": dropped}

amap = json.load(open(P("data", "interim", "author_token_map.json")))
amap = amap.get("map", amap)
next_tok = max(int(v.split("_")[1]) for v in amap.values() if str(v).startswith("Player_")) + 1
replace = {}
alltext = " ".join(p["text"] for p in posts)
for name, tok in amap.items():
    if len(name) >= 4 and name not in NOT_USERNAMES and re.search(r"(?<![\w])" + re.escape(name) + r"(?![\w])", alltext):
        replace[name] = STAFF.get(name, tok)
for m in set(re.findall(r"@([A-Za-z0-9_\-]{3,})", alltext)):
    if m not in replace and m not in NOT_USERNAMES:
        replace[m] = STAFF.get(m) or f"Player_{next_tok}"
        if m not in STAFF:
            next_tok += 1
pats = [(re.compile(r"(?<![\w])" + re.escape(n) + r"(?![\w])"), t) for n, t in sorted(replace.items(), key=lambda x: -len(x[0]))]
touched = Counter()
for p in posts:
    for field in ["text"]:
        t = p[field]
        for pat, tok in pats:
            t, n = pat.subn(tok, t)
            if n:
                touched[p["post_id"]] += n
        p[field] = t
    for d in (p.get("dart") or {}).values():
        if isinstance(d, dict) and d.get("evidence"):
            for pat, tok in pats:
                d["evidence"] = pat.sub(tok, d["evidence"])
log["pseudonimizacao"] = {"n_nomes": len(replace), "n_posts": len(touched), "ocorrencias": sum(touched.values())}

for p in posts:
    if re.fullmatch(r"\s*\[URL_ANONYMIZED\]\s*", p["text"]):
        p["conteudo_vazio"] = True
        log["post_vazio_assinalado"].append(p["post_id"])

import sys
sys.path.insert(0, ROOT)
from sanitizer import sanitize_text

norm = lambda s: re.sub(r"\W+", " ", (s or "").lower()).strip()
stat = Counter()
for p in posts:
    # O LLM recebeu o texto com palavrões substituídos; uma citação desse texto conta como verbatim.
    body = norm(p["text"]) + " || " + norm(sanitize_text(p["text"]))
    for dim, d in (p.get("dart") or {}).items():
        if not isinstance(d, dict):
            continue
        score, ev = d.get("score", 0) or 0, (d.get("evidence") or "").strip()
        if score == 0:
            status = "nao_aplicavel"
        elif not ev:
            status = "sem_evidencia"
        else:
            frags = [f for f in re.split(r"\.\.\.|…|\|", ev) if len(norm(f)) >= 12] or [ev]
            found = [norm(f) in body for f in frags]
            status = "verbatim" if all(found) else ("parcial" if any(found) else "nao_verbatim")
        d["evidencia_verificada"] = status
        stat[status] += 1
log["evidencia"] = dict(stat)

with open(P("data", "analysis", "netnography_results_v4_1.jsonl"), "w", encoding="utf-8") as f:
    for p in posts:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")

corpus = json.load(open(P("data", "target_corpus_303.json")))
seen, out, removed = set(), [], []
eve_ids = {t.replace("reddit_", "") for t in EVE_THREADS_MISLABELED}
for c in corpus:
    tid = str(c["topic_id"])
    if tid in eve_ids and c["game"] == "World of Warcraft":
        removed.append([tid, c["canonical_url"], "entrada r/wow inexistente (subreddit real: r/Eve)"])
        if any(str(x["topic_id"]) == tid for x in corpus if x["game"] == "EVE Online"):
            continue
        c = dict(c, game="EVE Online", community="r/Eve",
                 canonical_url=c["canonical_url"].replace("/r/wow/", "/r/Eve/"))
    key = (tid, c["game"])
    if key in seen:
        removed.append([tid, c["canonical_url"], "duplicado"])
        continue
    seen.add(key)
    out.append(c)
json.dump(out, open(P("data", "target_corpus_v4_1.json"), "w"), indent=2, ensure_ascii=False)
log["catalogo"] = {"entradas_originais": len(corpus), "entradas_v4_1": len(out), "removidas_ou_corrigidas": removed}

log["jogo_corrigido"] = {"n_posts": len(log["jogo_corrigido"]), "topicos": EVE_THREADS_MISLABELED}
json.dump(log, open(P("data", "analysis", "correcoes_v4_1_log.json"), "w"), indent=2, ensure_ascii=False)

print("posts v4.1:", len(posts), "| tópicos:", len({p["thread_id"] for p in posts}))
print("jogo:", Counter(p["game"] for p in posts))
print("jogo corrigido:", log["jogo_corrigido"]["n_posts"], "posts | fusão 3000003:", len(merged), "fundidos,", len(dropped), "removidos")
print("pseudonimização:", log["pseudonimizacao"], sorted(replace))
print("evidência:", log["evidencia"])
print("catálogo:", len(corpus), "->", len(out))
