import java.io.OutputStream;
import java.io.PrintStream;

public class Mandelbrot {
    public static void main(String[] args) throws Exception {
        int N = Integer.parseInt(args[0]);
        int iterations = 50;
        double lim = 2.0 * 2.0;

        // Validate against reference.pbm for N=200
        if (N == 200) {
            System.out.println("Validating output...");
            compareOutput(N);
        }

        PrintStream out = new PrintStream(System.out);

        // Output PBM P4 header
        out.print("P4\n");
        out.printf("%d %d\n", N, N);
        out.printf("%d\n", 8); // bits per pixel

        int[] pixels = new int[N * N];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;

                int zr = 0, zi = 0;
                for (int i = 0; i < iterations && zr * zr + zi * zi <= lim; i++) {
                    double temp = zr * zr + zi * zi;
                    if (temp > lim) break;
                    double newZi = realC * zr - imagC * zi;
                    zi = newZi;
                    zr = temp;
                }

                pixels[y * N + x] = (zr * zr + zi * zi <= lim ? 1 : 0);
            }
        }

        // Output binary pixel data
        int bytesPerRow = (N + 7) / 8; // Pad with zeros if N not divisible by 8
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < bytesPerRow; x++) {
                int byteValue = 0;
                for (int i = 0; i < 8 && y * N + x + i < N * N; i++) {
                    byteValue |= pixels[y * N + x + i] << (7 - i);
                }
                out.print(byteValue & 0xFF); // MSB first
            }
            out.println();
        }

        System.out.flush();
    }

    private static void compareOutput(int N) throws Exception {
        Process process = Runtime.getRuntime().exec("cmp output.pbm reference.pbm");
        int exitCode = process.waitFor();
        if (exitCode != 0) {
            throw new RuntimeException("Validation failed: cmp returned non-zero exit code " + exitCode);
        }
    }
}
