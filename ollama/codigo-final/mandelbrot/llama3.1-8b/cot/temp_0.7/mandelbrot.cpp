#include <iostream>
#include <fstream>

const int N = 200;
const int iterations = 50;
const double escape_threshold = 4.0;

// Coordinate mapping formulas
double real(double x) {
    return 2.0 * x / N - 1.5;
}

double imag(double y) {
    return 2.0 * y / N - 1.0;
}

int main() {
    // Create output file
    std::ofstream output("output.pbm");

    // Write PBM header
    output << "P4\n" << N << " " << N << "\n";

    int** pixels = new int*[N];
    for (int i = 0; i < N; i++) {
        pixels[i] = new int[N];
    }

    // Compute Mandelbrot set
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            double C = real(x) + imag(y) * I;
            double z = C;

            int iter = 0;
            while (iter < iterations && abs(z) <= escape_threshold) {
                double temp = z * z;
                double real_z = creal(temp);
                double imag_z = cimag(temp);
                if (real_z > escape_threshold || imag_z > escape_threshold)
                    break;

                z = C + z * z;
                iter++;
            }

            pixels[x][y] = iter;
        }
    }

    // Write pixel data
    for (int y = 0; y < N; y++) {
        int byte = 0;
        for (int x = 0; x < N; x += 8) {
            byte = 0;
            for (int i = 0; i < 8 && x + i < N; i++) {
                byte |= pixels[x + i][y] << (7 - i);
            }
            output.write((char*)&byte, 1);
        }
    }

    // Clean up
    for (int i = 0; i < N; i++) {
        delete[] pixels[i];
    }
    delete[] pixels;

    return 0;
}
