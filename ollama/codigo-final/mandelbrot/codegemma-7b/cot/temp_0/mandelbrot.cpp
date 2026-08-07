#include <iostream>
#include <cmath>

using namespace std;

const double lim = 4.0;
const int max_iterations = 50;

complex<double> iterate(complex<double> C) {
  complex<double> Z = {0, 0};
  for (int i = 0; i < max_iterations; i++) {
    if (abs(Z) > lim) {
      return {0, 0};
    }
    Z = Z * Z + C;
  }
  return {1, 0};
}

int main(int argc, char* argv[]) {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " N" << endl;
    return 1;
  }

  int N = atoi(argv[1]);
  if (N <= 0) {
    cerr << "Invalid N value: " << N << endl;
    return 1;
  }

  cout << "P4\n" << N << " " << N << endl;

  for (int y = 0; y < N; y++) {
    for (int x = 0; x < N; x++) {
      complex<double> C = {2.0 * x / N - 1.5, 2.0 * y / N - 1.0};
      cout << (int)iterate(C).real() << "";
    }
    if ((N - y) % 8 != 0) {
      for (int i = 0; i < 8 - (N - y) % 8; i++) {
        cout << 0;
      }
    }
    cout << endl;
  }

  return 0;
}
