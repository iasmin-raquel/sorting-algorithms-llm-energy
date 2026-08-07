import sys
from PIL import Image


def mandelbrot_set(width, height):
    img = Image.new('P', (width, height)), "black"

    for x in range(0, width):
        real = 2.0 * x / width - 1.5
        imag = 2.0 * y / height - 1.0
        zx, zy = 0, 0
        iteration_count = 0
        while (zr*zr + zi*zi) <= lim and iteration_count < 50:
            zx, zy = zx*zx - zy*zy + real, 2.0 * zx * zy / width + imag
            zr, zi = zx, zy
            iteration_count += 1
        if (zr*zr + zi*zi) <= lim and iteration_count == 50:
            img.putpixel((x, y)), "white"

    return img


def main():
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot.py <N>")
        exit(1)

    try:
        N = int(sys.argv[1]))
    except ValueError:
        print("Error: N must be an integer.")
        exit(1)

    width, height = 800, 600
    img = mandelbrot_set(width, height))
    img.save('mandelbrot.pbm', "PBM")


if __name__ == '__main__':
    main()
