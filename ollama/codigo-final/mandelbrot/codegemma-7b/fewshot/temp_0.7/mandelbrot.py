import sys

MANDELBROT_PARAMETERS = {
    "max_iter": 50,
    "escape_threshold": 4.0,
    "x_range": [-1.5, 0.5],
    "y_range": [-1.0, 1.0]
}

def mandelbrot(complex_number):
    z = 0
    for i in range(MANDELBROT_PARAMETERS["max_iter"]):
        z = z**2 + complex_number
        if abs(z) > MANDELBROT_PARAMETERS["escape_threshold"]:
            return i
    return 0

def main(N):
    width, height = N, N
    header = f"P4\n{width} {height}\n"

    x_scale = (MANDELBROT_PARAMETERS["x_range"][1] - MANDELBROT_PARAMETERS["x_range"][0]) / width
    y_scale = (MANDELBROT_PARAMETERS["y_range"][1] - MANDELBROT_PARAMETERS["y_range"][0]) / height

    pixels = []
    for x in range(width):
        for y in range(height):
            complex_number = complex(
                MANDELBROT_PARAMETERS["x_range"][0] + x * x_scale,
                MANDELBROT_PARAMETERS["y_range"][0] + y * y_scale
            )
            pixels.append(mandelbrot(complex_number))

    # Pack bits per row, MSB first
    packed_bits = sum(row << (i * width) for i, row in enumerate(pixels))

    print(header, end="")
    sys.stdout.write(packed_bits.to_bytes())

if __name__ == "__main__":
    main(int(sys.argv[1]))
