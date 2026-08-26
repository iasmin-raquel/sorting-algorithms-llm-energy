import java.io.*;

public class Mandelbrot {
    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.out.println("Usage: java Mandelbrot N");
            return;
        }

        int N = Integer.parseInt(args[0]);
        double limSquared = 4.0; // Escape threshold squared
        int maxIterations = 50;

        // Output PBM header
        System.out.println("P4\n" + N + " " + N);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double zr = 0, zi = 0;
                double cr = 2.0 * x / N - 1.5;
                double ci = 2.0 * y / N - 1.0;

                int iter;
                for (iter = 0; iter < maxIterations && (zr*zr + zi*zi <= limSquared); iter++) {
                    double zrNew = zr*zr - zi*zi + cr;
                    zi = 2.0 * zr * zi + ci;
                    zr = zrNew;
                }

                // Write the pixel data
                if (iter == maxIterations) {
                    System.out.print((char)0); // Bit set, pixel belongs to the set
                } else {
                    System.out.print((char)128); // Bit cleared, pixel not in the set
                }
            }

            // Pad with zeros if N is not divisible by 8
            for (int i = 0; i < (N % 8); i++) {
                System.out.print((char)0);
            }
        }
    }
}
