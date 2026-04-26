import os
import time
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "saida", "llama-3.3-70b", "temp_0", "zero_shot"))
RESULTADOS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "resultados", "llama-3.3-70b", "temp_0", "zero_shot", "isolado"))
os.makedirs(SAIDA_DIR, exist_ok=True)
os.makedirs(RESULTADOS_DIR, exist_ok=True)

PROMPT = "Please write your best implementation of BubbleSort in Java programming language."

print("=== BubbleSort | zero_shot | temperatura=0 ===")

tracker = EmissionsTracker(
    project_name="BubbleSort",
    experiment_id="922f11ca-1de2-4e5d-b278-9a888492cbaa",
    output_file=os.path.join(RESULTADOS_DIR, "emissoes_BubbleSort.csv"),
    save_to_api=True,
    log_level="error"
)

inicio = time.time()
tracker.start()
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0,
    max_completion_tokens=4096,
    stream=False,
)
emissoes = tracker.stop()
duracao = time.time() - inicio

with open(os.path.join(SAIDA_DIR, "BubbleSort.txt"), "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)

print(f"  Tokens gerados: {completion.usage.completion_tokens}")
print(f"  Duração:        {duracao:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
