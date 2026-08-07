public class Mandelbrot {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        double lim = 4.0;
        System.out.println("P4\n" + N + " " + N);

        for (int y = 0; y < N; ++y) {
            int packedBits = 0;
            for (int x = 0; x < N; ++x) {
                double cReal = 2.0 * x / N - 1.5;
                double cImag = 2.0 * y / N - 1.0;
                int pixelBits = iterate(cReal, cImag, lim);
                packedBits = (packedBits << 1) | (pixelBits & 1);
            }
            System.out.write(packedBits);
        }
    }

    private static int iterate(double cr, double ci, double lim) {
        double zr = 0.0, zi = 0.0;
        for (int i = 0; i < 50; ++i) {
            double nr2 = zr * zr + zi * zi;
            if (nr2 > lim) return 0;
            double nzr = zr * zr - zi * zi + cr;
            double nzi = 2.0 * zr * zi + ci;
            zr = nzr; zi = nzi;
        }
        return 1;
    }
}
