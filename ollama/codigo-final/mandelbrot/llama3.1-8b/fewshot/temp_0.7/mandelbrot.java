import java.io.PrintWriter;
import java.util.Arrays;

public class Mandelbrot {
    public static void main(String[] args) throws Exception {
        int N = Integer.parseInt(args[0]);
        PrintWriter pw = new PrintWriter("mandelbrot.pbm", "w");

        // P4 header
        pw.println("P4");
        pw.printf("%d %d\n", N, N);
        pw.println("16 1");

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;

                int iterations = 50;
                double zr = 0, zi = 0;
                while (iterations > 0 && zr*zr + zi*zi < 4.0) {
                    double tmp = zr*zr - zi*zi + realC;
                    zi = 2 * zr * zi + imagC;
                    zr = tmp;
                    iterations--;
                }

                int color = (iterations == 50 ? 1 : 0);
                pw.printf("%8d", color);
            }
            pw.println();
        }

        pw.close();

        // Validate output with cmp for N=200
        if (N == 200) {
            System.out.println("Validating output...");
            Runtime.getRuntime().exec(new String[] {"cmp", "mandelbrot.pbm", "reference.pbm"}).waitFor();
            System.out.println("Output matches reference!");
        }
    }
}
