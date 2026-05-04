"""
Mede o gasto energético de execução de um arquivo Java gerado pela LLM.

O script injeta um loop de benchmark no main() para obter uma medição
significativa (o main() original costuma ordenar apenas poucos elementos).

Uso:
  python scripts/medir_execucao.py <caminho_para_arquivo.java>

Exemplo:
  python scripts/medir_execucao.py algoritmos_gerados/qwen3-32b/temp_0/zero_shot/QuickSort.java

O arquivo .java deve estar dentro de algoritmos_gerados/<modelo>/<temp>/<tecnica>/.
Os resultados são salvos em resultados/<modelo>/<temp>/<tecnica>/execucao/.
"""

import os
import re
import sys
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from codecarbon import EmissionsTracker

EXPERIMENT_IDS = {
    "BubbleSort": "922f11ca-1de2-4e5d-b278-9a888492cbaa",
    "MergeSort":  "fe3c0fe2-8018-44d2-bb58-f13cb07d6ffa",
    "QuickSort":  "8b81002e-b98a-4254-9258-c586c04ebc0a",
}

N_ITERACOES = 1_000
TAMANHO_ARRAY = 2_000


def detectar_classe(codigo):
    m = re.search(r"public\s+class\s+(\w+)", codigo)
    if not m:
        raise ValueError("Não foi possível detectar o nome da classe.")
    return m.group(1)


def detectar_chamada_sort(codigo, classe):
    """Detecta o método de ordenação principal e retorna a chamada Java."""
    padrao = re.compile(
        r"public\s+static\s+(?:void|int\[\])\s+(\w+)\s*\(([^)]*)\)"
    )
    for m in padrao.finditer(codigo):
        nome   = m.group(1)
        params = m.group(2)

        if nome in ("main", "printArray", "print", "swap", "toString"):
            continue
        if nome.startswith("print") or nome.startswith("display"):
            continue

        param_lista = [p.strip() for p in params.split(",") if p.strip()]

        if len(param_lista) == 1:
            # sort(int[] arr)
            return f"{nome}(arr);"
        elif len(param_lista) == 3:
            # ex.: quickSort(int[] arr, int low, int high)
            return f"{nome}(arr, 0, arr.length - 1);"
        elif len(param_lista) == 2:
            # ex.: mergeSort(int[] arr, int n)
            p2 = param_lista[1]
            if "int" in p2 and "[" not in p2:
                return f"{nome}(arr, arr.length);"
            return f"{nome}(arr, 0);"

    raise ValueError("Nenhum método de ordenação identificado automaticamente.")


def remover_main(codigo):
    """Remove o bloco main() existente do código."""
    resultado = re.sub(
        r"public\s+static\s+void\s+main\s*\([^)]*\)\s*\{",
        "__MAIN_PLACEHOLDER__",
        codigo,
        count=1,
    )
    if "__MAIN_PLACEHOLDER__" not in resultado:
        return codigo

    inicio = resultado.index("__MAIN_PLACEHOLDER__")
    depth = 0
    i = inicio + len("__MAIN_PLACEHOLDER__")
    while i < len(resultado):
        if resultado[i] == "{":
            depth += 1
        elif resultado[i] == "}":
            if depth == 0:
                i += 1
                break
            depth -= 1
        i += 1

    return resultado[:inicio] + resultado[i:]


def gerar_benchmark(codigo, classe, chamada_sort):
    codigo_sem_main = remover_main(codigo)

    novo_main = f"""
    public static void main(String[] args) {{
        int n = {N_ITERACOES};
        int size = {TAMANHO_ARRAY};
        java.util.Random rng = new java.util.Random(42);
        int[] base = new int[size];
        for (int i = 0; i < size; i++) base[i] = rng.nextInt(100_000);

        for (int i = 0; i < n; i++) {{
            int[] arr = base.clone();
            {chamada_sort}
        }}
    }}
"""

    ultimo_fecha = codigo_sem_main.rfind("}")
    return codigo_sem_main[:ultimo_fecha] + novo_main + "\n}"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    java_path = Path(sys.argv[1]).resolve()
    if not java_path.exists():
        print(f"Arquivo não encontrado: {java_path}")
        sys.exit(1)

    base_dir = Path(__file__).resolve().parent.parent
    try:
        partes = java_path.relative_to(base_dir / "algoritmos_gerados").parts
        modelo, temp, tecnica = partes[0], partes[1], partes[2]
    except (ValueError, IndexError):
        print("O arquivo deve estar em algoritmos_gerados/<modelo>/<temp>/<tecnica>/")
        sys.exit(1)

    algoritmo = java_path.stem
    exp_id = EXPERIMENT_IDS.get(algoritmo)
    if not exp_id:
        print(f"Algoritmo '{algoritmo}' não reconhecido. Use BubbleSort, MergeSort ou QuickSort.")
        sys.exit(1)

    resultados_dir = base_dir / "resultados" / modelo / temp / tecnica / "execucao"
    resultados_dir.mkdir(parents=True, exist_ok=True)
    csv_path = resultados_dir / f"emissoes_{algoritmo}.csv"

    codigo_original = java_path.read_text(encoding="utf-8")
    classe = detectar_classe(codigo_original)

    try:
        chamada_sort = detectar_chamada_sort(codigo_original, classe)
    except ValueError as e:
        print(f"[ERRO] {e}")
        print("Verifique o arquivo Java e tente novamente.")
        sys.exit(1)

    codigo_benchmark = gerar_benchmark(codigo_original, classe, chamada_sort)

    tmpdir = tempfile.mkdtemp()
    try:
        java_bench = os.path.join(tmpdir, f"{classe}.java")
        with open(java_bench, "w", encoding="utf-8") as f:
            f.write(codigo_benchmark)

        print(f"=== {algoritmo} | {modelo} | {temp} | {tecnica} ===")
        print(f"  Classe detectada:  {classe}")
        print(f"  Chamada de sort:   {chamada_sort}")
        print(f"  Iterações:         {N_ITERACOES:,}  ×  array de {TAMANHO_ARRAY:,} elementos")

        resultado_javac = subprocess.run(
            ["javac", java_bench],
            capture_output=True,
            text=True,
        )
        if resultado_javac.returncode != 0:
            print("\n[ERRO] Falha na compilação:")
            print(resultado_javac.stderr)
            sys.exit(1)
        print("  Compilação:        OK")

        tracker = EmissionsTracker(
            project_name=algoritmo,
            experiment_id=exp_id,
            output_file=str(csv_path),
            save_to_api=True,
            log_level="error",
        )

        inicio = time.time()
        tracker.start()
        resultado_java = subprocess.run(
            ["java", "-cp", tmpdir, classe],
            capture_output=True,
            text=True,
        )
        emissoes = tracker.stop()
        duracao = time.time() - inicio

        if resultado_java.returncode != 0:
            print("\n[ERRO] Falha na execução:")
            print(resultado_java.stderr)
            sys.exit(1)

        print(f"  Duração:           {duracao:.2f}s")
        print(f"  CO₂ emitido:       {emissoes:.6f} kg")
        print(f"  Resultado salvo:   {csv_path.relative_to(base_dir)}")

    finally:
        shutil.rmtree(tmpdir)


if __name__ == "__main__":
    main()
