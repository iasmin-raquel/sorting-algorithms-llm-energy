#include <cmath>
#include <iostream>

const double PI = 3.141592653589793;
const double SOLAR_MASS = 4 * PI * PI;
const double DAYS_PER_YEAR = 365.24;

struct Body {
    double x, y, z, vx, vy, vz, mass;
};

void adjustSunVelocity(Body* bodies, int N) {
    double totalMomentum[3] = {0, 0, 0};
    for (int i = 1; i <= N; ++i) {
        Body& body = bodies[i];
        totalMomentum[0] += body.mass * body.vx;
        totalMomentum[1] += body.mass * body.vy;
        totalMomentum[2] += body.mass * body.vz;
    }
    double sunVelocity[3] = {bodies[0].vx, bodies[0].vy, bodies[0].vz};
    for (int i = 0; i < 3; ++i) {
        sunVelocity[i] -= totalMomentum[i] / SOLAR_MASS;
    }
    bodies[0].vx = sunVelocity[0];
    bodies[0].vy = sunVelocity[1];
    bodies[0].vz = sunVelocity[2];
}

void symplecticIntegrator(Body* bodies, int N, double dt) {
    for (int i = 1; i <= N; ++i) {
        Body& body = bodies[i];
        // Update velocities
        body.vx += 0.5 * dt * body.ax;
        body.vy += 0.5 * dt * body.ay;
        body.vz += 0.5 * dt * body.az;

        // Update positions
        body.x += dt * body.vx;
        body.y += dt * body.vy;
        body.z += dt * body.vz;

        // Recalculate accelerations (after half-step)
        double G = 1.0 / SOLAR_MASS;
        for (int j = 1; j <= N; ++j) {
            if (i != j) {
                Body& otherBody = bodies[j];
                double r[3] = {body.x - otherBody.x, body.y - otherBody.y, body.z - otherBody.z};
                double rMag2 = r[0]*r[0] + r[1]*r[1] + r[2]*r[2];
                double Fmag = G * bodies[i].mass * otherBody.mass / pow(rMag2, 1.5);
                double Fa[3] = {Fmag * r[0] / rMag2, Fmag * r[1] / rMag2, Fmag * r[2] / rMag2};
                body.ax += Fa[0];
                body.ay += Fa[1];
                body.az += Fa[2];

                double otherBodyAx[3] = {Fa[0], Fa[1], Fa[2]};
                otherBody.ax -= Fa[0];
                otherBody.ay -= Fa[1];
                otherBody.az -= Fa[2];
            }
        }

        // Update velocities (after full step)
        body.vx += 0.5 * dt * body.ax;
        body.vy += 0.5 * dt * body.ay;
        body.vz += 0.5 * dt * body.az;
    }
}

void calculateEnergy(Body* bodies, int N) {
    double kineticEnergy = 0.0;
    for (int i = 1; i <= N; ++i) {
        Body& body = bodies[i];
        double velocityMag2 = pow(body.vx, 2) + pow(body.vy, 2) + pow(body.vz, 2);
        kineticEnergy += 0.5 * body.mass * velocityMag2;
    }

    double potentialEnergy = 0.0;
    for (int i = 1; i <= N; ++i) {
        Body& body = bodies[i];
        for (int j = i+1; j <= N; ++j) {
            Body& otherBody = bodies[j];
            double r[3] = {body.x - otherBody.x, body.y - otherBody.y, body.z - otherBody.z};
            double rMag2 = r[0]*r[0] + r[1]*r[1] + r[2]*r[2];
            potentialEnergy -= G * bodies[i].mass * otherBody.mass / rMag2;
        }
    }

    std::cout << "E_initial: " << kineticEnergy + potentialEnergy << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: ./nbody <N>" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);

    Body bodies[N+1];

    // Initialize Sun
    bodies[0].x = 0.0;
    bodies[0].y = 0.0;
    bodies[0].z = 0.0;
    bodies[0].vx = 0.0;
    bodies[0].vy = 0.0;
    bodies[0].vz = 0.0;
    bodies[0].mass = SOLAR_MASS;

    // Initialize Jupiter
    bodies[1].x = 4.84143144246472090e+00;
    bodies[1].y = -1.16032004402742839e+00;
    bodies[1].z = -1.03622044471123109e-01;
    bodies[1].vx = 1.66007664274403694e-03 * DAYS_PER_YEAR;
    bodies[1].vy = 7.69901118419740425e-03 * DAYS_PER_YEAR;
    bodies[1].vz = -6.90460016972063023e-05 * DAYS_PER_YEAR;
    bodies[1].mass = 9.54791938424326609e-04 * SOLAR_MASS;

    // Initialize Saturn
    bodies[2].x = 8.34336671824457987e+00;
    bodies[2].y = 4.12479856412430479e+00;
    bodies[2].z = -4.03523417114321381e-01;
    bodies[2].vx = -2.76742510726862411e-03 * DAYS_PER_YEAR;
    bodies[2].vy = 4.99852801234917238e-03 * DAYS_PER_YEAR;
    bodies[2].vz = 2.30417297573763929e-05 * DAYS_PER_YEAR;
    bodies[2].mass = 2.85885980666130812e-04 * SOLAR_MASS;

    // Initialize Uranus
    bodies[3].x = 1.28943695621391310e+01;
    bodies[3].y = -1.51111514016986312e+01;
    bodies[3].z = -2.23307578892655734e-01;
    bodies[3].vx = 2.96460137564761618e-03 * DAYS_PER_YEAR;
    bodies[3].vy = 2.37847173959480950e-03 * DAYS_PER_YEAR;
    bodies[3].vz = -2.96589568540237556e-05 * DAYS_PER_YEAR;
    bodies[3].mass = 4.36624404335156298e-05 * SOLAR_MASS;

    // Initialize Neptune
    bodies[4].x = 1.53796971148509165e+01;
    bodies[4].y = -2.59193146099879641e+01;
    bodies[4].z = 1.79258772950371181e-01;
    bodies[4].vx = 2.68067772490389322e-03 * DAYS_PER_YEAR;
    bodies[4].vy = 1.62824170038242295e-03 * DAYS_PER_YEAR;
    bodies[4].vz = -9.51592254519715870e-05 * DAYS_PER_YEAR;
    bodies[4].mass = 5.15138902046611451e-05 * SOLAR_MASS;

    // Adjust Sun's velocity to ensure zero total momentum
    adjustSunVelocity(bodies, N);

    // Simulate orbits with the specified initial conditions
    double dt = 0.01; // time step in years
    int numSteps = 10000;
    for (int i = 0; i < numSteps; ++i) {
        symplecticIntegrator(bodies, N, dt);
    }

    // Calculate and print the initial and final energies
    calculateEnergy(bodies, N);

    return 0;
}
