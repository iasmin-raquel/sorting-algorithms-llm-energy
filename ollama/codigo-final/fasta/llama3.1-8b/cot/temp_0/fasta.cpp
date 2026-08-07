#include <iostream>
#include <string>
#include <vector>

// Function to generate a random number using LCG
int lcg(int seed) {
    return (seed * 1103515245 + 12345) % 2147483648;
}

// Function to generate ALU sequence
std::string alu(int n) {
    std::string alu = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAA ATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGC AGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAG CTTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";
    std::string result = "";
    for (int i = 0; i < n * 2; ++i) {
        int r = lcg(42);
        if (r % 4 == 0) result += 'A';
        else if (r % 4 == 1) result += 'C';
        else if (r % 4 == 2) result += 'G';
        else result += 'T';
    }
    return alu + "\n" + result;
}

// Function to generate IUB sequence
std::string iub(int n) {
    std::vector<std::pair<char, double>> probabilities = {{'A', 0.27}, {'C', 0.12}, {'G', 0.12}, {'T', 0.27},
        {'B', 0.02}, {'D', 0.02}, {'H', 0.02}, {'K', 0.02}, {'M', 0.02}, {'N', 0.02},
        {'R', 0.02}, {'S', 0.02}, {'V', 0.02}, {'W', 0.02}};
    std::string result = "";
    for (int i = 0; i < n * 3; ++i) {
        int r = lcg(42);
        double cumulative_prob = 0;
        char base;
        for (const auto& prob : probabilities) {
            if (cumulative_prob <= static_cast<double>(r) / 2147483647 && cumulative_prob + prob.second < static_cast<double>(r) / 2147483647) {
                base = prob.first;
                break;
            }
            cumulative_prob += prob.second;
        }
        result += base;
    }
    return "TWO IUB ambiguity codes\n" + result;
}

// Function to generate Homo sapiens sequence
std::string homo_sapiens(int n) {
    std::vector<std::pair<char, double>> probabilities = {{'A', 0.3029549426680}, {'C', 0.1979883004921},
        {'G', 0.1975473066391}, {'T', 0.3015094502008}};
    std::string result = "";
    for (int i = 0; i < n * 5; ++i) {
        int r = lcg(42);
        double cumulative_prob = 0;
        char base;
        for (const auto& prob : probabilities) {
            if (cumulative_prob <= static_cast<double>(r) / 2147483647 && cumulative_prob + prob.second < static_cast<double>(r) / 2147483647) {
                base = prob.first;
                break;
            }
            cumulative_prob += prob.second;
        }
        result += base;
    }
    return "THREE Homo sapiens frequency\n" + result;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int n = std::stoi(argv[1]);
    std::cout << alu(n);
    std::cout << iub(n);
    std::cout << homo_sapiens(n);

    return 0;
}
