#include <iostream>
#include <complex>

const int N = 1000;
const int MAX_ITERATIONS = 50;
const double ESCAPE_THRESHOLD = 4.0;
const double IMAG_C = -1.0;
const double REAL_C = -1.5;

std::complex<double> mandelbrot(int x, int y) {
    std::complex<double> C(REAL_C * (x + 0.5) / N, IMAG_C * (y + 0.5) / N);
    std::complex<double> Z(0.0, 0.0));
    int iterations = 0;
    while (abs(Z)) < ESCAPE_THRESHOLD && iterations < MAX_ITERATIONS {
        iterations++;
        Z = Z * Z + C;
    }
    return Z;
}

void print_header() {
    std::cout << "P4\n";
    std::cout << N << " " << N << "\n";
}

int main(int argc, char** argv) {
    if (argc != 2)) {
        std::cerr << "Usage: " << argv[0] << " <N>\n";
        return 1;
    }

    print_header();

    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            auto z = mandelbrot(x, y));
            if (abs(z)) >= ESCAPE_THRESHOLD) {
                std::cout << "1 ";
            } else {
                std::cout << "0 ";
            }
        }
        std::cout << "\n";
    }

    return 0;
}
