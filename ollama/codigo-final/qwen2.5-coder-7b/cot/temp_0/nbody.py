import sys
import math

# Constants
PI = 3.141592653589793
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

# Initial conditions for the planets
planets = [
    {"x": 0, "y": 0, "z": 0, "vx": 0, "vy": 0, "vz": 0, "mass": SOLAR_MASS},
    {"x": 4.84143144246472090e+00, "y": -1.16032004402742839e+00, "z": -1.03622044471123109e-01, "vx": 1.66007664274403694e-03 * DAYS_PER_YEAR, "vy": 7.69901118419740425e-03 * DAYS_PER_YEAR, "vz": -6.90460016972063023e-05 * DAYS_PER_YEAR, "mass": 9.54791938424326609e-04 * SOLAR_MASS},
    {"x": 8.34336671824457987e+00, "y": 4.12479856412430479e+00, "z": -4.03523417114321381e-01, "vx": -2.76742510726862411e-03 * DAYS_PER_YEAR, "vy": 4.99852801234917238e-03 * DAYS_PER_YEAR, "vz": 2.30417297573763929e-05 * DAYS_PER_YEAR, "mass": 2.85885980666130812e-04 * SOLAR_MASS},
    {"x": 1.28943695621391310e+01, "y": -1.51111514016986312e+01, "z": -2.23307578892655734e-01, "vx": 2.96460137564761618e-03 * DAYS_PER_YEAR, "vy": 2.37847173959480950e-03 * DAYS_PER_YEAR, "vz": -2.96589568540237556e-05 * DAYS_PER_YEAR, "mass": 4.36624404335156298e-05 * SOLAR_MASS},
    {"x": 1.53796971148509165e+01, "y": -2.59193146099879641e+01, "z": 1.79258772950371181e-01, "vx": 2.68067772490389322e-03 * DAYS_PER_YEAR, "vy": 1.62824170038242295e-03 * DAYS_PER_YEAR, "vz": -9.51592254519715870e-05 * DAYS_PER_YEAR, "mass": 5.15138902046611451e-05 * SOLAR_MASS}
]

# Parse command-line argument
N = int(sys.argv[1])

# Function to calculate the distance between two planets
def distance(p1, p2):
    dx = p1["x"] - p2["x"]
    dy = p1["y"] - p2["y"]
    dz = p1["z"] - p2["z"]
    return math.sqrt(dx * dx + dy * dy + dz * dz)

# Function to calculate the gravitational force between two planets
def gravitational_force(p1, p2):
    r = distance(p1, p2)
    F = (SOLAR_MASS * p1["mass"] * p2["mass"]) / (r * r * r)
    return F

# Function to update velocities using the symplectic integrator
def update_velocities(planets, dt):
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            dx = planets[j]["x"] - planets[i]["x"]
            dy = planets[j]["y"] - planets[i]["y"]
            dz = planets[j]["z"] - planets[i]["z"]
            r = distance(planets[i], planets[j])
            F = gravitational_force(planets[i], planets[j])
            ax = F * dx / (planets[i]["mass"] * r)
            ay = F * dy / (planets[i]["mass"] * r)
            az = F * dz / (planets[i]["mass"] * r)
            planets[i]["vx"] += ax * dt
            planets[i]["vy"] += ay * dt
            planets[i]["vz"] += az * dt
            planets[j]["vx"] -= ax * dt
            planets[j]["vy"] -= ay * dt
            planets[j]["vz"] -= az * dt

# Function to update positions using the symplectic integrator
def update_positions(planets, dt):
    for i in range(len(planets)):
        planets[i]["x"] += planets[i]["vx"] * dt
        planets[i]["y"] += planets[i]["vy"] * dt
        planets[i]["z"] += planets[i]["vz"] * dt

# Function to calculate the total energy of the system
def total_energy(planets):
    kinetic_energy = 0
    potential_energy = 0
    for i in range(len(planets)):
        kinetic_energy += 0.5 * planets[i]["mass"] * (planets[i]["vx"] ** 2 + planets[i]["vy"] ** 2 + planets[i]["vz"] ** 2)
        for j in range(i + 1, len(planets)):
            r = distance(planets[i], planets[j])
            potential_energy -= gravitational_force(planets[i], planets[j]) / r
    return kinetic_energy + potential_energy

# Main simulation loop
dt = 0.01  # Time step
num_steps = 20000  # Number of steps

# Calculate initial energy
initial_energy = total_energy(planets)

# Adjust Sun's velocity to ensure zero total momentum
total_momentum_x = sum(p["vx"] * p["mass"] for p in planets)
total_momentum_y = sum(p["vy"] * p["mass"] for p in planets)
total_momentum_z = sum(p["vz"] * p["mass"] for p in planets)
planets[0]["vx"] -= total_momentum_x / SOLAR_MASS
planets[0]["vy"] -= total_momentum_y / SOLAR_MASS
planets[0]["vz"] -= total_momentum_z / SOLAR_MASS

# Simulate the system
for _ in range(num_steps):
    update_velocities(planets, dt)
    update_positions(planets, dt)

# Calculate final energy
final_energy = total_energy(planets)

# Print initial and final energy
print("%.9f" % (initial_energy / SOLAR_MASS))
print("%.9f" % (final_energy / SOLAR_MASS))
