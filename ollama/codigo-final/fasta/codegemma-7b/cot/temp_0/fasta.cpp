#include <iostream>
#include <string>
#include <random>

using namespace std;

const string ALU = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA"
                 "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT"
                 "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG"
                 "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG"
                 "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

const double IUB_probs[] = {0.27, 0.12, 0.12, 0.27, 0.02};
const double Homo_probs[] = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};

const int IM = 139968;
const int IA = 3877;
const int IC = 29573;
const int Seed = 42;

int main(int argc, char* argv[]) {
  if (argc != 2) {
    cerr << "Usage: fasta N" << endl;
    return 1;
  }

  int N = atoi(argv[1]);
  if (N <= 0) {
    return 0;
  }

  random_device rd;
  mt19937 gen(rd());
  uniform_real_distribution<> dis(0.0, 1.0);

  for (int n : {N * 2, N * 3, N * 5}) {
    cout << ">ONE Homo sapiens alu" << endl;
    for (int i = 0; i < n; i++) {
      cout << ALU[i % ALU.size()];
      if (i % 60 == 59) {
        cout << endl;
      }
    }
    cout << endl;

    cout << ">TWO IUB ambiguity codes" << endl;
    for (int i = 0; i < n; i++) {
      double r = dis(gen);
      int index = 0;
      while (r > 0) {
        r -= IUB_probs[index++];
      }
      cout << "ACGTBNDHRVWSY"[index - 1];
      if (i % 60 == 59) {
        cout << endl;
      }
    }
    cout << endl;

    cout << ">THREE Homo sapiens frequency" << endl;
    for (int i = 0; i < n; i++) {
      double r = dis(gen);
      int index = 0;
      while (r > 0) {
        r -= Homo_probs[index++];
      }
      cout << "ACGT"[index - 1];
      if (i % 60 == 59) {
        cout << endl;
      }
    }
    cout << endl;
  }

  return 0;
}
