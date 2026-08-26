import java.io.IOException;
import java.util.Scanner;

public class MandelbrotGenerator {
    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.out.println("Usage: java MandelbrotGenerator <N>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        double limSquared = 2.0 * 2.0;

        // PBM P4 header
        System.out.printf("P4\n%d %d\n", N, N);

        for (int y = 0; y < N; y++) {
            int pixelRow = 0;
            for (int x = 0; x < N; x++) {
                double cr = 2.0 * x / N - 1.5;
                double ci = 2.0 * y / N - 1.0;
                double zr = 0.0, zi = 0.0;
                int iteration = 0;

                while (zr * zr + zi * zi <= limSquared && iteration < 50) {
                    double tempZr = zr * zr - zi * zi + cr;
                    zi = 2.0 * zr * zi + ci;
                    zr = tempZr;
                    iteration++;
                }

                // Set pixel color based on the number of iterations
                int color = (iteration == 50) ? 1 : 0;

                // Pack pixels into bytes
                pixelRow |= (color << ((N - x - 1) % 8));

                if ((N - x - 1) % 8 == 7 || x == N - 1) {
                    System.out.write(pixelRow);
                    pixelRow = 0;
                }
            }

            // Pad the last byte with zeros if necessary
            while (N % 8 != 0) {
                System.out.write(0);
            }
        }
    }
}
