import sys
from math import sqrt, pow

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z*z + c
    return max_iter

def main():
    N = int(sys.argv[1])
    width = N
    height = N
    max_iter = 50
    lim = 2.0 * 2.0

    # Coordinate mapping
    xmin = -2.5
    xmax = 1.5
    ymin = -1.5
    ymax = 1.5

    # PBM header
    with open('mandelbrot.pbm', 'w') as f:
        f.write('P4\n')
        f.write(f'{width} {height}\n')
        f.write('8\n')

    # Binary pixel data
    pixels = bytearray(width * height)
    for y in range(height):
        for x in range(width):
            c = complex(2.0 * (x / N - 1.5), 2.0 * (y / N - 1.0))
            n = mandelbrot(c, max_iter)
            if n == max_iter:
                pixels[y * width + x] |= 0xFF
            else:
                pixels[y * width + x] &= ~0xFF

    # Pad with zeros if N not divisible by 8
    padding = (8 - (width % 8)) % 8
    pixels += bytearray(padding * height)

    # Write binary pixel data to file
    with open('mandelbrot.pbm', 'ab') as f:
        f.write(pixels)

if __name__ == '__main__':
    main()
