"""DART-NET v4.1 — tira dos ficheiros das Etapas 1 e 2 as colunas opcionais (a azul) e acerta as instruções.

Etapa 1: saem VC_Secundario, Notas, IA_Presentes e Interacoes_Presentes. Etapa 2: sai Notas.
Os valores já preenchidos nessas colunas ficam no histórico do git. Correr uma só vez (ficheiros sem colunas azuis são ignorados).
"""
import copy, os

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = lambda f: os.path.join(ROOT, "output", f)
AZUL = ("00D9E1F2", "FFD9E1F2")
CODERS = ["JPaulo", "Emmanoel", "Roger", "Gomide"]

E1_TEXTO = {  # início do texto atual -> texto novo (None apaga a linha)
    "• Preencha apenas as colunas a amarelo": "• Preencha todas as colunas a amarelo (obrigatórias). Não altere as colunas a branco, a ordem das linhas nem o nome das colunas.",
    "• Se tiver dúvidas entre duas categorias": "• Se tiver dúvidas entre duas categorias, escolha a que melhor descreve o sentido global e baixe a Confiança.",
    "VC_Secundario [azul": None,
    "Notas [azul": None,
    "Regras de decisão: (a) VC1": "Regras de decisão: (a) VC1 exige um resultado concreto e não apenas uma intenção (senão é VC2). (b) Uma queixa genérica sem dano concreto relatado é VC4, não VC3. (c) Um único post de cocriação perdido numa discussão maioritariamente reflexiva não torna o tópico VC1. (d) Leve em conta a ironia: um elogio sarcástico à IA não é cocriação.",
    "Branco = identificação (não alterar)": "Branco = identificação (não alterar) · Amarelo = obrigatório.",
    "8. PORQUÊ VC PRINCIPAL E VC SECUNDÁRIO": None,
    "• VC_Principal é a medida principal": None,
    "• VC_Secundario serve para": None,
    "• Permite medir acordo parcial": None,
    "• O secundário exige": None,
    "• No relatório, as conclusões assentam": None,
    "9. TIPO DE IA, INTERAÇÃO E DIMENSÕES DART": "8. TIPO DE IA, INTERAÇÃO E DIMENSÕES DART (colunas J–O)",
    "IA_Presentes [azul]": None,
    "Interacoes_Presentes [azul]": None,
}
E2_TEXTO = {
    "Depois de abrir este ficheiro NÃO pode alterar": "Depois de abrir este ficheiro NÃO pode alterar a Etapa 1.",
    "Passo 2 — Releia o tópico original": "Passo 2 — Releia o tópico original através do link.",
    "Passo 4 — Compare o resumo com o tópico": "Passo 4 — Compare o resumo com o tópico e preencha as colunas a amarelo (obrigatórias), usando as listas pendentes.",
    "Notas [azul": None,
    "Branco = identificação e resumo": "Branco = identificação e resumo (não alterar) · Amarelo = obrigatório.",
    "7. REAVALIAÇÃO DOS RESUMOS NOVOS": None,
    "Os resumos das colunas E–J foram gerados": None,
    "Os resumos da coluna K (Resumo_IA_v2)": None,
}


def instrucoes(ins, textos):
    for r in range(ins.max_row, 0, -1):
        v = str(ins.cell(r, 1).value or "")
        for prefixo, novo in textos.items():
            if v.startswith(prefixo):
                if novo is None:
                    ins.delete_rows(r)
                else:
                    ins.cell(r, 1).value = novo
                break
    # tira linhas em branco repetidas deixadas pelas secções apagadas
    for r in range(ins.max_row, 1, -1):
        if ins.cell(r, 1).value is None and ins.cell(r - 1, 1).value is None:
            ins.delete_rows(r)


def colunas(ws):
    azuis = [c for c in range(1, ws.max_column + 1) if ws.cell(2, c).fill.fgColor.rgb in AZUL]
    if not azuis:
        return []
    last = max(r for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value)
    head = lambda c: ws.cell(1, c).value
    larg = {head(c): ws.column_dimensions[openpyxl.utils.get_column_letter(c)].width for c in range(1, ws.max_column + 1)}
    listas = {}
    for dv in ws.data_validations.dataValidation:
        for rng in dv.sqref.ranges:  # o Excel pode juntar colunas vizinhas numa só regra (ex.: G2:H19)
            for col in range(rng.min_col, rng.max_col + 1):
                listas[head(col)] = dv
    removidas = [head(c) for c in azuis]
    for c in reversed(azuis):
        ws.delete_cols(c)
    ws.data_validations.dataValidation = []
    for c in range(1, ws.max_column + 1):
        h, L = head(c), openpyxl.utils.get_column_letter(c)
        ws.column_dimensions[L].width = larg.get(h, 12)
        if h in listas and h not in removidas:
            o = listas[h]
            dv = DataValidation(type=o.type, formula1=o.formula1, allow_blank=o.allow_blank, showErrorMessage=o.showErrorMessage,
                                errorTitle=o.errorTitle, error=o.error)
            dv.add(f"{L}2:{L}{last}")
            ws.add_data_validation(dv)
    for c in range(ws.max_column + 1, ws.max_column + 1 + len(azuis)):  # larguras das colunas que ficaram vazias
        ws.column_dimensions[openpyxl.utils.get_column_letter(c)].width = 9
    return removidas


for coder in CODERS:
    for f, sheet, textos in [(f"etapa_1_Codificacao_Topicos_{coder}.xlsx", "Codificacao", E1_TEXTO),
                             (f"etapa_2_Avaliacao_Resumos_{coder}.xlsx", "Avaliacao_Resumos", E2_TEXTO)]:
        wb = openpyxl.load_workbook(OUT(f))
        rem = colunas(wb[sheet])
        if rem:
            instrucoes(wb["Instrucoes"], textos)
            wb.save(OUT(f))
        print(f, "removidas:", rem)
