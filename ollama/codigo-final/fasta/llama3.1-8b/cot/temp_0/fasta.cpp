#include <iostream>
#include <string>
#include <vector>

// Function to generate a random number using LCG
int lcg(int seed) {
    return (seed * 1103515245 + 12345) % 139968;
}

// Function to generate ALU sequence
std::string alu(int n) {
    std::string seq = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAA ATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGC AGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAG CTTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";
    std::string result;
    for (int i = 0; i < n * 2; ++i) {
        int r = lcg(42);
        if (r % 4 == 0) result += 'A';
        else if (r % 4 == 1) result += 'C';
        else if (r % 4 == 2) result += 'G';
        else result += 'T';
    }
    return seq + "\n" + result;
}

// Function to generate IUB sequence
std::string iub(int n) {
    std::vector<std::pair<char, double>> bases = {{'A', 0.27}, {'C', 0.12}, {'G', 0.12}, {'T', 0.27},
        {'B', 0.02}, {'D', 0.02}, {'H', 0.02}, {'K', 0.02}, {'M', 0.02}, {'N', 0.02},
        {'R', 0.02}, {'S', 0.02}, {'V', 0.02}, {'W', 0.02}};
    std::string result;
    for (int i = 0; i < n * 3; ++i) {
        double r = static_cast<double>(lcg(42)) / 139968;
        char base;
        for (const auto& b : bases) {
            if (r <= b.second) {
                base = b.first;
                break;
            }
            r -= b.second;
        }
        result += base;
    }
    return "TWO IUB ambiguity codes\n" + result;
}

// Function to generate Homo sapiens sequence
std::string homo(int n) {
    std::vector<std::pair<char, double>> bases = {{'A', 0.3029549426680}, {'C', 0.1979883004921},
        {'G', 0.1975473066391}, {'T', 0.3015094502008}};
    std::string result;
    for (int i = 0; i < n * 5; ++i) {
        double r = static_cast<double>(lcg(42)) / 139968;
        char base;
        for (const auto& b : bases) {
            if (r <= b.second) {
                base = b.first;
                break;
            }
            r -= b.second;
        }
        result += base;
    }
    return "THREE Homo sapiens frequency\n" + result;
}

int main(int argc, char* argv[]) {
    int n = std::stoi(argv[1]);
    std::cout << alu(n) << iub(n) << homo(n);
    return 0;
}
