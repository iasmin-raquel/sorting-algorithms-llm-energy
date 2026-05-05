"""
Mede o gasto energético de execução do benchmark RevComp.

Uso: python scripts/benchmark/medir_revcomp.py
"""

import os
import subprocess
import time
from codecarbon import EmissionsTracker

BASE_DIR   = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BENCH_DIR  = os.path.join(BASE_DIR, "algoritmos_benchmark")
RESULTADOS = os.path.join(BASE_DIR, "resultados", "benchmark", "execucao")
os.makedirs(RESULTADOS, exist_ok=True)

INPUT = os.path.join(BENCH_DIR, "knucleotide-input25000000.txt")

tracker = EmissionsTracker(
    project_name="RevComp",
    output_file=os.path.join(RESULTADOS, "emissoes_RevComp.csv"),
    save_to_api=False,
    log_level="error",
)

print("=== RevComp benchmark ===")

inicio = time.time()
tracker.start()
resultado = subprocess.run(
    ["java", "-cp", BENCH_DIR, "revcomp"],
    stdin=open(INPUT, "rb"),
    capture_output=True,
)
emissoes = tracker.stop()
duracao = time.time() - inicio

print(resultado.stdout.decode()[:500])
print(f"  Duração:     {duracao:.2f}s")
print(f"  CO₂ emitido: {emissoes:.6f} kg")
print(f"  Resultado salvo em: resultados/benchmark/execucao/emissoes_RevComp.csv")
