#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);

    const double lim = 4.0;

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double realC = 2.0 * x / N - 1.5;
            double imagC = 2.0 * y / N - 1.0;

            int iterations = 50;
            double zReal = 0, zImag = 0;

            for (int i = 0; i < iterations; ++i) {
                double newZReal = zReal * zReal - zImag * zImag + realC;
                zImag = 2.0 * zReal * zImag + imagC;
                zReal = newZReal;

                if (zReal * zReal + zImag * zImag > lim) {
                    iterations = i + 1;
                    break;
                }
            }

            std::cout << static_cast<char>(iterations & 0xFF);
        }

        // Pad with zeros
        int padding = N % 8;
        for (int i = 0; i < padding; ++i) {
            std::cout << '0';
        }

        std::cout << '\n';
    }

    return 0;
}
