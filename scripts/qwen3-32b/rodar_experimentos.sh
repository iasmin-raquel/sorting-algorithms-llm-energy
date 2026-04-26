#!/bin/bash

REPETICOES=1

for i in $(seq 1 $REPETICOES); do
  echo "=== Rodada $i/$REPETICOES ==="
  python3 temp_0/quicksort.py
  python3 temp_0/mergesort.py
  python3 temp_0/bubblesort.py
  python3 temp_0.7/quicksort.py
  python3 temp_0.7/mergesort.py
  python3 temp_0.7/bubblesort.py
done

echo "=== Concluido ==="
