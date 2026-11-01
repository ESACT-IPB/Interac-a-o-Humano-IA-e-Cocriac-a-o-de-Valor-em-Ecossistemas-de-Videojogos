"""DART-NET v4.1 — codificação holística cega ao nível do tópico (mesmas instruções dos codificadores humanos).

O modelo recebe apenas o texto dos posts (por ordem cronológica), nunca os rótulos micro nem resumos anteriores.
Usa deepseek-v4-pro sem fallback para outro modelo, para manter a independência face à codificação micro (flash).
"""
import json, os, re, sys, time, threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import config
from api_client import call_deepseek_raw
from sanitizer import sanitize_text

MODEL = config.MODEL_PRO
IN_FILE = os.path.join(ROOT, "data", "analysis", "netnography_results_v4_1.jsonl")
OUT_FILE = os.path.join(ROOT, "data", "analysis", "topic_holistic_coding_v4_1.json")
MAX_CHARS = 90000

SYSTEM = """És um codificador qualitativo especialista em netnografia e cocriação de valor (Service-Dominant Logic, modelo DART de Prahalad & Ramaswamy).
Vais classificar UM tópico de discussão de um fórum de videojogos sobre inteligência artificial, lendo-o como um TODO (post de abertura → respostas → desfecho).

DINÂMICA DE VALOR — escolhe UMA categoria principal (VC_Principal):
VC1 — Cocriação Efetiva de Valor: jogador(es) e IA produzem em conjunto um benefício tangível e verificável. Ex.: uma ferramenta ou addon feito com ajuda de um LLM que funciona e é partilhado; um problema resolvido através da interação com a IA.
VC2 — Potencial de Cocriação: há intenção, proposta, protótipo ou teste de cocriação com IA, mas o benefício ainda não se materializou ou é incerto.
VC3 — Codestruição de Valor: a interação com IA (ou com sistemas automatizados) gera dano, perda, injustiça ou quebra de confiança. Ex.: banimento injusto por sistema automático; suporte com respostas automáticas inúteis; bots que arruínam a competição; perda de recursos por conselho errado de um LLM.
VC4 — Sem Evidência Direta de Valor: debate reflexivo, opinativo, normativo ou especulativo sobre IA, sem relato de ganho ou perda concretos.
Regras de decisão: (a) VC1 exige um resultado concreto e não apenas uma intenção (senão é VC2). (b) Uma queixa genérica sem dano concreto relatado é VC4, não VC3. (c) Um único post de cocriação perdido numa discussão maioritariamente reflexiva não torna o tópico VC1 — usa-o como VC_Secundario. (d) Tem em conta a ironia: um elogio sarcástico à IA não é cocriação.
VC_Secundario: segunda dinâmica claramente presente, diferente da principal. Só pode ser VC1, VC2 ou VC3 (VC4 nunca é secundário, porque é ausência de valor). Usa-o apenas se houver um episódio concreto dessa dinâmica num post; não o uses para exprimir dúvida (para isso baixa a confiança). null se não existir.

CLUSTER TEMÁTICO (1–5) — o tema dominante:
1 — Ferramentas Externas, APIs e MCP: a IA comunica automaticamente com dados vivos do jogo via API (ex.: ESI de EVE, servidores MCP, killboards).
2 — Fair Play, Deteção Algorítmica e Integridade Competitiva: bots, batota assistida por IA, deteção de automação, integridade do PvP e dos mercados.
3 — Suporte ao Cliente, Moderação Automatizada e Banning: uso de IA pela editora em tickets, moderação, sanções, despedimentos ligados à IA.
4 — Agentes Oficiais In-Game: companheiros, NPCs e assistentes de IA criados pela editora (ex.: Follower Dungeons, Delves/Brann em WoW; Aura em EVE).
5 — Copilotos, Addons e Vibe-Coding: o jogador usa um LLM externo como assistente pessoal, sem ligação por API ao jogo (addons Lua, WeakAuras, macros, planeamento, brainstorming).
Fronteira 1 vs 5: se a IA acede automaticamente aos dados do jogo por API → 1; se é o jogador que faz a ponte manual entre o jogo e o LLM → 5.

CONFIANÇA (1–3): 1 = baixa (muito ambíguo); 2 = média; 3 = alta.
IRONIA_SATIRA: "Sim" se o sentido do tópico depende de ironia/sarcasmo/humor; "Parcial" se há ironia relevante em parte; "Não" se o discurso é literal.
EVIDÊNCIA: copia do tópico um excerto curto (até 40 palavras) EXATAMENTE como está escrito, que justifique o VC_Principal, e indica o POST ID de onde vem.

Responde APENAS com um objeto JSON válido, sem texto adicional:
{"cluster": 1, "vc_principal": "VC1", "vc_secundario": null, "confianca": 3, "evidencia_citacao": "...", "post_ancora_id": "...", "ironia_satira": "Não", "justificacao": "máximo 80 palavras"}"""

norm = lambda s: re.sub(r"\W+", " ", (s or "").lower()).strip()


def load_threads():
    posts = [json.loads(l) for l in open(IN_FILE)]
    th = defaultdict(list)
    for p in posts:
        if not p.get("conteudo_vazio"):
            th[p["thread_id"]].append(p)
    for tid in th:
        th[tid].sort(key=lambda p: (p.get("timestamp") or "", p["post_id"]))
    return th


def build_user(tposts):
    p0 = tposts[0]
    head = (f"TÍTULO: {p0.get('title','')}\nJOGO: {p0['game']}\nCOMUNIDADE: {p0.get('community','')} ({p0.get('platform','')})\n"
            f"Nº DE POSTS: {len(tposts)}\n\n")
    body, used = [], 0
    for p in tposts:
        block = f"--- POST ID: {p['post_id']} | {(p.get('timestamp') or '')[:10]} | {p.get('author_id','')} ---\n{p['text']}\n"
        if used + len(block) > MAX_CHARS:
            body.append(f"[... {len(tposts) - len(body)} posts omitidos por limite de tamanho ...]")
            break
        body.append(block)
        used += len(block)
    return head + "\n".join(body), len(body) < len(tposts)


def parse(content):
    m = re.search(r"\{.*\}", content, re.S)
    if not m:
        raise ValueError("sem JSON")
    d = json.loads(m.group())
    assert int(d["cluster"]) in (1, 2, 3, 4, 5)
    assert d["vc_principal"] in ("VC1", "VC2", "VC3", "VC4")
    if d.get("vc_secundario") in ("", "null", "None", d["vc_principal"]):
        d["vc_secundario"] = None
    assert d["vc_secundario"] in (None, "VC1", "VC2", "VC3"), "VC4 não é aceite como secundário"
    assert int(d["confianca"]) in (1, 2, 3)
    assert d["ironia_satira"] in ("Sim", "Parcial", "Não")
    d["cluster"], d["confianca"] = int(d["cluster"]), int(d["confianca"])
    return d


def verbatim(ev, tposts):
    corpus = " || ".join(norm(p["text"]) + " || " + norm(sanitize_text(p["text"])) for p in tposts)
    frags = [f for f in re.split(r"\.\.\.|…", ev or "") if len(norm(f)) >= 8] or [ev or ""]
    return bool(norm(ev)) and all(norm(f) in corpus for f in frags)


def code_thread(tid, tposts):
    user, truncated = build_user(tposts)
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
    last_err = None
    for attempt in range(4):
        try:
            content, _ = call_deepseek_raw(MODEL, messages, thinking_enabled=False, temperature=0.0, max_tokens=1200)
            d = parse(content)
            d["evidencia_verbatim"] = verbatim(d.get("evidencia_citacao"), tposts)
            if not d["evidencia_verbatim"] and attempt < 2:
                messages = messages + [{"role": "assistant", "content": content},
                                       {"role": "user", "content": "A evidencia_citacao não aparece literalmente no tópico. Copia um excerto EXATO do texto dos posts e devolve o JSON completo novamente."}]
                continue
            d.update({"thread_id": tid, "game": tposts[0]["game"], "n_posts": len(tposts), "truncado": truncated,
                      "modelo": MODEL, "tentativas": attempt + 1})
            return d
        except Exception as e:
            last_err = e
            time.sleep(3 * (attempt + 1))
    return {"thread_id": tid, "erro": str(last_err), "modelo": MODEL}


def main():
    threads = load_threads()
    results = json.load(open(OUT_FILE)) if os.path.exists(OUT_FILE) else {}
    todo = [t for t in threads if t not in results or "erro" in results[t]]
    print(f"Tópicos: {len(threads)} | já feitos: {len(threads) - len(todo)} | a codificar: {len(todo)}", flush=True)
    lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(code_thread, t, threads[t]): t for t in todo}
        for i, f in enumerate(as_completed(futs), 1):
            r = f.result()
            with lock:
                results[r["thread_id"]] = r
                json.dump(results, open(OUT_FILE, "w"), indent=2, ensure_ascii=False)
            print(f"[{i}/{len(todo)}] {r['thread_id']}: {r.get('vc_principal', 'ERRO')} C{r.get('cluster', '-')} verbatim={r.get('evidencia_verbatim')}", flush=True)
    errs = [t for t, r in results.items() if "erro" in r]
    print("Concluído. Erros:", errs)


if __name__ == "__main__":
    main()
