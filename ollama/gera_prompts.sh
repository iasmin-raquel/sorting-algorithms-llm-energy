#!/usr/bin/env bash
# Gera os prompts a partir dos meta-prompts, usando um modelo (SLM) local.
#
# Uso: ./gera_prompts.sh <problema> <modelo>
#   ex: ./gera_prompts.sh nbody qwen3-1.7b
#       ./gera_prompts.sh mandelbrot gemma3-4b
#
# Le:     meta-prompts/<problema>/<estrategia>-<linguagem>.txt   (so os que existem)
# Chama:  <modelo>-temp0  e  <modelo>-temp07   (via API local do Ollama)
# Salva:  outputs/<problema>/<modelo>/<estrategia>/<temp>/<linguagem>.txt
set -euo pipefail
cd "$(dirname "$0")"

if [ $# -ne 2 ]; then
  echo "Uso: $0 <problema> <modelo>"
  echo "  ex: $0 nbody qwen3-1.7b"
  exit 1
fi

PROBLEMA="$1"
MODELO="$2"
API="http://localhost:11434/api/generate"
API_TAGS="http://localhost:11434/api/tags"

# Os modelfiles registram os modelos com hifen (gemma3-4b-temp0), mas o tag
# original do Ollama usa dois-pontos (gemma3:4b). Aceita as duas formas.
MODELO="${MODELO//:/-}"
if [ "$MODELO" != "$2" ]; then
  echo "aviso: usando '${MODELO}' no lugar de '${2}'"
fi

META_DIR="meta-prompts/${PROBLEMA}"
OUT_ROOT="outputs/${PROBLEMA}/${MODELO}"
MODEL_TEMP0="${MODELO}-temp0"
MODEL_TEMP07="${MODELO}-temp07"

[ -d "$META_DIR" ] || { echo "ERRO: pasta nao existe: $META_DIR"; exit 1; }

# Confere que os dois modelos existem ANTES de comecar: a API responde 200 com
# {"error": "model ... not found"} para modelo inexistente, e sem essa checagem
# a mensagem de erro acabava gravada no .txt de saida no lugar do prompt.
INSTALADOS="$(curl -sf "$API_TAGS" \
  | python3 -c "import json,sys; print('\n'.join(m['name'].split(':')[0] for m in json.load(sys.stdin)['models']))")" \
  || { echo "ERRO: Ollama nao respondeu em ${API_TAGS}"; exit 1; }

for m in "$MODEL_TEMP0" "$MODEL_TEMP07"; do
  grep -qxF "$m" <<< "$INSTALADOS" || {
    echo "ERRO: modelo nao instalado: ${m}"
    echo "Crie-o com: ollama create ${m} -f modelfiles/gera-prompt/${MODELO}/Modelfile-${m##*-}"
    echo "Modelos de prompt disponiveis:"
    grep -E -- '-temp0$' <<< "$INSTALADOS" | sed 's/-temp0$//' | sort -u | sed 's/^/  - /'
    exit 1
  }
done

for meta in "$META_DIR"/*.txt; do
  nome="$(basename "$meta" .txt)"   # ex.: cot-cpp
  strat="${nome%%-*}"               # cot
  lang="${nome#*-}"                 # cpp

  for temp in temp_0 temp_0.7; do
    case "$temp" in
      temp_0)   MODEL="$MODEL_TEMP0"  ;;
      temp_0.7) MODEL="$MODEL_TEMP07" ;;
    esac

    out_dir="${OUT_ROOT}/${strat}/${temp}"
    mkdir -p "$out_dir"
    dst="${out_dir}/${lang}.txt"

    echo ">> ${PROBLEMA}/${MODELO}/${strat}/${temp}/${lang}  (${MODEL})"

    # Grava o destino so depois de validar a resposta: 'error' na API ou texto
    # vazio abortam o script, em vez de virarem um arquivo de prompt falso.
    resposta="$(MODEL="$MODEL" python3 -c "import json,sys,os; print(json.dumps({'model':os.environ['MODEL'],'prompt':sys.stdin.read(),'stream':False}))" < "$meta" \
      | curl -s "$API" -d @- \
      | python3 -c "
import json, sys
d = json.load(sys.stdin)
if d.get('error'):
    sys.exit('ERRO da API: ' + d['error'])
r = d.get('response', '').strip()
if not r:
    sys.exit('ERRO: o modelo devolveu resposta vazia')
print(r)
")" || { echo "   falhou: ${dst} nao foi gravado"; exit 1; }

    printf '%s\n' "$resposta" > "$dst"
  done
done

echo "OK. Prompts em ${OUT_ROOT}/"
