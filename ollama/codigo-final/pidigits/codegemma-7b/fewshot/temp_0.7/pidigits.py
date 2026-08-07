import sys
from math import floor

# State variables
q = 1
r = 0
t = 1
k = 0

# Function to extract a digit
def extract(x):
    return floor((q * x + r) / t)

# Function to advance the state
def next_step(q, r):
    global k
    k += 1
    r = r + 2 * q
    r *= (2 * k + 1)
    t *= (2 * k + 1)
    q *= k

# Function to update state after digit selection
def produce(d):
    q *= 10
    r = (r - t * d) * 10

# Parse N from command line argument
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30

# Calculate and output digits
digits_output = []
for _ in range(N):
    while True:
        next_step(q, r)
        d = extract(3)
        if extract(4) == d:
            produce(d)
            digits_output.append(str(d))
            break

    # Format and print output
    line = "".join(digits_output[-10:] or [""] * 10)
    print(f"{line}\t:{k}:", end="\n" if digits_output else "")
