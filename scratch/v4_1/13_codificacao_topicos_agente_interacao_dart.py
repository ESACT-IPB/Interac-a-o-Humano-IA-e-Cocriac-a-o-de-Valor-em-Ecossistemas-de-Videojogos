"""DART-NET v4.1 — codificação ao nível do tópico do tipo de IA (A1–A6), da interação (I1–I6) e das dimensões DART.

Complementa 02_codificacao_holistica_topicos.py (cluster e VC): o modelo lê o tópico completo
(05_corpus_topicos_completos.py), por ordem cronológica, sem ver rótulos dos posts, e codifica o tópico como um todo.
As definições de A, I e DART são as do NetnographyAgent (agents/netnography_agent.py), traduzidas.
Cada pontuação DART > 0 exige uma citação literal, verificada contra o texto do tópico.
Saída: data/analysis/topic_coding_ai_interacao_dart_v4_1_completos.json
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
IN_FILE = os.path.join(ROOT, "data", "processed", "topicos_completos_v4_1.jsonl")
OUT_FILE = os.path.join(ROOT, "data", "analysis", "topic_coding_ai_interacao_dart_v4_1_completos.json")
MAX_CHARS = 300000
A_TYPES = ["A1", "A2", "A3", "A4", "A5", "A6"]
I_TYPES = ["I1", "I2", "I3", "I4", "I5", "I6"]
DIMS = ["dialogo", "acesso", "risco", "transparencia"]

SYSTEM = """És um codificador qualitativo especialista em netnografia e cocriação de valor (modelo DART de Prahalad & Ramaswamy).
Vais codificar UM tópico de discussão de um fórum de videojogos sobre inteligência artificial, lendo-o como um TODO (post de abertura → respostas → desfecho).
Um agente de IA é um sistema computacional capaz de executar tarefas, tomar decisões ou agir com algum grau de autonomia em nome de, ou em interação com, um jogador. Não classifiques automaticamente qualquer bot, script ou automação como agente de IA. Quando a evidência é insuficiente, não infiras que um bot é IA.

TIPO DE IA (A1–A6):
A1 — Agente de IA: há evidência de que o sistema usa IA e tem algum grau de autonomia.
A2 — Bot convencional: há software automatizado, mas sem evidência suficiente de que seja baseado em IA.
A3 — Script / automação: script, macro ou automação determinística, sem evidência de IA.
A4 — Humano assistido por IA: a IA ajuda o jogador, mas o humano continua a ser quem decide.
A5 — Discussão sobre IA: discute-se IA, mas sem descrever uma interação real com um agente de IA.
A6 — Irrelevante: o conteúdo não tem relação com IA nos videojogos.
Conta como episódio concreto um uso real de IA relatado num post, mesmo que tenha acontecido fora do fórum ou fora do jogo: por exemplo, um jogador que escreveu um addon ou uma aplicação com ajuda de um LLM (A4), uma ferramenta de IA apresentada e usada pelo autor (A1 ou A4, conforme a autonomia), uma resposta de suporte que o jogador identifica como gerada por IA (A1 ou A2, conforme a evidência). Um conselho hipotético ("podes pedir ao ChatGPT...") não é um episódio concreto.
- IA_Principal: o tipo que melhor caracteriza o tópico no seu conjunto. Se o tópico gira em torno de um episódio concreto (o anúncio de uma ferramenta, o relato de um uso), usa o tipo desse episódio; usa A5 quando o tópico é sobretudo debate, opinião ou especulação sem um episódio concreto central.
- IA_Presentes: todos os tipos de A1–A4 de que há um episódio concreto descrito em algum post, incluindo episódios secundários que não são o tema principal do tópico (lista, pode ser vazia). Não incluas A5 nem A6.

INTERAÇÃO (I1–I6):
I1 — Humano → agente de IA: um jogador comunica com, dá instruções a, ou interage diretamente com um agente de IA.
I2 — Agente de IA → humano: o agente produz uma ação, recomendação, resposta ou resultado que afeta o jogador.
I3 — Humano ↔ agente de IA: há interação nos dois sentidos (iteração, ajuste, conversa).
I4 — Humano → humano sobre IA: os humanos discutem IA, mas não interagem diretamente com ela.
I5 — Humano → ambiente mediado por IA: a IA influencia o ambiente de jogo em que os humanos atuam.
I6 — Sem interação relevante: a IA é mencionada, mas não há interação relevante.
As interações I1, I2, I3 e I5 também contam quando são relatadas num post como episódio concreto (por exemplo, "pedi ao Claude que corrigisse o código e fui ajustando" é I3).
- Interacao_Principal: a interação que melhor caracteriza o tópico no seu conjunto, com a mesma regra do IA_Principal: a do episódio concreto central, ou I4 quando o tópico é sobretudo discussão entre humanos.
- Interacoes_Presentes: todas as interações I1, I2, I3 ou I5 de que há um episódio concreto descrito em algum post, incluindo episódios secundários (lista, pode ser vazia).

DIMENSÕES DART (0 a 5, cada uma de forma independente, avaliando o tópico como um todo):
Diálogo — comunicação, interação, feedback, negociação, instruções, respostas, troca conversacional, influência mútua entre jogadores e IA (ou entre jogadores e editora sobre a IA).
Acesso — a IA muda ou facilita o acesso a informação, recursos, capacidades, funções do jogo, conhecimento ou decisão.
Risco — batota, vantagem injusta, riscos económicos, segurança, privacidade, dependência, manipulação, perda de controlo, perturbação do ecossistema.
Transparência — divulgação do uso de IA, explicabilidade, visibilidade do comportamento da IA, compreensão de como o sistema funciona, opacidade, confiança, responsabilização.
Escala: 0 = ausente; 1 = fraca; 2 = moderada; 3 = forte; 4 = muito forte; 5 = explícita e central no tópico.
Para cada dimensão com pontuação > 0, copia do tópico um excerto curto (até 40 palavras) EXATAMENTE como está escrito, que justifique a pontuação, e indica o POST ID. Se a pontuação for 0, deixa a citação vazia.

CONFIANÇA (1–3): 1 = baixa (muito ambíguo); 2 = média; 3 = alta.

Responde APENAS com um objeto JSON válido, sem texto adicional:
{"ia_principal": "A5", "ia_presentes": [], "interacao_principal": "I4", "interacoes_presentes": [],
 "dart": {"dialogo": {"score": 0, "citacao": "", "post_id": ""}, "acesso": {"score": 0, "citacao": "", "post_id": ""},
          "risco": {"score": 0, "citacao": "", "post_id": ""}, "transparencia": {"score": 0, "citacao": "", "post_id": ""}},
 "confianca": 2, "justificacao": "máximo 80 palavras"}"""

norm = lambda s: re.sub(r"\W+", " ", (s or "").lower()).strip()


def load_threads():
    th = defaultdict(list)
    for l in open(IN_FILE):
        p = json.loads(l)
        th[p["thread_id"]].append(p)  # o ficheiro já está por ordem cronológica
    return th


def build_user(tposts):
    p0 = tposts[0]
    head = (f"TÍTULO: {p0.get('title', '')}\nJOGO: {p0['game']}\nCOMUNIDADE: {p0.get('community', '')} ({p0.get('platform', '')})\n"
            f"Nº DE POSTS: {len(tposts)}\n\n")
    body, used = [], 0
    for p in tposts:
        block = f"--- POST ID: {p['post_id']} | {(p.get('timestamp') or '')[:10]} | {p.get('author_id', '')} ---\n{p['text']}\n"
        if used + len(block) > MAX_CHARS:
            body.append(f"[... {len(tposts) - len(body)} posts omitidos por limite de tamanho ...]")
            break
        body.append(block)
        used += len(block)
    return head + "\n".join(body), len(body) < len(tposts)


def verbatim(ev, corpus):
    frags = [f for f in re.split(r"\.\.\.|…", ev or "") if len(norm(f)) >= 8] or [ev or ""]
    return bool(norm(ev)) and all(norm(f) in corpus for f in frags)


def parse(content):
    m = re.search(r"\{.*\}", content, re.S)
    if not m:
        raise ValueError("sem JSON")
    d = json.loads(m.group())
    assert d["ia_principal"] in A_TYPES and d["interacao_principal"] in I_TYPES
    d["ia_presentes"] = sorted(set(x for x in d.get("ia_presentes") or [] if x in ("A1", "A2", "A3", "A4")))
    d["interacoes_presentes"] = sorted(set(x for x in d.get("interacoes_presentes") or [] if x in ("I1", "I2", "I3", "I5")))
    for k in DIMS:
        x = d["dart"][k]
        x["score"] = int(x["score"])
        assert 0 <= x["score"] <= 5
    d["confianca"] = int(d["confianca"])
    assert d["confianca"] in (1, 2, 3)
    return d


def code_thread(tid, tposts):
    user, truncated = build_user(tposts)
    corpus = " || ".join(norm(p["text"]) + " || " + norm(sanitize_text(p["text"])) for p in tposts)
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
    last_err = None
    for attempt in range(4):
        try:
            content, _ = call_deepseek_raw(MODEL, messages, thinking_enabled=False, temperature=0.0, max_tokens=1500)
            d = parse(content)
            falhas = [k for k in DIMS if d["dart"][k]["score"] > 0 and not verbatim(d["dart"][k]["citacao"], corpus)]
            if falhas and attempt < 2:
                messages = messages + [{"role": "assistant", "content": content},
                                       {"role": "user", "content": f"As citações de {', '.join(falhas)} não aparecem literalmente no tópico. "
                                                                   "Copia excertos EXATOS do texto dos posts e devolve o JSON completo novamente."}]
                continue
            for k in DIMS:
                d["dart"][k]["verbatim"] = d["dart"][k]["score"] == 0 or verbatim(d["dart"][k]["citacao"], corpus)
            d.update({"thread_id": tid, "game": tposts[0]["game"], "n_posts": len(tposts), "truncado": truncated,
                      "modelo": MODEL, "tentativas": attempt + 1})
            return d
        except Exception as e:
            last_err = e
            time.sleep(3 * (attempt + 1))
    return {"thread_id": tid, "erro": str(last_err), "modelo": MODEL}


def main():
    threads = load_threads()
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    results = json.load(open(OUT_FILE)) if os.path.exists(OUT_FILE) else {}
    todo = [t for t in (only or threads) if t not in results or "erro" in results[t]]
    print(f"Tópicos: {len(threads)} | a codificar: {len(todo)}", flush=True)
    lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(code_thread, t, threads[t]): t for t in todo}
        for i, f in enumerate(as_completed(futs), 1):
            r = f.result()
            with lock:
                results[r["thread_id"]] = r
                json.dump(results, open(OUT_FILE, "w"), indent=2, ensure_ascii=False)
            print(f"[{i}/{len(todo)}] {r['thread_id']}: {r.get('ia_principal', 'ERRO')} {r.get('interacao_principal', '')} "
                  f"DART={[r['dart'][k]['score'] for k in DIMS] if 'dart' in r else '-'}", flush=True)
    print("Concluído. Erros:", [t for t, r in results.items() if "erro" in r])


if __name__ == "__main__":
    main()
