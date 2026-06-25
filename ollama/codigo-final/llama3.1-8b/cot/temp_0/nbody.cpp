#include <iostream>
#include <cmath>

// Constants
const double PI = 3.141592653589793;
const double SOLAR_MASS = 4 * PI * PI;
const double DAYS_PER_YEAR = 365.24;

// Initial conditions for the Jovian planets (in SI units)
struct Planet {
    double x, y, z; // Position
    double vx, vy, vz; // Velocity
    double mass; // Mass

    Planet(double x, double y, double z, double vx, double vy, double vz, double mass) 
        : x(x), y(y), z(z), vx(vx), vy(vy), vz(vz), mass(mass) {}
};

// Function to calculate the energy of a system
double calculateEnergy(const Planet& sun, const std::vector<Planet>& planets) {
    double totalEnergy = 0.5 * SOLAR_MASS * (sun.vx * sun.vx + sun.vy * sun.vy + sun.vz * sun.vz);
    for (const auto& planet : planets) {
        totalEnergy += 0.5 * planet.mass * (planet.vx * planet.vx + planet.vy * planet.vy + planet.vz * planet.vz);
    }
    return totalEnergy;
}

// Function to adjust the Sun's velocity to ensure zero total momentum
void offsetMomentum(Planet& sun, const std::vector<Planet>& planets) {
    double totalMomentum = 0.0;
    for (const auto& planet : planets) {
        totalMomentum += planet.mass * (sun.vx + planet.vx);
    }
    sun.vx -= totalMomentum / SOLAR_MASS;
}

// Symplectic integrator function
void symplecticIntegrator(Planet& sun, std::vector<Planet>& planets, double dt) {
    // Update velocities first
    for (auto& planet : planets) {
        planet.vx += 0.5 * dt * (sun.mass / (planet.x - sun.x));
        planet.vy += 0.5 * dt * (sun.mass / (planet.y - sun.y));
        planet.vz += 0.5 * dt * (sun.mass / (planet.z - sun.z));
    }

    // Update positions
    for (auto& planet : planets) {
        planet.x += dt * planet.vx;
        planet.y += dt * planet.vy;
        planet.z += dt * planet.vz;

        // Update the Sun's position as well
        sun.x += dt * sun.vx;
        sun.y += dt * sun.vy;
        sun.z += dt * sun.vz;
    }
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);

    // Define the initial conditions for the Jovian planets
    Planet sun(0, 0, 0, 0, 0, 0, SOLAR_MASS);
    std::vector<Planet> planets;

    planets.push_back(Planet(
        4.84143144246472090e+00, -1.16032004402742839e+00, -1.03622044471123109e-01,
        1.66007664274403694e-03 * DAYS_PER_YEAR, 7.69901118419740425e-03 * DAYS_PER_YEAR, 
        -6.90460016972063023e-05 * DAYS_PER_YEAR, 9.54791938424326609e-04 * SOLAR_MASS
    ));

    planets.push_back(Planet(
        8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01,
        -2.76742510726862411e-03 * DAYS_PER_YEAR, 4.99852801234917238e-03 * DAYS_PER_YEAR, 
        2.30417297573763929e-05 * DAYS_PER_YEAR, 2.85885980666130812e-04 * SOLAR_MASS
    ));

    planets.push_back(Planet(
        1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01,
        2.96460137564761618e-03 * DAYS_PER_YEAR, 2.37847173959480950e-03 * DAYS_PER_YEAR, 
        -2.96589568540237556e-05 * DAYS_PER_YEAR, 4.36624404335156298e-05 * SOLAR_MASS
    ));

    planets.push_back(Planet(
        1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01,
        2.68067772490389322e-03 * DAYS_PER_YEAR, 1.62824170038242295e-03 * DAYS_PER_YEAR, 
        -9.51592254519715870e-05 * DAYS_PER_YEAR, 5.15138902046611451e-05 * SOLAR_MASS
    ));

    // Adjust the Sun's velocity to ensure zero total momentum
    offsetMomentum(sun, planets);

    double dt = 1e-8; // Time step for the simulation

    double E_initial = calculateEnergy(sun, planets);
    std::cout << "Initial energy: " << E_initial << std::endl;

    for (int i = 0; i < N; ++i) {
        symplecticIntegrator(sun, planets, dt);
    }

    double E_final = calculateEnergy(sun, planets);
    std::cout << "Final energy: " << E_final << std::endl;

    return 0;
}
