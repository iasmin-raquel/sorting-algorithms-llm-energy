import os
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = os.path.join(BASE_DIR, "..", "..", "..", "saida", "llama-3.3-70b", "temp_0.7")
RESULTADOS_DIR = os.path.join(BASE_DIR, "..", "..", "..", "resultados", "llama-3.3-70b", "temp_0.7", "isolado")

PROMPT = "Please write your best implementation of QuickSort in Java programming language."

print("=== QuickSort | temperatura=0.7 ===")

tracker = EmissionsTracker(
    project_name="QuickSort",
    experiment_id="8b81002e-b98a-4254-9258-c586c04ebc0a",
    output_file=os.path.join(RESULTADOS_DIR, "emissoes_QuickSort.csv"),
    save_to_api=True,
    log_level="error"
)

tracker.start()
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0.7,
    max_completion_tokens=4096,
    stream=False,
)
emissoes = tracker.stop()

with open(os.path.join(SAIDA_DIR, "QuickSort.txt"), "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)

print(f"  Tokens gerados: {completion.usage.completion_tokens}")
print(f"  Duração:        {tracker.final_emissions_data.duration:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
