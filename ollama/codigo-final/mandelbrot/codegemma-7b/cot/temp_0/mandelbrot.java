import java.util.Scanner;

public class Mandelbrot {

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        int lim = 4;
        int maxIterations = 50;

        System.out.println("P4\n" + N + " " + N);

        for (int y = 0; y < N; y++) {
            byte row = 0;
            for (int x = 0; x < N; x++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;
                double realZ = 0;
                double imagZ = 0;
                int iterations = 0;

                while (iterations < maxIterations) {
                    double realTemp = realZ * realZ - imagZ * imagZ;
                    imagZ = 2 * realZ * imagZ + imagC;
                    realZ = realTemp + realC;
                    iterations++;

                    if (realZ * realZ + imagZ * imagZ > lim) {
                        break;
                    }
                }

                row |= (iterations < maxIterations) ? (1 << (7 - x % 8)) : 0;
                if (x % 8 == 7) {
                    System.out.print(row);
                }
            }

            if (N % 8 != 0 && x == N - 1) {
                System.out.print(row);
            }
        }
    }
}
