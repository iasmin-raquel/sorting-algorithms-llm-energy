#!/usr/bin/env python3
"""
Compila, executa e valida (contra a referência do CLBG) todo código em
codigo-final/<problema>/, gerando judge/avaliacao-codigo/avaliacao_codigo_<problema>.csv
no mesmo formato usado antes da reavaliação do judge.

Uso:
  python3 scripts/validar_codigo.py <problema> [<problema> ...]
  ex: python3 scripts/validar_codigo.py binary-trees mandelbrot pidigits fasta

Parâmetros de validação (N e ferramenta de comparação) vêm dos meta-prompts
e da tabela oficial do CLBG — não são inventados aqui.
"""
import csv
import os
import re
import shutil
import subprocess
import sys
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # ollama/
REF_DIR = os.path.join(BASE_DIR, "judge", "reference-outputs")
OUT_DIR = os.path.join(BASE_DIR, "judge", "avaliacao-codigo")

VALIDACAO = {
    "binary-trees": {"N": "10", "ref": "binarytrees-output.txt", "tool": "diff"},
    "mandelbrot":   {"N": "200", "ref": "mandelbrot-output.txt", "tool": "cmp"},
    "pidigits":     {"N": "30", "ref": "pidigits-output.txt", "tool": "diff"},
    "fasta":        {"N": "1000", "ref": "fasta-output.txt", "tool": "diff"},
}

PAREADO = {
    "llama3.1-8b": "qwen3-1.7b",
    "stable-code-3b": "gemma3-4b",
    "qwen2.5-coder-7b": "mistral-7b",
    "codegemma-7b": "ministral-3.3b",
}

TIMEOUT = 60  # segundos por execução


def trunca(txt, n=200):
    txt = txt.strip().replace("\n", " ")
    return txt[:n]


def compara(saida_path, ref_path, tool):
    resultado = subprocess.run([tool, saida_path, ref_path], capture_output=True, text=True)
    if resultado.returncode == 0:
        return True, ""
    return False, ""


def valida_cpp(src, n, ref_path, tool, tmpdir):
    binario = os.path.join(tmpdir, "prog")
    comp = subprocess.run(["g++", "-O2", "-o", binario, src], capture_output=True, text=True)
    if comp.returncode != 0:
        return "nao", "-", "-", f"erro de compilacao: {trunca(comp.stderr)}"

    saida_path = os.path.join(tmpdir, "output.txt")
    try:
        with open(saida_path, "wb") as f:
            exe = subprocess.run([binario, n], stdout=f, stderr=subprocess.PIPE, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return "sim", "nao", "-", f"timeout ({TIMEOUT}s)"
    if exe.returncode != 0:
        return "sim", "nao", "-", trunca(exe.stderr.decode(errors="replace"))

    ok, _ = compara(saida_path, ref_path, tool)
    return "sim", "sim", ("sim" if ok else "nao"), ""


def valida_java(src, n, ref_path, tool, tmpdir):
    codigo = open(src, encoding="utf-8", errors="replace").read()
    m = re.search(r"public\s+class\s+(\w+)", codigo)
    if not m:
        return "nao", "-", "-", "sem classe publica"
    classe = m.group(1)

    java_path = os.path.join(tmpdir, f"{classe}.java")
    shutil.copy(src, java_path)
    comp = subprocess.run(["javac", java_path], capture_output=True, text=True)
    if comp.returncode != 0:
        return "nao", "-", "-", f"erro de compilacao: {trunca(comp.stderr)}"

    saida_path = os.path.join(tmpdir, "output.txt")
    try:
        with open(saida_path, "wb") as f:
            exe = subprocess.run(["java", "-cp", tmpdir, classe, n], stdout=f, stderr=subprocess.PIPE, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return "sim", "nao", "-", f"timeout ({TIMEOUT}s)"
    if exe.returncode != 0:
        return "sim", "nao", "-", trunca(exe.stderr.decode(errors="replace"))

    ok, _ = compara(saida_path, ref_path, tool)
    return "sim", "sim", ("sim" if ok else "nao"), ""


def valida_python(src, n, ref_path, tool, tmpdir):
    import py_compile
    try:
        py_compile.compile(src, doraise=True)
        compilou = "sim(sintaxe)"
    except py_compile.PyCompileError as e:
        return "nao", "-", "-", trunca(str(e))

    saida_path = os.path.join(tmpdir, "output.txt")
    try:
        with open(saida_path, "wb") as f:
            exe = subprocess.run([sys.executable, src, n], stdout=f, stderr=subprocess.PIPE, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return compilou, "nao", "-", f"timeout ({TIMEOUT}s)"
    if exe.returncode != 0:
        return compilou, "nao", "-", trunca(exe.stderr.decode(errors="replace"))

    ok, _ = compara(saida_path, ref_path, tool)
    return compilou, "sim", ("sim" if ok else "nao"), ""


VALIDADORES = {"cpp": valida_cpp, "java": valida_java, "py": valida_python}
EXT_TO_LANG = {"cpp": "cpp", "java": "java", "py": "python"}


def processa(problema):
    if problema not in VALIDACAO:
        print(f"!! sem parametros de validacao para '{problema}', pulando")
        return

    cfg = VALIDACAO[problema]
    ref_path = os.path.join(REF_DIR, cfg["ref"])
    codigo_dir = os.path.join(BASE_DIR, "codigo-final", problema)
    if not os.path.isdir(codigo_dir):
        print(f"!! {codigo_dir} nao existe, pulando")
        return

    linhas = []
    for modelo_codigo in sorted(os.listdir(codigo_dir)):
        modelo_prompt = PAREADO.get(modelo_codigo, "?")
        modelo_dir = os.path.join(codigo_dir, modelo_codigo)
        for raiz, _dirs, arquivos in os.walk(modelo_dir):
            for nome in arquivos:
                ext = nome.rsplit(".", 1)[-1]
                if nome != f"{problema}.{ext}" or ext not in VALIDADORES:
                    continue
                caminho = os.path.join(raiz, nome)
                rel = os.path.relpath(raiz, modelo_dir)  # estrategia/temp_X
                estrategia, temp_dir = rel.split(os.sep)
                temperatura = temp_dir.replace("temp_", "")
                linguagem = EXT_TO_LANG[ext]

                print(f">> {problema}/{modelo_codigo}/{estrategia}/{temperatura}/{linguagem}")
                with tempfile.TemporaryDirectory() as tmpdir:
                    compilou, executou, diff_correto, motivo = VALIDADORES[ext](
                        caminho, cfg["N"], ref_path, cfg["tool"], tmpdir
                    )

                linhas.append({
                    "algoritmo": problema,
                    "modelo_prompt": modelo_prompt,
                    "modelo_codigo": modelo_codigo,
                    "estrategia": estrategia,
                    "temperatura": temperatura,
                    "linguagem": linguagem,
                    "compilou": compilou,
                    "executou": executou,
                    "diff_correto": diff_correto,
                    "motivo_falha": motivo,
                })

    os.makedirs(OUT_DIR, exist_ok=True)
    csv_path = os.path.join(OUT_DIR, f"avaliacao_codigo_{problema}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "algoritmo", "modelo_prompt", "modelo_codigo", "estrategia", "temperatura",
            "linguagem", "compilou", "executou", "diff_correto", "motivo_falha",
        ])
        writer.writeheader()
        writer.writerows(linhas)

    corretos = sum(1 for l in linhas if l["diff_correto"] == "sim")
    print(f"{problema}: {corretos}/{len(linhas)} corretos -> {csv_path}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        processa(p)
