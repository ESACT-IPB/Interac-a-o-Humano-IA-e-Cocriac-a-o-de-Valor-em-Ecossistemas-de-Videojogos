"""DART-NET v4.1 — regenera os resumos da Etapa 2 a partir dos tópicos completos.

Usa o mesmo agente, prompt e modelo (deepseek-v4-flash) que geraram os resumos originais; só muda o texto de entrada:
todos os posts do tópico (05_corpus_topicos_completos.py), por ordem cronológica e com o jogo corrigido.
A cache e a saída são ficheiros novos; topic_discussion_cache.json e topic_discussions_insights.json não são tocados.
"""
import json, os, sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from agents.topic_discussion_analyst_agent import TopicDiscussionAnalystAgent

IN_FILE = os.path.join(ROOT, "data", "processed", "topicos_completos_v4_1.jsonl")
OUT_FILE = os.path.join(ROOT, "data", "analysis", "topic_discussions_insights_v4_1_completos.json")
CODERS = ["JPaulo", "Emmanoel", "Roger", "Gomide"]
FALLBACK = "Discussão comunitária sobre"

threads = {}
for l in open(IN_FILE):
    p = json.loads(l)
    t = threads.setdefault(p["thread_id"], {"thread_id": p["thread_id"], "title": p["title"], "game": p["game"],
                                            "platform": p["platform"], "community": p["community"], "posts": []})
    t["posts"].append(p)  # o ficheiro já está por ordem cronológica

sample = set()
for c in CODERS:
    ws = openpyxl.load_workbook(os.path.join(ROOT, "output", f"etapa_2_Avaliacao_Resumos_{c}.xlsx"))["Avaliacao_Resumos"]
    sample.update(str(r[0]) for r in ws.iter_rows(min_row=2, values_only=True) if r[0])
resolve = lambda x: x if x in threads else ("reddit_" + x if "reddit_" + x in threads else x.replace("reddit_", ""))
todo = {x: resolve(x) for x in sample}
assert all(t in threads for t in todo.values()), [x for x, t in todo.items() if t not in threads]

agent = TopicDiscussionAnalystAgent()
agent.cache_file = OUT_FILE.replace(".json", "_cache.json")
agent.cache = json.load(open(agent.cache_file)) if os.path.exists(agent.cache_file) else {}
agent.cache = {k: v for k, v in agent.cache.items() if not v["resumo_extenso_discussao"].startswith(FALLBACK)}


def run(tid):
    for _ in range(3):
        r = agent.analyze_single_topic(threads[tid])
        if not r["resumo_extenso_discussao"].startswith(FALLBACK):
            return r
        agent.cache.pop(tid, None)  # o agente grava um resumo genérico quando a chamada falha
    return r


with ThreadPoolExecutor(max_workers=6) as ex:
    res = dict(zip(todo.values(), ex.map(run, todo.values())))
agent._save_cache(force=True)

out = {x: res[t] for x, t in todo.items()}
json.dump(out, open(OUT_FILE, "w"), indent=2, ensure_ascii=False)
bad = [x for x, r in out.items() if r["resumo_extenso_discussao"].startswith(FALLBACK)]
print(f"Resumos: {len(out)} | falhados: {bad}")
