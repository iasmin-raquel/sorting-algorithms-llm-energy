#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

const double PI = 3.141592653589793;
const double SOLAR_MASS = 4 * PI * PI;
const double DAYS_PER_YEAR = 365.24;

struct Planet {
    double x, y, z;
    double vx, vy, vz;
    double mass;
};

double distance(const Planet& a, const Planet& b) {
    return std::sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) + (a.z - b.z) * (a.z - b.z));
}

double energy(const std::vector<Planet>& planets) {
    double kineticEnergy = 0.0, potentialEnergy = 0.0;
    for (size_t i = 0; i < planets.size(); ++i) {
        kineticEnergy += 0.5 * planets[i].mass * (planets[i].vx * planets[i].vx + planets[i].vy * planets[i].vy + planets[i].vz * planets[i].vz);
        for (size_t j = i + 1; j < planets.size(); ++j) {
            double r = distance(planets[i], planets[j]);
            potentialEnergy -= planets[i].mass * planets[j].mass / r;
        }
    }
    return kineticEnergy + potentialEnergy;
}

void offsetMomentum(std::vector<Planet>& planets, double& vx_sun, double& vy_sun, double& vz_sun) {
    for (const auto& planet : planets) {
        vx_sun += -planet.vx * planet.mass / SOLAR_MASS;
        vy_sun += -planet.vy * planet.mass / SOLAR_MASS;
        vz_sun += -planet.vz * planet.mass / SOLAR_MASS;
    }
}

void updateVelocities(const std::vector<Planet>& planets, double dt) {
    for (size_t i = 0; i < planets.size(); ++i) {
        for (size_t j = i + 1; j < planets.size(); ++j) {
            double dx = planets[j].x - planets[i].x;
            double dy = planets[j].y - planets[i].y;
            double dz = planets[j].z - planets[i].z;
            double r2 = dx * dx + dy * dy + dz * dz;
            double r3 = std::cbrt(r2);
            planets[i].vx -= planets[j].mass * (dx / r3) * dt;
            planets[i].vy -= planets[j].mass * (dy / r3) * dt;
            planets[i].vz -= planets[j].mass * (dz / r3) * dt;
            planets[j].vx += planets[i].mass * (dx / r3) * dt;
            planets[j].vy += planets[i].mass * (dy / r3) * dt;
            planets[j].vz += planets[i].mass * (dz / r3) * dt;
        }
    }
}

void updatePositions(const std::vector<Planet>& planets, double dt) {
    for (const auto& planet : planets) {
        planet.x += planet.vx * dt;
        planet.y += planet.vy * dt;
        planet.z += planet.vz * dt;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);
    std::vector<Planet> planets = {
        {0, 0, 0, 0, 0, 0, SOLAR_MASS},
        {4.84143144246472090e+00, -1.16032004402742839e+00, -1.03622044471123109e-01, 1.66007664274403694e-03 * DAYS_PER_YEAR, 7.69901118419740425e-03 * DAYS_PER_YEAR, -6.90460016972063023e-05 * DAYS_PER_YEAR, 9.54791938424326609e-04 * SOLAR_MASS},
        {8.34336671824457987e+00, 4.12479856412430479e+00, -4.03523417114321381e-01, -2.76742510726862411e-03 * DAYS_PER_YEAR, 4.99852801234917238e-03 * DAYS_PER_YEAR, 2.30417297573763929e-05 * DAYS_PER_YEAR, 2.85885980666130812e-04 * SOLAR_MASS},
        {1.28943695621391310e+01, -1.51111514016986312e+01, -2.23307578892655734e-01, 2.96460137564761618e-03 * DAYS_PER_YEAR, 2.37847173959480950e-03 * DAYS_PER_YEAR, -2.96589568540237556e-05 * DAYS_PER_YEAR, 4.36624404335156298e-05 * SOLAR_MASS},
        {1.53796971148509165e+01, -2.59193146099879641e+01, 1.79258772950371181e-01, 2.68067772490389322e-03 * DAYS_PER_YEAR, 1.62824170038242295e-03 * DAYS_PER_YEAR, -9.51592254519715870e-05 * DAYS_PER_YEAR, 5.15138902046611451e-05 * SOLAR_MASS}
    };

    double vx_sun = 0, vy_sun = 0, vz_sun = 0;
    offsetMomentum(planets, vx_sun, vy_sun, vz_sun);
    planets[0].vx += vx_sun / SOLAR_MASS;
    planets[0].vy += vy_sun / SOLAR_MASS;
    planets[0].vz += vz_sun / SOLAR_MASS;

    double dt = 2 * PI / (DAYS_PER_YEAR * 365.25);
    for (int t = 0; t < N; ++t) {
        updateVelocities(planets, dt);
        updatePositions(planets, dt);
    }

    double initialEnergy = energy(planets);
    updateVelocities(planets, -dt); // Reverse to get the final state
    updatePositions(planets, -dt);
    double finalEnergy = energy(planets);

    std::cout << std::fixed << std::setprecision(9) << (initialEnergy / finalEnergy * 100.0) << std::endl;

    return 0;
}
