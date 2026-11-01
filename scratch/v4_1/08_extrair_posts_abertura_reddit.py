"""DART-NET v4.1 — extrai o post de abertura dos tópicos do Reddit a partir das páginas HTML guardadas à mão.

A recolha original do Reddit guardou o título e os comentários, mas não o texto do post de abertura.
As páginas foram guardadas pelo investigador (Links_Reddit/, Links_Reedit_2/); aqui só se lê o elemento <shreddit-post>.
Saída (dados brutos, não anonimizados): data/raw_reddit_op/reddit_posts_abertura.json
Correr com: python -I scratch/v4_1/08_extrair_posts_abertura_reddit.py
"""
import glob, html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FOLDERS = ["Links_Reddit", "Links_Reedit_2"]
OUT_DIR = os.path.join(ROOT, "data", "raw_reddit_op")
OUT_FILE = os.path.join(OUT_DIR, "reddit_posts_abertura.json")


def element(h, start):
    """Devolve o elemento <div> que começa em start, contando aberturas e fechos de <div>."""
    depth, i = 0, start
    for m in re.finditer(r"<(/?)div\b[^>]*>", h[start:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return h[start:start + m.end()]
    return h[start:]


def to_text(fragment):
    fragment = re.sub(r"<(script|style)\b.*?</\1>", " ", fragment, flags=re.S)
    fragment = re.sub(r"<br\s*/?>|</p>|</li>", "\n", fragment)
    text = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return "\n".join(re.sub(r"[ \t]+", " ", l).strip() for l in text.splitlines() if l.strip())


posts = {}
for folder in FOLDERS:
    for f in sorted(glob.glob(os.path.join(ROOT, folder, "*.html"))):
        h = open(f, encoding="utf-8", errors="ignore").read()
        tag = re.search(r"<shreddit-post\b[^>]*>", h)
        if not tag:
            print("sem <shreddit-post>:", os.path.basename(f))
            continue
        a = {k: html.unescape(v) for k, v in re.findall(r'([\w-]+)="([^"]*)"', tag.group())}
        rid = a["id"].replace("t3_", "")
        body = re.search(r'<div[^>]+slot="text-body"', h)
        text = to_text(element(h, body.start())) if body else ""
        block = h[tag.start():h.find("</shreddit-post>", tag.start())]
        removed = "this post was removed by Reddit" in block or "this post was deleted by the person" in block \
            or "[deleted by user]" in a.get("post-title", "")
        posts[rid] = {"id": rid, "title": a.get("post-title", ""), "author": a.get("author", ""),
                      "created": a.get("created-timestamp", ""), "post_type": a.get("post-type", ""),
                      "link": a.get("content-href", ""), "subreddit": a.get("subreddit-prefixed-name", ""),
                      "text": text, "removido": removed, "ficheiro": f"{folder}/{os.path.basename(f)}"}

os.makedirs(OUT_DIR, exist_ok=True)
json.dump(posts, open(OUT_FILE, "w"), indent=1, ensure_ascii=False)
print(f"Posts de abertura: {len(posts)} | com texto: {sum(bool(p['text']) for p in posts.values())}")
for p in posts.values():
    if not p["text"]:
        print(f"  sem texto: {p['id']} ({p['post_type']}{', removido' if p['removido'] else ''}) {p['link'][:60]}")
