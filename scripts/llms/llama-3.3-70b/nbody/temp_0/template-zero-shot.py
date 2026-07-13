import os
import time
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "..", "saida", "llama-3.3-70b", "nbody", "temp_0", "zero_shot"))
RESULTADOS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "..", "resultados", "llama-3.3-70b", "nbody", "temp_0", "zero_shot"))
os.makedirs(SAIDA_DIR, exist_ok=True)
os.makedirs(RESULTADOS_DIR, exist_ok=True)

PROMPT = """\
You will generate a prompt for an LLM to implement the n-body problem from the Computer Language Benchmarks Game in Java code.
Problem description:
Simulate the orbits of Jovian planets under mutual gravitation.
The output must be validatable with ndiff -abserr 1.0e-8 with N=1000.
The following physical constants and initial conditions must be used exactly as given:
Constants:
- PI = 3.141592653589793
- SOLAR_MASS = 4 * PI * PI
- DAYS_PER_YEAR = 365.24
Initial conditions (x, y, z, vx, vy, vz, mass):
Sun: x=0, y=0, z=0, vx=0, vy=0, vz=0, mass=SOLAR_MASS
Jupiter:
  x = 4.84143144246472090e+00
  y = -1.16032004402742839e+00
  z = -1.03622044471123109e-01
  vx = 1.66007664274403694e-03 * DAYS_PER_YEAR
  vy = 7.69901118419740425e-03 * DAYS_PER_YEAR
  vz = -6.90460016972063023e-05 * DAYS_PER_YEAR
  mass = 9.54791938424326609e-04 * SOLAR_MASS
Saturn:
  x = 8.34336671824457987e+00
  y = 4.12479856412430479e+00
  z = -4.03523417114321381e-01
  vx = -2.76742510726862411e-03 * DAYS_PER_YEAR
  vy = 4.99852801234917238e-03 * DAYS_PER_YEAR
  vz = 2.30417297573763929e-05 * DAYS_PER_YEAR
  mass = 2.85885980666130812e-04 * SOLAR_MASS
Uranus:
  x = 1.28943695621391310e+01
  y = -1.51111514016986312e+01
  z = -2.23307578892655734e-01
  vx = 2.96460137564761618e-03 * DAYS_PER_YEAR
  vy = 2.37847173959480950e-03 * DAYS_PER_YEAR
  vz = -2.96589568540237556e-05 * DAYS_PER_YEAR
  mass = 4.36624404335156298e-05 * SOLAR_MASS
Neptune:
  x = 1.53796971148509165e+01
  y = -2.59193146099879641e+01
  z = 1.79258772950371181e-01
  vx = 2.68067772490389322e-03 * DAYS_PER_YEAR
  vy = 1.62824170038242295e-03 * DAYS_PER_YEAR
  vz = -9.51592254519715870e-05 * DAYS_PER_YEAR
  mass = 5.15138902046611451e-05 * SOLAR_MASS

The generated prompt must ensure that the produced Java code:
Receives N as a command-line argument
Prints the initial and final energy in %.9f format
Adjusts the Sun's initial velocity so that the total momentum of the system is zero (offsetMomentum)
Uses the symplectic integrator order: update all velocities first, then update all positions
The generated prompt must reproduce all physical constants and initial conditions with their exact numeric values
"""

print("=== NBody | zero_shot | temperatura=0 ===")

tracker = EmissionsTracker(
    project_name="NBody",
    output_file=os.path.join(RESULTADOS_DIR, "emissoes_NBody.csv"),
    save_to_api=False,
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

with open(os.path.join(SAIDA_DIR, "NBody.txt"), "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)

print(f"  Tokens gerados: {completion.usage.completion_tokens}")
print(f"  Duração:        {duracao:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
