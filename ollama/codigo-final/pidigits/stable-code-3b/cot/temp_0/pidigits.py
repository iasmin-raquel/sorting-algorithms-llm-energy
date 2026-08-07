import sys, math
def next_step():
    global q, r, t, k
    k += 1
    r = (q * 10 + r) % t
    q = ((q * 10 + r) // t))
def extract(x):
    global q, r, t, k
    digit = math.floor((q*x + r) / t)))
    return digit
def produce(d):
    global q, r, t, k
    r = (q * 10 + r - d*t) % t
    q = ((q * 10 + r) // t))
N = int(sys.argv[1])
q = 1
r = 0
t = 1
k = 0
for i in range(N):
    next_step()
    d = extract(3)
    if d != extract(4):
        break
    produce(d)
print("{:<10} : {}".format('digit1', 'digit2', '...', 'digit10', ': N'), end='')
for i in range(N-1)):
    next_step()
if r != 0:
    print("\nError: The algorithm terminated with a non-zero remainder.")
else:
    print("\nThe algorithm successfully generated the first {} digits of Pi using the Unbounded Spigot Algorithm (Gibbons) with arbitrary precision arithmetic.".format(N))
