#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

// LCG Constants
const int IM = 139968;
const int IA = 3877;
const int IC = 29573;

// Seed for the random number generator
int seed = 42;

// Function to generate a random number using LCG
int lcg() {
    seed = (seed * IA + IC) % IM;
    return seed;
}

// Function to generate DNA sequence based on probabilities
std::string generateDnaSequence(int length, const std::vector<std::pair<char, double>>& alphabet, int totalProbability) {
    std::string sequence;
    for (int i = 0; i < length; ++i) {
        double randomValue = lcg() / static_cast<double>(IM);
        double cumulativeProbability = 0.0;
        for (const auto& entry : alphabet) {
            cumulativeProbability += entry.second;
            if (randomValue <= cumulativeProbability) {
                sequence += entry.first;
                break;
            }
        }
    }
    return sequence;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::atoi(argv[1]);

    // ALU sequence
    const std::string aluSequence("GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA"
                                   "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT"
                                   "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG"
                                   "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG"
                                   "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA");

    // IUB Alphabet and Probabilities
    std::vector<std::pair<char, double>> iubAlphabet = {
        {'a', 0.27}, {'c', 0.12}, {'g', 0.12}, {'t', 0.27},
        {'B', 0.02}, {'D', 0.02}, {'H', 0.02}, {'K', 0.02},
        {'M', 0.02}, {'N', 0.02}, {'R', 0.02}, {'S', 0.02},
        {'V', 0.02}, {'W', 0.02}, {'Y', 0.02}
    };
    int totalIubProbability = 100; // Total probability in percentage

    // Homo sapiens Alphabet and Probabilities
    std::vector<std::pair<char, double>> homoSapiensAlphabet = {
        {'a', 0.3029549426680}, {'c', 0.1979883004921},
        {'g', 0.1975473066391}, {'t', 0.3015094502008}
    };
    int totalHomoSapiensProbability = 100; // Total probability in percentage

    // Generate DNA sequences
    std::string aluSequenceResult = generateDnaSequence(N, {}, N); // ALU sequence is not based on probabilities
    std::string iubResult = generateDnaSequence(N, iubAlphabet, totalIubProbability);
    std::string homoSapiensResult = generateDnaSequence(N, homoSapiensAlphabet, totalHomoSapiensProbability);

    // Output the results
    std::cout << "alu\n";
    for (int i = 0; i < N / 60 + 1; ++i) {
        std::cout << aluSequence.substr(i * 60, 60) << "\n";
    }

    std::cout << "iub\n";
    for (int i = 0; i < N / 60 + 1; ++i) {
        std::cout << iubResult.substr(i * 60, 60) << "\n";
    }

    std::cout << "homosapiens\n";
    for (int i = 0; i < N / 60 + 1; ++i) {
        std::cout << homoSapiensResult.substr(i * 60, 60) << "\n";
    }

    return 0;
}
