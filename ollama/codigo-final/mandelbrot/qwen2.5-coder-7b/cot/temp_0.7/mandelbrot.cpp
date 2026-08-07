#include <iostream>
#include <fstream>
#include <cmath>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);
    const int maxIterations = 50;
    double lim = 4.0;

    // Output PBM header
    std::cout << "P4" << std::endl;
    std::cout << N << ' ' << N << std::endl;

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double zx = 0.0, zy = 0.0;
            double cr = 2.0 * x / N - 1.5;
            double ci = 2.0 * y / N - 1.0;
            int iteration = 0;

            while (zx*zx + zy*zy <= lim && iteration < maxIterations) {
                double temp = zx*zx - zy*zy + cr;
                zy = 2.0*zx*zy + ci;
                zx = temp;
                ++iteration;
            }

            // Output pixel value as binary
            std::cout << (iteration % 8 == 0 ? '\n' : ' ') << (iteration < maxIterations ? '1' : '0');
        }
    }

    return 0;
}
