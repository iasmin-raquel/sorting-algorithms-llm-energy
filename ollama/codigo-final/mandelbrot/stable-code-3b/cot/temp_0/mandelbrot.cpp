#include <iostream>
#include <cmath>

const int N = 200; // Command-line argument parsing for N
const int MAX_ITERATIONS = 50; // Fixed iteration limit (50)
const double ESCAPE_THRESHOLD = 2.0 * 2.0; // Fixed escape threshold (lim = 2.0 * 2.0)

void mandelbrot(int width, int height) {
    std::cout << "P4\n";
    std::cout << N << " " << N << "\n";

    double x_min = -1.5;
    double x_max = 0.5;
    double y_min = -1.0;
    double y_max = 1.0;

    for (int y = 0; y < height; ++y) {
        double py = y * (y_max - y_min) / (height - 1) + y_min;

        for (int x = 0; x < width; ++x) {
            double px = x * (x_max - x_min) / (width - 1) + x_min;

            double Zr = 0.0; // Initialize real part of complex number Z
            double Zi = 0.0; // Initialize imaginary part of complex number Z

            const double C_REAL = 2.0 * px / N - 1.5; // Calculate real part of complex number C
            const double C_IMAGINARY = 2.0 * py / N - 1.0; // Calculate imaginary part of complex number C

            double ZrSquared = 0.0; // Initialize squared magnitude of complex number Z
            double ZiSquared = 0.0; // Initialize squared magnitude of complex number Z

            Zr = 0.0; // Reset real part of complex number Z
            Zi = 0.0; // Reset imaginary part of complex number Z

            for (int i = 0; i < MAX_ITERATIONS; ++i) {
                double new_Zr = Zr * Zr - C_REAL + C_IMAGINARY * Zi; // Calculate real part of complex number Z after one iteration
                double new_Zi = 2.0 * Zr * Zi + C_IMAGINARY * (1.0 - C_REAL / (N - 1)) - C_IMAGINARY * (C_REAL / (N - 1)) - C_IMAGINARY * (1.0 - C_REAL / (N - 1))) / (ZrSquared + ZiSquared); // Calculate imaginary part of complex number Z after one iteration

                if ((new_Zr * new_Zr) + (new_Zi * new_Zi) > ESCAPE_THRESHOLD) {
                    std::cout << "1 "; // Set pixel to white (1)
                    break;
                }

                Zr = new_Zr; // Update real part of complex number Z
                Zi = new_Zi; // Update imaginary part of complex number Z
            }

            if ((new_Zr * new_Zr) + (new_Zi * new_Zi) <= ESCAPE_THRESHOLD) {
                std::cout << "0 "; // Set pixel to black (0)
            }
        }
    }
    std::cout << "\n";
}

int main() {
    mandelbrot(N, N));
    return 0;
}
