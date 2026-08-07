#include <iostream>
#include <cmath>

const int MAX_ITERATIONS = 50;
const double ESCAPE_THRESHOLD = 4.0;

void mandelbrot(int N) {
    std::cout << "P4\n";
    std::cout << N << ' ' << N << '\n';

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double real_C = 2.0 * x / N - 1.5;
            double imag_C = 2.0 * y / N - 1.0;

            double zr = 0.0;
            double zi = 0.0;
            double zr_squared = 0.0;
            int iteration = 0;

            while (zr_squared <= ESCAPE_THRESHOLD && iteration < MAX_ITERATIONS) {
                const double temp1 = zr * zr + zi * zi;
                zr = temp1 - zr;
                zi = 1.0 * (temp1 - zr) / zr * 2.0 + imag_C;

                zr_squared = zr * zr + zi * zi;
                ++iteration;
            }

            int membership = (zr_squared <= ESCAPE_THRESHOLD) ? 1 : 0;

            std::cout << "N" << membership;

            if ((x + 1) % 8 != 0) {
                for (int j = 0; j < 7 - (x + 1) % 8; ++j) {
                    std::cout << '0';
                }
            }

            std::cout << '\n';
        }
    }

    std::cout << "N" << '\n';
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: mandelbrot N\n";
        return 1;
    }

    int N = std::stoi(argv[1]));

    mandelbrot(N);

    return 0;
}
