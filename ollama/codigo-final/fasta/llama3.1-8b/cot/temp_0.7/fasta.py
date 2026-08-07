import sys
import random
from itertools import product

def lcg(seed):
    im = 139968
    ia = 3877
    ic = 29573
    x = seed
    while True:
        x = (ia * x + ic) % im
        yield x / float(im)

def probability(alphabet, probabilities, rand_num):
    cumulative_prob = [0] * len(probabilities)
    for i in range(len(probabilities)):
        cumulative_prob[i] = sum(probabilities[:i+1])
    nucleotides = []
    for prob, cumul in zip(probabilities, cumulative_prob):
        if rand_num < cumul:
            return alphabet[probabilities.index(prob)]
        else:
            rand_num -= cumul
    return None

def dna_sequence(sequence, n, rand):
    total_chars = len(sequence) * n
    sequence_list = [''] * 3
    for i in range(3):
        index = 0
        for _ in range(n):
            next_nucleotide = probability(['a', 'c', 'g', 't'], [0.27, 0.12, 0.12, 0.27], rand.next()) 
            sequence_list[i] += next_nucleotide * (total_chars // 4)
    return '\n'.join(sequence_list)

def main():
    if len(sys.argv) != 2:
        print("Usage: python fasta.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])
    ALU_sequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" \
                  + "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT" \
                  + "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG" \
                  + "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG" \
                  + "CACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA"

    IUB_probabilities = {'a': 0.27, 'c': 0.12, 'g': 0.12, 't': 0.27,
                         'B': 0.02, 'D': 0.02, 'H': 0.02, 'K': 0.02,
                         'M': 0.02, 'N': 0.02, 'R': 0.02, 'S': 0.02,
                         'V': 0.02, 'W': 0.02}

    Homo_sapiens_probabilities = {'a': 0.3029549426680, 'c': 0.1979883004921, 
                                  'g': 0.1975473066391, 't': 0.3015094502008}

    with open('output.txt', 'w') as f:
        rand = lcg(42)
        sequence_list = []
        
        # Generate ALU sequence
        alu_sequence = dna_sequence(ALU_sequence, N, rand)
        sequence_list.append(">" + "ONE Homo sapiens alu")
        while len(alu_sequence) % 60 != 0:
            alu_sequence += 'a'
        sequence_list.append(alu_sequence[:60])
        
        # Generate IUB ambiguity codes
        iub_sequence = dna_sequence('', N, rand)
        for prob, nucleotide in sorted(IUB_probabilities.items()):
            probability = IUB_probabilities[prob] / sum(IUB_probabilities.values())
            while len(iub_sequence) % 3 != 0:
                iub_sequence += nucleotide
            for _ in range(int(probability * N)):
                next_nucleotide = probability(['a', 'c', 'g', 't'], [0.27, 0.12, 0.12, 0.27], rand.next()) 
                iub_sequence += next_nucleotide
        sequence_list.append(">" + "TWO IUB ambiguity codes")
        while len(iub_sequence) % 60 != 0:
            iub_sequence += 'a'
        sequence_list.append(iub_sequence[:60])
        
        # Generate Homo sapiens frequency
        homo_sapiens_sequence = dna_sequence('', N, rand)
        for prob, nucleotide in sorted(Homo_sapiens_probabilities.items()):
            probability = Homo_sapiens_probabilities[prob] / sum(Homo_sapiens_probabilities.values())
            while len(homo_sapiens_sequence) % 5 != 0:
                homo_sapiens_sequence += nucleotide
            for _ in range(int(probability * N)):
                next_nucleotide = probability(['a', 'c', 'g', 't'], [0.27, 0.12, 0.12, 0.27], rand.next()) 
                homo_sapiens_sequence += next_nucleotide
        sequence_list.append(">" + "THREE Homo sapiens frequency")
        while len(homo_sapiens_sequence) % 60 != 0:
            homo_sapiens_sequence += 'a'
        sequence_list.append(homo_sapiens_sequence[:60])

        f.write('\n'.join(sequence_list))
        
if __name__ == "__main__":
    main()
