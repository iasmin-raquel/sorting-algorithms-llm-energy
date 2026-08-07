import java.io.*;
import java.util.*;

public class Mandelbrot {
    public static void main(String[] args) throws Exception {
        int N = Integer.parseInt(args[0]);
        if (N % 8 != 0) {
            System.out.println("Error: N must be divisible by 8.");
            return;
        }

        int maxIterations = 50;
        double threshold = 4.0;

        BufferedImage img = new BufferedImage(N, N, BufferedImage.TYPE_INT_RGB);
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;
                int iterationCount = computeMandelbrot(realC, imagC);
                Color color = getColor(iterationCount, maxIterations, threshold);
                img.setRGB(x, y, color.getRGB());
            }
        }

        File outputFile = new File("output.pbm");
        try (BufferedImageIOHandler writer = new BufferedImageIOHandler(outputFile)) {
            writer.write(img);
        } catch (IOException e) {
            System.err.println("Error writing output file: " + e.getMessage());
        }
    }

    private static int computeMandelbrot(double realC, double imagC) {
        double zr = 0.0;
        double zi = 0.0;

        for (int iteration = 0; iteration < 50; iteration++) {
            double newZr = zr * zr - zi * zi + realC;
            double newZi = 2 * zr * zi + imagC;
            if ((newZr * newZr + newZi * newZi) > threshold * threshold) {
                return iteration;
            }
            zr = newZr;
            zi = newZi;
        }

        return maxIterations - 1; // escape at last iteration
    }

    private static Color getColor(int iterationCount, int maxIterations, double threshold) {
        int red = (iterationCount * 255 / maxIterations);
        int green = (iterationCount * 255 / maxIterations);
        int blue = (iterationCount * 255 / maxIterations);

        return new Color(red, green, blue);
    }

    private static class BufferedImageIOHandler implements AutoCloseable {
        private final File outputFile;
        private final DataOutputStream out;

        public BufferedImageIOHandler(File outputFile) throws IOException {
            this.outputFile = outputFile;
            try (DataOutputStream tmpOut = new DataOutputStream(new FileOutputStream(outputFile))) {
                tmpOut.writeBytes("P4\n");
                tmpOut.writeBytes(N + " " + N + "\n");

                for (int y = 0; y < N / 8; y++) {
                    byte[] rowBuffer = new byte[8 * N];
                    int offset = y * 8;
                    for (int x = 0; x < N / 8; x++) {
                        int pixelValue = img.getRGB(x * 8, offset);
                        rowBuffer[x * 8] = (byte) ((pixelValue >> 24) & 0xFF);
                        rowBuffer[(x * 8) + 1] = (byte) ((pixelValue >> 16) & 0xFF);
                        rowBuffer[(x * 8) + 2] = (byte) ((pixelValue >> 8) & 0xFF);
                        rowBuffer[(x * 8) + 3] = (byte) (pixelValue & 0xFF);
                    }
                    tmpOut.write(rowBuffer);
                }

                if (N % 8 != 0) {
                    byte[] padding = new byte[8 - (N % 8)];
                    for (int i = 0; i < padding.length; i++) {
                        padding[i] = 0;
                    }
                    tmpOut.write(padding);
                }
            } catch (IOException e) {
                System.err.println("Error writing output file: " + e.getMessage());
            }
        }

        public void write(BufferedImage img) throws IOException {
            // Not implemented, as the BufferedImageIOHandler is already doing the work
        }

        @Override
        public void close() throws Exception {
            if (out != null) {
                out.close();
            }
        }
    }
}
