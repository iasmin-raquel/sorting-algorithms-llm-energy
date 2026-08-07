#include <iostream>
#include <cmath>
#include <cstring>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }

    int N = std::atoi(argv[1]);
    double lim = 4.0; // Escape threshold squared
    const int maxIter = 50;

    // PBM P4 header
    std::cout << "P4\n" << N << ' ' << N << '\n';

    for (int y = 0; y < N; ++y) {
        unsigned char row[N / 8];
        memset(row, 0, sizeof(row));

        for (int x = 0; x < N; ++x) {
            double zx = 2.0 * x / N - 1.5;
            double zy = 2.0 * y / N - 1.0;
            double cr = zx;
            double ci = zy;
            int iter = 0;

            while (zx * zx + zy * zy <= lim && iter < maxIter) {
                double temp = zx * zx - zy * zy + cr;
                zy = 2.0 * zx * zy + ci;
                zx = temp;
                ++iter;
            }

            // Set the pixel if it belongs to the Mandelbrot set
            if (iter == maxIter) {
                int byteIndex = x / 8;
                int bitIndex = x % 8;
                row[byteIndex] |= (1 << (7 - bitIndex));
            }
        }

        // Output the row of pixels
        std::cout.write(reinterpret_cast<char*>(row), sizeof(row));
    }

    return 0;
}
