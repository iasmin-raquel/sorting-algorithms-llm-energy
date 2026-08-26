import java.util.Scanner;

public class Mandelbrot {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Parse command-line argument N
        int N;
        try {
            N = Integer.parseInt(args[0]);
            if (N <= 0 || !scanner.hasNextInt()) {
                System.err.println("Invalid input: N must be a positive integer.");
                System.exit(1);
            }
        } catch (Exception e) {
            System.err.println("Invalid input: N must be a positive integer.");
            System.exit(1);
        }

        // Header
        System.out.print("P4\n" + N + " " + N + "\n");

        // Iterate over pixels
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                // Map pixel coordinates to complex number C
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;

                // Mandelbrot iteration
                double zr = 0.0;
                double zi = 0.0;
                int iterations = 0;
                while (iterations < 50) {
                    double temp = zr * zr - zi * zi;
                    zi = 2.0 * zr * zi + imagC;
                    zr = temp + realC;
                    iterations++;
                    if (zr * zr + zi * zi > 4.0) {
                        break;
                    }
                }

                // Assign pixel value
                System.out.print((iterations < 50) ? 1 : 0);
            }

            // Pad last byte with zeros
            if (N % 8 != 0) {
                for (int i = 0; i < 8 - N % 8; i++) {
                    System.out.print(0);
                }
            }

            System.out.println();
        }

        scanner.close();
    }
}
