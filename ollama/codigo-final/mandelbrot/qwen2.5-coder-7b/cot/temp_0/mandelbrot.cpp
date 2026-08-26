#include <iostream>
#include <cmath>
#include <cstring>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::atoi(argv[1]);
    double lim = 4.0; // Escape threshold squared
    const int maxIter = 50;

    // PBM P4 header
    std::cout << "P4" << std::endl;
    std::cout << N << " " << N << std::endl;

    for (int y = 0; y < N; ++y) {
        unsigned char row[N / 8];
        memset(row, 0, sizeof(row));

        for (int x = 0; x < N; ++x) {
            double zx = 0.0, zy = 0.0;
            double cx = 2.0 * x / N - 1.5;
            double cy = 2.0 * y / N - 1.0;

            int iter = 0;
            while (zx * zx + zy * zy <= lim && iter < maxIter) {
                double nxz = zx * zx - zy * zy + cx;
                zy = 2.0 * zx * zy + cy;
                zx = nxz;
                ++iter;
            }

            if (iter == maxIter) {
                // Pixel belongs to the set, mark as black
                int byteIndex = x / 8;
                int bitIndex = x % 8;
                row[byteIndex] |= (1 << (7 - bitIndex));
            }
        }

        std::cout.write(reinterpret_cast<char*>(row), sizeof(row));
    }

    return 0;
}
