#include <iostream>
#include <string>
#include <vector>

// LCG constants
const int IM = 139968;
const int IA = 3877;
const int IC = 29573;
const int Seed = 42;

// Function to generate a random number using LCG
int lcg() {
    static int x = Seed;
    return (x *= (IA * x + IC)) / IM;
}

// Function to select a nucleotide based on probabilities
char selectNucleotide(const std::string& alphabet, const double* probs) {
    int r = lcg();
    for (int i = 0; i < alphabet.size(); ++i) {
        if (r < probs[i] * IM) return alphabet[i];
        r -= probs[i] * IM;
    }
    // If no nucleotide is selected, return a random one
    return 'a' + lcg() % 4;
}

// Function to generate an ALU sequence of length n*2
std::string generateALUSquence(int n) {
    std::string seq = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA";
    for (int i = 0; i < n * 2; ++i) {
        seq += selectNucleotide("ACGT", new double[4]{0.25, 0.25, 0.25, 0.25});
    }
    return seq;
}

// Function to generate an IUB sequence of length n*3
std::string generateIUBSequence(int n) {
    std::string alphabet = "acgtBDRSVMKHN";
    double probs[] = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02};
    std::string seq;
    for (int i = 0; i < n * 3; ++i) {
        seq += selectNucleotide(alphabet, probs);
    }
    return seq;
}

// Function to generate a Homo sapiens sequence of length n*5
std::string generateHomoSapiensSequence(int n) {
    std::string alphabet = "acgt";
    double probs[] = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};
    std::string seq;
    for (int i = 0; i < n * 5; ++i) {
        seq += selectNucleotide(alphabet, probs);
    }
    return seq;
}

// Function to output the sequences in the exact format
void outputSequences(int n) {
    std::cout << "ALU" << std::endl;
    for (int i = 0; i < n * 2 / 60 + 1; ++i) {
        std::string seq = generateALUSquence(n);
        for (int j = 0; j < 60 && j < seq.size(); ++j) {
            std::cout << seq[j];
        }
        if (seq.size() > 60) std::cout << std::endl;
    }

    std::cout << "Random" << std::endl;
    for (int i = 0; i < n * 3 / 60 + 1; ++i) {
        std::string seq = generateIUBSequence(n);
        for (int j = 0; j < 60 && j < seq.size(); ++j) {
            std::cout << seq[j];
        }
        if (seq.size() > 60) std::cout << std::endl;
    }

    std::cout << "Homo sapiens" << std::endl;
    for (int i = 0; i < n * 5 / 60 + 1; ++i) {
        std::string seq = generateHomoSapiensSequence(n);
        for (int j = 0; j < 60 && j < seq.size(); ++j) {
            std::cout << seq[j];
        }
        if (seq.size() > 60) std::cout << std::endl;
    }
}

int main(int argc, char* argv[]) {
    int n = atoi(argv[1]);
    outputSequences(n);
    return 0;
}
