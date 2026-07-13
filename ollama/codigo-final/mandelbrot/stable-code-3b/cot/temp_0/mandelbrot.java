import java.io.*;
public class Mandelbrot {
    private static final int MAX_ITERATIONS = 50;
    private static final double ESCAPE_THRESHOLD = 4.0;
    private static final int N = 200; // Set the bitmap size here

    public static void main(String[] args) throws IOException {
        if (args.length != 1)) {
            System.out.println("Usage: java Mandelbrot <bitmap size>");
            return;
        }
        int width = N * 2 + 1;
        int height = (N * 2 + 1) / (2 * N + 1));
        File outputFile = new File("output.pbm");
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile)))) {
            writer.write("P4\n" + width + " " + height + "\n");
            double xMin = -1.5;
            double xMax = 0.5;
            double yMin = -1.0;
            double yMax = 1.0;
            int[] pixels = new int[width * height];
            for (int i = 0; i < height; i++) {
                double y = yMin + (yMax - yMin) * i / (height - 1));
                for (int j = 0; j < width; j++) {
                    double x = xMin + (xMax - xMin) * j / (width - 1));
                    Complex z = new Complex(x, y));
                    int iterations = 0;
                    while (iterations < MAX_ITERATIONS)) {
                        z = z.multiply(z).add(new Complex(x, y))));
                        double magnitude = z.getMagnitude();
                        if (magnitude > ESCAPE_THRESHOLD)) {
                            pixels[i * width + j] = 0; // Mark the point as "escaped"
                            break;
                        }
                        iterations++;
                    }
                }
            }
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    pixels[i * width + j] *= 255; // Scale the pixel color value to [0, 255] range
                }
            }
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    System.out.write(ByteBuffer.allocate(1)).put((byte) pixels[i * width + j])
                            .array());
                }
            }
        }
    }

    private static class Complex {
        private final double real;
        private final double imaginary;

        public Complex(double real, double imaginary) {
            this.real = real;
            this.imaginary = imaginary;
        }

        public Complex multiply(Complex other) {
            return new Complex(
                    this.real * other.real - this.imaginary * other.imaginary,
                    this.real * other.imaginary + this.imaginary * other.real
            );
        }

        public double getMagnitude() {
            return Math.sqrt(this.real * this.real + this.imaginary * this.imaginary));
        }
    }
}
