import java.util.Arrays;

public class Mandelbrot {

    private static final double lim = 2.0 * 2.0;
    private static final int MAX_ITERATIONS = 50;

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);

        byte[] pixels = generateMandelbrot(N);

        // P4 header
        System.out.println("P4");
        System.out.println(N + " " + N);

        // Pixel data
        System.out.print(Arrays.toString(pixels).replace("[", "").replace("]", ""));
    }

    private static byte[] generateMandelbrot(int N) {
        byte[] pixels = new byte[(N * N + 7) / 8];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double C = complex(x, y, N);
                int iterations = mandelbrot(C);
                pixels[x / 8 + y * N / 8] |= (byte) (iterations << (7 - x % 8));
            }
        }

        return pixels;
    }

    private static double complex(int x, int y, int N) {
        return 2.0 * x / N - 1.5 + (2.0 * y / N - 1.0) * 1.0i;
    }

    private static int mandelbrot(double C) {
        double Z = 0 + 0i;
        for (int i = 0; i < MAX_ITERATIONS; i++) {
            Z = Z * Z + C;
            if (Math.abs(Z) * Math.abs(Z) > lim) {
                return i;
            }
        }
        return 0;
    }
}
