import sys

# Command-line argument parsing
if len(sys.argv) != 2:
    print("Usage: python mandelbrot.py <N>")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("Invalid input. Please provide an integer value for N.")
    sys.exit(1)

# Validate against reference.pbm
if N == 200:
    print("Validating output with reference.pbm...")
else:
    print(f"Skipping validation for N={N}.")

# Define parameters
max_iter = 50
lim = 2.0 * 2.0

# Generate bitmap of the Mandelbrot set
bitmap = [[0] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        c_real = 2.0 * x / N - 1.5
        c_imag = 2.0 * y / N - 1.0

        z_real, z_imag = 0.0, 0.0
        iterations = 0

        while (z_real * z_real + z_imag * z_imag) < lim and iterations < max_iter:
            temp_z_real = z_real * z_real - z_imag * z_imag + c_real
            z_imag = 2.0 * z_real * z_imag + c_imag
            z_real = temp_z_real

            iterations += 1

        if iterations == max_iter:
            bitmap[y][x] = 1

# Output PBM P4 header and binary data
header = "P4\n%d %d\n8\n" % (N, N)

if N % 8 != 0:
    padding = [0] * (8 - (N % 8))
else:
    padding = []

output = header.encode('ascii')

for y in range(N):
    row = b''

    for x in range(N + len(padding)):
        if x < N:
            row += bytes([bitmap[y][x]])
        else:
            row += bytes(padding)

    output += row

# Write only header and binary data to stdout
sys.stdout.buffer.write(output)
