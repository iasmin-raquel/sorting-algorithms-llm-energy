#include <iostream>
#include <string>
#include <cstdlib>

// Define constants for LCG
const int IM = 139968;
const int IA = 3877;
const int IC = 29573;

// Function to generate a random number using the LCG
int randLCG(int seed) {
    return (seed * IA + IC) % IM;
}

// Function to select a character based on probabilities
char choose(char* alphabet, double* prob, int i) {
    double r = static_cast<double>(randLCG(42)) / (IM - 1);
    double psum = 0.0;

    for (int j = 0; j < 14; ++j) {
        if (r >= psum && r <= psum + prob[j]) {
            return alphabet[j];
        }
        psum += prob[j];
    }

    // In case of equality, select the last character
    return alphabet[13];
}

// Function to generate a DNA sequence with specified parameters
std::string fasta(char* sequence, int N) {
    double p[] = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02,
                  0.02, 0.02, 0.02, 0.02, 0.02, 0.02};
    char alphabet[] = "acgtBDMRNKSVW";
    std::string output;
    int seed = 42;

    for (int i = 0; i < N * 60; ++i) {
        if (sequence != nullptr) {
            output.push_back(sequence[i % static_cast<int>(strlen(sequence))]);
        } else {
            output.push_back(choose(alphabet, p, randLCG(seed)));
            seed = randLCG(seed);
        }
    }

    return output;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        exit(1);
    }

    int N = atoi(argv[1]);
    char* repeatFasta = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCG"
                        "GGCGGAACCCCGTCTCTACTAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGC"
                        "TGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGC"
                        "GGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCG"
                        "AGACTCCGTCTCAAAAA";

    std::string repeatFastaSeq = fasta(repeatFasta, N);
    std::string randomIUB = fasta(nullptr, N);
    char* HomoSapiensAlphabet = "acgt";
    double pHS[] = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};
    std::string randomHomoSapiens = fasta(nullptr, N);

    // Append a newline character at the end
    for (int i = 0; i < 60; ++i) {
        repeatFastaSeq.push_back('\n');
        randomIUB.push_back('\n');
        randomHomoSapiens.push_back('\n');
    }

    std::ofstream out("output.txt");
    out << repeatFastaSeq.substr(0, N * 60);
    out << "Random IUB: \n" << randomIUB.substr(0, N * 60);
    out << "Homo sapiens: \n" << randomHomoSapiens.substr(0, N * 60);

    return 0;
}
