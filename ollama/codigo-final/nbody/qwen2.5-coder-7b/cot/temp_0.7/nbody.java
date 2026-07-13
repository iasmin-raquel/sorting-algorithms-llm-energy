public class NBody {
    private static final double PI = 3.141592653589793;
    private static final double SOLAR_MASS = 4 * Math.PI * Math.PI;
    private static final double DAYS_PER_YEAR = 365.24;

    private static class Planet {
        double x, y, z; // position
        double vx, vy, vz; // velocity
        double mass; // mass

        public Planet(double x, double y, double z, double vx, double vy, double vz, double mass) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.vx = vx;
            this.vy = vy;
            this.vz = vz;
            this.mass = mass;
        }
    }

    private static double energy(Planet[] planets) {
        double e = 0.0;
        int n = planets.length;

        for (int i = 0; i < n; ++i) {
            e += 0.5 * planets[i].mass *
                (planets[i].vx * planets[i].vx +
                 planets[i].vy * planets[i].vy +
                 planets[i].vz * planets[i].vz);
        }

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                double dx = planets[j].x - planets[i].x;
                double dy = planets[j].y - planets[i].y;
                double dz = planets[j].z - planets[i].z;
                double distance = Math.sqrt(dx * dx + dy * dy + dz * dz);
                e -= (planets[i].mass * planets[j].mass) / distance;
            }
        }

        return e;
    }

    private static void offsetMomentum(Planet[] planets) {
        double px = 0.0, py = 0.0, pz = 0.0;

        for (int i = 1; i < planets.length; ++i) { // start from 1 to exclude the Sun
            px += planets[i].mass * planets[i].vx;
            py += planets[i].mass * planets[i].vy;
            pz += planets[i].mass * planets[i].vz;
        }

        planets[0].vx = -px / SOLAR_MASS;
        planets[0].vy = -py / SOLAR_MASS;
        planets[0].vz = -pz / SOLAR_MASS;
    }

    private static void updateVelocity(Planet[] planets, double dt) {
        int n = planets.length;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j) {
                    double dx = planets[j].x - planets[i].x;
                    double dy = planets[j].y - planets[i].y;
                    double dz = planets[j].z - planets[i].z;
                    double distance = Math.sqrt(dx * dx + dy * dy + dz * dz);
                    double force = (planets[i].mass * planets[j].mass) / (distance * distance * distance);

                    planets[i].vx += dt * force * dx / planets[i].mass;
                    planets[i].vy += dt * force * dy / planets[i].mass;
                    planets[i].vz += dt * force * dz / planets[i].mass;
                }
            }
        }
    }

    private static void updatePosition(Planet[] planets, double dt) {
        int n = planets.length;

        for (int i = 0; i < n; ++i) {
            planets[i].x += dt * planets[i].vx;
            planets[i].y += dt * planets[i].vy;
            planets[i].z += dt * planets[i].vz;
        }
    }

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        double dt = 2.59e-6; // time step in years
        int T = (int) (365.25 * DAYS_PER_YEAR); // number of time steps

        Planet[] planets = new Planet[N + 1];

        // Sun
        planets[0] = new Planet(0, 0, 0, 0, 0, 0, SOLAR_MASS);

        // Jovian planets
        planets[1] = new Planet(4.8414314424647209e+00, -1.16032004402742839e+00, -1.03622044471123109e-01,
                1.66007664274403694e-03 * DAYS_PER_YEAR, 7.69901118419740425e-03 * DAYS_PER_YEAR, -6.90460016972063023e-05 * DAYS_PER_YEAR,
                9.54791938424326609e-04 * SOLAR_MASS);
        planets[2] = new Planet(8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01,
                -2.76742510726862411e-03 * DAYS_PER_YEAR, 4.99852801234917238e-03 * DAYS_PER_YEAR, 2.30417297573763929e-05 * DAYS_PER_YEAR,
                2.85885980666130812e-04 * SOLAR_MASS);
        planets[3] = new Planet(1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01,
                2.96460137564761618e-03 * DAYS_PER_YEAR, 2.37847173959480950e-03 * DAYS_PER_YEAR, -2.96589568540237556e-05 * DAYS_PER_YEAR,
                4.36624404335156298e-05 * SOLAR_MASS);
        planets[4] = new Planet(1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01,
                2.68067772490389322e-03 * DAYS_PER_YEAR, 1.62824170038242295e-03 * DAYS_PER_YEAR, -9.51592254519715870e-05 * DAYS_PER_YEAR,
                5.15138902046611451e-05 * SOLAR_MASS);

        // Add more planets if N > 5

        offsetMomentum(planets);

        double initialEnergy = energy(planets);
        System.out.printf("%.9f\n", initialEnergy);

        for (int t = 0; t < T; ++t) {
            updateVelocity(planets, dt);
            updatePosition(planets, dt);
        }

        double finalEnergy = energy(planets);
        System.out.printf("%.9f\n", finalEnergy);
    }
}
