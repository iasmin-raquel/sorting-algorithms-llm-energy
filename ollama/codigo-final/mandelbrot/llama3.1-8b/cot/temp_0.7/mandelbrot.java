import java.io.*;
import java.util.*;

public class Mandelbrot {
    public static void main(String[] args) throws Exception {
        int N = Integer.parseInt(args[0]);
        if (N % 8 != 0) {
            System.out.println("Error: N must be divisible by 8 for proper padding");
            return;
        }

        double lim = 2.0 * 2.0;

        byte[] pixels = new byte[N*N];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double cx = 2.0 * x / N - 1.5;
                double cy = 2.0 * y / N - 1.0;

                double zx = 0.0, zy = 0.0;

                for (int i = 0; i < 50; i++) {
                    double temp = zx * zx + zy * zy;
                    if (temp > lim) {
                        break;
                    }

                    double newzx = zx * zx - zy * zy + cx;
                    double newzy = 2.0 * zx * zy + cy;

                    zx = newzx;
                    zy = newzy;
                }

                int byteIndex = (x / 8) + (y / 8) * N / 8;
                int bitIndex = x % 8;

                if (i < 50) {
                    pixels[byteIndex] |= (1 << (7 - bitIndex));
                } else {
                    pixels[byteIndex] &= ~(1 << (7 - bitIndex));
                }
            }
        }

        // Output PBM header
        System.out.println("P4\n" + N + " " + N);

        // Pack pixels 8 per byte in MSB order, padding with zeros if needed
        for (int i = 0; i < pixels.length / 8; i++) {
            int index = i * 8;
            byte b = 0;

            for (int j = 7; j >= 0; j--) {
                b |= (pixels[index + j] & 1) << j;
                if ((index + j + 1) % 8 == 0 && j < 7) {
                    System.out.print((char)b);
                    b = 0;
                }
            }

            if (b != 0 || index % 8 != 0) {
                System.out.println((char)b);
            }
        }
    }
}
