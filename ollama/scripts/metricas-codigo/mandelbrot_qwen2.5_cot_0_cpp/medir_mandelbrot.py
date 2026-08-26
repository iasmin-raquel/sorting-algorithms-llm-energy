"""
Mede o gasto energético de execução do único código de mandelbrot
aprovado no pipeline — combo definido nas constantes abaixo
(MODELO_PROMPT, MODELO_CODIGO, ESTRATEGIA, TEMPERATURA, LINGUAGEM).

Segue a metodologia oficial do Computer Language Benchmarks Game:
- Compila com as flags de otimização do CLBG (-O3 -fomit-frame-pointer),
  trocando -march=ivybridge (CPU específica da máquina deles) por
  -march=native (otimiza para a CPU local, não para hardware alheio).
- Valida corretude em N=200 com `cmp` contra a referência (não cronometrado).
- Mede tempo/energia em N=16000 (tamanho que o próprio CLBG recomenda
  para avaliar performance — não há arquivo de referência nesse N).

CodeCarbon isola o processo (tracking_mode="process"). O combo é
gravado na coluna 'project_name' de cada linha do CSV, para não se
perder se mais combos passarem a ser medidos no mesmo arquivo.

Uso: python3 ollama/scripts/metricas-codigo/mandelbrot_qwen2.5_cot_0_cpp/medir_mandelbrot.py

Cada execução do script ADICIONA uma linha ao CSV de resultados. A
página do CLBG não documenta quantas medições eles fazem — decida e
fixe um número de repetições (ex.: 10 ou 30) e documente no TCC:

  for i in $(seq 10); do python3 medir_mandelbrot.py; done
"""
import os
import shutil
import subprocess
import tempfile
import time
from codecarbon import OfflineEmissionsTracker

PROBLEMA = "mandelbrot"
MODELO_PROMPT = "mistral-7b"    # gerou o prompt aprovado (judge/avaliacao-codigo)
MODELO_CODIGO = "qwen2.5-coder-7b"  # gerou o código a partir do prompt aprovado
ESTRATEGIA = "cot"
TEMPERATURA = "temp_0"
LINGUAGEM = "cpp"
COMBO = f"{PROBLEMA}/{MODELO_PROMPT}->{MODELO_CODIGO}/{ESTRATEGIA}/{TEMPERATURA}/{LINGUAGEM}"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # .../metricas-codigo/<combo>/
COMBO_DIR = os.path.basename(SCRIPT_DIR)  # nome da pasta = identificação do combo, ex.: mandelbrot_qwen2.5_cot_0_cpp
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))  # ollama/

SRC = os.path.join(BASE_DIR, "codigo-final", PROBLEMA, MODELO_CODIGO, ESTRATEGIA, TEMPERATURA, f"{PROBLEMA}.{LINGUAGEM}")
REFERENCIA = os.path.join(BASE_DIR, "judge", "reference-outputs", f"{PROBLEMA}-output.txt")
# pasta de resultados espelha o nome da pasta do script (mesma nomenclatura do combo)
RESULTADOS = os.path.join(BASE_DIR, "resultados", COMBO_DIR)
os.makedirs(RESULTADOS, exist_ok=True)

GPP_FLAGS = ["-O3", "-fomit-frame-pointer", "-march=native"]  # espírito das flags do CLBG, adaptadas à CPU local
N_VALIDACAO = "200"    # tamanho com referência disponível -> checagem de corretude, não cronometrado
N_MEDICAO = "16000"    # tamanho recomendado pelo CLBG para avaliar performance -> o que é cronometrado/medido


def tamanho_pbm_esperado(n):
    largura_linha = n // 8 + (1 if n % 8 else 0)
    header = f"P4\n{n} {n}\n".encode()
    return len(header) + n * largura_linha


def leitor_bit_pbm(caminho, n):
    """Retorna uma função bit(x, y) que lê o pixel (0/1) de um PBM P4."""
    largura_linha = n // 8 + (1 if n % 8 else 0)
    header_len = len(f"P4\n{n} {n}\n".encode())
    with open(caminho, "rb") as f:
        dados = f.read()

    def bit(x, y):
        offset = header_len + y * largura_linha + x // 8
        return (dados[offset] >> (7 - (x % 8))) & 1

    return bit


def main():
    print(f"=== {COMBO} ===")

    tmpdir = tempfile.mkdtemp()
    try:
        binario = os.path.join(tmpdir, "mandelbrot")
        compilacao = subprocess.run(["g++", *GPP_FLAGS, "-o", binario, SRC], capture_output=True, text=True)
        if compilacao.returncode != 0:
            print("[ERRO] Falha na compilação:")
            print(compilacao.stderr)
            raise SystemExit(1)
        print("  Compilação:        OK")

        # --- validação de corretude (N=200, cmp contra a referência, não cronometrada) ---
        validacao_path = os.path.join(tmpdir, "validacao.pbm")
        with open(validacao_path, "wb") as f:
            exec_validacao = subprocess.run([binario, N_VALIDACAO], stdout=f, stderr=subprocess.PIPE)
        if exec_validacao.returncode != 0:
            print("[ERRO] Falha na execução de validação:")
            print(exec_validacao.stderr.decode())
            raise SystemExit(1)

        cmp_resultado = subprocess.run(["cmp", validacao_path, REFERENCIA], capture_output=True, text=True)
        status_validacao = "OK (cmp idêntico)" if cmp_resultado.returncode == 0 else f"FALHOU: {cmp_resultado.stdout.strip()}"

        # --- medição de performance/energia (N=16000, sem referência disponível) ---
        saida_path = os.path.join(tmpdir, "output.pbm")

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
        with open(saida_path, "wb") as f:
            execucao = subprocess.run([binario, N_MEDICAO], stdout=f, stderr=subprocess.PIPE)
        emissoes_kg = tracker.stop()
        duracao = time.time() - inicio

        if execucao.returncode != 0:
            print("[ERRO] Falha na execução de medição:")
            print(execucao.stderr.decode())
            raise SystemExit(1)

        tamanho_real = os.path.getsize(saida_path)
        tamanho_esperado = tamanho_pbm_esperado(int(N_MEDICAO))
        tamanho_ok = tamanho_real == tamanho_esperado

        # N_MEDICAO é múltiplo exato de N_VALIDACAO (16000 = 80 * 200): o
        # pixel (x*80, y*80) da imagem grande mapeia pro MESMO número
        # complexo C que o pixel (x, y) da imagem pequena (mapeamento de
        # coordenada é escala linear exata), logo tem que dar o mesmo
        # resultado de pertencimento ao conjunto. Comparamos os 40.000
        # pixels correspondentes contra a referência (já validada por cmp).
        n_val, n_med = int(N_VALIDACAO), int(N_MEDICAO)
        escala = n_med // n_val
        bit_referencia = leitor_bit_pbm(REFERENCIA, n_val)
        bit_medicao = leitor_bit_pbm(saida_path, n_med)
        divergencias = sum(
            1
            for y in range(n_val)
            for x in range(n_val)
            if bit_referencia(x, y) != bit_medicao(x * escala, y * escala)
        )
        total_amostrado = n_val * n_val

        if tamanho_ok and divergencias == 0:
            status_medicao = f"OK (tamanho confere e {total_amostrado} pixels amostrados batem com a referência)"
        elif divergencias > 0:
            status_medicao = f"FALHOU: {divergencias}/{total_amostrado} pixels amostrados divergem da referência"
        else:
            status_medicao = f"SUSPEITO: {tamanho_real} bytes, esperado {tamanho_esperado}"

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
