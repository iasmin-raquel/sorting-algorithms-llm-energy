import java.util.Scanner;

public class Mandelbrot {

    private static int MAX_ITERATIONS = 50;
    private static double ESCAPE_THRESHOLD = 4.0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in));
        System.out.print("Enter the size (N) of the bitmap: ");
        int N = Integer.parseInt(scanner.nextLine()));

        double stepX = 2.0 / N;
        double stepY = 2.0 / N;

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;

                double zr = 0.0;
                double zi = 0.0;

                int iterationCount = 0;

                while (iterationCount < MAX_ITERATIONS) {
                    double zrSquared = zr * zr;
                    double ziSquared = zi * zi;

                    if (zrSquared + ziSquared > ESCAPE_THRESHOLD * ESCAPE_THRESHOLD)) {
                        break;
                    }

                    double newZr = zr * zr - zi * zi + realC;
                    double newZi = 2.0 * zr * zi + imagC;

                    zr = newZr;
                    zi = newZi;

                    iterationCount++;
                }

                int pixelValue = (int) ((1.0 / Math.sqrt(2)) * Math.sqrt(zr * zr + zi * zi))) > 4.0 ? 0 : 1;

                System.out.print(pixelValue);
            }
        }
    }
}
