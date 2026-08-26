import random

# Define LCG parameters
IM = 139968
IA = 3877
IC = 29573
Seed = 42

def lcg(seed):
    """Linear Congruential Generator"""
    global IM, IA, IC
    seed = (seed * IA + IC) % IM
    return seed

# Define ALU sequence
alu_sequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" \
               "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"

# Define IUB probabilities
iub_probabilities = {
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

# Define Homo sapiens probabilities
homo_sapiens_probabilities = {
    'a': 0.3029549426680,
    'c': 0.1979883004921,
    'g': 0.1975473066391,
    't': 0.3015094502008
}

def generate_sequence(probabilities, length):
    """Generate a random sequence based on given probabilities"""
    sequence = ''
    for _ in range(length):
        r = lcg(Seed)
        Seed = r
        total_prob = sum(probabilities.values())
        rand_num = (r % 100) / 100
        cumulative_prob = 0
        for base, prob in probabilities.items():
            cumulative_prob += prob / total_prob
            if rand_num < cumulative_prob:
                sequence += base
                break
    return sequence

def generate_fasta(n):
    """Generate three DNA sequences based on specific rules and probabilities"""
    Seed = 42
    alu_sequence = alu_sequence * (n*2)
    iub_sequence = generate_sequence(iub_probabilities, n*3)
    homo_sapiens_sequence = generate_sequence(homo_sapiens_probabilities, n*5)

    with open('output.txt', 'w') as f:
        f.write("ONE Homo sapiens alu\n")
        for i in range(0, len(alu_sequence), 60):
            f.write(alu_sequence[i:i+60] + "\n")
        f.write("\nTWO IUB ambiguity codes\n")
        for i in range(0, len(iub_sequence), 60):
            f.write(iub_sequence[i:i+60] + "\n")
        f.write("\nTHREE Homo sapiens frequency\n")
        for i in range(0, len(homo_sapiens_sequence), 60):
            f.write(homo_sapiens_sequence[i:i+60] + "\n")

generate_fasta(1000)
