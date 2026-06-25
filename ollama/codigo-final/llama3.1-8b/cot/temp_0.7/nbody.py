import sys
import numpy as np

# Constants
DAYS_PER_YEAR = 365.25
SOLAR_MASS = 1.98910e30  # kg
G = 6.67408e-11  # m^3 kg^-1 s^-2

class Planet:
    def __init__(self, name, x, y, z, vx, vy, vz, mass):
        self.name = name
        self.x = np.array([x, y, z])
        self.vx = np.array([vx, vy, vz])
        self.mass = mass

# Sun
sun_x = 0.0
sun_y = 0.0
sun_z = 0.0
sun_vx = 0.0
sun_vy = 0.0
sun_vz = 0.0
sun_mass = 4 * np.pi ** 2

# Jovian planets
jupiter_x = 4.84143144246472090e+00
jupiter_y = -1.16032004402742839e+00
jupiter_z = -1.03622044471123109e-01
jupiter_vx = 1.66007664274403694e-03 * DAYS_PER_YEAR
jupiter_vy = 7.69901118419740425e-03 * DAYS_PER_YEAR
jupiter_vz = -6.90460016972063023e-05 * DAYS_PER_YEAR
jupiter_mass = 9.54791938424326609e-04 * SOLAR_MASS

saturn_x = 8.34336671824457987e+00
saturn_y = 4.12479856412430479e+00
saturn_z = -4.03523417114321381e-01
saturn_vx = -2.76742510726862411e-03 * DAYS_PER_YEAR
saturn_vy = 4.99852801234917238e-03 * DAYS_PER_YEAR
saturn_vz = 2.30417297573763929e-05 * DAYS_PER_YEAR
saturn_mass = 2.85885980666130812e-04 * SOLAR_MASS

uranus_x = 1.28943695621391310e+01
uranus_y = -1.51111514016986312e+01
uranus_z = -2.23307578892655734e-01
uranus_vx = 2.96460137564761618e-03 * DAYS_PER_YEAR
uranus_vy = 2.37847173959480950e-03 * DAYS_PER_YEAR
uranus_vz = -2.96589568540237556e-05 * DAYS_PER_YEAR
uranus_mass = 4.36624404335156298e-05 * SOLAR_MASS

neptune_x = 1.53796971148509165e+01
neptune_y = -2.59193146099879641e+01
neptune_z = 1.79258772950371181e-01
neptune_vx = 2.68067772490389322e-03 * DAYS_PER_YEAR
neptune_vy = 1.62824170038242295e-03 * DAYS_PER_YEAR
neptune_vz = -9.51592254519715870e-05 * DAYS_PER_YEAR
neptune_mass = 5.15138902046611451e-05 * SOLAR_MASS

planets = [
    Planet("Sun", sun_x, sun_y, sun_z, sun_vx, sun_vy, sun_vz, sun_mass),
    Planet("Jupiter", jupiter_x, jupiter_y, jupiter_z, jupiter_vx, jupiter_vy,
           jupiter_vz, jupiter_mass),
    Planet("Saturn", saturn_x, saturn_y, saturn_z, saturn_vx, saturn_vy,
          saturn_vz, saturn_mass),
    Planet("Uranus", uranus_x, uranus_y, uranus_z, uranus_vx, uranus_vy,
         uranus_vz, uranus_mass),
    Planet("Neptune", neptune_x, neptune_y, neptune_z, neptune_vx, neptune_vy,
            neptune_vz, neptune_mass)
]

def calculate_momentum(planet):
    return planet.mass * np.array([planet.vx[0], planet.vx[1], planet.vx[2]])

def offset_momentum(planets):
    total_momentum = sum(calculate_momentum(planet) for planet in planets)
    sun_velocity = -total_momentum / (planets[0].mass * 4 * np.pi ** 2)
    planets[0].vx = sun_velocity

def update_velocities(planets, dt):
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            dx = planets[j].x - planets[i].x
            dy = planets[j].y - planets[i].y
            dz = planets[j].z - planets[i].z
            r = np.linalg.norm([dx, dy, dz])
            F = G * planets[j].mass / (r ** 2)
            if i == 0:  # Sun's velocity is adjusted first
                continue
            a = F / planets[i].mass
            planet_i_velocity = planets[i].vx + a * [dx, dy, dz]
            planets[i].vx += planet_i_velocity

def update_positions(planets, dt):
    for i in range(len(planets)):
        if i == 0:  # Sun's position is not updated
            continue
        dx = planets[i].x - planets[0].x
        dy = planets[i].y - planets[0].y
        dz = planets[i].z - planets[0].z
        r = np.linalg.norm([dx, dy, dz])
        F = G * planets[0].mass / (r ** 2)
        a = F / planets[i].mass
        planet_i_position = planets[i].x + dt * [planet_i_velocity[0], planet_i_velocity[1], planet_i_velocity[2]]
        planets[i].x = planet_i_position

def calculate_energy(planets):
    total_kinetic_energy = 0.5 * sum(planet.mass * np.linalg.norm(planet.vx) ** 2 for planet in planets)
    gravitational_potential_energy = -G * sum(sum(np.linalg.norm([planets[i].x[0] - planets[j].x[0], planets[i].y[0] - planets[j].y[0], planets[i].z[0] - planets[j].z[0]]) ** 2 for j in range(len(planets))) for i in range(len(planets)))
    return total_kinetic_energy + gravitational_potential_energy

def main():
    if len(sys.argv) != 2:
        print("Usage: python n_body_problem.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])

    offset_momentum(planets)
    dt = DAYS_PER_YEAR / (N - 1)

    for i in range(N):
        update_velocities(planets, dt)
        update_positions(planets, dt)

        if i == 0:
            initial_energy = calculate_energy(planets)
            print(f"Initial energy: {initial_energy:.9f}")
        elif i == N - 1:
            final_energy = calculate_energy(planets)
            print(f"Final energy: {final_energy:.9f}")

if __name__ == "__main__":
    main()
