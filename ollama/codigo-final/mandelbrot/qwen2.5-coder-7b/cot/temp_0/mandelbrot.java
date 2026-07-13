import java.io.IOException;
import java.util.Scanner;

public class MandelbrotGenerator {
    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.out.println("Usage: java MandelbrotGenerator <N>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        double escapeThreshold = 4.0;
        int maxIterations = 50;

        // PBM P4 header
        System.out.println("P4");
        System.out.printf("%d %d\n", N, N);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double real = -1.5 + (x * 2.0 / N);
                double imag = -1.0 + (y * 2.0 / N);
                int iteration = mandelbrot(real, imag, maxIterations, escapeThreshold);

                // Write the pixel data byte-by-byte with MSB first
                if ((iteration & 0x80) != 0) {
                    System.out.print((char) 128); // Set the most significant bit
                } else {
                    System.out.print((char) 0);
                }

                iteration <<= 1;
                if ((iteration & 0x80) != 0) {
                    System.out.print((char) 64); // Set the second most significant bit
                } else {
                    System.out.print((char) 0);
                }

                iteration <<= 1;
                if ((iteration & 0x80) != 0) {
                    System.out.print((char) 32); // Set the third most significant bit
                } else {
                    System.out.print((char) 0);
                }

                iteration <<= 1;
                if ((iteration & 0x80) != 0) {
                    System.out.print((char) 16); // Set the fourth most significant bit
                } else {
                    System.out.print((char) 0);
                }
            }
        }
    }

    private static int mandelbrot(double real, double imag, int maxIterations, double escapeThreshold) {
        double zReal = 0.0;
        double zImag = 0.0;
        for (int i = 0; i < maxIterations; i++) {
            double temp = zReal * zReal - zImag * zImag + real;
            zImag = 2 * zReal * zImag + imag;
            zReal = temp;

            if (zReal * zReal + zImag * zImag > escapeThreshold) {
                return i;
            }
        }
        return maxIterations;
    }
}
