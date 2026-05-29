import os
import time
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE    = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "..", "saida", "llama-3.3-70b", "nbody", "temp_0", "zero_shot", "NBody.txt"))
SAIDA_DIR      = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "..", "saida", "qwen3-32b", "nbody", "temp_0"))
RESULTADOS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "..", "resultados", "qwen3-32b", "nbody", "temp_0"))
os.makedirs(SAIDA_DIR, exist_ok=True)
os.makedirs(RESULTADOS_DIR, exist_ok=True)

with open(PROMPT_FILE, encoding="utf-8") as f:
    PROMPT = f.read()

print("=== NBody | qwen3-32b | temperatura=0 ===")

tracker = EmissionsTracker(
    project_name="NBody",
    output_file=os.path.join(RESULTADOS_DIR, "emissoes_NBody.csv"),
    save_to_api=False,
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

with open(os.path.join(SAIDA_DIR, "NBody.txt"), "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)

print(f"  Tokens gerados: {completion.usage.completion_tokens}")
print(f"  Duração:        {duracao:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
