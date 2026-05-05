import os
import sys
from groq import Groq

client = Groq()

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "saida", "qwen3-32b", "temp_0", "determinismo", "bubblesort"))
os.makedirs(SAIDA_DIR, exist_ok=True)

LOG_FILE = open(os.path.join(SAIDA_DIR, "output.log"), "w", encoding="utf-8")

def log(msg=""):
    print(msg)
    LOG_FILE.write(msg + "\n")

PROMPT = "Please write your best implementation of BubbleSort in Java programming language."

saidas = []

for rodada in range(1, 6):
    log(f"=== BubbleSort | Rodada {rodada} ===")
    completion = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0,
        seed=42,
        max_completion_tokens=4096,
        top_p=0.95,
        reasoning_effort="none",
        stream=False,
    )
    texto = completion.choices[0].message.content
    tokens = completion.usage.completion_tokens
    saidas.append(texto)

    caminho = os.path.join(SAIDA_DIR, f"BubbleSort_run{rodada}.txt")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)

    log(f"  Tokens gerados: {tokens}")
    log(f"  Arquivo salvo:  BubbleSort_run{rodada}.txt\n")

log("=== Comparação ===")
pares_iguais = []
pares_diferentes = []
for i in range(len(saidas)):
    for j in range(i + 1, len(saidas)):
        if saidas[i] == saidas[j]:
            pares_iguais.append((i + 1, j + 1))
        else:
            pares_diferentes.append((i + 1, j + 1))

log(f"Pares IDÊNTICOS ({len(pares_iguais)}):")
if pares_iguais:
    for r1, r2 in pares_iguais:
        log(f"  Run{r1} == Run{r2}")
else:
    log("  Nenhum par idêntico.")

log(f"\nPares DIFERENTES ({len(pares_diferentes)}):")
if pares_diferentes:
    for r1, r2 in pares_diferentes:
        linhas1 = saidas[r1 - 1].splitlines()
        linhas2 = saidas[r2 - 1].splitlines()
        diferencas = [(i+1, l1, l2) for i, (l1, l2) in enumerate(zip(linhas1, linhas2)) if l1 != l2]
        extras = abs(len(linhas1) - len(linhas2))
        log(f"  Run{r1} != Run{r2}: {len(diferencas)} linha(s) divergem, {extras} linha(s) a mais/menos.")
        for num, l1, l2 in diferencas[:3]:
            log(f"    Linha {num}:")
            log(f"      Run{r1}: {l1}")
            log(f"      Run{r2}: {l2}")
else:
    log("  Nenhum par diferente.")

LOG_FILE.close()
