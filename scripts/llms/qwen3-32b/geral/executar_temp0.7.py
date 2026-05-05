import os
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = os.path.join(BASE_DIR, "..", "..", "saida", "Qwen3-32B", "temp_0.7")
RESULTADOS_DIR = os.path.join(BASE_DIR, "..", "..", "resultados", "qwen3-32b", "temp_0.7", "geral")

PROMPT = "Please write your best implementation of {algoritmo} in Java programming language."

algoritmos = [
    ("QuickSort",  "8b81002e-b98a-4254-9258-c586c04ebc0a"),
    ("MergeSort",  "fe3c0fe2-8018-44d2-bb58-f13cb07d6ffa"),
    ("BubbleSort", "922f11ca-1de2-4e5d-b278-9a888492cbaa"),
]

for nome, experiment_id in algoritmos:
    print(f"=== {nome} | temperatura=0.7 ===")

    tracker = EmissionsTracker(
        project_name=nome,
        experiment_id=experiment_id,
        output_file=os.path.join(RESULTADOS_DIR, f"emissoes_{nome}.csv"),
        save_to_api=True,
        log_level="error"
    )

    tracker.start()
    completion = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[{"role": "user", "content": PROMPT.format(algoritmo=nome)}],
        temperature=0.7,
        max_completion_tokens=4096,
        top_p=0.95,
        reasoning_effort="default",
        stream=False,
    )
    emissoes = tracker.stop()

    resposta = completion.choices[0].message.content
    with open(os.path.join(SAIDA_DIR, f"{nome}.txt"), "w", encoding="utf-8") as f:
        f.write(resposta)

    print(f"  Tokens gerados: {completion.usage.completion_tokens}")
    print(f"  CO₂ emitido: {emissoes:.6f} kg\n")
