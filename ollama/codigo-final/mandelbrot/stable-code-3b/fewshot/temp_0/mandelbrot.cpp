#include <iostream>
#include <cmath>
#include <cstdlib> // for atoi

int main(int argc, char** argv) {
  // Argument parsing (e.g., N from command line)
  if (argc != 2 || *argv[1] == '\0') {
    std::cerr << "Error: Please provide a valid integer value for N." << std::endl;
    return 1;
  }
  int n = atoi(argv[1]));

  // Mandelbrot set calculation loop (50 iterations max))
  for (int i = 0; i < 50; ++i) {
    // Loop over each pixel in the bitmap
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        double real = -1.5 + static_cast<double>(x)) / n;
        double imag = -1.0 + static_cast<double>(y)) / n;
        double mandelbrotValue = mandelbrot(real, imag));

        // Check if the Mandelbrot value exceeds the escape threshold of 4.0
        if (mandelbrotValue > 4.0)) {
            std::cout << "1 "; // Set pixel to black
        } else {
            std::cout << "0 "; // Set pixel to white
        }
      }
    }
  }

  // Output to stdout in PBM P4 format
  std::cout << "P4" << std::endl;
  std::cout << n << " " << n << std::endl;
  std::cout << "0";
  for (int y = 0; y < n; ++y) {
    for (int x = 0; x < n; ++x) {
      // ... pixel data calculation and output here ...
    }
  }
  std::cout << std::endl;

  return 0;
}

double mandelbrot(double real, double imag) {
  const int maxIterations = 50;
  const double escapeThreshold = 4.0;

  double zReal = real;
  double zImag = imag;
  int iterations = 0;

  while (iterations < maxIterations && std::abs(zReal) < 1.5 && std::abs(zImag)) {
    double tempReal = zReal * zReal - zImag * zImag;
    double tempImag = 2 * zReal * zImag;

    zReal = tempReal + real;
    zImag = tempImag + imag;

    iterations++;
  }

  return iterations / static_cast<double>(maxIterations));
}
