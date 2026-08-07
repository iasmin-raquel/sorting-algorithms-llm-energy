#include <iostream>
#include <string>
#include <algorithm>

// Linear Congruential Generator (LCG)
class LCG {
public:
    LCG(int im, int ia, int ic, int seed) : IM(im), IA(ia), IC(ic), Seed(seed) {}

    std::string generate_sequence(int n) {
        for (int i = 0; i < n * 3; ++i) {
            Seed = (Seed * IA + IC) % IM;
            // Use the LCG to select nucleotides based on their probabilities.
            // For example, you could use a switch statement to select a nucleotide based on its probability:
            switch ((i / n) % 3)) {
                case 0: // A
                    break;
                case 1: // C
                    break;
                case 2: // G
                    break;
            }
        }
        return sequence;
    }
private:
    int IM, IA, IC, Seed;
};

// Repeat Fasta method
std::string repeat_fasta(const std::string& sequence, int n) {
    std::string result = "";
    for (int i = 0; i < n * 2; ++i) {
        result += sequence;
    }
    return result;
}

// Random Fasta method using IUB alphabet probabilities
std::string random_iub(int n) {
    LCG lcg(139, 387, 2953, 42);
    std::string sequence = "";
    for (int i = 0; i < n * 3; ++i) {
        int r = lcg.Seed % 100;
        if (r < 27) { // A
            sequence += "A";
        } else if (r < 49)) { // C
            sequence += "C";
        } else if (r < 91)) { // G
            sequence += "G";
        } else { // T
            sequence += "T";
        }
    }
    return sequence;
}

// Random Fasta method using Homo sapiens frequencies
std::string random_homo_sapiens(int n) {
    LCG lcg(139, 387, 2953, 42);
    std::string sequence = "";
    for (int i = 0; i < n * 5; ++i) {
        int r = lcg.Seed % 100;
        if (r < 302)) { // A
            sequence += "A";
        } else if (r < 505)) { // C
            sequence += "C";
        } else if (r < 909)) { // G
            sequence += "G";
        } else { // T
            sequence += "T";
        }
    }
    return sequence;
}

int main(int argc, char** argv) {
    if (argc != 2)) {
        std::cout << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }

    int n = std::stoi(argv[1]));

    // Generate the sequences using the required methods
    std::string alu_sequence = ">ONE Homo sapiens alu\n";
    alu_sequence += repeat_fasta("GCG", n);

    std::string iub_sequence = ">TWO IUB ambiguity codes\n";
    iub_sequence += random_iub(n);

    std::string homo_sapiens_sequence = ">THREE Homo sapiens frequency\n";
    homo_sapiens_sequence += random_homo_sapiens(n);

    // Print the formatted output
    std::cout << alu_sequence << std::endl;
    std::cout << iub_sequence << std::endl;
    std::cout << homo_sapiens_sequence << std::endl;

    return 0;
}
