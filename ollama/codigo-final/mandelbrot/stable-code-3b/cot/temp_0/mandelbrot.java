import java.util.Scanner;

public class Mandelbrot {

    private static final int MAX_ITERATIONS = 50;
    private static final double ESCAPE_THRESHOLD = 2.0 * 2.0;

    public static void main(String[] args) {
        
        // Read N from command-line argument
        Scanner scanner = new Scanner(System.in));
        int N = scanner.nextInt();
        scanner.close();
        
        // Generate Mandelbrot set bitmap
        double xScale = 2.0 / N;
        double yScale = 2.0 / N;
        double xOffset = -1.5;
        double yOffset = -1.0;
        int[] pixels = generateMandelbrotSet(N, xScale, yScale, xOffset, yOffset));
        
        // Output the bitmap in PBM P4 format
        System.out.println("P4");
        System.out.printf("%d %d%n", N, N));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int pixelValue = pixels[i * N + j]];
                System.out.print(pixelValue > ESCAPE_THRESHOLD ? "1" : "0"));
            }
            System.out.println();
        }
    }

    private static int[] generateMandelbrotSet(int N, double xScale, double yScale, double xOffset, double yOffset)) {
        
        // Initialize the pixels array with 0s
        int[] pixels = new int[N * N]];
        for (int i = 0; i < N * N; i++) {
            pixels[i] = 0;
        }
        
        // Calculate Mandelbrot set for each pixel
        double x, y;
        int iterationCount;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                x = xScale * (i + 1) / N - xOffset;
                y = yScale * (j + 1) / N - yOffset;
                iterationCount = mandelbrotIterations(x, y));
                if (iterationCount >= MAX_ITERATIONS || iterationCount <= 0)) {
                    pixels[i * N + j]] = 1;
                }
            }
        }
        
        return pixels;
    }

    private static int mandelbrotIterations(double x, double y)) {
        int iterationCount = 0;
        double zr = 0.0;
        double zi = 0.0;
        while (zr * zr + zi * zi <= ESCAPE_THRESHOLD && iterationCount < MAX_ITERATIONS)) {
            double zrTemp = zr * zr - zi * zi + x;
            double ziTemp = 2.0 * zr * zi / N + y;
            zr = zrTemp;
            zi = ziTemp;
            iterationCount++;
        }
        return iterationCount;
    }

    private static int[] generateReferenceBitmap(int N)) {
        // Generate a reference bitmap for validation purposes
        int[] pixels = new int[N * N]];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                pixels[i * N + j]] = 1; // Set to any non-zero value for validation purposes
            }
        }
        return pixels;
    }

    private static boolean validateBitmap(int[] generatedPixels, int[] referencePixels)) {
        // Validate the generated bitmap against a reference bitmap
        boolean isValid = true;
        for (int i = 0; i < generatedPixels.length && isValid; i++) {
            if (generatedPixels[i]] != referencePixels[i]) {
                isValid = false;
            }
        }
        return isValid;
    }

    private static void printUsage() {
        System.out.println("Usage: java Mandelbrot <N>");
        System.exit(1);
    }

    public static void main(String[] args)) {
        if (args.length != 1)) {
            printUsage();
        }
        int N = Integer.parseInt(args[0]));
        if (N <= 0 || N > 200)) {
            System.out.println("Error: N must be a positive integer less than or equal to 200."));
            System.exit(1);
        }
        int[] generatedPixels = generateMandelbrotSet(N, xScale, yScale, xOffset, yOffset));
        int[] referencePixels = generateReferenceBitmap(N));
        boolean isValid = validateBitmap(generatedPixels, referencePixels));
        if (isValid)) {
            System.out.println("The generated bitmap is validatable against a reference bitmap.");
        } else {
            System.out.println("Error: The generated bitmap is not validatable against the reference bitmap.");
            System.exit(1);
        }
    }
}
