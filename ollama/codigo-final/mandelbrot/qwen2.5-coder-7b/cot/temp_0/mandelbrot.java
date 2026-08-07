import java.io.IOException;
import java.util.Scanner;

public class MandelbrotSet {
    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.out.println("Usage: java MandelbrotSet <N>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        double limSquared = 2.0 * 2.0;

        // PBM P4 header
        System.out.printf("P4\n%d %d\n", N, N);

        for (int y = 0; y < N; y++) {
            int pixel = 0;
            int bitIndex = 7;

            for (int x = 0; x < N; x++) {
                double cr = 2.0 * x / N - 1.5;
                double ci = 2.0 * y / N - 1.0;
                double zr = 0.0, zi = 0.0;

                for (int i = 0; i < 50; i++) {
                    double zrSquared = zr * zr;
                    double ziSquared = zi * zi;
                    if (zrSquared + ziSquared > limSquared) break;
                    zi = 2 * zr * zi + ci;
                    zr = zrSquared - ziSquared + cr;
                }

                // Set bit based on whether the point is in the set
                pixel |= (i == 50 ? 1 : 0) << bitIndex;

                // Move to next bit or start new byte if necessary
                if (--bitIndex < 0) {
                    System.out.write(pixel);
                    pixel = 0;
                    bitIndex = 7;
                }
            }

            // Write any remaining bits in the last byte
            if (bitIndex != 7) {
                System.out.write(pixel << (8 - bitIndex));
            }
        }
    }
}
