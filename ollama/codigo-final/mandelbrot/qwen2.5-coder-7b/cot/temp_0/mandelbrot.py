import sys

def mandelbrot(x, y):
    c = complex(x, y)
    z = 0
    for i in range(50):
        if abs(z) > 4.0:
            return i
        z = z*z + c
    return 50

def generate_mandelbrot(N):
    width = N
    height = N
    pixels = bytearray()

    # PBM header
    print("P4")
    print(f"{width} {height}")

    for y in range(height):
        for x in range(width):
            pixel_value = mandelbrot((x / width) * 2.0 - 1.5, (y / height) * 2.0 - 1.0)
            pixels.append(pixel_value >> 7)
            pixels.append(pixel_value >> 6 & 1)
            pixels.append(pixel_value >> 5 & 1)
            pixels.append(pixel_value >> 4 & 1)
            pixels.append(pixel_value >> 3 & 1)
            pixels.append(pixel_value >> 2 & 1)
            pixels.append(pixel_value >> 1 & 1)
            pixels.append(pixel_value & 1)

    # Write binary pixel data
    sys.stdout.buffer.write(bytes(pixels))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot.py <N>")
        sys.exit(1)
    
    N = int(sys.argv[1])
    generate_mandelbrot(N)
