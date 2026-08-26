#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
    int N = atoi(argv[1]);
    const int max_iterations = 50;
    const double lim = 2.0 * 2.0;

    ofstream output("output.pbm");
    if (!output.is_open()) {
        cerr << "Error opening output file." << endl;
        return 1;
    }

    output << "P4\n" << N << " " << N << "\n";
    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double real = 2.0 * x / N - 1.5;
            double imag = 2.0 * y / N - 1.0;

            complex<double> z(real, imag);
            int iterations = 0;
            while (iterations < max_iterations && abs(z) <= lim) {
                z = z*z + complex<double>(real, imag);
                ++iterations;
            }

            if (iterations == max_iterations)
                output << "1";
            else
                output << "0";

            // Pad with zeros to 8 bytes per row
            if ((x+1)%8 == 0 && x != N-1) {
                output << "\n";
            }
        }
    }

    output.close();

    return 0;
}
