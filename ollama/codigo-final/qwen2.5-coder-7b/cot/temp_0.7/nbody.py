import sys
import numpy as np

# Constants
PI = 3.141592653589793
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

# Initial conditions for the planets
initial_conditions = {
    'Sun': {'x': 0, 'y': 0, 'z': 0, 'vx': 0, 'vy': 0, 'vz': 0, 'mass': SOLAR_MASS},
    'Jupiter': {'x': 4.84143144246472090e+00, 'y': -1.16032004402742839e+00, 'z': -1.03622044471123109e-01,
                'vx': 1.66007664274403694e-03 * DAYS_PER_YEAR, 'vy': 7.69901118419740425e-03 * DAYS_PER_YEAR,
                'vz': -6.90460016972063023e-05 * DAYS_PER_YEAR, 'mass': 9.54791938424326609e-04 * SOLAR_MASS},
    'Saturn': {'x': 8.34336671824457987e+00, 'y': 4.12479856412430479e+00, 'z': -4.03523417114321381e-01,
               'vx': -2.76742510726862411e-03 * DAYS_PER_YEAR, 'vy': 4.99852801234917238e-03 * DAYS_PER_YEAR,
               'vz': 2.30417297573763929e-05 * DAYS_PER_YEAR, 'mass': 2.85885980666130812e-04 * SOLAR_MASS},
    'Uranus': {'x': 1.28943695621391310e+01, 'y': -1.51111514016986312e+01, 'z': -2.23307578892655734e-01,
               'vx': 2.96460137564761618e-03 * DAYS_PER_YEAR, 'vy': 2.37847173959480950e-03 * DAYS_PER_YEAR,
               'vz': -2.96589568540237556e-05 * DAYS_PER_YEAR, 'mass': 4.36624404335156298e-05 * SOLAR_MASS},
    'Neptune': {'x': 1.53796971148509165e+01, 'y': -2.59193146099879641e+01, 'z': 1.79258772950371181e-01,
                'vx': 2.68067772490389322e-03 * DAYS_PER_YEAR, 'vy': 1.62824170038242295e-03 * DAYS_PER_YEAR,
                'vz': -9.51592254519715870e-05 * DAYS_PER_YEAR, 'mass': 5.15138902046611451e-05 * SOLAR_MASS}
}

# Function to calculate gravitational force
def gravitational_force(masses, positions):
    N = len(masses)
    F = np.zeros((N, 3))
    for i in range(N):
        for j in range(i+1, N):
            dx = positions[j][0] - positions[i][0]
            dy = positions[j][1] - positions[i][1]
            dz = positions[j][2] - positions[i][2]
            r_squared = dx**2 + dy**2 + dz**2
            Fij = SOLAR_MASS * masses[i] * masses[j] / (r_squared * np.sqrt(r_squared))
            F[i] += Fij * (dx / r_squared, dy / r_squared, dz / r_squared)
            F[j] -= Fij * (dx / r_squared, dy / r_squared, dz / r_squared)
    return F

# Function to update positions and velocities using a symplectic integrator
def symplectic_integrator(masses, positions, velocities, dt):
    N = len(masses)
    F = gravitational_force(masses, positions)
    
    # Update velocities first
    for i in range(N):
        velocities[i] += F[i] * dt / masses[i]
    
    # Update positions next
    for i in range(N):
        positions[i] += velocities[i] * dt

# Function to calculate total energy of the system
def total_energy(masses, positions, velocities):
    N = len(masses)
    kinetic_energy = 0.5 * np.sum([masses[i] * (vx**2 + vy**2 + vz**2) for i in range(N)])
    potential_energy = 0
    for i in range(N):
        for j in range(i+1, N):
            dx = positions[j][0] - positions[i][0]
            dy = positions[j][1] - positions[i][1]
            dz = positions[j][2] - positions[i][2]
            r_squared = dx**2 + dy**2 + dz**2
            potential_energy -= SOLAR_MASS * masses[i] * masses[j] / np.sqrt(r_squared)
    return kinetic_energy + potential_energy

# Adjust the Sun's initial velocity to zero total momentum
def offsetMomentum(masses, positions, velocities):
    px, py, pz = 0, 0, 0
    for i in range(len(masses)):
        px += masses[i] * velocities[i][0]
        py += masses[i] * velocities[i][1]
        pz += masses[i] * velocities[i][2]
    velocities[0][0], velocities[0][1], velocities[0][2] = -px, -py, -pz

# Main function
def main(N):
    # Initialize positions and velocities
    positions = [np.array([initial_conditions[planet]['x'], initial_conditions[planet]['y'],
                           initial_conditions[planet]['z']]) for planet in initial_conditions]
    velocities = [np.array([initial_conditions[planet]['vx'], initial_conditions[planet]['vy'],
                            initial_conditions[planet]['vz']]) for planet in initial_conditions]
    
    # Adjust Sun's velocity to zero total momentum
    offsetMomentum(initial_conditions['Sun']['mass'], positions, velocities)
    
    # Calculate initial energy
    initial_energy = total_energy([initial_conditions[planet]['mass'] for planet in initial_conditions],
                                 positions, velocities)
    
    # Simulate the system
    dt = 0.01 * DAYS_PER_YEAR / N
    for _ in range(N):
        symplectic_integrator([initial_conditions[planet]['mass'] for planet in initial_conditions],
                               positions, velocities, dt)
    
    # Calculate final energy
    final_energy = total_energy([initial_conditions[planet]['mass'] for planet in initial_conditions],
                                positions, velocities)
    
    # Print the initial and final energy in %.9f format
    print(f"{initial_energy:.9f}")
    print(f"{final_energy:.9f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <N>")
        sys.exit(1)
    
    N = int(sys.argv[1])
    main(N)
