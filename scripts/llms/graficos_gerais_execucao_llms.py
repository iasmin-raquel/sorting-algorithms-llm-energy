"""
Gera gráficos comparando o gasto energético de execução dos algoritmos
gerados pelos LLMs (BubbleSort, MergeSort, QuickSort).

Execução: python scripts/graficos_execucao.py
"""

import os
import warnings
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

warnings.filterwarnings("ignore")

BASE_DIR      = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESULTADOS    = os.path.join(BASE_DIR, "resultados")
GRAFICOS_DIR  = os.path.join(RESULTADOS, "graficos_execucao")
os.makedirs(GRAFICOS_DIR, exist_ok=True)

MODELOS    = ["llama-3.3-70b", "qwen3-32b"]
TEMPS      = ["temp_0", "temp_0.7"]
TECNICAS   = ["zero_shot", "few_shot"]
ALGORITMOS = ["BubbleSort", "MergeSort", "QuickSort"]

CORES = {
    "BubbleSort": "#e74c3c",
    "MergeSort":  "#3498db",
    "QuickSort":  "#2ecc71",
}

def ler_emissoes(modelo, temp, tecnica, algoritmo):
    csv = os.path.join(
        RESULTADOS, modelo, temp, tecnica, "execucao",
        f"emissoes_{algoritmo}.csv"
    )
    try:
        df = pd.read_csv(csv)
        col = next(
            (c for c in ["emissions", "emissions_kg", "co2_eq_emissions"] if c in df.columns),
            None,
        )
        if col:
            return float(df[col].iloc[-1]) * 1e6
    except FileNotFoundError:
        pass
    return None


# ── Gráfico 1: por modelo (agrupando temp e técnica) ──────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=False)
fig.suptitle("Emissões de CO₂ – Execução dos Algoritmos Gerados (µg CO₂eq)", fontsize=13)

for ax, modelo in zip(axes, MODELOS):
    labels, data_bs, data_ms, data_qs = [], [], [], []
    for temp in TEMPS:
        for tec in TECNICAS:
            labels.append(f"{temp}\n{tec}")
            data_bs.append(ler_emissoes(modelo, temp, tec, "BubbleSort"))
            data_ms.append(ler_emissoes(modelo, temp, tec, "MergeSort"))
            data_qs.append(ler_emissoes(modelo, temp, tec, "QuickSort"))

    x = np.arange(len(labels))
    w = 0.25
    bars = [
        ax.bar(x - w, data_bs, w, label="BubbleSort", color=CORES["BubbleSort"]),
        ax.bar(x,     data_ms, w, label="MergeSort",  color=CORES["MergeSort"]),
        ax.bar(x + w, data_qs, w, label="QuickSort",  color=CORES["QuickSort"]),
    ]

    ax.set_title(modelo, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("CO₂eq (µg)" if ax == axes[0] else "")
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.3f"))
    ax.legend(fontsize=8)
    ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
caminho = os.path.join(GRAFICOS_DIR, "execucao_por_modelo.png")
plt.savefig(caminho, dpi=150)
plt.close()
print(f"[OK] {os.path.relpath(caminho, BASE_DIR)}")


# ── Gráfico 2: por algoritmo (comparando modelos × técnica) ──────────────────
fig, axes = plt.subplots(1, 3, figsize=(16, 6), sharey=False)
fig.suptitle("Emissões de CO₂ por Algoritmo – Comparativo Modelos (µg CO₂eq)", fontsize=13)

combos = [(m, tec) for m in MODELOS for tec in TECNICAS]
combo_labels = [f"{m.split('-')[0]}\n{tec}" for m, tec in combos]

for ax, algo in zip(axes, ALGORITMOS):
    x = np.arange(len(TEMPS))
    w = 0.18
    offsets = np.linspace(-1.5 * w, 1.5 * w, len(combos))

    for offset, (modelo, tec), label in zip(offsets, combos, combo_labels):
        valores = [ler_emissoes(modelo, t, tec, algo) for t in TEMPS]
        ax.bar(x + offset, valores, w, label=label)

    ax.set_title(algo, fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(TEMPS, fontsize=9)
    ax.set_ylabel("CO₂eq (µg)" if ax == axes[0] else "")
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.3f"))
    ax.legend(fontsize=7, ncol=2)
    ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
caminho = os.path.join(GRAFICOS_DIR, "execucao_por_algoritmo.png")
plt.savefig(caminho, dpi=150)
plt.close()
print(f"[OK] {os.path.relpath(caminho, BASE_DIR)}")


# ── Gráfico 3: resumo geral – média por algoritmo ─────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
fig.suptitle("Média de CO₂eq por Algoritmo – Todos os Cenários (µg)", fontsize=13)

medias, stds, cores_lista = [], [], []
for algo in ALGORITMOS:
    vals = [
        v for m in MODELOS for t in TEMPS for tec in TECNICAS
        if (v := ler_emissoes(m, t, tec, algo)) is not None
    ]
    medias.append(np.mean(vals) if vals else 0)
    stds.append(np.std(vals) if vals else 0)
    cores_lista.append(CORES[algo])

x = np.arange(len(ALGORITMOS))
bars = ax.bar(x, medias, color=cores_lista, yerr=stds, capsize=5)
ax.set_xticks(x)
ax.set_xticklabels(ALGORITMOS)
ax.set_ylabel("CO₂eq médio (µg)")
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.3f"))
ax.grid(axis="y", alpha=0.3)

for bar, v in zip(bars, medias):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(stds) * 0.05,
            f"{v:.3f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
caminho = os.path.join(GRAFICOS_DIR, "execucao_resumo_geral.png")
plt.savefig(caminho, dpi=150)
plt.close()
print(f"[OK] {os.path.relpath(caminho, BASE_DIR)}")

print("\nGráficos salvos em resultados/graficos_execucao/")
