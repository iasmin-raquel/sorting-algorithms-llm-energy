#!/usr/bin/env python3
"""
Deriva prompts-aprovados/<problema>/<modelo>.txt a partir da coluna
'aprovado' em judge/avaliacao_judge_<problema>.csv.

Uso:
  python3 atualiza_aprovados.py <problema> [<problema> ...]
  ex: python3 atualiza_aprovados.py binary-trees fasta pidigits mandelbrot

Cada execucao SOBRESCREVE prompts-aprovados/<problema>/<modelo>.txt por
inteiro (o CSV do judge e a fonte da verdade). Modelos sem nenhum combo
aprovado ganham um arquivo vazio, para que gera_codigo.sh nao falhe por
"arquivo nao encontrado" e simplesmente nao gere nada para esse modelo.
"""
import csv
import os
import sys
from collections import defaultdict

APROVADO_OK = {"sim", "yes", "true", "1"}


def normaliza_temp(temp_raw: str) -> str:
    temp_raw = temp_raw.strip()
    return temp_raw if temp_raw.startswith("temp_") else f"temp_{temp_raw}"


def normaliza_modelo(modelo_raw: str) -> str:
    return modelo_raw.strip().replace(":", "-")


def processa(problema: str) -> None:
    csv_path = f"judge/avaliacao_judge_{problema}.csv"
    if not os.path.exists(csv_path):
        print(f"!! {csv_path} nao encontrado, pulando '{problema}'")
        return

    aprovados = defaultdict(list)   # modelo -> [combo, ...]
    modelos_vistos = set()
    total_rows = 0

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        faltando = {"modelo", "estrategia", "temperatura", "linguagem", "aprovado"} - set(reader.fieldnames or [])
        if faltando:
            print(f"!! {csv_path}: colunas ausentes {faltando}, pulando '{problema}'")
            return

        for row in reader:
            total_rows += 1
            modelo = normaliza_modelo(row["modelo"])
            modelos_vistos.add(modelo)

            if row["aprovado"].strip().lower() not in APROVADO_OK:
                continue

            estrategia = row["estrategia"].strip()
            temp = normaliza_temp(row["temperatura"])
            linguagem = row["linguagem"].strip()
            aprovados[modelo].append(f"{estrategia}/{temp}/{linguagem}")

    out_dir = f"prompts-aprovados/{problema}"
    os.makedirs(out_dir, exist_ok=True)

    total_aprovados = 0
    for modelo in sorted(modelos_vistos):
        combos = sorted(set(aprovados.get(modelo, [])))
        dst = f"{out_dir}/{modelo}.txt"
        with open(dst, "w", encoding="utf-8") as f:
            for combo in combos:
                f.write(combo + "\n")
        total_aprovados += len(combos)
        print(f"  {modelo}: {len(combos)} aprovados -> {dst}")

    print(f"{problema}: {total_aprovados}/{total_rows} aprovados no total\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    for problema in sys.argv[1:]:
        processa(problema)
