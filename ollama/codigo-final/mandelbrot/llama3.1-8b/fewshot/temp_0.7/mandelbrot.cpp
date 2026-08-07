#include <iostream>
#include <complex>

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " N" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);

    const double iterations = 50.0;
    const double escape_threshold = 4.0;

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            std::complex<double> c(2.0 * x / N - 1.5, 2.0 * y / N - 1.0);
            std::complex<double> z(0.0);

            for (double iteration = 0; iteration < iterations; ++iteration) {
                if (std::abs(z) > escape_threshold) {
                    break;
                }

                z = z * z + c;
            }

            int color = ((int)(iteration % 8)) << 5;

            std::cout << (char)color;
        }

        // Pad last byte of each row with zeros if N is not divisible by 8
        if (N % 8 != 0) {
            for (int i = 7; i > N % 8 - 1; --i) {
                std::cout << '\x00';
            }
        }

        std::cout << '\n';
    }

    return 0;
}
