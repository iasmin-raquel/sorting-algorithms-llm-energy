/*
 * The Computer Language Benchmarks Game
 * https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
 *
 * contributed by [Your Name]
 */

#include <stdio.h>
#include <stdlib.h>

namespace {
  // Helper function to calculate the squared magnitude of a complex number
  inline double mag2(double zr, double zi) {
    return zr*zr + zi*zi;
  }

  // Function to determine if a point belongs to the Mandelbrot set
  inline bool in_mandelbrot(double cr, double ci, int max_iter = 50, double lim = 4.0) {
    double zr = 0.0, zi = 0.0;
    for (int i = 0; i < max_iter && mag2(zr, zi) <= lim; ++i) {
      double new_zr = zr*zr - zi*zi + cr;
      zi = 2.0 * zr * zi + ci;
      zr = new_zr;
    }
    return mag2(zr, zi) > lim;
  }
}

int main(int argc, char** argv) {
  int N = atoi(argv[1]);

  // Write PBM P4 header
  printf("P4\n%d %d\n", N, N);

  // Iterate over each pixel and determine if it belongs to the Mandelbrot set
  for (int y = 0; y < N; ++y) {
    for (int x = 0; x < N; ++x) {
      double cr = 2.0 * x / N - 1.5;
      double ci = 2.0 * y / N - 1.0;
      putchar(in_mandelbrot(cr, ci) ? '\377' : '\0');
    }
  }

  return 0;
}
