import java.io.PrintStream;

public class Mandelbrot {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        double lim = 4.0; // Escape threshold squared

        // Write PBM header
        System.out.println("P4");
        System.out.printf("%d %d%n", N, N);

        // Write binary pixel data
        for (int y = 0; y < N; y++) {
            int line = 0;
            for (int x = 0; x < N; x++) {
                double zx = 0.0, zy = 0.0, cx = 2.0 * x / N - 1.5, cy = 2.0 * y / N - 1.0;
                int i = 0;
                while (zx*zx + zy*zy <= lim && i < 50) {
                    double nx = zx*zx - zy*zy + cx;
                    zy = 2.0 * zx * zy + cy;
                    zx = nx;
                    i++;
                }
                line |= (i == 50 ? 1 : 0) << (7 - x % 8);
                if ((x % 8) == 7) {
                    System.out.print((char)(line & 0xFF));
                    line = 0;
                }
            }
            // Pad the last byte if necessary
            if ((N % 8) != 0) {
                System.out.print((char)(line & 0xFF));
            }
        }
    }
}
