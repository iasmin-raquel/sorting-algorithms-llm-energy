"""
Junta os resumos de múltiplos lotes (e múltiplos combos) num único CSV,
adicionando colunas 'combo' e 'lote' pra identificar a origem de cada linha.

Uso:
  python3 ollama/scripts/metricas-codigo/consolidar_lotes.py <saida.csv> <combo1> <combo2> ...
  ex: python3 consolidar_lotes.py consolidado_pidigits.csv \
        pidigits_codegemma-7b_cot_0_python pidigits_baseline_clbg_python

Lê ollama/resultados/<combo>/lotes/resumo_<problema>_lote*.csv de cada combo
passado e escreve ollama/resultados/<saida.csv>.
"""
import csv
import glob
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # ollama/


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    saida_nome = sys.argv[1]
    combos = sys.argv[2:]

    linhas = []
    for combo in combos:
        lotes_dir = os.path.join(BASE_DIR, "resultados", combo, "lotes")
        arquivos = sorted(glob.glob(os.path.join(lotes_dir, "resumo_*_lote*.csv")))
        if not arquivos:
            print(f"!! nenhum resumo de lote encontrado em {lotes_dir}, pulando '{combo}'")
            continue
        for caminho in arquivos:
            m = re.search(r"lote(\d+)\.csv$", caminho)
            lote = m.group(1) if m else "?"
            with open(caminho, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    row_nova = {"combo": combo, "lote": lote, **row}
                    linhas.append(row_nova)

    if not linhas:
        print("Nada pra consolidar.")
        sys.exit(1)

    colunas = list(linhas[0].keys())
    saida_path = os.path.join(BASE_DIR, "resultados", saida_nome)
    with open(saida_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(linhas)

    print(f"{len(linhas)} linhas consolidadas de {len(combos)} combo(s) -> {os.path.relpath(saida_path, BASE_DIR)}")


if __name__ == "__main__":
    main()
