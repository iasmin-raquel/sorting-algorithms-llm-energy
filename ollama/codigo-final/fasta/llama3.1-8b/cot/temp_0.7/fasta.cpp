#include <iostream>
#include <string>
#include <random>

// Function to generate random number using LCG
int lcgNaive(int seed, int IM, int IA, int IC) {
    return (seed * IA + IC) % IM;
}

// Function to calculate cumulative probability for each nucleotide
std::string calculateCumulativeProbability(double probability) {
    std::string result;
    double cumProb = 0.0;

    // Add A with probability
    result += "A";
    cumProb += probability;

    if (cumProb < 1.0) {
        // Add C with remaining probability
        result += "C";
        cumProb += probability;

        if (cumProb < 1.0) {
            // Add G with remaining probability
            result += "G";
            cumProb += probability;
        }

        if (cumProb < 1.0) {
            // Add T with remaining probability
            result += "T";
            cumProb = 1.0; // Ensure cumulative probability is 1.0
        }
    }

    return result;
}

// Function to generate sequence using LCG and cumulative probabilities
std::string generateSequence(int length, int seed, int IM, int IA, int IC, double a, double c, double g, double t) {
    std::string sequence;

    // Use LCG to generate random numbers for each nucleotide
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> dis(0.0, 1.0);

    for (int i = 0; i < length; ++i) {
        double num = lcgNaive(seed, IM, IA, IC);
        seed = num;

        // Calculate cumulative probability
        double cumProbA = a;
        double cumProbC = c + a;
        double cumProbG = g + c + a;
        double cumProbT = 1.0 - (g + c + a);

        // Choose nucleotide based on cumulative probability
        if (dis(gen) < cumProbA) {
            sequence += "A";
        } else if (dis(gen) < cumProbC) {
            sequence += "C";
        } else if (dis(gen) < cumProbG) {
            sequence += "G";
        } else {
            sequence += "T";
        }
    }

    return sequence;
}

// Function to generate Fasta problem with three types of sequences
void generateFastaProblem(int N) {
    std::string aluSequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG CACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

    // Use LCG with exact parameters
    int seed = 42;
    int IM = 139968;
    int IA = 3877;
    int IC = 29573;

    // Calculate probabilities for IUB and Homo sapiens alphabets
    double aIUB = 0.27;
    double cIUB = 0.12;
    double gIUB = 0.12;
    double tIUB = 0.27;
    double B = 0.02;
    double D = 0.02;
    double H = 0.02;
    double K = 0.02;
    double M = 0.02;
    double N = 0.02;
    double R = 0.02;
    double S = 0.02;
    double V = 0.02;
    double W = 0.02;

    double aHS = 0.3029549426680;
    double cHS = 0.1979883004921;
    double gHS = 0.1975473066391;
    double tHS = 0.3015094502008;

    // Generate sequences of length 2*N, 3*N, and 5*N
    std::string sequence2N = generateSequence(2 * N, seed, IM, IA, IC, aIUB, cIUB, gIUB, tIUB);
    std::string sequence3N = generateSequence(3 * N, seed, IM, IA, IC, aHS, cHS, gHS, tHS);
    std::string sequence5N = aluSequence;

    // Print Fasta problem with specified headers and lengths
    std::cout << ">Sequence_2N" << std::endl;
    for (int i = 0; i < 60 && i < sequence2N.length(); ++i) {
        std::cout << sequence2N[i];
    }
    std::cout << std::endl;

    std::cout << ">Sequence_3N" << std::endl;
    for (int i = 0; i < 60 && i < sequence3N.length(); ++i) {
        std::cout << sequence3N[i];
    }
    std::cout << std::endl;

    std::cout << ">Sequence_5N" << std::endl;
    for (int i = 0; i < 60 && i < sequence5N.length(); ++i) {
        std::cout << sequence5N[i];
    }
    std::cout << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = atoi(argv[1]);
    generateFastaProblem(N);

    return 0;
}
