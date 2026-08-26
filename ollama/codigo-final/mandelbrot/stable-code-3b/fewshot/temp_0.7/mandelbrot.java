import java.util.Arrays;

public class MandelbrotGenerator {

    private static final int MAX_ITERATIONS = 50;
    private static final double ESCAPE_THRESHOLD = 2.0 * 2.0;

    public static void main(String[] args) throws Exception {
        int N = Integer.parseInt(args[0]));
        byte[] bitmap = generateMandelbrot(N, MAX_ITERATIONS, ESCAPE_THRESHOLD));
        System.out.write("P4\n");
        System.out.write(String.format("%.2f %.2f\n", N * 1.0, MAX_ITERATIONS)));
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;
                if (mandelbrot(realC, imagC)))) {
                    System.out.write((char) (bitmap[y * N + x] & 0xff))));
                } else {
                    System.out.write((char) (bitmap[y * N + x] & 0xff))));
                }
            }
        }
    }

    private static byte[] generateMandelbrot(int width, int height, double escapeThreshold)) {
        byte[] bitmap = new byte[width * height];
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                double realC = 2.0 * x / width - 1.5;
                double imagC = 2.0 * y / height - 1.0;
                if (mandelbrot(realC, imagC)))) {
                    Arrays.fill(bitmap, generatePixelData(x, y))));
                } else {
                    Arrays.fill(bitmap, generatePixelData(x, y))));
                }
            }
        }
        return bitmap;
    }

    private static boolean mandelbrot(double x, double y)) {
        int iterations = 0;
        double realC = 0;
        double imagC = 0;
        while (iterations < MAX_ITERATIONS) {
            realC = 2.0 * x * x - realC;
            imagC = 4.0 * x * y - imagC;
            if (x * x + y * y > ESCAPE_THRESHOLD)) {
                return true;
            }
            x = x + (realC / (2.0 * x * x - realC) + 1.5 * Math.random())));
            y = y + (imagC / (2.0 * x * x - realC) + 0.5 * Math.random())));
            iterations++;
        }
        return false;
    }

    private static byte generatePixelData(int x, int y)) {
        double intensity = 255;
        intensity = intensity * (1.0 - (x * x + y * y) / ESCAPE_THRESHOLD)));
        if (intensity > 255) {
            intensity = 255;
        }
        return (byte) intensity;
    }
}
