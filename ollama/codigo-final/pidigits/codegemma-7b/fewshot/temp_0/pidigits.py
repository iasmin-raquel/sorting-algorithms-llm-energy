import sys

def extract(x):
    return (q*x + r) // t

def produce(d):
    global q, r
    q *= 10
    r = (r - t*d)*10

def next_step():
    global k, q, r, t
    k += 1
    r = r + 2 * q
    r *= (2*k + 1)
    t *= (2*k + 1)
    q *= k

def pidigits(N):
    digits_output = []
    while True:
        next_step()
        d = extract(3)
        if d == extract(4):
            digits_output.append(str(d))
            produce(d)
        else:
            continue
        if len(digits_output) == N:
            break

    formatted = []
    for i in range(N // 10):
        chunk = digits_output[i*10:(i+1)*10]
        line = "".join(chunk).ljust(10) + "\t:N"
        formatted.append(line)

    if N % 10 > 0:
        chunk = digits_output[(N // 10)*10:]
        line = "".join(chunk).ljust(10) + "\t:N"
        formatted.append(line)

    return "\n".join(formatted)

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    print(pidigits(N))
