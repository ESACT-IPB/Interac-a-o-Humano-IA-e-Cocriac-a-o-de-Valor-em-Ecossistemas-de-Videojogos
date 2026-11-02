"""DART-NET v4.1 — corpus de tópicos completos para a análise ao nível do tópico (meso).

A validação semântica avalia cada post isoladamente e corta as respostas que não falam de IA (778 → 110 posts nos
18 tópicos da amostra). Para ler um tópico como um todo, usam-se todos os posts recolhidos (scraped_posts.json),
apenas com os filtros de data (>= 2024) e de tamanho (>= 50 caracteres) aplicados na recolha.
Os 151 tópicos, o jogo corrigido e o título vêm do corpus v4.1. Autores e texto são anonimizados como na pipeline.
"""
import glob, json, os, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from agents.anonymizer_agent import AnonymizerAgent
from agents.scraper_agent import strip_html_tags

A = lambda *p: os.path.join(ROOT, "data", *p)
OUT_FILE = A("processed", "topicos_completos_v4_1.jsonl")
MAP_FILE = A("interim", "author_token_map_topicos_completos_v4_1.json")

v4 = [json.loads(l) for l in open(A("analysis", "netnography_results_v4_1.jsonl"))]
scraped = json.load(open(A("interim", "scraped_posts.json")))

# Tópico v4.1 -> tópicos de origem (inclui fusões, ex.: 2248893 + 3000003)
meta, sources = {}, defaultdict(set)
for p in v4:
    t = p["thread_id"]
    meta.setdefault(t, {"game": p["game"], "title": p.get("title", ""), "platform": p.get("platform", ""),
                        "community": p.get("community", "")})
    sources[t].add(t)
    sources[t].add(str(p.get("id") or p["post_id"]).rsplit("_", 1)[0])
src_to_topic = {s: t for t, ss in sources.items() for s in ss}

anon = AnonymizerAgent()  # o mapa original não é gravado; os novos autores vão para MAP_FILE
n_map = len(anon.author_map)
out, seen = defaultdict(list), set()
for p in scraped:
    t = src_to_topic.get(str(p.get("thread_id")))
    if not t or p["post_id"] in seen:
        continue
    seen.add(p["post_id"])
    m = meta[t]
    out[t].append({"thread_id": t, "post_id": p["post_id"], "timestamp": p.get("timestamp") or "",
                   "author_id": anon._get_or_create_synthetic_id(p.get("author_id")),
                   "text": anon.anonymize_text(p.get("text") or ""), "game": m["game"], "title": m["title"],
                   "platform": m["platform"], "community": m["community"]})

# Post de abertura: entra sempre, mesmo que seja anterior a 2024 ou curto, porque dá o contexto do tópico.
# Reddit: a recolha não guardou o texto; vem das páginas HTML (08_extrair_posts_abertura_reddit.py).
# Discourse: vem do post_number 1 em data/raw/ quando os filtros da recolha o cortaram.
OP_FILE = A("raw_reddit_op", "reddit_posts_abertura.json")
reddit_op = json.load(open(OP_FILE)) if os.path.exists(OP_FILE) else {}
op_status = {}
for t, m in meta.items():
    rid = t.replace("reddit_", "")
    raw = glob.glob(A("raw", f"topic_fetched_*_{rid}.json"))
    if raw and "topic_fetched_reddit_" in raw[0]:
        st = json.load(open(raw[0]))["post_stream"]
        st = st["posts"] if isinstance(st, dict) else st
        rop = next((x for x in st if strip_html_tags(x.get("cooked", "")).startswith("(Reddit post)")), None)
        if rop:  # poucos tópicos têm o post de abertura na recolha
            pid = f"{t}_{rop['id']}"
            if not any(p["post_id"] == pid for p in out[t]):
                out[t].append({"thread_id": t, "post_id": pid, "timestamp": rop.get("created_at") or "",
                               "author_id": anon._get_or_create_synthetic_id(rop.get("username")),
                               "text": anon.anonymize_text(strip_html_tags(rop.get("cooked", ""))), "game": m["game"],
                               "title": m["title"], "platform": m["platform"], "community": m["community"]})
            op_status[t] = "ja_na_recolha"
            continue
        op = reddit_op.get(rid)
        if not op:
            op_status[t] = "em_falta"
            continue
        if op["text"]:
            text, op_status[t] = op["text"], "texto"
        else:
            kind = "removido ou apagado" if op["removido"] else {"image": "só imagem", "crosspost": "crosspost de outro subreddit",
                                                                   "link": "ligação externa"}.get(op["post_type"], "sem texto")
            dom = re.match(r"https?://([^/]+)", op["link"] or "")
            extra = f"; ligava para {dom.group(1)}" if dom and "reddit.com" not in dom.group(1) else ""
            text, op_status[t] = f"[Post de abertura sem texto: {kind}{extra}]", kind
        out[t].insert(0, {"thread_id": t, "post_id": f"{t}_op", "timestamp": op["created"],
                          "author_id": anon._get_or_create_synthetic_id(op["author"]) if op["author"] != "[deleted]" else "Player_Anonymous",
                          "text": anon.anonymize_text(f"(Post de abertura) {op['title']}\n\n{text}"), "game": m["game"],
                          "title": m["title"], "platform": m["platform"], "community": m["community"]})
    elif raw:
        st = json.load(open(raw[0]))["post_stream"]
        st = st["posts"] if isinstance(st, dict) else st
        op = next((x for x in st if str(x.get("post_number")) == "1"), None)
        pid = op and f"{t}_{op['id']}"
        if op and not any(p["post_id"] == pid for p in out[t]):
            out[t].append({"thread_id": t, "post_id": pid, "timestamp": op.get("created_at") or "",
                           "author_id": anon._get_or_create_synthetic_id(op.get("username")),
                           "text": anon.anonymize_text(strip_html_tags(op.get("cooked", ""))), "game": m["game"],
                           "title": m["title"], "platform": m["platform"], "community": m["community"]})
            op_status[t] = "recuperado_raw"
print("Post de abertura:", dict(Counter(op_status.values())))
print("Reddit sem página HTML:", sorted(t for t, s in op_status.items() if s == "em_falta"))

with open(OUT_FILE, "w") as f:
    for t in sorted(out):
        for p in sorted(out[t], key=lambda p: (p["timestamp"], p["post_id"])):
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
json.dump(anon.author_map, open(MAP_FILE, "w"), indent=1, ensure_ascii=False)

n_v4 = defaultdict(int)
for p in v4:
    n_v4[p["thread_id"]] += 1
print(f"Tópicos: {len(out)}/{len(meta)} | posts completos: {sum(map(len, out.values()))} | posts v4.1: {len(v4)}"
      f" | novos autores anonimizados: {len(anon.author_map) - n_map}")
print("Tópicos com menos posts do que no v4.1:", [t for t in meta if len(out[t]) < n_v4[t]])
