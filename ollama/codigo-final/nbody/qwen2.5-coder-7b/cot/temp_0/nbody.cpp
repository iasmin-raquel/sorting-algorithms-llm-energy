#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>

const double PI = 3.141592653589793;
const double SOLAR_MASS = 4 * PI * PI;
const double DAYS_PER_YEAR = 365.24;

struct Planet {
    double x, y, z;
    double vx, vy, vz;
    double mass;
};

double distance(const Planet& p1, const Planet& p2) {
    return std::sqrt((p1.x - p2.x) * (p1.x - p2.x) +
                      (p1.y - p2.y) * (p1.y - p2.y) +
                      (p1.z - p2.z) * (p1.z - p2.z));
}

double potentialEnergy(const Planet& p1, const Planet& p2) {
    double r = distance(p1, p2);
    return -SOLAR_MASS * p2.mass / r;
}

double kineticEnergy(const Planet& p) {
    return 0.5 * p.mass * (p.vx * p.vx + p.vy * p.vy + p.vz * p.vz);
}

double totalEnergy(const std::vector<Planet>& planets) {
    double potential = 0, kinetic = 0;
    for (size_t i = 0; i < planets.size(); ++i) {
        for (size_t j = i + 1; j < planets.size(); ++j) {
            potential += potentialEnergy(planets[i], planets[j]);
        }
        kinetic += kineticEnergy(planets[i]);
    }
    return potential + kinetic;
}

void offsetMomentum(std::vector<Planet>& planets) {
    double px = 0, py = 0, pz = 0;
    for (const auto& planet : planets) {
        px += planet.mass * planet.vx;
        py += planet.mass * planet.vy;
        pz += planet.mass * planet.vz;
    }
    planets[0].vx -= px / SOLAR_MASS;
    planets[0].vy -= py / SOLAR_MASS;
    planets[0].vz -= pz / SOLAR_MASS;
}

void symplecticIntegrator(std::vector<Planet>& planets, double dt) {
    for (auto& planet : planets) {
        planet.vx += dt * planet.mass * 0; // No external force on the Sun
        planet.vy += dt * planet.mass * 0;
        planet.vz += dt * planet.mass * 0;
    }

    for (size_t i = 1; i < planets.size(); ++i) {
        for (size_t j = 0; j < i; ++j) {
            double dx = planets[i].x - planets[j].x;
            double dy = planets[i].y - planets[j].y;
            double dz = planets[i].z - planets[j].z;
            double r = distance(planets[i], planets[j]);
            double f = SOLAR_MASS * planets[j].mass / (r * r);
            planets[i].vx += dt * f * dx / planets[i].mass;
            planets[i].vy += dt * f * dy / planets[i].mass;
            planets[i].vz += dt * f * dz / planets[i].mass;
        }
    }

    for (auto& planet : planets) {
        planet.x += dt * planet.vx;
        planet.y += dt * planet.vy;
        planet.z += dt * planet.vz;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::atoi(argv[1]);
    if (N <= 0) {
        std::cerr << "N must be a positive integer" << std::endl;
        return 1;
    }

    std::vector<Planet> planets = {
        {0, 0, 0, 0, 0, 0, SOLAR_MASS}, // Sun
        {4.8414314424647209e+00, -1.16032004402742839e+00, -1.03622044471123109e-01, 1.66007664274403694e-03 * DAYS_PER_YEAR, 7.69901118419740425e-03 * DAYS_PER_YEAR, -6.90460016972063023e-05 * DAYS_PER_YEAR, 9.54791938424326609e-04 * SOLAR_MASS}, // Jupiter
        {8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01, -2.76742510726862411e-03 * DAYS_PER_YEAR, 4.99852801234917238e-03 * DAYS_PER_YEAR, 2.30417297573763929e-05 * DAYS_PER_YEAR, 2.85885980666130812e-04 * SOLAR_MASS}, // Saturn
        {1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01, 2.96460137564761618e-03 * DAYS_PER_YEAR, 2.37847173959480950e-03 * DAYS_PER_YEAR, -2.96589568540237556e-05 * DAYS_PER_YEAR, 4.36624404335156298e-05 * SOLAR_MASS}, // Uranus
        {1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01, 2.68067772490389322e-03 * DAYS_PER_YEAR, 1.62824170038242295e-03 * DAYS_PER_YEAR, -9.51592254519715870e-05 * DAYS_PER_YEAR, 5.15138902046611451e-05 * SOLAR_MASS} // Neptune
    };

    double dt = 2 * PI / (N * DAYS_PER_YEAR);
    offsetMomentum(planets);

    double initialEnergy = totalEnergy(planets);
    symplecticIntegrator(planets, dt);
    double finalEnergy = totalEnergy(planets);

    std::cout << std::fixed;
    std::cout << std::setprecision(9) << (initialEnergy / SOLAR_MASS * 100) << " "
              << (finalEnergy / SOLAR_MASS * 100) << std::endl;

    return 0;
}
