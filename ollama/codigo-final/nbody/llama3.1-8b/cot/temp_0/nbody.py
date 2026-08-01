import sys
import math
from datetime import timedelta

# Constants
SOLAR_MASS = 1.989e30  # kg
DAYS_PER_YEAR = 365.25 * 24 * 3600  # s
PI = math.pi

def offsetMomentum(planets):
    total_momentum = [0, 0, 0]
    for planet in planets:
        total_momentum[0] += planet['mass'] * planet['vx']
        total_momentum[1] += planet['mass'] * planet['vy']
        total_momentum[2] += planet['mass'] * planet['vz']

    if math.isclose(sum(total_momentum), 0, abs_tol=1e-8):
        return

    sun = planets[0]
    sun['vx'] -= total_momentum[0] / (sun['mass'])
    sun['vy'] -= total_momentum[1] / (sun['mass'])
    sun['vz'] -= total_momentum[2] / (sun['mass'])

def symplectic_integrator(planets, dt):
    for planet in planets:
        # Update velocities
        planet['vx'] += dt * planet['ax']
        planet['vy'] += dt * planet['ay']
        planet['vz'] += dt * planet['az']

        # Update positions
        planet['x'] += dt * planet['vx']
        planet['y'] += dt * planet['vy']
        planet['z'] += dt * planet['vz']

def calculate_energy(planets):
    kinetic_energy = 0
    potential_energy = 0

    for i, planet in enumerate(planets):
        if i == 0:
            continue

        r = math.sqrt((planet['x'] - planets[0]['x'])**2 +
                      (planet['y'] - planets[0]['y'])**2 +
                      (planet['z'] - planets[0]['z'])**2)

        kinetic_energy += 0.5 * planet['mass'] * (planet['vx']**2 + planet['vy']**2 + planet['vz']**2)
        potential_energy -= G * planet['mass'] * planets[0]['mass'] / r

    return kinetic_energy, potential_energy

def main():
    if len(sys.argv) != 2:
        print("Usage: python n_body.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])

    # Initial conditions
    G = 6.674e-11  # m^3 kg^-1 s^-2

    planets = [
        {'x': 0, 'y': 0, 'z': 0, 'vx': 0, 'vy': 0, 'vz': 0, 'mass': 4 * PI**2},
        {'x': 4.84143144246472090e+00, 'y': -1.16032004402742839e+00,
         'z': -1.03622044471123109e-01, 'vx': 1.66007664274403694e-03 * DAYS_PER_YEAR,
         'vy': 7.69901118419740425e-03 * DAYS_PER_YEAR, 'vz': -6.90460016972063023e-05 * DAYS_PER_YEAR,
         'mass': 9.54791938424326609e-04 * SOLAR_MASS},
        {'x': 8.34336671824457987e+00, 'y': 4.12479856412430479e+00,
         'z': -4.03523417114321381e-01, 'vx': -2.76742510726862411e-03 * DAYS_PER_YEAR,
         'vy': 4.99852801234917238e-03 * DAYS_PER_YEAR, 'vz': 2.30417297573763929e-05 * DAYS_PER_YEAR,
         'mass': 2.85885980666130812e-04 * SOLAR_MASS},
        {'x': 1.28943695621391310e+01, 'y': -1.51111514016986312e+01,
         'z': -2.23307578892655734e-01, 'vx': 2.96460137564761618e-03 * DAYS_PER_YEAR,
         'vy': 2.37847173959480950e-03 * DAYS_PER_YEAR, 'vz': -2.96589568540237556e-05 * DAYS_PER_YEAR,
         'mass': 4.36624404335156298e-05 * SOLAR_MASS},
        {'x': 1.53796971148509165e+01, 'y': -2.59193146099879641e+01,
         'z': 1.79258772950371181e-01, 'vx': 2.68067772490389322e-03 * DAYS_PER_YEAR,
         'vy': 1.62824170038242295e-03 * DAYS_PER_YEAR, 'vz': -9.51592254519715870e-05 * DAYS_PER_YEAR,
         'mass': 5.15138902046611451e-05 * SOLAR_MASS},
    ]

    offsetMomentum(planets)

    dt = 1e3  # s
    t_end = N * dt

    for i in range(int(t_end / dt)):
        symplectic_integrator(planets, dt)
        kinetic_energy, potential_energy = calculate_energy(planets)
        print(f"Time: {i * dt:.2f} s, Energy: {kinetic_energy + potential_energy:.9f}")

if __name__ == "__main__":
    main()
