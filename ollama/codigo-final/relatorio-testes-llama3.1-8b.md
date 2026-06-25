# Relatório de testes — código n-body gerado pelo llama3.1:8b

**Pipeline:** prompts aprovados (gerados pelo Qwen3:1.7b, estratégia *Chain-of-Thought*, temperaturas 0 e 0.7) → enviados ao **llama3.1:8b** (via API local do Ollama) → código n-body em C++, Java e Python.

**Como foi testado (na máquina local):**
- **C++:** `g++ -std=c++17 nbody.cpp -o nbody && ./nbody 1000`
- **Java:** renomear para o nome da classe pública, `javac` e `java <Classe> 1000`
- **Python:** `python3 nbody.py 1000`

## Resumo

| Temp | Linguagem | Compilou? | Executou? | Saída correta? |
|:---:|:---|:---:|:---:|:---:|
| 0   | C++    | ❌ Não | — | — |
| 0   | Python | ⚠️ Sintaxe ok | ❌ Não (`KeyError`) | — |
| 0   | Java   | ✅ Sim | ✅ Sim | ❌ Não (inicial = final; valor incorreto) |
| 0.7 | C++    | ❌ Não | — | — |
| 0.7 | Python | ⚠️ Sintaxe ok | ❌ Não (`AttributeError`) | — |
| 0.7 | Java   | ❌ Não | — | — |

**Placar: 1/6 executou; 0/6 produziu resultado correto.**

Observação importante: as condições iniciais (posições, velocidades e massas dos 5 corpos) foram reproduzidas corretamente em todos os 6 códigos. As falhas estão na **coerência do código** (uso de símbolos não declarados) e na **física da simulação** (constante gravitacional, passo de tempo e fórmulas de força/energia), que o prompt não especificava.

---

## C++ — temp 0 — CoT

### Resultado
Não compila.

#### Motivos
- **`std::vector` usado sem `#include <vector>`** (linhas 20, 29, 38, 69) — erro de compilação.
- Física incorreta: o "integrador" faz `planet.vx += 0.5 * dt * (sun.mass / (planet.x - sun.x))` — **não é a força gravitacional** (sem `1/r²`, divisão pela diferença de coordenada, divisão por zero se alinhado).
- `calculateEnergy` calcula **só energia cinética** (falta a potencial).
- `dt = 1e-8` (o benchmark usa `0.01`); `offsetMomentum` com fórmula incorreta.

---

## Python — temp 0 — CoT

### Resultado
Sintaxe válida, mas **aborta em execução**: `KeyError: 'ax'`.

#### Motivos
- `symplectic_integrator` usa `planet['ax']`, `planet['ay']`, `planet['az']`, mas **esses campos nunca são criados** nos dicionários (a aceleração nunca é calculada) → `KeyError`.
- Constantes em unidades SI erradas para o benchmark (`SOLAR_MASS = 1.989e30`, `DAYS_PER_YEAR` em segundos).
- `G` é definido **local em `main`**, mas usado em `calculate_energy` (escopo global) → causaria `NameError` também.
- `dt = 1e3`; saída por iteração, fora do formato esperado.

---

## Java — temp 0 — CoT

### Resultado
**Compila e executa.** Saída obtida:
```
Initial Energy: 0,006068068
Final Energy: 0,006068068
```

#### Motivos (executa, mas o resultado está errado)
- **Energia inicial e final são calculadas as duas *depois* da simulação** (ambas chamadas no fim) → ficam **idênticas**.
- Energia cinética usa a **massa ao quadrado**: `0.5 * Math.pow(getMass(), 2) * v²`.
- Energia potencial usa `SOLAR_MASS` no lugar do **produto das massas** e considera só pares Sol–planeta.
- `dt = DAYS_PER_YEAR` (devia ser `0.01`); a energia **exclui o Sol**.
- Saída com **vírgula decimal** (locale pt-BR) → não validável por `ndiff`, que espera ponto.

---

## C++ — temp 0.7 — CoT

### Resultado
Não compila.

#### Motivos
- A `struct Body` **não tem os membros `ax/ay/az`**, mas o integrador usa `body.ax`, `body.ay`, `body.az` (linhas 33-35, 51-58, 63-65).
- **`G` não declarado** no escopo de `calculateEnergy` (linha 84) — só existe como variável local dentro do integrador.
- Física incoerente: acelerações nunca inicializadas/zeradas entre passos.

---

## Python — temp 0.7 — CoT

### Resultado
Sintaxe válida, mas **aborta em execução**: `AttributeError: 'Planet' object has no attribute 'y'`.

#### Motivos
- A classe `Planet` guarda a posição em `self.x` (vetor `[x, y, z]`) — **não existem `self.y` nem `self.z`**, mas `update_velocities` acessa `planets[j].y` (linha 82) → `AttributeError`.
- `update_positions` usa `planet_i_velocity`, que **não existe nesse escopo** (linha 102) → `NameError` também.
- Constantes em unidades SI erradas; fórmula de energia potencial incorreta (usa distância² em vez de `1/r`, sem o produto das massas).

---

## Java — temp 0.7 — CoT

### Resultado
Não compila.

#### Motivos
- O código chama **`planet.getMass()`** em vários pontos (linhas 56, 58, 86, 93, 105, 116, 121, 128, 131, 137), mas a classe `Planet` **não define o método `getMass()`** (só `getPosition`, `getVelocity`, `setPosition`, `setVelocity`).
- Física incorreta: a aceleração usa a posição absoluta em relação à origem (não as interações par a par); `dt = 1e-4 * DAYS_PER_YEAR`.

---

## Conclusão

Apesar de os prompts gerados pelo Qwen3:1.7b serem **bem estruturados** e trazerem as condições iniciais corretas, o código produzido pelo llama3.1:8b é **majoritariamente não-executável** (apenas 1 dos 6 rodou, e ainda assim com saída incorreta).

As falhas têm duas naturezas:

1. **Coerência interna do código** — o modelo referencia símbolos que ele mesmo não declarou: cabeçalhos ausentes (`<vector>`), campos inexistentes (`ax/ay/az`, `.y`), métodos inexistentes (`getMass()`) e constantes não declaradas (`G`).
2. **Física da simulação** — a constante gravitacional, o passo de tempo (`dt`) e as fórmulas de força/energia não estavam especificados no prompt, e o modelo os preencheu de forma inconsistente (unidades SI vs. unidades naturais, `dt` arbitrário, energia incompleta).

Isso evidencia que a **completude do prompt** — não apenas nomear os corpos e listar valores, mas fixar a física (`G = 1`, `dt = 0.01`, fórmulas de aceleração e energia) — é determinante para a qualidade do código gerado a jusante.
