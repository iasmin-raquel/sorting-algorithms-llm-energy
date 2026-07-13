#!/usr/bin/env bash
# Gera o codigo final a partir dos prompts APROVADOS, usando um modelo gerador
# de codigo local. A lista de aprovados vem de um arquivo (dado, nao codigo).
#
# Uso: ./gera_codigo.sh <problema> <modelo_prompt> <modelo_codigo>
#   ex: ./gera_codigo.sh nbody mistral-7b qwen2.5-coder-7b
#       ./gera_codigo.sh mandelbrot qwen3-1.7b llama3.1-8b
#
# Le a lista: prompts-aprovados/<problema>/<modelo_prompt>.txt
#             (um combo por linha, no formato: <estrategia>/<temp>/<linguagem>)
# Le o prompt: outputs/<problema>/<modelo_prompt>/<combo>.txt
# Salva:       codigo-final/<problema>/<modelo_codigo>/<combo_dir>/<problema>.<ext>
set -euo pipefail
cd "$(dirname "$0")"

if [ $# -ne 3 ]; then
  echo "Uso: $0 <problema> <modelo_prompt> <modelo_codigo>"
  echo "  ex: $0 nbody mistral-7b qwen2.5-coder-7b"
  exit 1
fi

PROBLEMA="$1"
MODELO_PROMPT="$2"
MODELO_CODIGO="$3"

PROMPTS_DIR="outputs/${PROBLEMA}/${MODELO_PROMPT}"
OUT_ROOT="codigo-final/${PROBLEMA}/${MODELO_CODIGO}"
APROVADOS="prompts-aprovados/${PROBLEMA}/${MODELO_PROMPT}.txt"
API="http://localhost:11434/api/generate"

[ -f "$APROVADOS" ] || { echo "ERRO: lista de aprovados nao existe: $APROVADOS"; exit 1; }

declare -A EXT=( [cpp]=cpp [java]=java [python]=py )

while read -r combo; do
  [ -z "$combo" ] && continue
  case "$combo" in \#*) continue ;; esac      # ignora comentarios

  case "$combo" in
    */temp_0/*)   MODEL="${MODELO_CODIGO}-temp0"  ;;
    */temp_0.7/*) MODEL="${MODELO_CODIGO}-temp07" ;;
    *) echo "!! combo sem temperatura reconhecida: $combo"; continue ;;
  esac

  lang="${combo##*/}"
  ext="${EXT[$lang]:-txt}"

  src="${PROMPTS_DIR}/${combo}.txt"
  [ -f "$src" ] || { echo "!! prompt nao encontrado: $src"; continue; }

  out_dir="${OUT_ROOT}/$(dirname "$combo")"
  mkdir -p "$out_dir"
  dst="${out_dir}/${PROBLEMA}.${ext}"

  # Extracao tolerante: se o modelo usou o cabecalho "### Prompt Structure",
  # corta o preambulo (ex.: bloco "Thinking..." do qwen3). Se nao usou os
  # cabecalhos, manda o arquivo inteiro.
  if grep -q "Prompt Structure" "$src"; then
    prompt="$(sed -n '/Prompt Structure/,$p' "$src")"
  else
    prompt="$(cat "$src")"
  fi

  echo ">> ${combo}  ->  ${dst}  (${MODEL})"

  resp="$(MODEL="$MODEL" python3 -c "import json,sys,os; print(json.dumps({'model':os.environ['MODEL'],'prompt':sys.stdin.read(),'stream':False}))" <<< "$prompt" \
    | curl -s "$API" -d @- \
    | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('response', d.get('error','')))")"

  # extrai o 1o bloco de codigo (entre as cercas ```); se nao houver, usa tudo
  code="$(printf '%s' "$resp" | awk '/^```/{c++; next} c==1')"
  [ -z "$code" ] && code="$resp"

  printf '%s\n' "$code" > "$dst"
done < "$APROVADOS"

echo "OK. Codigo em ${OUT_ROOT}/"
