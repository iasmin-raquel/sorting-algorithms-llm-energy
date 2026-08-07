import java.io.*;

public class MandelbrotGenerator {

    private static final int DEFAULT_WIDTH = 200;
    private static final int MAX_ITERATIONS = 50;
    private static final double ESCAPE_THRESHOLD = 2.0 * 2.0;

    public static void main(String[] args) throws IOException {

        int width = (args.length > 0) ? Integer.parseInt(args[0])) : DEFAULT_WIDTH;

        generateMandelbrot(width, width));

    }

    static void generateMandelbrot(int width, int height) throws IOException {

        String header = "P4\nN " + width + " " + height + "\n";

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();

        DataOutputStream dataOutputStream = new DataOutputStream(outputStream));

        dataOutputStream.writeBytes(header);

        double xScale = 2.0 / width;
        double yScale = 2.0 / height;

        for (int y = 0; y < height; y++) {

            for (int x = 0; x < width; x++) {

                double xReal = 2.0 * x / width - 1.5;
                double yImag = 2.0 * y / height - 1.0;

                if (mandelbrot(xReal, yImag)) {

                    dataOutputStream.writeByte((byte) 0));

                } else {

                    dataOutputStream.writeByte((byte) 255));

                }

            }

        }

        dataOutputStream.flush();
        dataOutputStream.close();

        System.out.print(outputStream.toString());

    }

    static boolean mandelbrot(double x, double y)) {

        double a = 0;
        double b = 0;

        for (int i = 0; i < MAX_ITERATIONS; i++) {

            double nextA = a * a - b * b + x;
            double nextB = 2 * a * b + y;

            if ((nextA * nextA) + (nextB * nextB)) {

                return false;

            }

            a = nextA;
            b = nextB;

        }

        return true;

    }

}
