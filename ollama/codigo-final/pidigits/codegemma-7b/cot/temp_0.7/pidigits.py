import sys

def next_step(q, r, t):
    k = k + 1
    r = q * 4 + 2 * r
    t = 2 * t * k + 1
    q = r // t
    return q, r, t

def extract(x):
    return (q * x + r) // t

def produce(d):
    global N
    if d == extract(3):
        print(d, end=" ")
        N += 1
        if N % 10 == 0:
            print(f"\t:{N}")
    elif d == extract(4):
        while True:
            d = extract(3)
            if d == extract(4):
                print(d, end=" ")
                N += 1
                if N % 10 == 0:
                    print(f"\t:{N}")
                break

# Input validation
try:
    N = int(sys.argv[1])
except ValueError:
    print("Error: Invalid input. Please provide a positive integer.")
    sys.exit(1)

if N <= 0:
    print("Error: Invalid input. Please provide a positive integer.")
    sys.exit(1)

# Initialization
q, r, t = 1, 0, 1
k = 0

# Algorithm loop
while q > r:
    q, r, t = next_step(q, r, t)
    produce(extract(3))
    produce(extract(4))

# Output formatting
print()  # Remove trailing newline if necessary
