import sys
import math

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z[0]**2 + z[1]**2) > 4.0:
            return i
        z = (z[0]**2 + z[1]**2, 2*z[0]*z[1])
    return max_iter

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python mandelbrot.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])

    width, height = N, N
    pixels = [[0]*width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            c = (2.0*x/N - 1.5, 2.0*y/N - 1.0)
            iter_count = mandelbrot(c, 50)
            if iter_count < 50:
                pixels[y][x] = iter_count

    # Pad with zeros if N is not divisible by 8
    padding = (8 - width % 8) % 8
    for row in pixels:
        row.extend([0]*padding)

    print("P4\n{} {}\n".format(width, height))
    for row in pixels:
        byte = b''
        for pixel in row[:width]:
            if pixel == 50:
                # Escape threshold (all bits set)
                byte += b'\xff'
            elif pixel < 8:
                # Pack 1-bit values
                byte += chr(0x80 >> pixel).encode()
            else:
                # Pad with zeros for pixels > 7
                byte += b'\x00'
        print(byte.hex())

if __name__ == "__main__":
    main()
