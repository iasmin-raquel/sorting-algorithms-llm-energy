import java.io.OutputStreamWriter;
import java.io.BufferedOutputStream;

public class Mandelbrot {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Mandelbrot <N>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        double realMin = -1.5, realMax = 0.5;
        double imagMin = -1.0, imagMax = 1.0;
        int maxIterations = 50;
        double escapeThreshold = 4.0;

        // PBM header
        System.out.println("P4");
        System.out.print(N + " " + N + "\n");

        try (OutputStreamWriter writer = new OutputStreamWriter(new BufferedOutputStream(System.out))) {
            for (int y = 0; y < N; y++) {
                double imag = imagMin + y * (imagMax - imagMin) / N;
                for (int x = 0; x < N; x++) {
                    double real = realMin + x * (realMax - realMin) / N;
                    if (isInMandelbrot(real, imag, maxIterations, escapeThreshold)) {
                        writer.write('0');
                    } else {
                        writer.write('1');
                    }
                }
                // Pad with zeros to make each row a multiple of 8 bits
                for (int i = (N + 7) / 8 * 8 - N; i > 0; i--) {
                    writer.write('0');
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static boolean isInMandelbrot(double real, double imag, int maxIterations, double escapeThreshold) {
        double zReal = 0.0;
        double zImag = 0.0;
        for (int i = 0; i < maxIterations; i++) {
            double newZReal = zReal * zReal - zImag * zImag + real;
            double newZImag = 2 * zReal * zImag + imag;
            if (newZReal * newZReal + newZImag * newZImag > escapeThreshold) {
                return false;
            }
            zReal = newZReal;
            zImag = newZImag;
        }
        return true;
    }
}
