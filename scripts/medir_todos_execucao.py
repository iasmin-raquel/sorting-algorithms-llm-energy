"""
Roda medir_execucao.py para todos os arquivos Java em algoritmos_gerados/
(exclui pasta determinismo). Pula arquivos cujo CSV já existe.

Execução: python scripts/medir_todos_execucao.py
"""

import os
import subprocess
import sys

BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GERADOS_DIR = os.path.join(BASE_DIR, "algoritmos_gerados")
SCRIPT      = os.path.join(BASE_DIR, "scripts", "medir_execucao.py")
TECNICAS    = {"zero_shot", "few_shot"}

java_files = []
for raiz, dirs, arquivos in os.walk(GERADOS_DIR):
    dirs[:] = [d for d in dirs if d != "determinismo"]
    partes = os.path.relpath(raiz, GERADOS_DIR).split(os.sep)
    if len(partes) < 3:
        continue
    modelo, temp, tecnica = partes[0], partes[1], partes[2]
    if tecnica not in TECNICAS:
        continue
    for nome in sorted(arquivos):
        if nome.endswith(".java"):
            java_files.append(os.path.join(raiz, nome))

java_files.sort()
total = len(java_files)
print(f"Encontrados {total} arquivo(s) Java para medir.\n")

ok, pulados, erros = 0, 0, 0
for i, java_path in enumerate(java_files, 1):
    rel = os.path.relpath(java_path, BASE_DIR)
    partes = os.path.relpath(java_path, GERADOS_DIR).split(os.sep)
    modelo, temp, tecnica = partes[0], partes[1], partes[2]
    algoritmo = os.path.splitext(partes[3])[0]

    csv = os.path.join(
        BASE_DIR, "resultados", modelo, temp, tecnica,
        "execucao", f"emissoes_{algoritmo}.csv"
    )
    if os.path.exists(csv):
        print(f"[{i}/{total}] PULADO (já existe): {rel}")
        pulados += 1
        continue

    print(f"[{i}/{total}] Medindo: {rel}")
    resultado = subprocess.run(
        [sys.executable, SCRIPT, java_path],
        capture_output=False,
    )
    if resultado.returncode == 0:
        ok += 1
    else:
        erros += 1
    print()

print(f"\nResumo: {ok} medido(s), {pulados} pulado(s), {erros} erro(s).")
