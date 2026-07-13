import sys

def mandelbrot_set(N):
    # Define constants based on problem requirements
    max_iter = 50
    escape_threshold = 4.0
    real_range = (-1.5, 0.5)
    imag_range = (-1.0, 1.0)

    # Calculate the step size for real and imaginary axes
    real_step = (real_range[1] - real_range[0]) / N
    imag_step = (imag_range[1] - imag_range[0]) / N

    # Generate the Mandelbrot set
    pixels = bytearray()
    for i in range(N):
        for j in range(N):
            # Calculate the initial complex number z and c
            real = real_range[0] + j * real_step
            imag = imag_range[1] - i * imag_step
            z_real, z_imag = 0.0, 0.0
            iteration = 0

            # Iterate until the escape condition is met or max_iter is reached
            while (z_real * z_real + z_imag * z_imag) < escape_threshold and iteration < max_iter:
                temp_real = z_real * z_real - z_imag * z_imag + real
                z_imag = 2 * z_real * z_imag + imag
                z_real = temp_real
                iteration += 1

            # Set the pixel color based on the number of iterations
            pixels.append(0 if iteration == max_iter else 1)

    # Write the PBM P4 header and binary data to stdout
    print("P4")
    print(N, N)
    sys.stdout.buffer.write(pixels)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot.py <N>")
        sys.exit(1)
    N = int(sys.argv[1])
    mandelbrot_set(N)
