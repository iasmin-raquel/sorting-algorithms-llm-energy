import sys

# LCG parameters
IM = 139968
IA = 3877
IC = 29573
Seed = 42
Max = 1.0

# ALU sequence
ALU = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" \
      "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT" \
      "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG" \
      "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG" \
      "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"

# IUB alphabet probabilities
IUB_probs = [0.27, 0.12, 0.12, 0.27] + [0.02] * 8

# Homo sapiens alphabet probabilities
Homo_probs = [0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008]

def generate_random_number(seed):
    """Linear Congruential Generator"""
    Seed = (IA * Seed + IC) % IM
    return Seed / IM

def select_nucleotide(cumulative_probs, random_num):
    """Weighted selection based on cumulative probabilities"""
    for i, prob in enumerate(cumulative_probs):
        if random_num < prob:
            return i

def generate_sequence(alphabet, n_chars):
    """Generate a sequence of nucleotides"""
    sequence = ""
    for _ in range(n_chars):
        random_num = generate_random_number(Seed)
        index = select_nucleotide(alphabet, random_num)
        sequence += alphabet[index]
    return sequence

def main():
    # Parse command-line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Invalid command-line argument. Please provide a valid integer for N.")
        sys.exit(1)

    # Generate sequences
    alu_sequence = ALU * (N // 2)
    iub_sequence = generate_sequence(IUB_probs, N * 3)
    homo_sequence = generate_sequence(Homo_probs, N * 5)

    # Write sequences to file
    with open("output.txt", "w") as f:
        f.write(">ONE Homo sapiens alu\n")
        f.write(alu_sequence + "\n")
        f.write(">TWO IUB ambiguity codes\n")
        f.write(iub_sequence + "\n")
        f.write(">THREE Homo sapiens frequency\n")
        f.write(homo_sequence + "\n")

if __name__ == "__main__":
    main()
