import random

# Define the LCG parameters
IM = 139968
IA = 3877
IC = 29573
Seed = 42

def lcg(seed):
    """Linear Congruential Generator"""
    global IM, IA, IC
    seed = (seed * IA + IC) % IM
    return seed

# Define the ALU sequence
alu_sequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" \
               "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"

# Define the IUB probabilities
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

# Define the Homo sapiens probabilities
homo_sapiens_probabilities = {
    'a': 0.3029549426680,
    'c': 0.1979883004921,
    'g': 0.1975473066391,
    't': 0.3015094502008
}

def generate_sequence(probabilities, length):
    """Generate a random sequence based on the given probabilities"""
    sequence = ''
    for _ in range(length):
        r = lcg(Seed)
        Seed = r
        total = sum(probabilities.values())
        rand_num = (r % 100) / 100
        cumulative_prob = 0
        for base, prob in probabilities.items():
            cumulative_prob += prob / total
            if rand_num <= cumulative_prob:
                sequence += base
                break
    return sequence

def generate_fasta(sequence, name):
    """Generate a FASTA file with the given sequence and name"""
    lines = [f'>{name}\n']
    for i in range(0, len(sequence), 60):
        lines.append(sequence[i:i+60] + '\n')
    return ''.join(lines)

def main():
    N = 1000
    Seed = 42

    # Generate the ALU sequence
    alu_sequence = generate_sequence({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}, N*2)
    alu_fasta = generate_fasta(alu_sequence, "ONE Homo sapiens alu")

    # Generate the IUB sequence
    iub_sequence = generate_sequence(iub_probabilities, N*3)
    iub_fasta = generate_fasta(iub_sequence, "TWO IUB ambiguity codes")

    # Generate the Homo sapiens sequence
    homo_sapiens_sequence = generate_sequence(homo_sapiens_probabilities, N*5)
    homo_sapiens_fasta = generate_fasta(homo_sapiens_sequence, "THREE Homo sapiens frequency")

    with open('output.txt', 'w') as f:
        f.write(alu_fasta + '\n\n')
        f.write(iub_fasta + '\n\n')
        f.write(homo_sapiens_fasta)

if __name__ == "__main__":
    main()
