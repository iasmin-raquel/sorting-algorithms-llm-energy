#include <iostream>
#include <iomanip>

using namespace std;

const double PI = 3.141592653589793;
const double SOLAR_MASS = 4 * PI * PI;
const double DAYS_PER_YEAR = 365.24;

struct Body {
  double x, y, z;
  double vx, vy, vz;
  double mass;
};

double distance(Body& a, Body& b) {
  return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) + (a.z - b.z) * (a.z - b.z));
}

double gravitationalForce(Body& a, Body& b) {
  double d = distance(a, b);
  double G = 6.67430e-11;
  return G * a.mass * b.mass / (d * d);
}

double kineticEnergy(Body& b) {
  return 0.5 * b.mass * (b.vx * b.vx + b.vy * b.vy + b.vz * b.vz);
}

double potentialEnergy(Body& a, Body& b) {
  return -gravitationalForce(a, b) * distance(a, b);
}

double totalEnergy(Body& sun, Body& jupiter, Body& saturn, Body& uranus, Body& neptune) {
  return kineticEnergy(sun) + potentialEnergy(sun, jupiter) + potentialEnergy(sun, saturn) + potentialEnergy(sun, uranus) + potentialEnergy(sun, neptune) +
         kineticEnergy(jupiter) + kineticEnergy(saturn) + kineticEnergy(uranus) + kineticEnergy(neptune);
}

void updateVelocities(Body& a, Body& b) {
  double f = gravitationalForce(a, b);
  double d = distance(a, b);
  a.vx -= f * (a.x - b.x) / (d * d * a.mass);
  a.vy -= f * (a.y - b.y) / (d * d * a.mass);
  a.vz -= f * (a.z - b.z) / (d * d * a.mass);
  b.vx += f * (a.x - b.x) / (d * d * b.mass);
  b.vy += f * (a.y - b.y) / (d * d * b.mass);
  b.vz += f * (a.z - b.z) / (d * d * b.mass);
}

void updatePositions(Body& b) {
  b.x += b.vx * DAYS_PER_YEAR;
  b.y += b.vy * DAYS_PER_YEAR;
  b.z += b.vz * DAYS_PER_YEAR;
}

int main() {
  int N;
  cin >> N;

  Body sun = {0, 0, 0, 0, 0, 0, SOLAR_MASS};
  Body jupiter = {...};
  Body saturn = {...};
  Body uranus = {...};
  Body neptune = {...};

  double offsetMomentum = (jupiter.vx + saturn.vx + uranus.vx + neptune.vx) / -sun.mass;
  sun.vx += offsetMomentum;

  for (int t = 0; t < N; t++) {
    updateVelocities(sun, jupiter);
    updateVelocities(sun, saturn);
    updateVelocities(sun, uranus);
    updateVelocities(sun, neptune);

    updateVelocities(jupiter, saturn);
    updateVelocities(jupiter, uranus);
    updateVelocities(jupiter, neptune);

    updateVelocities(saturn, uranus);
    updateVelocities(saturn, neptune);

    updateVelocities(uranus, neptune);

    updatePositions(sun);
    updatePositions(jupiter);
    updatePositions(saturn);
    updatePositions(uranus);
    updatePositions(neptune);
  }

  double initialEnergy = totalEnergy(sun, jupiter, saturn, uranus, neptune);
  double finalEnergy = totalEnergy(sun, jupiter, saturn, uranus, neptune);

  cout << fixed << setprecision(9) << initialEnergy * 100 / finalEnergy << endl;

  return 0;
}
