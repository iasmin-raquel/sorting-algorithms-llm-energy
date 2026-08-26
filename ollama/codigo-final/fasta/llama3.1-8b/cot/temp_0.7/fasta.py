import sys
from random import randrange

IM = 139968
IA = 3877
IC = 29573
Seed = 42

def lcg(seed):
    while True:
        seed = (IA * seed + IC) % IM
        yield seed / float(IM)

def nucleotide(probabilities, alphabet):
    r = next(lcg(Seed))
    cumulative_prob = 0.0
    for n in range(len(alphabet)):
        cumulative_prob += probabilities[n]
        if r < cumulative_prob:
            return alphabet[n]

# Get the number of sequences from command line argument
N = int(sys.argv[1])

alu_sequence = 'GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA' \
              'TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT' \
              'AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG' \
              'GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCA' \
              'CTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA'

iub_probabilities = [0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, \
                     0.02, 0.02, 0.02, 0.02, 0.02]
iub_alphabet = 'acgtB_DHKNMRSVW'

homo_sapiens_probabilities = [0.3029549426680, 0.1979883004921, 0.1975473066391, \
                             0.3015094502008]
homo_sapiens_alphabet = 'actg'

# Print ONE Homo sapiens alu
print('>ONE Homo sapiens alu')
for _ in range(N):
    print(alu_sequence * 2)

# Print TWO IUB ambiguity codes
print('>TWO IUB ambiguity codes')
iub_seq = ''
for _ in range(N * 3):
    iub_seq += nucleotide(iub_probabilities, iub_alphabet)
    if len(iub_seq) == 60:
        print(iub_seq)
        iub_seq = ''

# Print THREE Homo sapiens frequency
print('>THREE Homo sapiens frequency')
homo_sapiens_seq = ''
for _ in range(N * 5):
    homo_sapiens_seq += nucleotide(homo_sapiens_probabilities, homo_sapiens_alphabet)
    if len(homo_sapiens_seq) == 60:
        print(homo_sapiens_seq)
        homo_sapiens_seq = ''

# Validate the output
output_file_name = 'output.txt'
with open(output_file_name, 'w') as f:
    # Print ONE Homo sapiens alu
    for _ in range(N):
        f.write(alu_sequence * 2 + '\n')

    # Print TWO IUB ambiguity codes
    iub_seq = ''
    for _ in range(N * 3):
        iub_seq += nucleotide(iub_probabilities, iub_alphabet)
        if len(iub_seq) == 60:
            f.write(iub_seq + '\n')
            iub_seq = ''

    # Print THREE Homo sapiens frequency
    homo_sapiens_seq = ''
    for _ in range(N * 5):
        homo_sapiens_seq += nucleotide(homo_sapiens_probabilities, homo_sapiens_alphabet)
        if len(homo_sapiens_seq) == 60:
            f.write(homo_sapiens_seq + '\n')
            homo_sapiens_seq = ''

import subprocess
subprocess.run(['diff', 'output.txt', 'reference.txt'])
