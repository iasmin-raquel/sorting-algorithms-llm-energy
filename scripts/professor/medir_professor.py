import subprocess
import os
import pandas as pd
from codecarbon import EmissionsTracker

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
ALGORITMOS_DIR = os.path.join(BASE_DIR, "..", "saida")
RESULTADOS_DIR = os.path.join(BASE_DIR, "..", "resultados", "professor")

print("=== Compilando arquivos Java ===")
for classe in ["QuickSort", "MergeSort", "BubbleSort"]:
    subprocess.run(["javac", f"professor/{classe}.java"], cwd=ALGORITMOS_DIR, check=True)
print("Compilação concluída.\n")

algoritmos = [
    ("QuickSort",  "f4bd571c-94aa-452f-9622-031068498020"),
    ("MergeSort",  "9d3111a1-3d2b-428c-8929-8a514bbc93fa"),
    ("BubbleSort", "e18b5f48-2afe-4198-a282-8997382c600e"),
]

for nome, experiment_id in algoritmos:
    print(f"=== Medindo {nome} ===")

    tracker = EmissionsTracker(
        project_name=nome,
        experiment_id=experiment_id,
        output_file=os.path.join(RESULTADOS_DIR, f"emissoes_{nome}.csv"),
        save_to_api=True,
        log_level="error"
    )

    tracker.start()
    resultado = subprocess.run(
        ["java", f"professor.{nome}"],
        cwd=ALGORITMOS_DIR,
        capture_output=True,
        text=True
    )
    emissoes = tracker.stop()

    print(resultado.stdout.strip())
    print(f"CO₂ emitido: {emissoes:.6f} kg\n")

print("=== Resumo Comparativo ===")
resumo = []
for nome, _ in algoritmos:
    csv_path = os.path.join(RESULTADOS_DIR, f"emissoes_{nome}.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        ultima = df.iloc[-1]
        resumo.append({
            "Algoritmo":      nome,
            "CO₂ (kg)":       ultima.get("emissions", "N/A"),
            "Energia (kWh)":  ultima.get("energy_consumed", "N/A"),
            "Duração (s)":    ultima.get("duration", "N/A"),
        })

df_resumo = pd.DataFrame(resumo)
print(df_resumo.to_string(index=False))
