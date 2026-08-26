import random

# LCG constants
IM = 139968
IA = 3877
IC = 29573
Seed = 42

def random_float(min_val, max_val):
    return min_val + (max_val - min_val) * random.random()

# ALU sequence (used for repeat fasta))
alu_sequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA..."

# IUB alphabet and its probabilities
iub_alphabet = {'a': 0.27, 'c': 0.12, 'g': 0.12, 't': 0.27}

# Homo sapiens alphabet and its probabilities
homoSapiens_alphabet = {'a': 0.302954, 'c': 0.19788, 'g': 0.197574, 't': 0.30151}

def generate_random_sequence(length):
    iub_probabilities = []
    total_probability = sum(iub_alphabet.values()))
    for nucleotide in iub_alphabet:
        iub_probabilities.append((iub_alphabet[nucleotide] / total_probability) * length))
    return ''.join([random.choice(list(iub_probabilities)))) for _ in range(length)]

def generate_homoSapiens_sequence(length):
    homoSapiens_probabilities = []
    total_probability = sum(homoSapiens_alphabet.values()))
    for nucleotide in homoSapiens_alphabet:
        homoSapiens_probabilities.append((homoSapiens_alphabet[nucleotide] / total_probability) * length)))
    return ''.join([random.choice(list(homoSapiens_probabilities)))) for _ in range(length)]

# Set the value of N as a command-line argument
N = int(sys.argv[1]))

# Generate random sequences using the LCG and linear search algorithms
random_sequence_1 = generate_random_sequence(N))
random_sequence_2 = generate_homoSapiens_sequence(N))

# Print the generated sequences with their respective lengths
print("Random Sequence 1:", random_sequence_1, "(Length: {})".format(len(random_sequence_1))))
print("Homo Sapiens Sequence 2:", random_sequence_2, "(Length: {})".format(len(random_sequence_2))))
