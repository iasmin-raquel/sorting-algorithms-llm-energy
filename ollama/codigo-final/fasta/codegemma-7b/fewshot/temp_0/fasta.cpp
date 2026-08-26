#include <iostream>
#include <string>
#include <vector>

struct RandomGenerator {
    int seed;
    double random(double max) {
        seed = ((seed * IA + IC) % IM);
        return max * seed / IM;
    }
};

constexpr int IM = 139968, IA = 3877, IC = 29573;

std::string generateRepeatFasta(const std::string& pattern, int n) {
    std::string result;
    for (int i = 0; i < n; i++) {
        result += pattern;
    }
    return result;
}

std::string generateRandomFasta(const std::vector<std::pair<char, double>>& alphabet,
                               int length) {
    RandomGenerator rng{42};
    std::string result;
    for (int i = 0; i < length; i++) {
        double r = rng.random(1.0);
        int index = 0;
        for (const auto& [_, p] : alphabet) {
            if (r < p) {
                result += alphabet[index].first;
                break;
            }
            r -= p;
            index++;
        }
    }
    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }
    int N = std::stoi(argv[1]);

    const std::string ALU_SEQUENCE = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
                                   "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT" +
                                   "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG" +
                                   "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG" +
                                   "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

    const std::vector<std::pair<char, double>> IUB_ALPHABET = {
        {'a', 0.27}, {'c', 0.12}, {'g', 0.12}, {'t', 0.27},
        {'B', 0.02}, {'D', 0.02}, {'H', 0.02}, {'K', 0.02},
        {'M', 0.02}, {'N', 0.02}, {'R', 0.02}, {'S', 0.02},
        {'V', 0.02}, {'W', 0.02}, {'Y', 0.02}
    };

    const std::vector<std::pair<char, double>> HSAP_ALPHABET = {
        {'a', 0.3029549426680}, {'c', 0.1979883004921},
        {'g', 0.1975473066391}, {'t', 0.3015094502008}
    };

    auto repeat_alu = generateRepeatFasta(ALU_SEQUENCE, N * 2);
    auto random_iub   = generateRandomFasta(IUB_ALPHABET, N * 3);
    auto random_hsap  = generateRandomFasta(HSAP_ALPHABET, N * 5);

    std::cout << ">ONE Homo sapiens alu\n" << repeat_alu << "\n";
    std::cout << ">TWO IUB ambiguity codes\n" << random_iub << "\n";
    std::cout << ">THREE Homo sapiens frequency\n" << random_hsap;

    return 0;
}
