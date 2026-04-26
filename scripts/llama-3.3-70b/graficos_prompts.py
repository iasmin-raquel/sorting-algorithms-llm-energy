import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
RESULTADOS   = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "resultados", "llama-3.3-70b"))

algoritmos   = ["QuickSort", "MergeSort", "BubbleSort"]
temperaturas = ["temp_0", "temp_0.7"]
tecnicas     = ["zero_shot", "few_shot"]

def carregar(temp, tecnica, nome):
    caminho = os.path.join(RESULTADOS, temp, tecnica, "isolado", f"emissoes_{nome}.csv")
    df = pd.read_csv(caminho)
    return df.iloc[-1]

dados = []
for temp in temperaturas:
    for tecnica in tecnicas:
        for nome in algoritmos:
            try:
                r = carregar(temp, tecnica, nome)
                dados.append({
                    "Algoritmo":    nome,
                    "Temperatura":  temp.replace("temp_", ""),
                    "Técnica":      tecnica,
                    "CO₂ (kg)":     r["emissions"],
                    "Energia (kWh)": r["energy_consumed"],
                    "Duração (s)":  r["duration"],
                })
            except FileNotFoundError:
                print(f"  [aviso] Arquivo não encontrado: {temp}/{tecnica}/{nome}")

df = pd.DataFrame(dados)
if df.empty:
    print("Nenhum dado encontrado. Execute os experimentos primeiro.")
    exit()

print(df.to_string(index=False))

metricas = [
    ("CO₂ (kg)",       "CO₂ emitido (kg eq CO₂)", "CO₂ Emitido"),
    ("Energia (kWh)",  "Energia consumida (kWh)",   "Energia Consumida"),
    ("Duração (s)",    "Tempo de execução (s)",      "Duração"),
]

cores = {
    ("0",   "zero_shot"): "#1565C0",
    ("0",   "few_shot"):  "#42A5F5",
    ("0.7", "zero_shot"): "#B71C1C",
    ("0.7", "few_shot"):  "#EF9A9A",
}
rotulos = {
    ("0",   "zero_shot"): "t=0 zero_shot",
    ("0",   "few_shot"):  "t=0 few_shot",
    ("0.7", "zero_shot"): "t=0.7 zero_shot",
    ("0.7", "few_shot"):  "t=0.7 few_shot",
}

combinacoes = [("0", "zero_shot"), ("0", "few_shot"), ("0.7", "zero_shot"), ("0.7", "few_shot")]
n       = len(algoritmos)
largura = 0.18
x       = range(n)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Llama-3.3-70B — Zero-shot vs Few-shot por Temperatura", fontsize=13, fontweight="bold")

for ax, (coluna, ylabel, titulo) in zip(axes, metricas):
    for i, (temp, tecnica) in enumerate(combinacoes):
        offset = (i - 1.5) * largura
        subset = df[(df["Temperatura"] == temp) & (df["Técnica"] == tecnica)]
        if subset.empty:
            continue
        valores = [subset[subset["Algoritmo"] == a][coluna].values[0]
                   if not subset[subset["Algoritmo"] == a].empty else 0
                   for a in algoritmos]
        barras = ax.bar([xi + offset for xi in x], valores, largura,
                        label=rotulos[(temp, tecnica)],
                        color=cores[(temp, tecnica)],
                        edgecolor="black", linewidth=0.5)
        for barra, valor in zip(barras, valores):
            if valor == 0:
                continue
            fmt = f"{valor:.2e}" if coluna != "Duração (s)" else f"{valor:.1f}s"
            ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() * 1.02,
                    fmt, ha="center", va="bottom", fontsize=6, rotation=45)

    ax.set_title(titulo, fontsize=11, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_xlabel("Algoritmo", fontsize=9)
    ax.set_xticks(list(x))
    ax.set_xticklabels(algoritmos)
    ax.yaxis.set_major_formatter(
        ticker.FormatStrFormatter("%.2e") if coluna != "Duração (s)"
        else ticker.FormatStrFormatter("%.1f")
    )
    ax.legend(fontsize=7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()
saida = os.path.join(RESULTADOS, "comparativo_prompts.png")
plt.savefig(saida, dpi=150, bbox_inches="tight")
print(f"\nGráfico salvo em: {saida}")
plt.show()
