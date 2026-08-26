import java.io.PrintStream;
import java.util.Scanner;

public class MandelbrotSet {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java MandelbrotSet N");
            return;
        }

        int N = Integer.parseInt(args[0]);
        double limSquared = 2.0 * 2.0; // Escape threshold squared
        int maxIterations = 50;

        // PBM P4 header
        System.out.println("P4");
        System.out.println(N + " " + N);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;
                double zr = 0.0, zi = 0.0;
                boolean belongsToSet = true;

                for (int i = 0; i < maxIterations && belongsToSet; i++) {
                    double tempZr = zr * zr - zi * zi + realC;
                    zi = 2.0 * zr * zi + imagC;
                    zr = tempZr;
                    if (zr * zr + zi * zi > limSquared) {
                        belongsToSet = false;
                    }
                }

                // Write pixel data as binary, considering PBM P4 format
                if (belongsToSet) {
                    System.out.print("\x00"); // Black pixel
                } else {
                    System.out.print("\xFF"); // White pixel
                }
            }
        }
    }
}
