public final class Mandelbrot {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        plotMandelbrotSet(N);
    }

    static void plotMandelbrotSet(int N) {
        // Initialize the PBM header
        System.out.println("P4");
        System.out.println(N + " " + N);

        // Iterate over each pixel in the grid
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                // Map the pixel coordinates to the complex plane
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;

                // Initialize Z and C for the iteration
                ComplexNumber Z = new ComplexNumber(0, 0);
                ComplexNumber C = new ComplexNumber(realC, imagC);

                // Perform the Mandelbrot iteration
                int iterations = 0;
                while (iterations < 50 && Z.magnitudeSquared() <= 4.0) {
                    Z = Z.multiply(Z).add(C);
                    iterations++;
                }

                // Write the pixel to stdout as a binary value
                System.out.print(iterations % 2 == 0 ? "1" : "0");
            }
        }
    }

    // Helper class for complex numbers
    static class ComplexNumber {
        double real;
        double imag;

        ComplexNumber(double real, double imag) {
            this.real = real;
            this.imag = imag;
        }

        double magnitudeSquared() {
            return real * real + imag * imag;
        }

        ComplexNumber multiply(ComplexNumber other) {
            return new ComplexNumber(
                real * other.real - imag * other.imag,
                real * other.imag + imag * other.real
            );
        }

        ComplexNumber add(ComplexNumber other) {
            return new ComplexNumber(real + other.real, imag + other.imag);
        }
    }
}
