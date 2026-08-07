import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Mandelbrot {
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(args[0]);
        BufferedImage image = new BufferedImage(N, N, BufferedImage.TYPE_BYTE_GRAY);
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double realC = 2.0 * x / N - 1.5;
                double imagC = 2.0 * y / N - 1.0;
                double zReal = 0, zImag = 0;
                int iterations = 50;
                while (iterations-- > 0) {
                    double temp = zReal * zReal - zImag * zImag + realC;
                    zImag = 2 * zReal * zImag + imagC;
                    zReal = temp;
                    if (zReal * zReal + zImag * zImag > 4.0) {
                        image.setRGB(x, y, (iterations == 50 ? 0 : 1) << 7);
                        break;
                    }
                }
            }
        }
        byte[] pixels = ((DataBufferByte) image.getRaster().getDataBuffer()).getData();
        StringBuilder sb = new StringBuilder("P4\n" + N + " " + N + "\n");
        for (int i = 0; i < pixels.length; i++) {
            if ((i % 8 == 0 && i != 0)) {
                sb.append("\n");
            }
            sb.append(String.format("%8s", Integer.toBinaryString(pixels[i] & 255)).replace(' ', '0'));
        }
        File outputFile = new File("output.pbm");
        java.io.FileWriter writer = new java.io.FileWriter(outputFile);
        writer.write(sb.toString());
        writer.close();
    }
}
