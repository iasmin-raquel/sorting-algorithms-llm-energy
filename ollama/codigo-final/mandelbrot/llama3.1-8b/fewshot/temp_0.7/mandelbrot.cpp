#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char **argv) {
    if (argc != 2) {
        cerr << "Usage: mandelbrot N" << endl;
        return 1;
    }

    int n = atoi(argv[1]);
    if (n % 8 != 0) {
        cerr << "Error: N must be a multiple of 8 for correct padding." << endl;
        return 1;
    }

    cout << "P4\n" << n << " " << n << endl;

    const int max_iterations = 50;
    double lim = 4.0;

    for (int y = 0; y < n; ++y) {
        for (int x = 0; x < n; ++x) {
            double cx = 2.0 * x / static_cast<double>(n) - 1.5;
            double cy = 2.0 * y / static_cast<double>(n) - 1.0;

            complex<double> z(0, 0);
            bool is_in_set = true;

            for (int i = 0; i < max_iterations && abs(z) <= lim; ++i) {
                z = z*z + complex<double>(cx, cy);
            }

            if (abs(z) > lim) {
                is_in_set = false;
            }

            int pixel_value = is_in_set ? 255 : 0;

            for (int bit = 7; bit >= 0; --bit) {
                cout << ((pixel_value >> bit) & 1);
            }
        }
    }

    return 0;
}
