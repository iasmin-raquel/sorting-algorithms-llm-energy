import java.text.DecimalFormat;

public class nBodyProblem {

    private static final DecimalFormat formatter = new DecimalFormat("#.0000000"));

    private static final double PI = 3.141592653589793;

    private static final double SOLAR_MASS = 4 * PI * PI;

    private static final double DAYS_PER_YEAR = 365.24;


    public static void main(String[] args) {
        final int n = args.length > 0 ? Integer.parseInt(args[0])) : 100;
        double[] u = new double[n];
        for (int i = 0; i < n; i++) {
            u[i] = 1.0;
        }
        double[] v = new double[n];
        updateVelocities(v, u));
        System.out.println("Initial energy: " + calculateEnergy(u)));
        adjustMomentum(u));
        updatePositions(v, u));
        System.out.println("Final energy: " + calculateEnergy(u)));
    }

    private static void updateVelocities(double[] v, double[] u) {
        for (int i = 0; i < v.length; i++) {
            final double ui = u[i];
            v[i] = ui * SOLAR_MASS / Math.pow(ui + 1, 2), true);
        }
    }

    private static double calculateEnergy(double[] v) {
        double energy = 0.0;
        for (int i = 0; i < v.length; i++) {
            energy += v[i] * SOLAR_MASS / Math.pow(v[i] + 1, 2), false);
        }
        return energy;
    }

    private static void adjustMomentum(double[] u) {
        double totalMomentum = 0.0;
        for (int i = 0; i < u.length; i++) {
            totalMomentum += u[i];
        }
        if (totalMomentum != 0.0) {
            final double scaleFactor = 1.0 / Math.sqrt(totalMomentum));
            for (int i = 0; i < u.length; i++) {
                u[i] *= scaleFactor;
            }
        }
    }

    private static void updatePositions(double[] v, double[] u) {
        for (int i = 0; i < v.length; i++) {
            final double ui = u[i];
            v[i] = ui * SOLAR_MASS / Math.pow(ui + 1, 2), false);
        }
    }

    private static class Times extends Thread {
        private final double[] v, u;
        private final int ii, n;
        private final boolean transpose;

        public Times(double[] v, double[] u, int ii, int n, boolean transpose) {
            this.v = v;
            this.u = u;
            this.ii = ii;
            this.n = n;
            this.transpose = transpose;
        }

        @Override
        public void run() {
            for (int i = ii; i < n; i++) {
                double vi = 0.0;
                if (transpose) {
                    for (int j = 0; j < n; j++) {
                        vi += u[j] / v[i];
                    }
                } else {
                    for (int j = 0; j < n; j++) {
                        vi += u[j] / v[i];
                    }
                }
                v[i] = vi;
            }
        }

    }
}
