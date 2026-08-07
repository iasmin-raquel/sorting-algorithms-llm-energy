import java.io.OutputStream;
import java.util.BitSet;

public class MandelbrotPBM {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]); // Get the value of N from command-line arguments
        BitSet image = new BitSet(N * N); // Create a bitset to store the pixel data
        double limSquared = 2.0 * 2.0; // Set the escape threshold squared

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double cx = 2.0 * x / N - 1.5; // Calculate real part of C
                double cy = 2.0 * y / N - 1.0; // Calculate imaginary part of C
                double zx = 0, zy = 0; // Initialize Z to (0, 0)
                int iter = 0;

                while (zx * zx + zy * zy <= limSquared && iter < 50) {
                    double newZx = zx * zx - zy * zy + cx; // Update real part of Z
                    zy = 2.0 * zx * zy + cy; // Update imaginary part of Z
                    zx = newZx; // Move to the next iteration
                    iter++;
                }

                if (iter == 50) {
                    image.set(y * N + x); // Set the pixel to black if in the set
                }
            }
        }

        // Output the PBM P4 format
        System.out.print("P4\n" + N + " " + N + "\n");
        for (int i = 0; i < image.length(); i += 8) {
            int byteValue = 0;
            for (int j = 0; j < 8 && i + j < image.length(); j++) {
                if (image.get(i + j)) {
                    byteValue |= (1 << (7 - j));
                }
            }
            System.out.write(byteValue);
        }
    }
}
