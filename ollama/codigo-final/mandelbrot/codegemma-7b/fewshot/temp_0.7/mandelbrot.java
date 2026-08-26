import java.io.PrintStream;

public class Mandelbrot {

    private static final double lim = 2.0 * 2.0;

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Mandelbrot N");
            System.exit(1);
        }

        int N = Integer.parseInt(args[0]);

        PrintStream out = System.out;
        out.println("P4");
        out.println(N + " " + N);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                out.print(pixel(x, y));
            }
        }
    }

    private static byte pixel(int x, int y) {
        double c_real = 2.0 * x / N - 1.5;
        double c_imag = 2.0 * y / N - 1.0;

        double z_real = 0;
        double z_imag = 0;
        int iter = 0;

        while (iter < 50) {
            double z_real_squared = z_real * z_real;
            double z_imag_squared = z_imag * z_imag;

            if (z_real_squared + z_imag_squared > lim) {
                break;
            }

            double temp = z_real_squared - z_imag_squared;
            z_imag = 2 * z_real * z_imag + c_imag;
            z_real = temp + c_real;
            iter++;
        }

        return (byte) (iter << 3 | iter >> 5);
    }
}
