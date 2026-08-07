# Import necessary modules
import math

# Define constants
IM = 139968
IA = 3877
IC = 29573
SEED = 42

# Define initial state variables
q = 1
r = 0
t = 1
k = 0

# Function to generate the next step in the sequence
def next_step():
    global q, r, t, k
    k += 1
    r = (IM * r + IA) % IC
    t = IC - r
    q *= 10

# Function to extract a digit from the sequence
def extract(x):
    return math.floor((q * x + r) / t)

# Function to produce the next digit in the sequence
def produce(d):
    global q, r, t
    q *= 10
    r = (r - t * d) * 10

# Main loop to generate digits
N = 30
print("\t:N")
for i in range(N):
    next_step()
    print("%010d" % extract(3), end='\t')
    produce(extract(4))
    print("%010d" % extract(3), flush=True)

# Verification for N=30
extract_3 = extract(3)
extract_4 = extract(4)
print("Verification:")
print("extract(3) =", extract_3)
print("extract(4) =", extract_4)
assert extract_3 == extract_4, "Verification failed"
