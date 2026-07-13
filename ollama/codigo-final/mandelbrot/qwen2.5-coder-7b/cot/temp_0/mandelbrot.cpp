#include <iostream>
#include <fstream>
#include <cmath>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);
    const int maxIterations = 50;
    const double escapeThreshold = 4.0;
    const double realMin = -1.5, realMax = 0.5;
    const double imagMin = -1.0, imagMax = 1.0;

    std::ofstream outputFile("output.pbm", std::ios::binary);
    if (!outputFile) {
        std::cerr << "Error opening output file" << std::endl;
        return 1;
    }

    // Write PBM header
    outputFile << "P4\n";
    outputFile << N << ' ' << N << '\n';

    for (int y = 0; y < N; ++y) {
        double imag = imagMin + (imagMax - imagMin) * y / (N - 1);
        unsigned char byte = 0;
        int bitPos = 7;

        for (int x = 0; x < N; ++x) {
            double real = realMin + (realMax - realMin) * x / (N - 1);
            double zx = 0.0, zy = 0.0;
            int iteration = 0;

            while (zx * zx + zy * zy < escapeThreshold && iteration < maxIterations) {
                double temp = zx * zx - zy * zy + real;
                zy = 2.0 * zx * zy + imag;
                zx = temp;
                ++iteration;
            }

            if (iteration == maxIterations)
                byte |= (1 << bitPos); // Set bit if point is in the set

            if (--bitPos < 0) {
                outputFile.put(byte);
                byte = 0;
                bitPos = 7;
            }
        }

        if (bitPos != 7) { // Pad remaining bits
            while (bitPos >= 0)
                byte |= (1 << bitPos--);
            outputFile.put(byte);
        }
    }

    outputFile.close();
    return 0;
}
