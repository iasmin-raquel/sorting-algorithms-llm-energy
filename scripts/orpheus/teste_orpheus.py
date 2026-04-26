import os
from pathlib import Path
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = Path(BASE_DIR) / ".." / ".." / "saida" / "orpheus"
RESULTADOS_DIR = Path(BASE_DIR) / ".." / ".." / "resultados" / "orpheus"

SAIDA_DIR.mkdir(parents=True, exist_ok=True)
RESULTADOS_DIR.mkdir(parents=True, exist_ok=True)

TEXTO = "Please write your best implementation of QuickSort in Java programming language."

print("=== Orpheus TTS | teste ===")

tracker = EmissionsTracker(
    project_name="Orpheus",
    experiment_id="8b81002e-b98a-4254-9258-c586c04ebc0a",
    output_file=str(RESULTADOS_DIR / "emissoes_orpheus.csv"),
    save_to_api=True,
    log_level="error"
)

tracker.start()
response = client.audio.speech.create(
    model="canopylabs/orpheus-v1-english",
    voice="autumn",
    response_format="wav",
    input=TEXTO,
)
emissoes = tracker.stop()

audio_path = SAIDA_DIR / "saida.wav"
response.write_to_file(audio_path)

print(f"  Áudio salvo em: {audio_path}")
print(f"  Duração:        {tracker.final_emissions_data.duration:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
