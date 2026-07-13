import java.math.BigDecimal;

public class NBodyProblem {

    // Constants
    private static final double PI = 3.141592653589793;
    private static final double SOLAR_MASS = 4 * PI * PI;
    private static final double DAYS_PER_YEAR = 365.24;

    // Celestial Body Class
    private static class CelestialBody {
        double x, y, z;
        double vx, vy, vz;
        double mass;
    }

    public static void main(String[] args) {
        // Parse command-line argument for number of iterations
        int N = Integer.parseInt(args[0]);

        // Initialize celestial bodies
        CelestialBody[] bodies = {
            // Sun, Jupiter, Saturn, Uranus, Neptune
        };

        // Adjust Sun's velocity to conserve total momentum
        offsetMomentum(bodies);

        // Simulate the N-body problem
        for (int i = 0; i < N; i++) {
            updateVelocities(bodies);
            updatePositions(bodies);
        }

        // Calculate and print initial and final energy
        double initialEnergy = calculateEnergy(bodies);
        double finalEnergy = calculateEnergy(bodies);
        System.out.printf("%.9f %.9f\n", initialEnergy, finalEnergy);
    }

    // Offset momentum of the Sun
    private static void offsetMomentum(CelestialBody[] bodies) {
        double totalVx = 0;
        double totalVy = 0;
        double totalVz = 0;

        for (CelestialBody body : bodies) {
            totalVx += body.vx * body.mass;
            totalVy += body.vy * body.mass;
            totalVz += body.vz * body.mass;
        }

        bodies[0].vx -= totalVx / SOLAR_MASS;
        bodies[0].vy -= totalVy / SOLAR_MASS;
        bodies[0].vz -= totalVz / SOLAR_MASS;
    }

    // Update velocities based on gravitational forces
    private static void updateVelocities(CelestialBody[] bodies) {
        for (int i = 0; i < bodies.length; i++) {
            for (int j = i + 1; j < bodies.length; j++) {
                double dx = bodies[j].x - bodies[i].x;
                double dy = bodies[j].y - bodies[i].y;
                double dz = bodies[j].z - bodies[i].z;

                double distanceSquared = dx * dx + dy * dy + dz * dz;
                double forceMagnitude = (bodies[i].mass * bodies[j].mass) / (distanceSquared * distanceSquared);

                double ax = forceMagnitude * dx / bodies[i].mass;
                double ay = forceMagnitude * dy / bodies[i].mass;
                double az = forceMagnitude * dz / bodies[i].mass;

                bodies[i].vx -= ax;
                bodies[i].vy -= ay;
                bodies[i].vz -= az;
            }
        }
    }

    // Update positions based on velocities
    private static void updatePositions(CelestialBody[] bodies) {
        for (CelestialBody body : bodies) {
            body.x += body.vx * DAYS_PER_YEAR;
            body.y += body.vy * DAYS_PER_YEAR;
            body.z += body.vz * DAYS_PER_YEAR;
        }
    }

    // Calculate total energy of the system
    private static double calculateEnergy(CelestialBody[] bodies) {
        double totalEnergy = 0;

        for (CelestialBody body : bodies) {
            totalEnergy += 0.5 * body.mass * (body.vx * body.vx + body.vy * body.vy + body.vz * body.vz);
            for (CelestialBody otherBody : bodies) {
                if (body != otherBody) {
                    double dx = body.x - otherBody.x;
                    double dy = body.y - otherBody.y;
                    double dz = body.z - otherBody.z;
                    totalEnergy -= (body.mass * otherBody.mass) / (Math.sqrt(dx * dx + dy * dy + dz * dz));
                }
            }
        }

        return totalEnergy;
    }
}
