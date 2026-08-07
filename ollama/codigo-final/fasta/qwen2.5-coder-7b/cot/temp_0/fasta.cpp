#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>

// Constants for LCG
const unsigned long IM = 139968;
const unsigned long IA = 3877;
const unsigned long IC = 29573;
unsigned long Seed = 42;

// Function to generate random number using LCG
unsigned long lcg() {
    Seed = (IA * Seed + IC) % IM;
    return Seed;
}

// Function to convert probability to cumulative probability
double probToCumulative(double prob, double prevCumulative) {
    return prevCumulative + prob;
}

// Function to generate random nucleotide based on IUB probabilities
char iubRandomNucleotide() {
    static const char* iubAlphabet = "ACGTBDHKMNRVWY";
    static const double iubProbabilities[] = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02};
    static const double iubCumulativeProbabilities[] = {0.27, 0.39, 0.51, 0.78, 0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94};
    double random = static_cast<double>(lcg()) / IM;
    for (int i = 0; i < 12; ++i) {
        if (random <= iubCumulativeProbabilities[i]) {
            return iubAlphabet[i];
        }
    }
    return 'N'; // Fallback, should not happen
}

// Function to generate random nucleotide based on Homo sapiens probabilities
char homoSapiensRandomNucleotide() {
    static const char* hsAlphabet = "ACGT";
    static const double hsProbabilities[] = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};
    static const double hsCumulativeProbabilities[] = {0.3029549426680, 0.5009432431601, 0.7004905497992, 1.0};
    double random = static_cast<double>(lcg()) / IM;
    for (int i = 0; i < 4; ++i) {
        if (random <= hsCumulativeProbabilities[i]) {
            return hsAlphabet[i];
        }
    }
    return 'N'; // Fallback, should not happen
}

// Function to generate and print a sequence
void generateAndPrintSequence(const std::string& header, int length, char (*generator)()) {
    std::cout << header << "\n";
    for (int i = 0; i < length; ++i) {
        if (i % 60 == 0 && i != 0) {
            std::cout << "\n";
        }
        std::cout << generator();
    }
    std::cout << "\n\n";
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>\n";
        return 1;
    }

    int N = std::atoi(argv[1]);
    const std::string aluSequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA\nTCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

    generateAndPrintSequence(">ONE Homo sapiens alu", N * 2, [&aluSequence]() {
        return aluSequence[lcg() % aluSequence.length()];
    });

    generateAndPrintSequence(">TWO IUB ambiguity codes", N * 3, iubRandomNucleotide);

    generateAndPrintSequence(">THREE Homo sapiens frequency", N * 5, homoSapiensRandomNucleotide);

    return 0;
}
