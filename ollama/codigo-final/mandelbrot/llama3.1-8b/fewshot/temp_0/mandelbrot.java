import java.io.OutputStream;
import java.io.PrintStream;

public class Mandelbrot {
    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(args[0]);
        int iterations = 50;
        double lim = 2.0 * 2.0;

        // Validate against reference.pbm for N=200
        if (n == 200) {
            System.out.println("Validating output...");
            compareOutput(n);
        }

        PrintStream out = new PrintStream(System.out);

        // Output PBM P4 header
        out.print("P4\n");
        out.printf("%d %d\n", n, n);
        out.print("8\n");

        int[] pixels = new int[n * n];

        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                double realC = 2.0 * x / n - 1.5;
                double imagC = 2.0 * y / n - 1.0;

                int zr = 0, zi = 0;
                for (int i = 0; i < iterations && zr * zr + zi * zi <= lim; i++) {
                    double temp = zr * zr + zi * zi;
                    if (temp > lim) break;
                    double newZi = realC * zr - imagC * zi;
                    zi = newZi;
                    zr = temp;
                }

                pixels[y * n + x] = zr * zr + zi * zi <= lim ? 1 : 0;
            }
        }

        // Pad with zeros if N not divisible by 8
        int padding = (n % 8 == 0) ? 0 : 8 - (n % 8);
        for (int i = n * n; i < n * n + padding; i++) {
            pixels[i] = 0;
        }

        // Output binary pixel data
        byte[] bytes = new byte[(n * n + padding) / 8];
        for (int i = 0; i < pixels.length; i += 8) {
            int byteValue = 0;
            for (int j = 0; j < 8 && i + j < pixels.length; j++) {
                byteValue |= (pixels[i + j] << j);
            }
            bytes[(i / 8)] = (byte) byteValue;
        }

        out.write(bytes);

        // Validate output
        if (n == 200) {
            System.out.println("Validation complete.");
        }
    }

    private static void compareOutput(int n) throws Exception {
        Process process = Runtime.getRuntime().exec(new String[] {"cmp", "output.pbm", "reference.pbm"});
        int exitCode = process.waitFor();
        if (exitCode != 0) {
            throw new RuntimeException("Validation failed.");
        }
    }
}
