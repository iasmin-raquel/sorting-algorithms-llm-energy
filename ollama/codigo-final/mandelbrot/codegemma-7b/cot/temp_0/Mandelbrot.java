import java.io.PrintStream;

public class Mandelbrot {

    private static final int MAX_ITERATIONS = 50;
    private static final double ESCAPE_THRESHOLD = 4.0;

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);

        boolean[][] pixels = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                pixels[i][j] = isInMandelbrot(mapPixelToComplex(i, j, N));
            }
        }

        printPbmP4(pixels, N);
    }

    private static boolean isInMandelbrot(Complex c) {
        Complex z = new Complex(0, 0);

        for (int i = 0; i < MAX_ITERATIONS; i++) {
            z = z.square().add(c);
            if (z.magnitude() > ESCAPE_THRESHOLD) {
                return false;
            }
        }

        return true;
    }

    private static Complex mapPixelToComplex(int i, int j, int N) {
        double x = -1.5 + (0.75 * i) / N;
        double y = -1.0 + (2.0 * j) / N;
        return new Complex(x, y);
    }

    private static void printPbmP4(boolean[][] pixels, int N) {
        PrintStream out = System.out;

        out.println("P4");
        out.println(N + " " + N);

        for (int i = 0; i < N; i++) {
            int bits = 0;
            for (int j = 0; j < N; j++) {
                bits |= (pixels[i][j] ? 1 : 0) << (N - j - 1);
                if (j == N - 1) {
                    out.print(bits);
                }
            }
            out.println();
        }
    }

    private static class Complex {
        private double real;
        private double imag;

        public Complex(double real, double imag) {
            this.real = real;
            this.imag = imag;
        }

        public Complex square() {
            return new Complex(real * real - imag * imag, 2 * real * imag);
        }

        public Complex add(Complex c) {
            return new Complex(real + c.real, imag + c.imag);
        }

        public double magnitude() {
            return Math.sqrt(real * real + imag * imag);
        }
    }
}
