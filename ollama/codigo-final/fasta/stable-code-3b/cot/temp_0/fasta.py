import sys
def lcg():
    global seed
    seed = (IA * seed + IC) % IM
    return seed
def random_iub(n):
    probabilities = {'a': 0.27, 'c': 0.12, 'g': 0.12, 't': 0.27, 'b': 0.02, 'd': 0.02, 'h': 0.02, 'k': 0.02, 'm': 0.02, 'n': 0.02, 'r': 0.02, 's': 0.02, 'v': 0.02, 'w': 0.02, 'y': 0.02}
    sequence = ''
    for i in range(n):
        r = random()
        cumulative_probabilities = []
        total_probability = 0
        for nucleotide, probability in probabilities.items():
            if r <= total_probability + probability:
                sequence += nucleotide
                break
            else:
                total_probability += probability
    return sequence
def random_homo_sapiens(n):
    probabilities = {'a': 0.302954, 'c': 0.197888, 'g': 0.197647, 't': 0.301509, 'b': 0.02, 'd': 0.02, 'h': 0.02, 'k': 0.02, 'm': 0.02, 'n': 0.02, 'r': 0.02, 's': 0.02, 'v': 0.02, 'w': 0.02, 'y': 0.02}
    sequence = ''
    for i in range(n):
        r = random()
        cumulative_probabilities = []
        total_probability = 0
        for nucleotide, probability in probabilities.items():
            if r <= total_probability + probability:
                sequence += nucleotide
                break
            else:
                total_probability += probability
    return sequence
def generate_fasta(n):
    alu_sequence = 'GGGCCGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT AAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA'
    iub_sequence = random_iub(n)
    homo_sapiens_sequence = random_homo_sapiens(n))
    print('>ONE Homo sapiens alu\n' + alu_sequence + '\n')
    print('>TWO IUB ambiguity codes\n' + iub_sequence + '\n')
    print('>THREE Homo sapiens frequency\n' + homo_sapiens_sequence + '\n')
if __name__ == '__main__':
    N = int(sys.argv[1])
    generate_fasta(N)
