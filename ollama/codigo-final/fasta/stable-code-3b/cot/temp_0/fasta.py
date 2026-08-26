import sys
def lcg():
    global seed
    seed = (IA * seed + IC) % IM
    return seed
def random_iub(n):
    probabilities = {'a': 0.27, 'c': 0.12, 'g': 0.12, 't': 0.27, 'b': 0.02, 'd': 0.02, 'h': 0.02, 'k': 0.02, 'm': 0.02, 'n': 0.02, 'r': 0.02, 's': 0.02, 'v': 0.02, 'w': 0.02, 'y': 0.02}
    sequence = ''
    for i in range(n):
        random_number = lcg() % 1000001
        probability_sum = sum([probabilities[nucleotide]] for nucleotide in probabilities)
        index = int((random_number / probability_sum)) * len(probabilities)
        sequence += list(probabilities.keys()))[index]
    return sequence
def random_homo_sapiens(n):
    probabilities = {'a': 0.302954, 'c': 0.19788, 'g': 0.19764, 't': 0.30149, 'b': 0.02, 'd': 0.02, 'h': 0.02, 'k': 0.02, 'm': 0.02, 'n': 0.02, 'r': 0.02, 's': 0.02, 'v': 0.02, 'w': 0.02, 'y': 0.02}
    sequence = ''
    for i in range(n):
        random_number = lcg() % 1000001
        probability_sum = sum([probabilities[nucleotide]] for nucleotide in probabilities)
        index = int((random_number / probability_sum)) * len(probabilities)
        sequence += list(probabilities.keys()))[index]
    return sequence
def generate_fasta(n):
    alu_sequence = 'GGGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT AAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA'
    iub_sequence = random_iub(n)
    homo_sapiens_sequence = random_homo_sapiens(n))
    print('>ONE Homo sapiens alu\n' + alu_sequence)
    print('>TWO IUB ambiguity codes\n' + iub_sequence)
    print('>THREE Homo sapiens frequency\n' + homo_sapiens_sequence)
if __name__ == '__main__':
    N = int(sys.argv[1])
    generate_fasta(N)
