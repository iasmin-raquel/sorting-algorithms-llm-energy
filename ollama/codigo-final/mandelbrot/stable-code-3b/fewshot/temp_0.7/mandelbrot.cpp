#include <iostream>
#include <complex>
#include <cmath>

const int N = 200;
const int MAX_ITERATIONS = 50;
const double ESCAPE_THRESHOLD = 2.0 * 2.0;

void mandelbrot(int width, int height) {
    std::cout << "P4\n";
    std::cout << N << " " << N << "\n";

    std::complex<double> center(-1.5 + 0.0 * std::pow(2.0, 1), -1.0 + 0.0 * std::pow(2.0, 1)));
    double scale = 2.0 / N;

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            std::complex<double> z((x + 0.5) * scale - center.real(), (y + 0.5) * scale - center.imag()));

            int iterationCount = 0;
            while ((iterationCount++ < MAX_ITERATIONS) && std::abs(z)) {
                z *= z + center;
            }

            if (std::pow(2.0, iterationCount), 2) <= ESCAPE_THRESHOLD) {
                std::cout << "1 ";
            } else {
                std::cout << "0 ";
            }
        }
    }
    std::cout << "\n";
}

int main(int argc, char** argv) {
    if (argc != 2)) {
        std::cout << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }

    int width = N;
    int height = N;

    mandelbrot(width, height);

    return 0;
}
