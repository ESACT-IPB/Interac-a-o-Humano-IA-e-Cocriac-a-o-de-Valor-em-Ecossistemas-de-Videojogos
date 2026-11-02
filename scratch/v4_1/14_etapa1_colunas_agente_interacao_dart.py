"""DART-NET v4.1 — acrescenta à Etapa 1 dos quatro codificadores as colunas de tipo de IA, interação e DART (L–S).

As definições são as mesmas usadas na codificação automática dos tópicos (13_codificacao_topicos_agente_interacao_dart.py).
Os dados já preenchidos (A–K) não são alterados. Correr uma só vez: se as colunas já existirem, o ficheiro é ignorado.
"""
import copy, os

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = lambda f: os.path.join(ROOT, "output", f)

# (cabeçalho, largura, obrigatória, lista)
COLS = [("IA_Principal (A1-A6)", 12, True, "A1,A2,A3,A4,A5,A6"),
        ("IA_Presentes", 14, False, None),
        ("Interacao_Principal (I1-I6)", 13, True, "I1,I2,I3,I4,I5,I6"),
        ("Interacoes_Presentes", 14, False, None),
        ("DART_Dialogo (0-5)", 10, True, "0,1,2,3,4,5"),
        ("DART_Acesso (0-5)", 10, True, "0,1,2,3,4,5"),
        ("DART_Risco (0-5)", 10, True, "0,1,2,3,4,5"),
        ("DART_Transparencia (0-5)", 12, True, "0,1,2,3,4,5")]

INSTR = [
    ("h", "9. TIPO DE IA, INTERAÇÃO E DIMENSÕES DART (colunas L–S)"),
    ("t", "Estas colunas codificam o tópico como um TODO, como nas restantes. Um agente de IA é um sistema capaz de executar tarefas, "
          "tomar decisões ou agir com algum grau de autonomia. Não classifique qualquer bot, script ou automação como IA: se a evidência "
          "for insuficiente, não infira que é IA."),
    ("t", "IA_Principal [amarelo] — A1 Agente de IA (usa IA e tem alguma autonomia); A2 Bot convencional (automação sem evidência de IA); "
          "A3 Script/automação determinística; A4 Humano assistido por IA (a IA ajuda, o humano decide); A5 Discussão sobre IA (sem um uso "
          "concreto); A6 Irrelevante. Se o tópico gira em torno de um episódio concreto (o anúncio de uma ferramenta, o relato de um uso), "
          "escolha o tipo desse episódio; escolha A5 quando o tópico é sobretudo debate, opinião ou especulação."),
    ("t", "IA_Presentes [azul] — todos os tipos A1–A4 de que há um episódio concreto em algum post, mesmo secundário (ex.: 'A1, A4'). "
          "Conta um uso real relatado num post, mesmo fora do jogo (ex.: um addon escrito com ajuda de um LLM é A4). Um conselho "
          "hipotético ('podes pedir ao ChatGPT...') não conta."),
    ("t", "Interacao_Principal [amarelo] — I1 Humano → IA (instruções, perguntas a um agente); I2 IA → humano (a IA produz uma ação ou "
          "resposta que afeta o jogador); I3 Humano ↔ IA (iteração nos dois sentidos); I4 Humano → humano sobre IA (só discussão); "
          "I5 Humano → ambiente mediado por IA; I6 Sem interação relevante. Mesma regra do IA_Principal: a do episódio concreto central, "
          "ou I4 quando o tópico é sobretudo discussão."),
    ("t", "Interacoes_Presentes [azul] — todas as interações I1, I2, I3 ou I5 de que há um episódio concreto em algum post (ex.: 'I1, I3')."),
    ("t", "DART_Dialogo / DART_Acesso / DART_Risco / DART_Transparencia [amarelo] — intensidade de cada dimensão no tópico, de 0 a 5, "
          "avaliada de forma independente: 0 ausente; 1 fraca; 2 moderada; 3 forte; 4 muito forte; 5 explícita e central."),
    ("t", "Diálogo — comunicação, feedback, negociação, instruções, troca conversacional, influência mútua entre jogadores e IA (ou entre "
          "jogadores e editora sobre a IA). Acesso — a IA muda ou facilita o acesso a informação, recursos, capacidades, funções do jogo, "
          "conhecimento ou decisão. Risco — batota, vantagem injusta, riscos económicos, segurança, privacidade, dependência, manipulação, "
          "perda de controlo, perturbação do ecossistema. Transparência — divulgação do uso de IA, explicabilidade, visibilidade do "
          "comportamento da IA, opacidade, confiança, responsabilização."),
]


def update(coder):
    f = OUT(f"etapa_1_Codificacao_Topicos_{coder}.xlsx")
    wb = openpyxl.load_workbook(f)
    ws, ins = wb["Codificacao"], wb["Instrucoes"]
    if any(str(c.value or "").startswith(f"{coder}_IA_Principal") for c in ws[1]):
        print(coder, "já tem as colunas")
        return
    last = max(r for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value)
    req, opt = ws.cell(2, 6)._style, ws.cell(2, 7)._style  # VC_Principal (amarelo) e VC_Secundario (azul)
    for i, (h, w, obrig, lista) in enumerate(COLS):
        c = 12 + i
        L = openpyxl.utils.get_column_letter(c)
        ws.cell(1, c).value = f"{coder}_{h}"
        ws.cell(1, c)._style = copy.copy(ws.cell(1, 6)._style)
        ws.column_dimensions[L].width = w
        for r in range(2, last + 1):
            ws.cell(r, c)._style = copy.copy(req if obrig else opt)
        if lista:
            dv = DataValidation(type="list", formula1=f'"{lista}"', allow_blank=True, showErrorMessage=True,
                                errorTitle="Valor inválido", error="Escolha um valor da lista.")
            dv.add(f"{L}2:{L}{last}")
            ws.add_data_validation(dv)
    ins["A4"].value = (ins["A4"].value.rstrip(".") + ". Codifica também o tipo de IA, a interação e as quatro dimensões DART "
                       "do tópico (secção 9).")
    ins["A8"].value = "• Trabalhe sozinho. Não discuta os tópicos com os outros codificadores até todos terem entregue o ficheiro."
    ins["A21"].value = "Tempo estimado: 8–20 minutos por tópico, conforme a extensão da discussão."
    row = ins.max_row + 2
    for k, (kind, txt) in enumerate(INSTR):
        cell = ins.cell(row + k, 1, txt)
        cell._style = copy.copy(ins["A53" if kind == "h" else "A54"]._style)
    wb.save(f)
    print(coder, "ok", last - 1, "tópicos")


for c in ["JPaulo", "Emmanoel", "Roger", "Gomide"]:
    update(c)
