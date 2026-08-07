import sys

# Command-line argument for number of digits
N = int(sys.argv[1])

# Algorithm initialization
q = 1
r = 0
t = 1
k = 0

# Output variables
digits = []
count = 0

def next_step():
    global q, r, t, k
    k += 1
    r = r + 2 * q
    r = r * (2*k + 1)
    t = t * (2*k + 1)
    q = q * k

def extract(x):
    return (q*x + r) // t

def produce(d):
    global q, r
    q = q * 10
    r = (r - t*d) * 10

while count < N:
    next_step()
    d = extract(3)
    if d == extract(4):
        digits.append(d)
        produce(d)
        count += 1

# Print digits in groups of 10
for i in range(0, len(digits), 10):
    print(''.join(map(str, digits[i:i+10])), end='\t:')
    print(i+10)
