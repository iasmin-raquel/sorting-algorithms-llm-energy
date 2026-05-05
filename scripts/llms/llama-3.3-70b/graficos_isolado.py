import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DIR_T0    = os.path.join(BASE_DIR, "..", "..", "resultados", "llama-3.3-70b", "temp_0",   "isolado")
DIR_T07   = os.path.join(BASE_DIR, "..", "..", "resultados", "llama-3.3-70b", "temp_0.7", "isolado")

algoritmos = ["QuickSort", "MergeSort", "BubbleSort"]

def carregar(pasta, nome):
    caminho = os.path.join(pasta, f"emissoes_{nome}.csv")
    df = pd.read_csv(caminho)
    return df.iloc[-1]

dados = []
for nome in algoritmos:
    r0  = carregar(DIR_T0,  nome)
    r07 = carregar(DIR_T07, nome)
    dados.append({"Algoritmo": nome, "Temperatura": "0",   "CO₂ (kg)": r0["emissions"],  "Energia (kWh)": r0["energy_consumed"],  "Duração (s)": r0["duration"]})
    dados.append({"Algoritmo": nome, "Temperatura": "0.7", "CO₂ (kg)": r07["emissions"], "Energia (kWh)": r07["energy_consumed"], "Duração (s)": r07["duration"]})

df = pd.DataFrame(dados)
print(df.to_string(index=False))

metricas = [
    ("CO₂ (kg)",      "CO₂ emitido (kg eq CO₂)", "CO₂ Emitido"),
    ("Energia (kWh)", "Energia consumida (kWh)",   "Energia Consumida"),
    ("Duração (s)",   "Tempo de execução (s)",      "Duração"),
]

cores = {"0": "#2196F3", "0.7": "#F44336"}
x = range(len(algoritmos))
largura = 0.35

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Llama-3.3-70B — Comparativo por Algoritmo e Temperatura\n(modo isolado)", fontsize=13, fontweight="bold")

for ax, (coluna, ylabel, titulo) in zip(axes, metricas):
    for temp, offset in [("0", -largura/2), ("0.7", largura/2)]:
        valores = [df[(df["Algoritmo"] == a) & (df["Temperatura"] == temp)][coluna].values[0] for a in algoritmos]
        barras = ax.bar([xi + offset for xi in x], valores, largura, label=f"temp={temp}", color=cores[temp], edgecolor="black", linewidth=0.5)
        for barra, valor in zip(barras, valores):
            fmt = f"{valor:.2e}" if coluna != "Duração (s)" else f"{valor:.1f}s"
            ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() * 1.02,
                    fmt, ha="center", va="bottom", fontsize=7)

    ax.set_title(titulo, fontsize=11, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_xlabel("Algoritmo", fontsize=9)
    ax.set_xticks(list(x))
    ax.set_xticklabels(algoritmos)
    ax.yaxis.set_major_formatter(
        ticker.FormatStrFormatter("%.2e") if coluna != "Duração (s)"
        else ticker.FormatStrFormatter("%.1f")
    )
    ax.legend(fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()
saida = os.path.join(BASE_DIR, "..", "..", "resultados", "llama-3.3-70b", "comparativo_isolado.png")
plt.savefig(saida, dpi=150, bbox_inches="tight")
print(f"\nGráfico salvo em: {os.path.abspath(saida)}")
plt.show()