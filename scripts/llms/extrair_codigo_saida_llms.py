"""
Extrai o primeiro bloco de código Java de cada arquivo .txt em saida/
e salva o arquivo .java correspondente em algoritmos_gerados/.

Execução: python scripts/extrair_codigo.py
"""

import os
import re

BASE_DIR    = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SAIDA_DIR   = os.path.join(BASE_DIR, "saida")
DESTINO_DIR = os.path.join(BASE_DIR, "algoritmos_gerados")

TECNICAS = {"zero_shot", "few_shot"}

def extrair_java(texto):
    match = re.search(r"```java\s*(.*?)```", texto, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

processados = 0
erros = 0

for raiz, dirs, arquivos in os.walk(SAIDA_DIR):
    dirs[:] = [d for d in dirs if d != "determinismo"]

    partes = os.path.relpath(raiz, SAIDA_DIR).split(os.sep)
    if len(partes) < 3:
        continue

    modelo, temp, tecnica = partes[0], partes[1], partes[2]
    if tecnica not in TECNICAS:
        continue

    for nome in arquivos:
        if not nome.endswith(".txt"):
            continue

        algoritmo = nome.replace(".txt", "")
        caminho_txt = os.path.join(raiz, nome)

        with open(caminho_txt, encoding="utf-8") as f:
            conteudo = f.read()

        codigo = extrair_java(conteudo)
        if not codigo:
            print(f"[AVISO] Nenhum bloco Java encontrado em: {os.path.relpath(caminho_txt, BASE_DIR)}")
            erros += 1
            continue

        destino = os.path.join(DESTINO_DIR, modelo, temp, tecnica)
        os.makedirs(destino, exist_ok=True)

        caminho_java = os.path.join(destino, f"{algoritmo}.java")
        with open(caminho_java, "w", encoding="utf-8") as f:
            f.write(codigo + "\n")

        print(f"[OK] {os.path.relpath(caminho_java, BASE_DIR)}")
        processados += 1

print(f"\n{processados} arquivo(s) extraído(s), {erros} aviso(s).")
