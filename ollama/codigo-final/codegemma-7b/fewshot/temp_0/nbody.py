import sys, math

# Constants
PI = 3.141592653589793
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

# Initial conditions
# ... (as provided in the prompt)

def offsetMomentum(bodies):
    total_momentum = [0, 0, 0]
    for body in bodies:
        total_momentum[0] += body['mass'] * body['vx']
        total_momentum[1] += body['mass'] * body['vy']
        total_momentum[2] += body['mass'] * body['vz']
    for body in bodies:
        body['vx'] -= total_momentum[0] / bodies[0]['mass']
        body['vy'] -= total_momentum[1] / bodies[0]['mass']
        body['vz'] -= total_momentum[2] / bodies[0]['mass']

def calculateEnergy(bodies):
    kinetic_energy = 0
    potential_energy = 0
    for body in bodies:
        kinetic_energy += 0.5 * body['mass'] * (body['vx']**2 + body['vy']**2 + body['vz']**2)
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            distance = math.sqrt((bodies[i]['x'] - bodies[j]['x'])**2 + (bodies[i]['y'] - bodies[j]['y'])**2 + (bodies[i]['z'] - bodies[j]['z'])**2)
            potential_energy -= 1 / distance
    return kinetic_energy + potential_energy

def symplecticEuler(bodies, dt):
    for body in bodies:
        body['ax'] = 0
        body['ay'] = 0
        body['az'] = 0
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            distance = math.sqrt((bodies[i]['x'] - bodies[j]['x'])**2 + (bodies[i]['y'] - bodies[j]['y'])**2 + (bodies[i]['z'] - bodies[j]['z'])**2)
            acceleration = 1 / distance**3 * (bodies[j]['x'] - bodies[i]['x'], bodies[j]['y'] - bodies[i]['y'], bodies[j]['z'] - bodies[i]['z'])
            bodies[i]['ax'] += acceleration[0] * bodies[j]['mass']
            bodies[i]['ay'] += acceleration[1] * bodies[j]['mass']
            bodies[i]['az'] += acceleration[2] * bodies[j]['mass']
    for body in bodies:
        body['vx'] += dt * body['ax']
        body['vy'] += dt * body['ay']
        body['vz'] += dt * body['az']
        body['x'] += dt * body['vx']
        body['y'] += dt * body['vy']
        body['z'] += dt * body['vz']

def main():
    N = int(sys.argv[1])
    dt = 1.0  # Fixed timestep

    # Offset momentum
    offsetMomentum(bodies)

    # Calculate initial energy
    initial_energy = calculateEnergy(bodies)

    # Simulate orbits
    for _ in range(N):
        symplecticEuler(bodies, dt)

    # Calculate final energy
    final_energy = calculateEnergy(bodies)

    # Print results
    print(f"{initial_energy:.9f}")
    print(f"{final_energy:.9f}")

if __name__ == "__main__":
    main()
