import sys

# Input validation
try:
    N = int(sys.argv[1])
except ValueError:
    sys.exit("Invalid input: N must be an integer.")
if N <= 0 or N > 1000:
    sys.exit("Invalid input: N must be between 1 and 1000.")

# Output header
print("P4\n" + str(N) + " " + str(N))

# Iterate over pixels
for y in range(N):
    byte = 0
    for x in range(N):
        # Calculate complex constant
        C_real = 2.0 * x / N - 1.5
        C_imag = 2.0 * y / N - 1.0

        # Mandelbrot iteration
        Z = (0, 0)
        for _ in range(50):
            Z = (Z[0]**2 - Z[1]**2 + C_real, 2*Z[0]*Z[1] + C_imag)
            if Z[0]**2 + Z[1]**2 > 4.0:
                byte |= 1
                break

    # Write packed byte to output
    sys.stdout.write(bytes([byte]))

# Flush output
sys.stdout.flush()
