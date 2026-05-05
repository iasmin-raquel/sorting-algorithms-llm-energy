import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
RESULTADOS_DIR = os.path.join(BASE_DIR, "..", "resultados", "professor")

experimentos = {
    "QuickSort":  "f4bd571c-94aa-452f-9622-031068498020",
    "MergeSort":  "9d3111a1-3d2b-428c-8929-8a514bbc93fa",
    "BubbleSort": "e18b5f48-2afe-4198-a282-8997382c600e",
}

dados = []
for nome, exp_id in experimentos.items():
    csv_path = os.path.join(RESULTADOS_DIR, f"emissoes_{nome}.csv")
    df = pd.read_csv(csv_path)
    ultima = df[df["experiment_id"] == exp_id].iloc[-1]
    dados.append({
        "Algoritmo":     nome,
        "CO₂ (kg)":      ultima["emissions"],
        "Energia (kWh)": ultima["energy_consumed"],
        "Duração (s)":   ultima["duration"],
    })

df = pd.DataFrame(dados)
print(df.to_string(index=False))

algoritmos = df["Algoritmo"].tolist()
cores = ["#4CAF50", "#2196F3", "#F44336"]

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
fig.suptitle("Comparativo de Algoritmos de Ordenação\n(50 elementos, 10.000 repetições)", fontsize=13, fontweight="bold")

metricas = [
    ("CO₂ (kg)",      "CO₂ emitido (kg eq CO₂)", "CO₂ Emitido"),
    ("Energia (kWh)", "Energia consumida (kWh)",   "Energia Consumida"),
    ("Duração (s)",   "Tempo de execução (s)",      "Duração"),
]

for ax, (coluna, ylabel, titulo) in zip(axes, metricas):
    valores = df[coluna].tolist()
    barras = ax.bar(algoritmos, valores, color=cores, edgecolor="black", linewidth=0.5)
    ax.set_title(titulo, fontsize=11, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_xlabel("Algoritmo", fontsize=9)
    ax.yaxis.set_major_formatter(
        ticker.FormatStrFormatter("%.2e") if coluna != "Duração (s)"
        else ticker.FormatStrFormatter("%.2f")
    )
    for barra, valor in zip(barras, valores):
        fmt = f"{valor:.2e}" if coluna != "Duração (s)" else f"{valor:.2f}s"
        ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() * 1.02,
                fmt, ha="center", va="bottom", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

plt.tight_layout()
saida = os.path.join(RESULTADOS_DIR, "comparativo_algoritmos.png")
plt.savefig(saida, dpi=150, bbox_inches="tight")
print(f"\nGráfico salvo em: {saida}")
plt.show()
