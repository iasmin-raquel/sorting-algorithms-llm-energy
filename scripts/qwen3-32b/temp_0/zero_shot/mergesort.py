import os
import time
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "saida", "qwen3-32b", "temp_0", "zero_shot"))
RESULTADOS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "resultados", "qwen3-32b", "temp_0", "zero_shot", "isolado"))
os.makedirs(SAIDA_DIR, exist_ok=True)
os.makedirs(RESULTADOS_DIR, exist_ok=True)

PROMPT = "Please write your best implementation of MergeSort in Java programming language."

print("=== MergeSort | zero_shot | temperatura=0 ===")

tracker = EmissionsTracker(
    project_name="MergeSort",
    experiment_id="fe3c0fe2-8018-44d2-bb58-f13cb07d6ffa",
    output_file=os.path.join(RESULTADOS_DIR, "emissoes_MergeSort.csv"),
    save_to_api=True,
    log_level="error"
)

inicio = time.time()
tracker.start()
completion = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0,
    max_completion_tokens=4096,
    top_p=0.95,
    reasoning_effort="none",
    stream=False,
)
emissoes = tracker.stop()
duracao = time.time() - inicio

with open(os.path.join(SAIDA_DIR, "MergeSort.txt"), "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)

print(f"  Tokens gerados: {completion.usage.completion_tokens}")
print(f"  Duração:        {duracao:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
