import sys

def mandelbrot(N):
    # Parameters
    max_iterations = 50
    escape_threshold = 4.0
    real_range = [-1.5, 0.5]
    imaginary_range = [-1.0, 1.0]

    # Output PBM P4 header
    print("P3")  # PBM P4 format
    print(f"N {N}")
    print("255")  # Max color value

    for row in range(N):
        for col in range(N):
            # Calculate complex number
            c = complex(-1.5 + (col / N) * (0.5 - (-1.5))), -1.0 + (row / N) * (1.0 - (-1.0)))

            z = 0
            for i in range(max_iterations)):
                z = z*z + c
                if abs(z) > escape_threshold:
                    break

            # Convert to grayscale value (black background))
            pixel_value = 0
            if i == max_iterations:
                pixel_value = 255  # Set pixel to white if escaped

            # Output pixel data as byte
            print(pixel_value.to_bytes(1, 'big'))


if __name__ == "__main__":
    N = int(sys.argv[1])
    mandelbrot(N)
