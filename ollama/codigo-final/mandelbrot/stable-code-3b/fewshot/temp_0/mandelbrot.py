import sys

def mandelbrot(width, height):
    # Initialize the bitmap
    bitmap = [[0 for _ in range(height)] for _ in range(width)]

    # Define the coordinate mapping
    real_min = -2.0
    real_max = 2.0
    imag_min = -1.0
    imag_max = 1.0

    # Define the maximum iterations
    max_iterations = 50

    # Define the escape threshold
    lim = 2.0 * 2.0

    # Iterate over each pixel in the bitmap
    for y in range(height):
        for x in range(width):
            # Calculate the real and imaginary coordinates of the current pixel
            real_coord = (x + 1) / N * (real_max - real_min) + real_min
            imag_coord = (y + 1) / N * (imag_max - imag_min) + imag_min

            # Initialize the complex number Z and the iteration count
            Z = (0, 0)
            iteration_count = 0

            # Iterate until the squared magnitude of Z exceeds lim or we reach max_iterations
            while abs(Z[0]) ** 2 + abs(Z[1]) ** 2 <= lim and iteration_count < max_iterations:
                # Calculate the next complex number in the Mandelbrot sequence
                Z = (Z[0] * Z[0] - Z[1] * Z[1]) / (2.0 * Z[0] + 1.0) + (real_coord, imag_coord))

                # Increment the iteration count
                iteration_count += 1

            # Set the value of the current pixel to the iteration count if it's within the allowed range; otherwise, set it to 0
            if iteration_count <= max_iterations:
                bitmap[x][y] = iteration_count
            else:
                bitmap[x][y] = 0

    # Return the completed bitmap
    return bitmap

def main():
    # Parse the command-line argument N
    N = int(sys.argv[1]))

    # Calculate the width and height of the bitmap
    width = N
    height = N

    # Generate the Mandelbrot set using the specified parameters
    mandelbrot_set = mandelbrot(width, height))

    # Print the header for the PBM P4 image file
    print("P4\n")

    # Print the binary pixel data to stdout
    for row in mandelbrot_set:
        for pixel in row:
            sys.stdout.buffer.write(bytes([pixel])))

if __name__ == "__main__":
    main()
