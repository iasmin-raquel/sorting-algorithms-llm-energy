"""
Mede o gasto energético de execução do benchmark Knucleotide.

Uso: python scripts/medir_benchmark.py
"""

import os
import subprocess
import time
from codecarbon import EmissionsTracker

BASE_DIR      = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BENCH_DIR     = os.path.join(BASE_DIR, "algoritmos_benchmark")
RESULTADOS    = os.path.join(BASE_DIR, "resultados", "benchmark", "execucao")
os.makedirs(RESULTADOS, exist_ok=True)

FASTUTIL  = "/home/iasmin/fastutil-8.5.13.jar"
INPUT     = os.path.join(BENCH_DIR, "knucleotide-input25000000.txt")
CLASSPATH = f"{BENCH_DIR}:{FASTUTIL}"

tracker = EmissionsTracker(
    project_name="Knucleotide",
    output_file=os.path.join(RESULTADOS, "emissoes_Knucleotide.csv"),
    save_to_api=False,
    log_level="error",
)

print("=== Knucleotide benchmark ===")

inicio = time.time()
tracker.start()
resultado = subprocess.run(
    ["java", "-cp", CLASSPATH, "Knucleotide"],
    stdin=open(INPUT, "rb"),
    capture_output=True,
)
emissoes = tracker.stop()
duracao = time.time() - inicio

print(resultado.stdout.decode())
print(f"  Duração:     {duracao:.2f}s")
print(f"  CO₂ emitido: {emissoes:.6f} kg")
print(f"  Resultado salvo em: resultados/benchmark/execucao/emissoes_Knucleotide.csv")