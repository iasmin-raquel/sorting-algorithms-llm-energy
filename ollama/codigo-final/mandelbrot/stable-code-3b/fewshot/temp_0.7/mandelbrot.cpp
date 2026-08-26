#include <iostream>
#include <complex>
#include <cmath>
#include <vector>

const int MAX_ITERATIONS = 50;
const double ESCAPE_THRESHOLD = 2.0 * 2.0;

std::vector<unsigned char> generate_mandelbrot(int N) {
    std::vector<unsigned char> image(N * N * 3);
    for (int x = 0; x < N; ++x) {
        for (int y = 0; y < N; ++y) {
            double real_C = 2.0 * x / N - 1.5;
            double imag_C = 2.0 * y / N - 1.0;

            std::complex<double> Z((real_C, imag_C)));
            int iterations = 0;
            while (abs(Z)) > ESCAPE_THRESHOLD && iterations < MAX_ITERATIONS) {
                Z *= Z + std::complex<double>(real_C, imag_C)) ;
                ++iterations;
            }

            if (iterations < MAX_ITERATIONS && abs(Z)) <= ESCAPE_THRESHOLD) {
                unsigned char r = static_cast<unsigned char>(255 * std::max({0.0, Z.real(), -1.5}, {-1.0, 0.0}))));
                unsigned char g = static_cast<unsigned char>(255 * std::max({0.0, Z.imag(), -1.0}, {0.0, 0.0}))));
                image[(x + y * N) * 3] = r;
                image[(x + y * N) * 3 + 1] = g;
            }
        }
    }
    return image;
}

int main(int argc, char** argv) {
    if (argc != 2)) {
        std::cout << "Usage: ./mandelbrot <N>" << std::endl;
        return 1;
    }

    int N = atoi(argv[1]));
    if (N <= 0)) {
        std::cout << "Error: N must be a positive integer." << std::endl;
        return 1;
    }

    std::vector<unsigned char> image = generate_mandelbrot(N));
    int size = N * N * 3;
    for (int i = 0; i < size; ++i) {
        if (image[i]) {
            std::cout << "Error: Failed to generate the Mandelbrot set image." << std::endl;
            return 1;
        }
    }

    std::cout << "P4\n";
    std::cout << N << " " << N << "\n";
    for (int i = 0; i < size; ++i) {
        std::cout.put(image[i]));
    }
    return 0;
}
