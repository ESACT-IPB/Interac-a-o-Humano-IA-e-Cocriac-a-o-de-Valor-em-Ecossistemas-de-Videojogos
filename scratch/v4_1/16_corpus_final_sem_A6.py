"""DART-NET v4.1 — corpus final de tópicos: exclui os tópicos que a codificação por tópico classificou como A6 (sem IA).

Também atualiza a amostra da auditoria humana: os tópicos A6 de quem ainda não codificou são substituídos por outro
tópico do mesmo cluster e jogo (mesmas regras de 10_amostra_auditoria_sem_repeticoes.py); os tópicos A6 já codificados
pelo JPaulo saem da análise sem substituição.
Saídas: data/analysis/corpus_topicos_v4_1_final.json; amostra_auditoria_v4_1_sem_repeticoes.json (atualizada).
"""
import json, os, random
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda *p: os.path.join(ROOT, "data", *p)
SEED, MAX_POSTS = 20261102, 100

hol = json.load(open(A("analysis", "topic_holistic_coding_v4_1_completos.json")))
aid = json.load(open(A("analysis", "topic_coding_ai_interacao_dart_v4_1_completos.json")))
n_posts = Counter(json.loads(l)["thread_id"] for l in open(A("processed", "topicos_completos_v4_1.jsonl")))
excl = sorted(t for t in aid if aid[t]["ia_principal"] == "A6")
incl = sorted(t for t in hol if t not in excl)
json.dump({"criterio": "excluídos os tópicos com ia_principal = A6 na codificação por tópico (13_codificacao_topicos_agente_interacao_dart.py)",
           "n_incluidos": len(incl), "incluidos": incl,
           "excluidos": [{"topico": t, "jogo": hol[t]["game"], "justificacao": aid[t]["justificacao"]} for t in excl]},
          open(A("analysis", "corpus_topicos_v4_1_final.json"), "w"), indent=2, ensure_ascii=False)

f = A("analysis", "amostra_auditoria_v4_1_sem_repeticoes.json")
am = json.load(open(f))
if "substituicoes_A6" not in am:
    rng = random.Random(SEED + 6)
    usados = {t for ts in am["amostra"].values() for t in ts}
    am["substituicoes_A6"], am["excluidos_A6_sem_substituicao"] = [], []
    for coder, ts in am["amostra"].items():
        for i, t in enumerate(list(ts)):
            if t not in excl:
                continue
            if coder == "JPaulo":  # já codificado: sai da análise
                am["excluidos_A6_sem_substituicao"].append({"codificador": coder, "topico": t})
                continue
            pool = sorted(x for x in incl if x not in usados and hol[x]["cluster"] == hol[t]["cluster"]
                          and hol[x]["game"] == hol[t]["game"] and n_posts[x] <= MAX_POSTS)
            novo = rng.choice(pool)
            usados.add(novo)
            ts[i] = novo
            am["substituicoes_A6"].append({"codificador": coder, "saiu": t, "entrou": novo, "cluster": hol[t]["cluster"], "jogo": hol[t]["game"]})
    json.dump(am, open(f, "w"), indent=2, ensure_ascii=False)
print("incluídos", len(incl), "| excluídos", len(excl), dict(Counter(hol[t]["game"] for t in excl)))
print("substituições", am["substituicoes_A6"], "| sem substituição", am["excluidos_A6_sem_substituicao"])
