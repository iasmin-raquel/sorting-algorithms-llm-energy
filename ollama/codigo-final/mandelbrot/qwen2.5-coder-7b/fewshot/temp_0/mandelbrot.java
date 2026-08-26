public class Mandelbrot {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        double lim = 2.0 * 2.0;
        System.out.println("P4");
        System.out.printf("%d %d\n", N, N);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                double cr = 2.0 * x / N - 1.5;
                double ci = 2.0 * y / N - 1.0;
                double zr = 0.0, zi = 0.0;
                boolean inSet = true;

                for (int i = 0; i < 50 && inSet; i++) {
                    double zr2 = zr * zr;
                    double zi2 = zi * zi;
                    if (zr2 + zi2 > lim) {
                        inSet = false;
                    } else {
                        zi = 2.0 * zr * zi + ci;
                        zr = zr2 - zi2 + cr;
                    }
                }

                System.out.print(inSet ? "\x01" : "\x00");
            }
        }
    }
}
