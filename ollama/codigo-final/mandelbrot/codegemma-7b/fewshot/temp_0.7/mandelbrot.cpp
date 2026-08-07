#include <cstdio>
#include <cstdlib>

const int N = 50; // Maximum iterations
const double lim = 4.0; // Escape threshold squared

int main(int argc, char* argv[]) {
    int n = atoi(argv[1]); // Read N from command line

    printf("P4\n%d %d\n", n, n); // PBM header

    for (int y = 0; y < n; y++) {
        int row = 0;
        for (int x = 0; x < n; x++) {
            double c_real = 2.0 * x / n - 1.5;
            double c_imag = 2.0 * y / n - 1.0;
            double z_real = 0.0;
            double z_imag = 0.0;

            for (int i = 0; i < N; i++) {
                double z_real_sq = z_real * z_real;
                double z_imag_sq = z_imag * z_imag;
                if (z_real_sq + z_imag_sq > lim) {
                    row |= (1 << (N - i - 1));
                    break;
                }
                z_imag = 2.0 * z_real * z_imag + c_imag;
                z_real = z_real_sq - z_imag_sq + c_real;
            }
        }

        printf("%08x\n", row); // Write binary row
    }

    return 0;
}
