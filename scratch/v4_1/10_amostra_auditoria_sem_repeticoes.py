"""DART-NET v4.1 — nova amostra da auditoria humana: um codificador por tópico, sem repetições.

JPaulo mantém os 18 tópicos que já codificou. Emmanoel, Roger e Gomide recebem 10 tópicos novos cada,
sorteados entre os restantes 133, sem tópicos com mais de 100 posts (carga de trabalho comparável).
Estratos pelo cluster da leitura holística dos tópicos completos: 6 tópicos por cluster no total, 2 por auditor;
cada auditor fica com 5 tópicos de EVE e 5 de WoW (C1 só tem EVE e C3 só tem WoW, por isso C2, C4 e C5 levam 1+1).
Saída: data/analysis/amostra_auditoria_v4_1_sem_repeticoes.json
"""
import json, os, random
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda *p: os.path.join(ROOT, "data", *p)
SEED, MAX_POSTS = 20261102, 100
AUDITORES = ["Emmanoel", "Roger", "Gomide"]
JPAULO = ["1mctiz6", "1hlv8xy", "reddit_1q7m0sl", "2056975", "1uqtdhy", "481937", "2176376", "2039353", "510327",
          "512367", "1i6m4i6", "reddit_1kylpvy", "2116712", "reddit_1r1dd9i", "503747", "2152188", "reddit_1rnbqbh", "1tdxixs"]
# (cluster, jogo) -> tópicos por auditor
PLANO = {(1, "EVE Online"): 2, (3, "World of Warcraft"): 2, (2, "EVE Online"): 1, (2, "World of Warcraft"): 1,
         (4, "EVE Online"): 1, (4, "World of Warcraft"): 1, (5, "EVE Online"): 1, (5, "World of Warcraft"): 1}

hol = json.load(open(A("analysis", "topic_holistic_coding_v4_1_completos.json")))
n_posts = Counter(json.loads(l)["thread_id"] for l in open(A("processed", "topicos_completos_v4_1.jsonl")))
rng = random.Random(SEED)

amostra = {"JPaulo": JPAULO}
usados = set(JPAULO)
for a in AUDITORES:
    amostra[a] = []
sorteio = {}
for (cl, g), k in sorted(PLANO.items()):
    pool = sorted(t for t in hol if t not in usados and hol[t]["cluster"] == cl and hol[t]["game"] == g
                  and n_posts[t] <= MAX_POSTS)
    sorteio[(cl, g)] = rng.sample(pool, k * len(AUDITORES))
    usados.update(sorteio[(cl, g)])
# Repartição: dentro de cada estrato, o tópico maior vai para o auditor com menos posts até ao momento
carga = Counter()
for (cl, g), ts in sorted(sorteio.items(), key=lambda x: -max(n_posts[t] for t in x[1])):
    vagas = Counter({a: PLANO[(cl, g)] for a in AUDITORES})
    for t in sorted(ts, key=lambda t: -n_posts[t]):
        a = min((a for a in AUDITORES if vagas[a]), key=lambda a: (carga[a], AUDITORES.index(a)))
        amostra[a].append(t)
        vagas[a] -= 1
        carga[a] += n_posts[t]

todos = [t for v in amostra.values() for t in v]
assert len(todos) == len(set(todos)) == 48
out = {"seed": SEED, "max_posts": MAX_POSTS, "plano_por_auditor": {f"C{c}|{g}": k for (c, g), k in PLANO.items()},
       "amostra": amostra}
json.dump(out, open(A("analysis", "amostra_auditoria_v4_1_sem_repeticoes.json"), "w"), indent=2, ensure_ascii=False)
for a, ts in amostra.items():
    print(a, len(ts), dict(Counter(hol[t]["game"][:3] for t in ts)), dict(sorted(Counter(hol[t]["cluster"] for t in ts).items())),
          dict(sorted(Counter(hol[t]["vc_principal"] for t in ts).items())), "posts:", sum(n_posts[t] for t in ts))
print("Total", dict(sorted(Counter(hol[t]["cluster"] for t in todos).items())), dict(sorted(Counter(hol[t]["vc_principal"] for t in todos).items())))
