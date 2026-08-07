#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <ctime>

const int IM = 139968;
const int IA = 3877;
const int IC = 29573;
const int Seed = 42;

// ALU sequence
const std::string alu_sequence = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA"
                                   "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT"
                                   "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG"
                                   "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG"
                                   "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

// IUB alphabet and probabilities
const std::map<char, double> iub_probabilities = {
    {'a', 0.27}, {'c', 0.12}, {'g', 0.12}, {'t', 0.27},
    {'B', 0.02}, {'D', 0.02}, {'H', 0.02}, {'K', 0.02}, {'M', 0.02},
    {'N', 0.02}, {'R', 0.02}, {'S', 0.02}, {'V', 0.02}, {'W', 0.02}, {'Y', 0.02}
};

// Homo sapiens alphabet and probabilities
const std::map<char, double> human_probabilities = {
    {'a', 0.3029549426680}, {'c', 0.1979883004921},
    {'g', 0.1975473066391}, {'t', 0.3015094502008}
};

// LCG function to generate pseudo-random numbers
int lcg(int seed) {
    return (IA * seed + IC) % IM;
}

// Generate sequence using weighted random selection from a map of probabilities
std::string generate_sequence(const std::map<char, double>& probabilities, int length) {
    std::vector<double> cumulative_probs;
    double sum = 0.0;
    
    for (const auto& pair : probabilities) {
        sum += pair.second;
        cumulative_probs.push_back(sum);
    }
    
    std::string sequence;
    for (int i = 0; i < length; ++i) {
        double random_value = static_cast<double>(lcg(seed)) / IM;
        seed = lcg(seed); // Update seed
        
        auto it = std::lower_bound(cumulative_probs.begin(), cumulative_probs.end(), random_value);
        if (it != cumulative_probs.end()) {
            sequence += (*it < random_value ? *(it + 1) : *it);
        }
    }
    
    return sequence;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }
    
    int N = std::stoi(argv[1]);
    int seed = Seed;
    
    // Generate and print the first sequence
    std::string alu_seq = alu_sequence.substr(0, N * 2);
    for (int i = 0; i < N; ++i) {
        alu_seq += alu_sequence.substr(i % alu_sequence.length(), 1);
        seed = lcg(seed); // Update seed
    }
    std::cout << "one\t" << alu_seq << std::endl;
    
    // Generate and print the second sequence
    std::string iub_seq = generate_sequence(iub_probabilities, N * 3);
    for (int i = 0; i < N * 3; ++i) {
        char nucleotide = iub_seq[i % iub_seq.length()];
        std::cout << "two\t" << nucleotide;
        seed = lcg(seed); // Update seed
    }
    std::cout << std::endl;
    
    // Generate and print the third sequence
    std::string human_seq = generate_sequence(human_probabilities, N * 5);
    for (int i = 0; i < N * 5; ++i) {
        char nucleotide = human_seq[i % human_seq.length()];
        std::cout << "three\t" << nucleotide;
        seed = lcg(seed); // Update seed
    }
    std::cout << std::endl;
    
    return 0;
}
