import sys

# LCG parameters
IM = 139968
IA = 3877
IC = 29573
Seed = 42
Max = 1.0

# IUB alphabet probabilities
iub_probs = [0.27, 0.12, 0.12, 0.27] + [0.02] * 6

# Homo sapiens alphabet probabilities
homo_probs = [0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008]

# ALU sequence
alu = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" \
      "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT" \
      "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG" \
      "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG" \
      "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"

def generate_random_number(seed):
    """Linear Congruential Generator"""
    Seed = (IA * Seed + IC) % IM
    return Seed / IM

def select_nucleotide(cumulative_probs, random_num):
    """Weighted selection based on cumulative probabilities"""
    for i, p in enumerate(cumulative_probs):
        if random_num < p:
            return i

def generate_sequence(alphabet, n_chars):
    """Generate a sequence of nucleotides"""
    sequence = ""
    for _ in range(n_chars):
        random_num = generate_random_number(Seed)
        nucleotide = alphabet[select_nucleotide(cumulative_probs, random_num)]
        sequence += nucleotide
        Seed = (IA * Seed + IC) % IM
    return sequence

def write_sequence(filename, sequence):
    """Write a sequence to a file in the specified format"""
    with open(filename, "a") as f:
        for i in range(0, len(sequence), 60):
            f.write(sequence[i:i+60] + "\n")

# Parse command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("Invalid command-line argument. Please provide a valid integer for N.")
    sys.exit(1)

# Generate sequences
alu_sequence = alu * 2
iub_sequence = generate_sequence(list("ACGTBDSVWY"), N * 3)
homo_sequence = generate_sequence(list("ACGT"), N * 5)

# Write sequences to file
write_sequence("output.txt", ">ONE Homo sapiens alu\n" + alu_sequence)
write_sequence("output.txt", ">TWO IUB ambiguity codes\n" + iub_sequence)
write_sequence("output.txt", ">THREE Homo sapiens frequency\n" + homo_sequence)

# Validation step
# Compare output.txt with reference.txt using diff
