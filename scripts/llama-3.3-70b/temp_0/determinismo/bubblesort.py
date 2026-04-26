import os
from groq import Groq

client = Groq()

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "saida", "llama-3.3-70b", "temp_0", "determinismo", "bubblesort"))
os.makedirs(SAIDA_DIR, exist_ok=True)

PROMPT = "Please write your best implementation of BubbleSort in Java programming language."

saidas = []

for rodada in range(1, 6):
    print(f"=== BubbleSort | Rodada {rodada} ===")
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0,
        seed=42,
        max_completion_tokens=4096,
        stream=False,
    )
    texto = completion.choices[0].message.content
    tokens = completion.usage.completion_tokens
    saidas.append(texto)

    caminho = os.path.join(SAIDA_DIR, f"BubbleSort_run{rodada}.txt")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"  Tokens gerados: {tokens}")
    print(f"  Arquivo salvo:  BubbleSort_run{rodada}.txt\n")

print("=== Comparação ===")
pares_iguais = []
pares_diferentes = []
for i in range(len(saidas)):
    for j in range(i + 1, len(saidas)):
        if saidas[i] == saidas[j]:
            pares_iguais.append((i + 1, j + 1))
        else:
            pares_diferentes.append((i + 1, j + 1))

print(f"Pares IDÊNTICOS ({len(pares_iguais)}):")
if pares_iguais:
    for r1, r2 in pares_iguais:
        print(f"  Run{r1} == Run{r2}")
else:
    print("  Nenhum par idêntico.")

print(f"\nPares DIFERENTES ({len(pares_diferentes)}):")
if pares_diferentes:
    for r1, r2 in pares_diferentes:
        linhas1 = saidas[r1 - 1].splitlines()
        linhas2 = saidas[r2 - 1].splitlines()
        diferencas = [(i+1, l1, l2) for i, (l1, l2) in enumerate(zip(linhas1, linhas2)) if l1 != l2]
        extras = abs(len(linhas1) - len(linhas2))
        print(f"  Run{r1} != Run{r2}: {len(diferencas)} linha(s) divergem, {extras} linha(s) a mais/menos.")
        for num, l1, l2 in diferencas[:3]:
            print(f"    Linha {num}:")
            print(f"      Run{r1}: {l1}")
            print(f"      Run{r2}: {l2}")
else:
    print("  Nenhum par diferente.")
