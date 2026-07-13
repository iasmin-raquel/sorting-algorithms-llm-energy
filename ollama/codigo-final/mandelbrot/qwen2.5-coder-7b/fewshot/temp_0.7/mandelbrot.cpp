#include <iostream>
#include <cmath>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }

    int N = std::atoi(argv[1]);
    double scale_real = (0.5 - (-1.5)) / N;
    double scale_imaginary = (1.0 - (-1.0)) / N;

    std::cout << "P4\n" << N << ' ' << N << '\n';

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double real = -1.5 + x * scale_real;
            double imag = -1.0 + y * scale_imaginary;

            double z_real = 0.0, z_imag = 0.0;
            int iteration = 0;

            while (z_real * z_real + z_imag * z_imag < 4.0 && iteration < 50) {
                double temp = z_real * z_real - z_imag * z_imag + real;
                z_imag = 2.0 * z_real * z_imag + imag;
                z_real = temp;
                ++iteration;
            }

            std::cout << (iteration % 2 == 0 ? '1' : '0');
        }
        std::cout << '\n';
    }

    return 0;
}
