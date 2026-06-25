import java.util.Scanner;

public class NBodySimulation {

    private static final double PI = 3.141592653589793;
    private static final double SOLAR_MASS = 4 * Math.pow(PI, 2);
    private static final double DAYS_PER_YEAR = 365.24;

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        Planet[] planets = new Planet[N + 1];

        // Initialize Sun
        planets[0] = new Planet(0, 0, 0, 0, 0, 0, SOLAR_MASS);

        // Initialize Jupiter
        double xJupiter = 4.84143144246472090e+00;
        double yJupiter = -1.16032004402742839e+00;
        double zJupiter = -1.03622044471123109e-01;
        double vxJupiter = 1.66007664274403694e-03 * DAYS_PER_YEAR;
        double vyJupiter = 7.69901118419740425e-03 * DAYS_PER_YEAR;
        double vzJupiter = -6.90460016972063023e-05 * DAYS_PER_YEAR;
        planets[1] = new Planet(xJupiter, yJupiter, zJupiter, vxJupiter, vyJupiter, vzJupiter, 9.54791938424326609e-04 * SOLAR_MASS);

        // Initialize Saturn
        double xSaturn = 8.34336671824457987e+00;
        double ySaturn = 4.12479856412430479e+00;
        double zSaturn = -4.03523417114321381e-01;
        double vxsaturn = -2.76742510726862411e-03 * DAYS_PER_YEAR;
        double vysaturn = 4.99852801234917238e-03 * DAYS_PER_YEAR;
        double vzsaturn = 2.30417297573763929e-05 * DAYS_PER_YEAR;
        planets[2] = new Planet(xSaturn, ySaturn, zSaturn, vxsaturn, vysaturn, vzsaturn, 2.85885980666130812e-04 * SOLAR_MASS);

        // Initialize Uranus
        double xUranus = 1.28943695621391310e+01;
        double yUranus = -1.51111514016986312e+01;
        double zUranus = -2.23307578892655734e-01;
        double vxUranus = 2.96460137564761618e-03 * DAYS_PER_YEAR;
        double vyUranus = 2.37847173959480950e-03 * DAYS_PER_YEAR;
        double vzUranus = -2.96589568540237556e-05 * DAYS_PER_YEAR;
        planets[3] = new Planet(xUranus, yUranus, zUranus, vxUranus, vyUranus, vzUranus, 4.36624404335156298e-05 * SOLAR_MASS);

        // Initialize Neptune
        double xNeptune = 1.53796971148509165e+01;
        double yNeptune = -2.59193146099879641e+01;
        double zNeptune = 1.79258772950371181e-01;
        double vxNeptune = 2.68067772490389322e-03 * DAYS_PER_YEAR;
        double vyNeptune = 1.62824170038242295e-03 * DAYS_PER_YEAR;
        double vzNeptune = -9.51592254519715870e-05 * DAYS_PER_YEAR;
        planets[4] = new Planet(xNeptune, yNeptune, zNeptune, vxNeptune, vyNeptune, vzNeptune, 5.15138902046611451e-05 * SOLAR_MASS);

        // Adjust Sun's velocity to ensure zero total momentum
        double sumMomentumX = planets[1].getMass() * planets[1].getVx() + planets[2].getMass() * planets[2].getVx()
                + planets[3].getMass() * planets[3].getVx() + planets[4].getMass() * planets[4].getVx();
        double sumMomentumY = planets[1].getMass() * planets[1].getVy() + planets[2].getMass() * planets[2].getVy()
                + planets[3].getMass() * planets[3].getVy() + planets[4].getMass() * planets[4].getVy();
        double sumMomentumZ = planets[1].getMass() * planets[1].getVz() + planets[2].getMass() * planets[2].getVz()
                + planets[3].getMass() * planets[3].getVz() + planets[4].getMass() * planets[4].getVz();
        double sunVelocityX = -sumMomentumX / SOLAR_MASS;
        double sunVelocityY = -sumMomentumY / SOLAR_MASS;
        double sunVelocityZ = -sumMomentumZ / SOLAR_MASS;

        // Update Sun's velocity
        planets[0].setVx(sunVelocityX);
        planets[0].setVy(sunVelocityY);
        planets[0].setVz(sunVelocityZ);

        // Simulate the orbits of the planets using a symplectic integrator
        for (int i = 0; i < N; i++) {
            for (int j = 1; j <= 4; j++) {
                double distanceX = Math.pow(planets[j].getX() - planets[0].getX(), 2);
                double distanceY = Math.pow(planets[j].getY() - planets[0].getY(), 2);
                double distanceZ = Math.pow(planets[j].getZ() - planets[0].getZ(), 2);
                double r = Math.sqrt(distanceX + distanceY + distanceZ);

                // Update velocity
                double ax = -planets[j].getMass() * (planets[0].getX() - planets[j].getX()) / Math.pow(r, 3);
                double ay = -planets[j].getMass() * (planets[0].getY() - planets[j].getY()) / Math.pow(r, 3);
                double az = -planets[j].getMass() * (planets[0].getZ() - planets[j].getZ()) / Math.pow(r, 3);

                planets[j].setVx(planets[j].getVx() + ax * DAYS_PER_YEAR);
                planets[j].setVy(planets[j].getVy() + ay * DAYS_PER_YEAR);
                planets[j].setVz(planets[j].getVz() + az * DAYS_PER_YEAR);

                // Update position
                planets[j].setX(planets[j].getX() + planets[j].getVx() * DAYS_PER_YEAR);
                planets[j].setY(planets[j].getY() + planets[j].getVy() * DAYS_PER_YEAR);
                planets[j].setZ(planets[j].getZ() + planets[j].getVz() * DAYS_PER_YEAR);

            }
        }

        // Print the initial and final energies
        double initialEnergy = calculateInitialEnergy(planets);
        System.out.printf("Initial Energy: %.9f\n", initialEnergy);

        double finalEnergy = calculateFinalEnergy(planets);
        System.out.printf("Final Energy: %.9f\n", finalEnergy);
    }

    private static double calculateInitialEnergy(Planet[] planets) {
        double totalKineticEnergy = 0;
        for (int i = 1; i <= 4; i++) {
            double kineticEnergy = 0.5 * Math.pow(planets[i].getMass(), 2)
                    * (Math.pow(planets[i].getVx(), 2) + Math.pow(planets[i].getVy(), 2) + Math.pow(planets[i].getVz(), 2));
            totalKineticEnergy += kineticEnergy;
        }

        double totalPotentialEnergy = -SOLAR_MASS * (1 / Math.sqrt(Math.pow(planets[1].getX() - planets[0].getX(), 2)
                + Math.pow(planets[1].getY() - planets[0].getY(), 2) + Math.pow(planets[1].getZ() - planets[0].getZ(), 2))
                + 1 / Math.sqrt(Math.pow(planets[2].getX() - planets[0].getX(), 2)
                + Math.pow(planets[2].getY() - planets[0].getY(), 2) + Math.pow(planets[2].getZ() - planets[0].getZ(), 2))
                + 1 / Math.sqrt(Math.pow(planets[3].getX() - planets[0].getX(), 2)
                + Math.pow(planets[3].getY() - planets[0].getY(), 2) + Math.pow(planets[3].getZ() - planets[0].getZ(), 2))
                + 1 / Math.sqrt(Math.pow(planets[4].getX() - planets[0].getX(), 2)
                + Math.pow(planets[4].getY() - planets[0].getY(), 2) + Math.pow(planets[4].getZ() - planets[0].getZ(), 2)));

        return totalKineticEnergy + totalPotentialEnergy;
    }

    private static double calculateFinalEnergy(Planet[] planets) {
        double totalKineticEnergy = 0;
        for (int i = 1; i <= 4; i++) {
            double kineticEnergy = 0.5 * Math.pow(planets[i].getMass(), 2)
                    * (Math.pow(planets[i].getVx(), 2) + Math.pow(planets[i].getVy(), 2) + Math.pow(planets[i].getVz(), 2));
            totalKineticEnergy += kineticEnergy;
        }

        double totalPotentialEnergy = -SOLAR_MASS * (1 / Math.sqrt(Math.pow(planets[1].getX() - planets[0].getX(), 2)
                + Math.pow(planets[1].getY() - planets[0].getY(), 2) + Math.pow(planets[1].getZ() - planets[0].getZ(), 2))
                + 1 / Math.sqrt(Math.pow(planets[2].getX() - planets[0].getX(), 2)
                + Math.pow(planets[2].getY() - planets[0].getY(), 2) + Math.pow(planets[2].getZ() - planets[0].getZ(), 2))
                + 1 / Math.sqrt(Math.pow(planets[3].getX() - planets[0].getX(), 2)
                + Math.pow(planets[3].getY() - planets[0].getY(), 2) + Math.pow(planets[3].getZ() - planets[0].getZ(), 2))
                + 1 / Math.sqrt(Math.pow(planets[4].getX() - planets[0].getX(), 2)
                + Math.pow(planets[4].getY() - planets[0].getY(), 2) + Math.pow(planets[4].getZ() - planets[0].getZ(), 2)));

        return totalKineticEnergy + totalPotentialEnergy;
    }

    private static class Planet {
        double x, y, z, vx, vy, vz, mass;

        public Planet(double x, double y, double z, double vx, double vy, double vz, double mass) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.vx = vx;
            this.vy = vy;
            this.vz = vz;
            this.mass = mass;
        }

        public double getX() {
            return x;
        }

        public void setX(double x) {
            this.x = x;
        }

        public double getY() {
            return y;
        }

        public void setY(double y) {
            this.y = y;
        }

        public double getZ() {
            return z;
        }

        public void setZ(double z) {
            this.z = z;
        }

        public double getVx() {
            return vx;
        }

        public void setVx(double vx) {
            this.vx = vx;
        }

        public double getVy() {
            return vy;
        }

        public void setVy(double vy) {
            this.vy = vy;
        }

        public double getVz() {
            return vz;
        }

        public void setVz(double vz) {
            this.vz = vz;
        }

        public double getMass() {
            return mass;
        }
    }
}
