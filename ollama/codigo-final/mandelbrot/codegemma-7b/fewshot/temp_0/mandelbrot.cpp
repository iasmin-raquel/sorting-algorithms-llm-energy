#include <cstdio>
#include <cmath>

int main(int argc, char* argv[]) {
    int N = atoi(argv[1]);

    // --- Mandelbrot core ---
    const double lim = 4.0;
    const int max_iter = 50;

    // PBM P4 header
    printf("P4\n%d %d\n", N, N);

    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            double cr = 2.0 * x / N - 1.5;
            double ci = 2.0 * y / N - 1.0;

            int iter = 0;
            double zr = 0, zi = 0;
            while (iter < max_iter && zr*zr + zi*zi <= lim) {
                double new_zr = zr*zr - zi*zi + cr;
                double new_zi = 2 * zr * zi + ci;
                zr = new_zr; zi = new_zi;
                iter++;
            }
            // Pack bits (MSB=in set, LSB=not in set)
            printf("%c", (iter == max_iter) ? '0' : '1');
        }

        // Pad last byte with zeros if necessary
        if (N % 8 != 0) {
            for (int i = 0; i < 8 - N % 8; i++) {
                printf("0");
            }
        }
        printf("\n");
    }

    return 0;
}
