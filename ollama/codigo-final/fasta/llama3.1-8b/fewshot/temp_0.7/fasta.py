import random

IM = 139968
IA = 3877
IC = 29573
Seed = 42

def lcg(random, seed):
    while True:
        seed = (IA * seed + IC) % IM
        yield seed / float(IM)

def generate_random_fasta(n, alphabet_probabilities, alphabet):
    random.seed(Seed)
    sequence = ''
    
    for _ in range(n*3):  # Generate n*3 characters per line, with a maximum length of 60 characters per line.
        next_number = int(next(lcg(random, Seed)))
        
        # Choose the character based on its probability
        cumulative_probabilities = [sum(alphabet_probabilities[:i+1]) for i in range(len(alphabet))]
        random_number = (next_number / float(IM)) % 1
        
        # Find which bucket the random number falls into
        for i, cum_prob in enumerate(cumulative_probabilities):
            if random_number < cum_prob:
                sequence += alphabet[i]
                break
                
    return sequence

def generate_fasta(n, alu_sequence, iub_alphabet, homo_sapiens_alphabet):
    # Generate the ALU fasta
    alu_random = generate_random_fasta(n*2, [0.25]*4 + [0.005]*8, list(alu_sequence))
    
    # Generate the IUB fasta
    iub_random = generate_random_fasta(n*3, iub_alphabet, 'actgBVDHKMRWS')
    
    # Generate the Homo sapiens fasta
    homo_sapiens_random = generate_random_fasta(n*5, homo_sapiens_alphabet, 'acgt')
    
    output = ''
    
    # Write the ALU fasta to the output string
    output += "ONE Homo sapiens alu\n"
    for i in range(0, len(alu_sequence), 60):
        if i + 60 <= len(alu_sequence):
            output += alu_sequence[i:i+60] + '\n'
        else:
            output += alu_sequence[i:] + '\n'
            
    # Write the IUB fasta to the output string
    output += "TWO IUB ambiguity codes\n"
    for i in range(0, len(iub_random), 60):
        if i + 60 <= len(iub_random):
            output += iub_random[i:i+60] + '\n'
        else:
            output += iub_random[i:] + '\n'
            
    # Write the Homo sapiens fasta to the output string
    output += "THREE Homo sapiens frequency\n"
    for i in range(0, len(homo_sapiens_random), 60):
        if i + 60 <= len(homo_sapiens_random):
            output += homo_sapiens_random[i:i+60] + '\n'
        else:
            output += homo_sapiens_random[i:] + '\n'
            
    return output

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python fasta.py <N>")
        exit(1)
    
    N = int(sys.argv[1])
    
    ALU_sequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT AAAAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGG AGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG CACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"
    IUB_alphabet = {'a': 0.27, 'c': 0.12, 'g': 0.12, 't': 0.27, 'B': 0.02, 'D': 0.02, 'H': 0.02, 'K': 0.02, 'M': 0.02, 'N': 0.02, 'R': 0.02, 'S': 0.02, 'V': 0.02, 'W': 0.02}
    Homo_sapiens_alphabet = {'a': 0.3029549426680, 'c': 0.1979883004921, 'g': 0.1975473066391, 't': 0.3015094502008}

    output = generate_fasta(N, ALU_sequence, IUB_alphabet, Homo_sapiens_alphabet)
    
    with open("output.txt", "w") as f:
        f.write(output)

# The code above generates the FASTA sequences according to the given problem.
