import sys

# Define the linear congruential generator (LCG) function
def lcg(seed, im, ia, ic):
    while True:
        seed = (ia * seed + ic) % im
        yield seed / im  # Return a floating-point value between 0 and 1

# Parse command-line argument N
N = int(sys.argv[1])

# Define the ALU sequence
ALU_sequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT AAAAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGG AGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG CACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"

# Define the IUB alphabet with probabilities
IUB_alphabet = {
    'a': 0.27,
    'c': 0.12,
    'g': 0.12,
    't': 0.27,
    'B': 0.02,
    'D': 0.02,
    'H': 0.02,
    'K': 0.02,
    'M': 0.02,
    'N': 0.02,
    'R': 0.02,
    'S': 0.02,
    'V': 0.02,
    'W': 0.02
}

# Define the Homo sapiens alphabet with probabilities
Homo_sapiens_alphabet = {
    'a': 0.3029549426680,
    'c': 0.1979883004921,
    'g': 0.1975473066391,
    't': 0.3015094502008
}

# LCG parameters
IM = 139968
IA = 3877
IC = 29573
Seed = 42

# Initialize the LCG with Seed as initial seed
lcg_instance = lcg(Seed, IM, IA, IC)

# Generate three DNA sequences based on given alphabets and probabilities
for i in range(N):
    # Sequence ONE: ALU
    alu_sequence = ""
    for j in range(i * 2):
        r = next(lcg_instance)  # Get a random number between 0 and 1
        if r < IUB_alphabet['a']:
            alu_sequence += 'A'
        elif r < (IUB_alphabet['a'] + IUB_alphabet['c']):
            alu_sequence += 'C'
        elif r < (IUB_alphabet['a'] + IUB_alphabet['c'] + IUB_alphabet['g']):
            alu_sequence += 'G'
        else:
            alu_sequence += 'T'

    # Sequence TWO: IUB
    iub_sequence = ""
    for j in range(i * 3):
        r = next(lcg_instance)  # Get a random number between 0 and 1
        if r < Homo_sapiens_alphabet['a']:
            iub_sequence += 'A'
        elif r < (Homo_sapiens_alphabet['a'] + Homo_sapiens_alphabet['c']):
            iub_sequence += 'C'
        elif r < (Homo_sapiens_alphabet['a'] + Homo_sapiens_alphabet['c'] + Homo_sapiens_alphabet['g']):
            iub_sequence += 'G'
        else:
            iub_sequence += 'T'

    # Sequence THREE: Homo sapiens
    homo_sequence = ""
    for j in range(i * 5):
        r = next(lcg_instance)  # Get a random number between 0 and 1
        if r < Homo_sapiens_alphabet['a']:
            homo_sequence += 'A'
        elif r < (Homo_sapiens_alphabet['a'] + Homo_sapiens_alphabet['c']):
            homo_sequence += 'C'
        elif r < (Homo_sapiens_alphabet['a'] + Homo_sapiens_alphabet['c'] + Homo_sapiens_alphabet['g']):
            homo_sequence += 'G'
        else:
            homo_sequence += 'T'

    # Print the sequences in order
    print("ONE Homo sapiens alu")
    for k in range(0, len(ALU_sequence), 60):
        print(ALU_sequence[k:k + 60])
    print()
    print("TWO IUB ambiguity codes")
    for k in range(0, len(iub_sequence), 60):
        print(iub_sequence[k:k + 60])
    print()
    print("THREE Homo sapiens frequency")
    for k in range(0, len(homo_sequence), 60):
        print(homo_sequence[k:k + 60])
    print()
