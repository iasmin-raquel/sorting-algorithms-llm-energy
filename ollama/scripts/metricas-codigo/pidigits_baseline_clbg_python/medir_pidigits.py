"""
Mede o gasto energético de execução do BASELINE oficial do pidigits
(implementação humana de referência do Computer Language Benchmarks Game,
não gerada por SLM) — usado como comparação de referência pro RQ2/RQ3.

Segue a mesma metodologia usada nos combos gerados por SLM:
- Executa com `python3 -OO` (flag do COMMAND LINE oficial do CLBG).
- Valida corretude em N=30 com `diff` contra a referência (não cronometrado).
- Mede tempo/energia em N=10000 (tamanho recomendado pelo CLBG para
  performance — não há arquivo de referência nesse N).

CodeCarbon isola o processo (tracking_mode="process"). O combo é gravado
na coluna 'project_name' de cada linha do CSV.

Uso: python3 ollama/scripts/metricas-codigo/pidigits_baseline_clbg_python/medir_pidigits.py

Cada execução do script ADICIONA uma linha ao CSV de resultados. Rode
várias vezes (ex.: 10) e agregue com resumo_medicoes.py:

  for i in $(seq 10); do python3 medir_pidigits.py; done
  python3 ../resumo_medicoes.py pidigits_baseline_clbg_python
"""
import os
import shutil
import subprocess
import sys
import tempfile
import time
from codecarbon import OfflineEmissionsTracker

PROBLEMA = "pidigits"
FONTE = "CLBG-baseline-humano"   # não é SLM: implementação de referência oficial
LINGUAGEM = "python"
COMBO = f"{PROBLEMA}/{FONTE}/{LINGUAGEM}"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # .../metricas-codigo/<combo>/
COMBO_DIR = os.path.basename(SCRIPT_DIR)  # pidigits_baseline_clbg_python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))  # ollama/

SRC = os.path.join(SCRIPT_DIR, "pidigits_baseline.py")  # fonte fica junto do script, não em codigo-final/
REFERENCIA = os.path.join(BASE_DIR, "judge", "reference-outputs", f"{PROBLEMA}-output.txt")
# pasta de resultados espelha o nome da pasta do script (mesma nomenclatura do combo)
RESULTADOS = os.path.join(BASE_DIR, "resultados", COMBO_DIR)
os.makedirs(RESULTADOS, exist_ok=True)

PYTHON_FLAGS = ["-OO"]  # flag do COMMAND LINE oficial do CLBG
N_VALIDACAO = "30"      # tamanho com referência disponível -> checagem de corretude, não cronometrado
N_MEDICAO = "10000"     # tamanho recomendado pelo CLBG para avaliar performance -> o que é cronometrado/medido


def main():
    print(f"=== {COMBO} ===")

    tmpdir = tempfile.mkdtemp()
    try:
        # --- validação de corretude (N=30, diff contra a referência, não cronometrada) ---
        validacao_path = os.path.join(tmpdir, "validacao.txt")
        with open(validacao_path, "w") as f:
            exec_validacao = subprocess.run(
                [sys.executable, *PYTHON_FLAGS, SRC, N_VALIDACAO],
                stdout=f, stderr=subprocess.PIPE, text=True,
            )
        if exec_validacao.returncode != 0:
            print("[ERRO] Falha na execução de validação:")
            print(exec_validacao.stderr)
            raise SystemExit(1)

        diff_resultado = subprocess.run(["diff", validacao_path, REFERENCIA], capture_output=True, text=True)
        status_validacao = "OK (diff idêntico)" if diff_resultado.returncode == 0 else f"FALHOU: {diff_resultado.stdout.strip()}"

        # --- medição de performance/energia (N=10000, sem referência disponível) ---
        saida_path = os.path.join(tmpdir, "output.txt")

        tracker = OfflineEmissionsTracker(
            project_name=COMBO,
            country_iso_code="BRA",
            tracking_mode="process",
            output_file=os.path.join(RESULTADOS, f"emissoes_{PROBLEMA}.csv"),
            save_to_api=False,
            log_level="error",
        )

        inicio = time.time()
        tracker.start()
        with open(saida_path, "w") as f:
            execucao = subprocess.run(
                [sys.executable, *PYTHON_FLAGS, SRC, N_MEDICAO],
                stdout=f, stderr=subprocess.PIPE, text=True,
            )
        emissoes_kg = tracker.stop()
        duracao = time.time() - inicio

        if execucao.returncode != 0:
            print("[ERRO] Falha na execução de medição:")
            print(execucao.stderr)
            raise SystemExit(1)

        with open(saida_path) as f:
            linhas_medicao = f.readlines()
        ultima_linha = linhas_medicao[-1].strip()
        termina_certo = ultima_linha.endswith(f":{N_MEDICAO}")

        # O algoritmo spigot é sequencial: os primeiros dígitos calculados
        # numa execução em N=10000 são idênticos aos de uma execução em
        # N=30 (não dependem do N alvo). Então dá pra comparar o PREFIXO
        # da saída medida contra a referência, mesmo sem ter uma
        # referência de 10000 dígitos.
        with open(REFERENCIA) as f:
            n_linhas_ref = len(f.readlines())
        prefixo_path = os.path.join(tmpdir, "prefixo.txt")
        with open(prefixo_path, "w") as f:
            f.writelines(linhas_medicao[:n_linhas_ref])
        prefixo_diff = subprocess.run(["diff", prefixo_path, REFERENCIA], capture_output=True, text=True)
        prefixo_ok = prefixo_diff.returncode == 0

        if termina_certo and prefixo_ok:
            status_medicao = f"OK (prefixo bate com a referência e termina em ':{N_MEDICAO}')"
        elif not prefixo_ok:
            status_medicao = f"FALHOU: prefixo diverge da referência: {prefixo_diff.stdout.strip()}"
        else:
            status_medicao = f"SUSPEITO: última linha é '{ultima_linha}'"

        emissoes_g = emissoes_kg * 1000
        taxa_g_s = (emissoes_g / duracao) if duracao > 0 else 0.0

        print(f"  Validação (N={N_VALIDACAO}):   {status_validacao}")
        print(f"  Medição (N={N_MEDICAO}):    {status_medicao}")
        print(f"  Duração (TE):      {duracao:.4f} s")
        print(f"  CO2 emitido (TCO2): {emissoes_g:.6f} g")
        print(f"  Taxa (CO2eq/s):    {taxa_g_s:.6f} g/s")
        print(f"  Resultado salvo em: {os.path.relpath(os.path.join(RESULTADOS, f'emissoes_{PROBLEMA}.csv'), BASE_DIR)}")
        print(f"  (identifique a linha no CSV pela coluna 'project_name' = '{COMBO}')")
    finally:
        shutil.rmtree(tmpdir)


if __name__ == "__main__":
    main()
