import sys

# Parse command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    sys.exit("Error: Invalid N value. Please provide a positive integer.")

# Constants
lim = 4.0
max_iterations = 50

# Coordinate mapping
def complex_plane_mapping(x, y):
    return complex(2.0 * x / N - 1.5, 2.0 * y / N - 1.0)

# Mandelbrot iteration
def is_in_mandelbrot(C):
    Z = 0 + 0j
    for _ in range(max_iterations):
        Z = Z**2 + C
        if abs(Z) > lim:
            return False
    return True

# Pack bits into bytes
def pack_bits(bits):
    packed_bytes = []
    byte = 0
    bit_count = 0
    for bit in bits:
        byte |= bit << (7 - bit_count)
        bit_count += 1
        if bit_count == 8:
            packed_bytes.append(byte)
            byte = 0
            bit_count = 0
    if bit_count > 0:
        packed_bytes.append(byte << (8 - bit_count))
    return packed_bytes

# Generate Mandelbrot set image
sys.stdout.buffer.write(b"P4\n" + b"%d %d\n" % (N, N))
bits = []
for y in range(N):
    for x in range(N):
        C = complex_plane_mapping(x, y)
        bits.append(int(is_in_mandelbrot(C)))

# Pack bits and write to output
packed_bytes = pack_bits(bits)
sys.stdout.buffer.write(b"".join(byte.to_bytes(1, "big") for byte in packed_bytes))
