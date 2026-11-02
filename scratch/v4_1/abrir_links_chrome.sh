#!/usr/bin/env bash
# Abre no Google Chrome (macOS) os links de um ficheiro de texto (um URL por linha).
#
# Uso:
#   ./abrir_links_chrome.sh [ficheiro] [tamanho_lote] [pausa_segundos]
#
#   ficheiro        default: reddit_paginas_html.txt (na mesma pasta do script)
#   tamanho_lote    nº de links abertos antes de pedir Enter (default: 10; 0 = todos de uma vez)
#   pausa_segundos  pausa entre cada link (default: 0.5)
#
# Só abre links do Reddit; linhas vazias, começadas por '#' ou de outros sites são ignoradas.

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
FICHEIRO="${1:-$DIR/reddit_paginas_html.txt}"
LOTE="${2:-10}"
PAUSA="${3:-0.5}"

if [[ ! -f "$FICHEIRO" ]]; then
  echo "Ficheiro não encontrado: $FICHEIRO" >&2
  exit 1
fi

# Lê os URLs válidos para um array
URLS=()
while IFS= read -r linha || [[ -n "$linha" ]]; do
  # Usa só o primeiro campo: permite linhas "URL<TAB>título"
  linha="$(echo "$linha" | tr -d '\r' | awk '{print $1}')"
  [[ -z "$linha" || "$linha" == \#* ]] && continue
  # Só links do Reddit
  [[ "$linha" =~ ^https?://([a-z]+\.)?reddit\.com/ ]] || continue
  URLS+=("$linha")
done < "$FICHEIRO"

TOTAL=${#URLS[@]}
echo "A abrir $TOTAL links de: $FICHEIRO"

for i in "${!URLS[@]}"; do
  n=$((i + 1))
  echo "[$n/$TOTAL] ${URLS[$i]}"
  open -a "Google Chrome" "${URLS[$i]}"
  sleep "$PAUSA"

  if [[ "$LOTE" -gt 0 && $((n % LOTE)) -eq 0 && "$n" -lt "$TOTAL" ]]; then
    read -r -p "Lote de $LOTE aberto. Enter para continuar (q para sair): " resp < /dev/tty
    [[ "$resp" == "q" ]] && { echo "Interrompido em $n/$TOTAL."; exit 0; }
  fi
done

echo "Concluído: $TOTAL links abertos."
