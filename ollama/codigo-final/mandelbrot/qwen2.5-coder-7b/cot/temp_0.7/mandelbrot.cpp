#include <iostream>
#include <cmath>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::atoi(argv[1]);
    double width = 0.5 - (-1.5);
    double height = 1.0 - (-1.0);
    double pixel_width = width / (N - 1);
    double pixel_height = height / (N - 1);

    std::cout << "P4\n" << N << ' ' << N << '\n';

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double real = -1.5 + x * pixel_width;
            double imag = -1.0 + y * pixel_height;
            double z_real = 0.0, z_imag = 0.0;
            bool escapes = false;

            for (int iter = 0; iter < 50 && !escapes; ++iter) {
                double new_z_real = z_real * z_real - z_imag * z_imag + real;
                double new_z_imag = 2.0 * z_real * z_imag + imag;
                if (new_z_real * new_z_real + new_z_imag * new_z_imag > 4.0) {
                    escapes = true;
                }
                z_real = new_z_real;
                z_imag = new_z_imag;
            }

            std::cout << (escapes ? '1' : '0');
        }
        std::cout << '\n';
    }

    return 0;
}
