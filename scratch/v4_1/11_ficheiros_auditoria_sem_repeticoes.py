"""DART-NET v4.1 — refaz os ficheiros das Etapas 1 e 2 de Emmanoel, Roger e Gomide para a amostra sem repetições.

Cada ficheiro é reconstruído a partir do ficheiro atual do mesmo codificador (estilos, listas e instruções),
com 10 linhas para os tópicos de 10_amostra_auditoria_sem_repeticoes.py. Os ficheiros do JPaulo não mudam.
"""
import copy, glob, json, os, re, sys

import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = lambda *p: os.path.join(ROOT, "data", *p)
OUT = lambda f: os.path.join(ROOT, "output", f)

amostra = json.load(open(A("analysis", "amostra_auditoria_v4_1_sem_repeticoes.json")))["amostra"]
res = json.load(open(A("analysis", "topic_discussions_insights_v4_1_completos.json")))
meta = {}
for l in open(A("processed", "topicos_completos_v4_1.jsonl")):
    p = json.loads(l)
    meta.setdefault(p["thread_id"], {"game": p["game"], "title": p["title"]})


def link(t):
    """Link para o início do tópico. No Reddit usa /comments/<id>, porque alguns url_fonte têm o subreddit errado."""
    rid = t.replace("reddit_", "")
    raw = glob.glob(A("raw", f"topic_fetched_*_{rid}.json"))
    if raw and "topic_fetched_reddit_" in raw[0]:
        return f"https://www.reddit.com/comments/{rid}"
    if raw:
        d = json.load(open(raw[0]))
        url = d.get("url_fonte") or d.get("canonical_url")
    else:
        url = next(json.loads(l)["url"] for l in open(A("analysis", "netnography_results_v4_1.jsonl"))
                   if json.loads(l)["thread_id"] == t and json.loads(l).get("url"))
    return re.sub(rf"(/{rid})/\d+/?$", r"\1", url)  # Discourse: tira o nº do post no fim


TEXTOS_E1 = {
    "A4": "Vai classificar {n} tópicos de discussão (threads) de fóruns de videojogos (World of Warcraft e EVE Online) sobre "
          "inteligência artificial. Para cada tópico atribui UMA dinâmica de valor principal (VC1–VC4) e o cluster temático "
          "(1–5), com base na leitura integral da discussão.",
    "A5": "Cada tópico é codificado por um único investigador: os tópicos não se repetem entre codificadores, para cobrir uma "
          "amostra maior. A sua codificação será comparada com a codificação automática da pipeline (κ de Cohen).",
    "A54": "• VC_Principal é a medida principal do estudo: a comparação com a codificação automática (κ de Cohen) é calculada "
           "só com esta coluna, porque o κ exige uma única categoria por tópico.",
    "A56": "• Permite medir acordo parcial: se o seu VC_Principal coincidir com o VC secundário da codificação automática "
           "(ou vice-versa), conta como acordo parcial e não como desacordo total.",
}
TEXTOS_E2 = {
    "A8": "Avaliar a qualidade dos {n} resumos gerados automaticamente pela pipeline DART-NET (agente TopicDiscussionAnalystAgent): "
          "até que ponto cada resumo descreve com rigor o que realmente se passou no tópico.",
}


def rebuild(path, sheet, tids, extra, textos):
    wb = openpyxl.load_workbook(path)
    ws, ins = wb[sheet], wb["Instrucoes"]
    for cell, txt in textos.items():
        ins[cell].value = txt.format(n=len(tids))
    old_last = max(r for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value)
    ncol = ws.max_column
    for i, t in enumerate(tids):
        r = 2 + i
        for c in range(1, ncol + 1):
            ws.cell(r, c).value = None
        ws.cell(r, 1).value, ws.cell(r, 2).value, ws.cell(r, 3).value = t, meta[t]["game"], meta[t]["title"]
        d = ws.cell(r, 4)
        d.value = d.hyperlink = link(t)
        d.style = "Hyperlink"
        d._style = copy.copy(ws.cell(2, 4)._style)
        for c, v in extra(t).items():
            ws.cell(r, c).value = v
    last = 1 + len(tids)
    if old_last > last:
        ws.delete_rows(last + 1, old_last - last)
    for dv in ws.data_validations.dataValidation:
        col = str(dv.sqref).split(":")[0].rstrip("0123456789")
        dv.sqref = openpyxl.worksheet.cell_range.MultiCellRange(f"{col}2:{col}{last}")
    wb.save(path)


for a in (sys.argv[1:] or ["Emmanoel", "Roger", "Gomide"]):
    tids = amostra[a]
    rebuild(OUT(f"etapa_1_Codificacao_Topicos_{a}.xlsx"), "Codificacao", tids, lambda t: {}, TEXTOS_E1)
    rebuild(OUT(f"etapa_2_Avaliacao_Resumos_{a}.xlsx"), "Avaliacao_Resumos", tids,
            lambda t: {5: res[t]["resumo_extenso_discussao"]}, TEXTOS_E2)
    print(a, len(tids))
