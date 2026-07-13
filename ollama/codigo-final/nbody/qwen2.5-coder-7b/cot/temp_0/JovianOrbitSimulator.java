import java.util.Arrays;

public class JovianOrbitSimulator {

    private static final double PI = 3.141592653589793;
    private static final double SOLAR_MASS = 4 * PI * PI;
    private static final double DAYS_PER_YEAR = 365.24;

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java JovianOrbitSimulator <N>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        Planet[] planets = new Planet[N];

        // Initial conditions
        planets[0] = new Planet(0, 0, 0, 0, 0, 0, SOLAR_MASS); // Sun
        planets[1] = new Planet(4.84143144246472090e+00, -1.16032004402742839e+00, -1.03622044471123109e-01,
                1.66007664274403694e-03 * DAYS_PER_YEAR, 7.69901118419740425e-03 * DAYS_PER_YEAR, -6.90460016972063023e-05 * DAYS_PER_YEAR,
                9.54791938424326609e-04 * SOLAR_MASS); // Jupiter
        planets[2] = new Planet(8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01,
                -2.76742510726862411e-03 * DAYS_PER_YEAR, 4.99852801234917238e-03 * DAYS_PER_YEAR, 2.30417297573763929e-05 * DAYS_PER_YEAR,
                2.85885980666130812e-04 * SOLAR_MASS); // Saturn
        planets[3] = new Planet(1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01,
                2.96460137564761618e-03 * DAYS_PER_YEAR, 2.37847173959480950e-03 * DAYS_PER_YEAR, -2.96589568540237556e-05 * DAYS_PER_YEAR,
                4.36624404335156298e-05 * SOLAR_MASS); // Uranus
        planets[4] = new Planet(1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01,
                2.68067772490389322e-03 * DAYS_PER_YEAR, 1.62824170038242295e-03 * DAYS_PER_YEAR, -9.51592254519715870e-05 * DAYS_PER_YEAR,
                5.15138902046611451e-05 * SOLAR_MASS); // Neptune

        // Initialize other planets with random positions and velocities
        for (int i = 5; i < N; i++) {
            double x = Math.random() * 100 - 50;
            double y = Math.random() * 100 - 50;
            double z = Math.random() * 100 - 50;
            double vx = Math.random() * 0.01 - 0.005;
            double vy = Math.random() * 0.01 - 0.005;
            double vz = Math.random() * 0.01 - 0.005;
            double mass = Math.random() * 1e-4 * SOLAR_MASS;
            planets[i] = new Planet(x, y, z, vx, vy, vz, mass);
        }

        // Offset the Sun's initial velocity to ensure zero total momentum
        offsetMomentum(planets);

        // Simulate the orbits
        double dt = 0.01; // Time step
        int steps = (int) (DAYS_PER_YEAR / dt); // Number of steps per year

        for (int t = 0; t < steps * N; t++) {
            updateVelocities(planets, dt);
            updatePositions(planets, dt);
        }

        // Calculate and print initial and final energy
        double initialEnergy = calculateTotalEnergy(planets);
        double finalEnergy = calculateTotalEnergy(planets);

        System.out.printf("%.9f %.9f%n", initialEnergy * 100, finalEnergy * 100);
    }

    private static void offsetMomentum(Planet[] planets) {
        double px = 0, py = 0, pz = 0;
        for (Planet planet : planets) {
            px += planet.mass * planet.vx;
            py += planet.mass * planet.vy;
            pz += planet.mass * planet.vz;
        }
        planets[0].vx -= px / SOLAR_MASS;
        planets[0].vy -= py / SOLAR_MASS;
        planets[0].vz -= pz / SOLAR_MASS;
    }

    private static void updateVelocities(Planet[] planets, double dt) {
        for (int i = 0; i < planets.length; i++) {
            Planet planet1 = planets[i];
            for (int j = i + 1; j < planets.length; j++) {
                Planet planet2 = planets[j];
                double dx = planet2.x - planet1.x;
                double dy = planet2.y - planet1.y;
                double dz = planet2.z - planet1.z;
                double distanceSquared = dx * dx + dy * dy + dz * dz;
                double distance = Math.sqrt(distanceSquared);
                double force = SOLAR_MASS * planet2.mass / (distanceSquared * distance);
                double ax = force * dx / planet1.mass;
                double ay = force * dy / planet1.mass;
                double az = force * dz / planet1.mass;
                planet1.vx += ax * dt;
                planet1.vy += ay * dt;
                planet1.vz += az * dt;
            }
        }
    }

    private static void updatePositions(Planet[] planets, double dt) {
        for (Planet planet : planets) {
            planet.x += planet.vx * dt;
            planet.y += planet.vy * dt;
            planet.z += planet.vz * dt;
        }
    }

    private static double calculateTotalEnergy(Planet[] planets) {
        double kineticEnergy = 0, potentialEnergy = 0;
        for (int i = 0; i < planets.length; i++) {
            Planet planet1 = planets[i];
            kineticEnergy += 0.5 * planet1.mass * (planet1.vx * planet1.vx + planet1.vy * planet1.vy + planet1.vz * planet1.vz);
            for (int j = i + 1; j < planets.length; j++) {
                Planet planet2 = planets[j];
                double dx = planet2.x - planet1.x;
                double dy = planet2.y - planet1.y;
                double dz = planet2.z - planet1.z;
                double distanceSquared = dx * dx + dy * dy + dz * dz;
                potentialEnergy -= SOLAR_MASS * planet2.mass / Math.sqrt(distanceSquared);
            }
        }
        return kineticEnergy + potentialEnergy;
    }

    static class Planet {
        double x, y, z;
        double vx, vy, vz;
        double mass;

        Planet(double x, double y, double z, double vx, double vy, double vz, double mass) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.vx = vx;
            this.vy = vy;
            this.vz = vz;
            this.mass = mass;
        }
    }
}
