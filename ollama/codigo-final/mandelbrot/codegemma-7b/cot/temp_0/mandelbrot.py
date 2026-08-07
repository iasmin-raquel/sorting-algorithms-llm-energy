import sys

# Validate input
try:
    N = int(sys.argv[1])
except ValueError:
    sys.exit("Error: N must be an integer.")
if N < 8:
    sys.exit("Error: N must be at least 8.")

# Initialize header
header = "P4\n" + str(N) + " " + str(N)

# Calculate complex constants and iterate Mandelbrot set
pixels = []
for y in range(N):
    row = []
    for x in range(N):
        C = complex(2.0 * x / N - 1.5, 2.0 * y / N - 1.0)
        Z = (0, 0)
        escaped = False
        for _ in range(50):
            Z = (Z[0] * Z[0] - Z[1] * Z[1] + C, 2 * Z[0] * Z[1] + C.imag)
            if Z[0] * Z[0] + Z[1] * Z[1] > 4.0:
                escaped = True
                break
        row.append(1 if escaped else 0)
    pixels.append(row)

# Pack pixels into bytes
binary_data = []
for row in pixels:
    byte = 0
    for bit in row:
        byte |= bit << (7 - row.index(bit))
    binary_data.append(byte)

# Write output
with open("mandelbrot.pbm", "wb") as f:
    f.write(header.encode())
    f.write(bytearray(binary_data))
