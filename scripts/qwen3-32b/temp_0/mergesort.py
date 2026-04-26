import os
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = os.path.join(BASE_DIR, "..", "..", "..", "saida", "Qwen3-32B", "temp_0")
RESULTADOS_DIR = os.path.join(BASE_DIR, "..", "..", "..", "resultados", "qwen3-32b", "temp_0", "isolado")

PROMPT = "Please write your best implementation of MergeSort in Java programming language."

print("=== MergeSort | temperatura=0 ===")

tracker = EmissionsTracker(
    project_name="MergeSort",
    experiment_id="fe3c0fe2-8018-44d2-bb58-f13cb07d6ffa",
    output_file=os.path.join(RESULTADOS_DIR, "emissoes_MergeSort.csv"),
    save_to_api=True,
    log_level="error"
)

tracker.start()
completion = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0,
    max_completion_tokens=4096,
    top_p=0.95,
    reasoning_effort="default",
    stream=False,
)
emissoes = tracker.stop()

with open(os.path.join(SAIDA_DIR, "MergeSort.txt"), "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)

print(f"  Tokens gerados: {completion.usage.completion_tokens}")
print(f"  Duração:        {tracker.final_emissions_data.duration:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
