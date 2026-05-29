public class NBody {
    static final double PI = 3.141592653589793;
    static final double SOLAR_MASS = 4.0 * PI * PI;
    static final double DAYS_PER_YEAR = 365.24;
    static final double DT = 0.01;

    static class Body {
        double x, y, z;
        double vx, vy, vz;
        double mass;

        Body(double x, double y, double z, double vx, double vy, double vz, double mass) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.vx = vx;
            this.vy = vy;
            this.vz = vz;
            this.mass = mass;
        }
    }

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);

        Body[] bodies = new Body[5];

        // Sun
        bodies[0] = new Body(
                0.0, 0.0, 0.0,
                0.0, 0.0, 0.0,
                SOLAR_MASS
        );

        // Jupiter
        bodies[1] = new Body(
                4.84143144246472090e+00, -1.16032004402742839e+00, -1.03622044471123109e-01,
                1.66007664274403694e-03 * DAYS_PER_YEAR,
                7.69901118419740425e-03 * DAYS_PER_YEAR,
                -6.90460016972063023e-05 * DAYS_PER_YEAR,
                9.54791938424326609e-04 * SOLAR_MASS
        );

        // Saturn
        bodies[2] = new Body(
                8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01,
                -2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR,
                2.85885980666130812e-04 * SOLAR_MASS
        );

        // Uranus
        bodies[3] = new Body(
                1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01,
                2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR,
                4.36624404335156298e-05 * SOLAR_MASS
        );

        // Neptune
        bodies[4] = new Body(
                1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01,
                2.68067772490389322e-03 * DAYS_PER_YEAR,
                1.62824170038242295e-03 * DAYS_PER_YEAR,
                -9.51592254519715870e-05 * DAYS_PER_YEAR,
                5.15138902046611451e-05 * SOLAR_MASS
        );

        double initialEnergy = computeEnergy(bodies);
        System.out.printf("%.9f\n", initialEnergy);

        for (int i = 0; i < N; i++) {
            // Compute acceleration
            double[] ax = new double[5];
            double[] ay = new double[5];
            double[] az = new double[5];

            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    if (j != k) {
                        double dx = bodies[j].x - bodies[k].x;
                        double dy = bodies[j].y - bodies[k].y;
                        double dz = bodies[j].z - bodies[k].z;
                        double dist = dx * dx + dy * dy + dz * dz;
                        double mag = 1.0 / (Math.sqrt(dist) * dist);
                        double factor = bodies[k].mass * mag;

                        ax[j] += factor * dx;
                        ay[j] += factor * dy;
                        az[j] += factor * dz;
                    }
                }
            }

            // Update velocities and positions
            for (int j = 0; j < 5; j++) {
                bodies[j].vx += ax[j] * DT;
                bodies[j].vy += ay[j] * DT;
                bodies[j].vz += az[j] * DT;

                bodies[j].x += bodies[j].vx * DT;
                bodies[j].y += bodies[j].vy * DT;
                bodies[j].z += bodies[j].vz * DT;
            }
        }

        double finalEnergy = computeEnergy(bodies);
        System.out.printf("%.9f\n", finalEnergy);
    }

    private static double computeEnergy(Body[] bodies) {
        double dx, dy, dz, dist;
        double potential = 0.0;
        double kinetic = 0.0;

        for (int i = 0; i < 5; i++) {
            kinetic += 0.5 * bodies[i].mass *
                    (bodies[i].vx * bodies[i].vx + bodies[i].vy * bodies[i].vy + bodies[i].vz * bodies[i].vz);

            for (int j = i + 1; j < 5; j++) {
                dx = bodies[i].x - bodies[j].x;
                dy = bodies[i].y - bodies[j].y;
                dz = bodies[i].z - bodies[j].z;
                dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
                potential -= (bodies[i].mass * bodies[j].mass) / dist;
            }
        }

        return kinetic + potential;
    }
}