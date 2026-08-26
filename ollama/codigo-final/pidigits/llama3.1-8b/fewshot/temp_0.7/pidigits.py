import math

def next_step(q, r, t, k):
    """Increment k, update r and t, then q"""
    k += 1
    r = (IA * r + IC) % IM
    t = (IC * t) % IM
    q = (q << 1) | ((r >> 15) & 1)
    return q, r, t, k

def extract(x):
    """Floor((q*x + r)/t)"""
    result = math.floor((q * x + r) / t)
    return result

def produce(d):
    """q = q*10, r = (r - t*d) * 10"""
    global q
    global r
    global t
    q *= 10
    r = (r - d * t) * 10

IM = 139968; IA = 3877; IC = 29573; SEED = 42
q = 1
r = 0
t = 1
k = 0
N = 30

for n in range(N):
    q, r, t, k = next_step(q, r, t, k)
    if (n + 1) % 10 == 0:
        print(f"{extract(3):010}{'\t':8}{extract(4):010}")
