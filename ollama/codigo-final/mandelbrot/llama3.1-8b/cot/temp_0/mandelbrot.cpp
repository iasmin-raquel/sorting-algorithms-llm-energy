#include <iostream>
#include <cstdint>

// Function to compute Mandelbrot set
void mandelbrot(int N, int iterations) {
    double lim = 2.0 * 2.0;
    uint8_t* pixelData = new uint8_t[N * N];

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            // Apply coordinate mapping
            double C_real = 2.0 * x / N - 1.5;
            double C_imag = 2.0 * y / N - 1.0;

            double Z_real = 0.0;
            double Z_imag = 0.0;

            for (int i = 0; i < iterations; ++i) {
                // Compute new Z
                double tempReal = Z_real * Z_real - Z_imag * Z_imag + C_real;
                double tempImag = 2.0 * Z_real * Z_imag + C_imag;

                if (tempReal * tempReal + tempImag * tempImag > lim) {
                    // Pixel is not in the set
                    pixelData[(y * N + x)] = 0;
                    break;
                }

                Z_real = tempReal;
                Z_imag = tempImag;
            }

            if (iterations == i) {
                // Pixel is in the set
                pixelData[(y * N + x)] = 1;
            }
        }
    }

    // Pad each row with zeros if N is not divisible by 8
    int padding = N % 8;
    for (int y = 0; y < N; ++y) {
        uint8_t* row = pixelData + (y * N);
        for (int i = 0; i < padding; ++i) {
            *(row + N - 1 - i) = 0;
        }
    }

    // Output PBM P4 format
    std::cout << "P4\nN " << N << "\n";
    for (int y = 0; y < N; ++y) {
        uint8_t* row = pixelData + (y * N);
        for (int x = 0; x < N; ++x) {
            std::cout << static_cast<int>(row[x]);
        }
        // Pad with zeros if necessary
        int padding = N % 8;
        for (int i = 0; i < padding; ++i) {
            std::cout << "0";
        }
        std::cout << "\n";
    }

    delete[] pixelData;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>\n";
        return 1;
    }

    int N = std::stoi(argv[1]);
    mandelbrot(N, 50);

    return 0;
}
