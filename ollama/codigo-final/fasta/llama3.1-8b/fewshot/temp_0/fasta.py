import sys
from random import Random

# Define constants
ALU = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" \
      "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"

IUB = "acgtB*DHKMNRSVW"
HOMO_SAPIENS = "acgt"

# Define LCG parameters
IM = 139968
IA = 3877
IC = 29573
Seed = 42

def lcg(seed):
    while True:
        seed = (seed * IA + IC) % IM
        yield seed

def random(max, rng):
    return chr(rng.next() % max)

# Define IUB and Homo sapiens alphabet probabilities
IUB_PROBS = {'a': 0.27, 'c': 0.12, 'g': 0.12, 't': 0.27,
             'B': 0.02, 'D': 0.02, 'H': 0.02, 'K': 0.02,
             'M': 0.02, 'N': 0.02, 'R': 0.02, 'S': 0.02,
             'V': 0.02, 'W': 0.02}

HOMO_SAPIENS_PROBS = {'a': 0.3029549426680, 'c': 0.1979883004921,
                      'g': 0.1975473066391, 't': 0.3015094502008}

def random_fasta(alphabet, probs, rng):
    sequence = ''
    for _ in range(N * 2):
        seed = rng.next()
        char = random(ord(alphabet[seed % len(alphabet)]), rng)
        sequence += char
    return sequence

# Parse command-line argument
N = int(sys.argv[1])

# Create LCG instance
rng = lcg(Seed)

# Generate sequences
repeat_fasta = ALU * (N // 60 + 1)[:60]
random_iub_fasta = random_fasta(IUB, IUB_PROBS, rng)
random_homo_sapiens_fasta = random_fasta(HOMO_SAPIENS, HOMO_SAPIENS_PROBS, rng)

# Print output
print("Repeat Fasta")
for i in range(0, len(repeat_fasta), 60):
    print(repeat_fasta[i:i+60])

print("\nRandom IUB Fasta")
for i in range(0, len(random_iub_fasta), 60):
    print(random_iub_fasta[i:i+60])

print("\nRandom Homo sapiens Fasta")
for i in range(0, len(random_homo_sapiens_fasta), 60):
    print(random_homo_sapiens_fasta[i:i+60])
