import java.util.Arrays;
import java.util.Scanner;

public class JovianPlanetsSimulation {

    private static final double PI = 3.141592653589793;
    private static final double SOLAR_MASS = 4 * Math.pow(PI, 2);
    private static final double DAYS_PER_YEAR = 365.24;
    private static final int NUM_PLANETS = 5;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Parse N from command-line argument
        int numPlanets = Integer.parseInt(args[0]);

        if (numPlanets != NUM_PLANETS) {
            System.out.println("Error: Invalid number of planets. Expected " + NUM_PLANETS);
            return;
        }

        Planet[] planets = new Planet[numPlanets];

        // Define Sun and planets
        double[][] initialPositions = {
                {0, 0, 0},
                {4.84143144246472090e+00, -1.16032004402742839e+00, -1.03622044471123109e-01},
                {8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01},
                {1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01},
                {1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01}
        };

        double[][] initialVelocities = {
                {0, 0, 0},
                {1.66007664274403694e-03 * DAYS_PER_YEAR, 7.69901118419740425e-03 * DAYS_PER_YEAR, -6.90460016972063023e-05 * DAYS_PER_YEAR},
                {-2.76742510726862411e-03 * DAYS_PER_YEAR, 4.99852801234917238e-03 * DAYS_PER_YEAR, 2.30417297573763929e-05 * DAYS_PER_YEAR},
                {2.96460137564761618e-03 * DAYS_PER_YEAR, 2.37847173959480950e-03 * DAYS_PER_YEAR, -2.96589568540237556e-05 * DAYS_PER_YEAR},
                {2.68067772490389322e-03 * DAYS_PER_YEAR, 1.62824170038242295e-03 * DAYS_PER_YEAR, -9.51592254519715870e-05 * DAYS_PER_YEAR}
        };

        double[] masses = {
                SOLAR_MASS,
                9.54791938424326609e-04 * SOLAR_MASS,
                2.85885980666130812e-04 * SOLAR_MASS,
                4.36624404335156298e-05 * SOLAR_MASS,
                5.15138902046611451e-05 * SOLAR_MASS
        };

        for (int i = 0; i < numPlanets; i++) {
            planets[i] = new Planet(initialPositions[i], initialVelocities[i], masses[i]);
        }

        // Calculate total momentum of other planets and adjust Sun's velocity accordingly
        double[] totalMomentum = new double[3];
        for (Planet planet : planets) {
            if (planet != null && planet.getMass() > 0) {
                for (int i = 0; i < 3; i++) {
                    totalMomentum[i] += planet.getVelocity()[i] * planet.getMass();
                }
            }
        }

        double[] initialVelocitiesAdjusted = planets[0].getVelocity().clone();

        if (totalMomentum[0] != 0 || totalMomentum[1] != 0 || totalMomentum[2] != 0) {
            for (int i = 0; i < 3; i++) {
                initialVelocitiesAdjusted[i] -= totalMomentum[i] / SOLAR_MASS;
            }
        }

        // Initialize simulation parameters
        double dt = 1e-4 * DAYS_PER_YEAR; // time step in years

        // Run simulation for a specified number of steps
        int numSteps = 1000;

        Planet[] planetsCopy = new Planet[numPlanets];
        System.arraycopy(planets, 0, planetsCopy, 0, numPlanets);

        double initialEnergy = calculateEnergy(planets);
        System.out.printf("Initial energy: %.9f%n", initialEnergy);

        for (int step = 0; step < numSteps; step++) {
            // Update velocities first
            for (Planet planet : planetsCopy) {
                if (planet != null && planet.getMass() > 0) {
                    updateVelocity(planet, dt);
                }
            }

            // Update positions next
            for (Planet planet : planetsCopy) {
                if (planet != null && planet.getMass() > 0) {
                    updatePosition(planet, dt);
                }
            }
        }

        double finalEnergy = calculateEnergy(planetsCopy);

        System.out.printf("Final energy: %.9f%n", finalEnergy);

        // Print final positions and velocities
        for (Planet planet : planetsCopy) {
            if (planet != null && planet.getMass() > 0) {
                System.out.println(planet);
            }
        }
    }

    private static double calculateEnergy(Planet[] planets) {
        double energy = 0;

        // Calculate kinetic energy of all planets
        for (Planet planet : planets) {
            if (planet != null && planet.getMass() > 0) {
                double[] velocitySquared = new double[3];
                for (int i = 0; i < 3; i++) {
                    velocitySquared[i] = Math.pow(planet.getVelocity()[i], 2);
                }
                energy += 0.5 * planet.getMass() * Arrays.stream(velocitySquared).sum();
            }
        }

        // Calculate potential energy of all pairs of planets
        for (int i = 0; i < planets.length; i++) {
            Planet p1 = planets[i];
            if (p1 != null && p1.getMass() > 0) {
                for (int j = i + 1; j < planets.length; j++) {
                    Planet p2 = planets[j];
                    if (p2 != null && p2.getMass() > 0) {
                        double[] positionDifference = new double[3];
                        for (int k = 0; k < 3; k++) {
                            positionDifference[k] = p1.getPosition()[k] - p2.getPosition()[k];
                        }
                        double distanceSquared = Arrays.stream(positionDifference).map(x -> Math.pow(x, 2)).sum();
                        energy -= SOLAR_MASS * p1.getMass() / (Math.sqrt(distanceSquared) + 0.000001);
                    }
                }
            }
        }

        return energy;
    }

    private static void updateVelocity(Planet planet, double dt) {
        double[] acceleration = new double[3];
        for (int i = 0; i < 3; i++) {
            acceleration[i] = -SOLAR_MASS * (planet.getPosition()[i] / Math.pow(Math.sqrt(Arrays.stream(planet.getPosition()).map(x -> Math.pow(x, 2)).sum()) + 0.000001, 3));
        }
        for (int i = 0; i < 3; i++) {
            planet.getVelocity()[i] += acceleration[i] * dt;
        }
    }

    private static void updatePosition(Planet planet, double dt) {
        for (int i = 0; i < 3; i++) {
            planet.getPosition()[i] += planet.getVelocity()[i] * dt;
        }
    }

    public static class Planet {
        private double[] position;
        private double[] velocity;
        private double mass;

        public Planet(double[] initialPosition, double[] initialVelocity, double mass) {
            this.position = initialPosition.clone();
            this.velocity = initialVelocity.clone();
            this.mass = mass;
        }

        public double[] getPosition() {
            return position;
        }

        public void setPosition(double[] newPosition) {
            position = newPosition;
        }

        public double[] getVelocity() {
            return velocity;
        }

        public void setVelocity(double[] newVelocity) {
            velocity = newVelocity;
        }

        @Override
        public String toString() {
            return "Planet{" +
                    "position=" + Arrays.toString(position) +
                    ", velocity=" + Arrays.toString(velocity) +
                    ", mass=" + mass +
                    '}';
        }
    }
}
