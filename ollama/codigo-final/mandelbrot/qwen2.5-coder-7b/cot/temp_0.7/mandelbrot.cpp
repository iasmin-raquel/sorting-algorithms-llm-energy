#include <iostream>
#include <cmath>

// Function to calculate whether a point belongs to the Mandelbrot set
bool isMandelbrot(double cr, double ci) {
    double zr = 0.0, zi = 0.0;
    for (int i = 0; i < 50; ++i) {
        double newZr = zr*zr - zi*zi + cr;
        zi = 2.0 * zr * zi + ci;
        zr = newZr;
        if (zr*zr + zi*zi > 4.0) {
            return false; // The point escapes the set
        }
    }
    return true; // The point belongs to the set
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::atoi(argv[1]);
    std::cout << "P4" << std::endl << N << ' ' << N << std::endl;

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double cr = 2.0 * x / N - 1.5;
            double ci = 2.0 * y / N - 1.0;
            if (isMandelbrot(cr, ci)) {
                std::cout << '\1';
            } else {
                std::cout << '\0';
            }
        }
        // Padding with zeros if necessary
        for (; x % 8 != 0; ++x) {
            std::cout << '\0';
        }
    }

    return 0;
}
