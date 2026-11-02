#!/usr/bin/env python3
"""
abrir_reddit_chrome.py
Abre os links do Reddit recolhidos no Google Chrome (macOS).
Suporta abertura em lotes (para evitar sobrecarregar o Chrome) ou contínua.
"""

import sys
import os
import time
import subprocess
import argparse

def carregar_links(origem="todos"):
    # Localizar ficheiro de links
    candidatos = []
    if origem == "analisados":
        candidatos = [
            "output/links_152_topicos_analisados.txt",
            "links_152_topicos_analisados.txt"
        ]
    else:
        candidatos = [
            "output/links.txt",
            "links.txt"
        ]

    ficheiro = None
    for c in candidatos:
        if os.path.exists(c):
            ficheiro = c
            break

    if not ficheiro:
        print(f"Erro: Não foi encontrado nenhum ficheiro de links ({candidatos})")
        sys.exit(1)

    with open(ficheiro, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]

    reddit_links = [l for l in linhas if "reddit.com" in l.lower()]
    return reddit_links, ficheiro

def abrir_url_no_chrome(url):
    """Abre uma URL no Google Chrome no macOS."""
    subprocess.run(["open", "-a", "Google Chrome", url], check=False)

def main():
    parser = argparse.ArgumentParser(
        description="Abre os links do Reddit do corpus de investigação no Google Chrome."
    )
    parser.add_argument(
        "--batch-size", "-b", type=int, default=10,
        help="Número de separadores a abrir de cada vez (predefinição: 10)."
    )
    parser.add_argument(
        "--delay", "-d", type=float, default=0.4,
        help="Intervalo em segundos entre cada separador (predefinição: 0.4s)."
    )
    parser.add_argument(
        "--start", "-s", type=int, default=1,
        help="Número do link inicial (1-indexado, útil para retomar)."
    )
    parser.add_argument(
        "--analisados", action="store_true",
        help="Abrir apenas os 59 links do Reddit dos tópicos analisados na netnografia."
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Abrir todos os links de seguida sem pedir confirmação entre lotes."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Apenas lista os links que seriam abertos sem iniciar o Chrome."
    )

    args = parser.parse_args()

    origem = "analisados" if args.analisados else "todos"
    links, ficheiro = carregar_links(origem)

    total = len(links)
    print("=" * 70)
    print(f"  ABERTURA DE LINKS DO REDDIT NO GOOGLE CHROME")
    print(f"  Ficheiro fonte: {ficheiro}")
    print(f"  Total de links Reddit encontrados: {total}")
    print(f"  Tamanho do lote: {args.batch_size} separadores")
    print("=" * 70)

    start_idx = max(0, args.start - 1)
    if start_idx >= total:
        print(f"Erro: O índice inicial ({args.start}) é superior ao total de links ({total}).")
        return

    idx = start_idx
    batch_num = 1

    while idx < total:
        fim_idx = min(idx + args.batch_size, total)
        lote = links[idx:fim_idx]

        print(f"\n--- Lote {batch_num} | Abrindo links {idx + 1} a {fim_idx} de {total} ---")
        for i, url in enumerate(lote, start=idx + 1):
            print(f"  [{i}/{total}] {url}")
            if not args.dry_run:
                abrir_url_no_chrome(url)
                time.sleep(args.delay)

        idx = fim_idx
        batch_num += 1

        if idx < total and not args.all:
            try:
                resp = input(f"\nPremir [ENTER] para abrir o próximo lote ({min(args.batch_size, total - idx)} links) ou [Q] para sair: ")
                if resp.strip().lower() == "q":
                    print(f"Interrompido pelo utilizador. Próximo link a abrir seria o #{idx + 1}.")
                    break
            except KeyboardInterrupt:
                print("\nOperação cancelada.")
                break

    if idx >= total:
        print("\n Concluído! Todos os links selecionados foram abertos no Google Chrome.")

if __name__ == "__main__":
    main()
