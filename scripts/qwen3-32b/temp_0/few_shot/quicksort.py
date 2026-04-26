import os
import time
from groq import Groq
from codecarbon import EmissionsTracker

client = Groq()

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
SAIDA_DIR      = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "saida", "qwen3-32b", "temp_0", "few_shot"))
RESULTADOS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "..", "resultados", "qwen3-32b", "temp_0", "few_shot", "isolado"))
os.makedirs(SAIDA_DIR, exist_ok=True)
os.makedirs(RESULTADOS_DIR, exist_ok=True)

PROMPT = """\
Here is an example of a sorting algorithm implementation in Java:

Algorithm: InsertionSort

```java
public class InsertionSort {
    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        sort(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
```

Now, following the same style and structure, please write your best implementation of QuickSort in Java programming language."""

print("=== QuickSort | few_shot | temperatura=0 ===")

tracker = EmissionsTracker(
    project_name="QuickSort",
    experiment_id="8b81002e-b98a-4254-9258-c586c04ebc0a",
    output_file=os.path.join(RESULTADOS_DIR, "emissoes_QuickSort.csv"),
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

with open(os.path.join(SAIDA_DIR, "QuickSort.txt"), "w", encoding="utf-8") as f:
    f.write(completion.choices[0].message.content)

print(f"  Tokens gerados: {completion.usage.completion_tokens}")
print(f"  Duração:        {duracao:.2f}s")
print(f"  CO₂ emitido:    {emissoes:.6f} kg")
