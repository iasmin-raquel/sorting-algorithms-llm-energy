import sys

def mandelbrot(width, height):
    # Initialize the image with all white pixels
    image = [[255] * width for _ in range(height)]

    for x in range(width):
        for y in range(height):
            # Calculate the complex number C based on the coordinate mapping
            real_C = 2.0 * x / (width - 1) - 1.5
            imag_C = 2.0 * y / (height - 1) - 1.0

            # Initialize Z to the initial value
            Z = (0, 0)

            # Perform the Mandelbrot set calculation for each point
            for _ in range(50):
                # Calculate Z' = Z\*Z + C
                Z_squared = Z[0] ** 2 - Z[1] ** 2
                Z_prime = (Z_squared * real_C - imag_C * Z[0] * Z[1]),
                               (Z_squared * imag_C + real_C * Z[0] * Z[1]))

                # Check if |Z'|² <= lim after each iteration
                if abs(Z_prime[0]) ** 2 + abs(Z_prime[1]) ** 2 <= lim:
                    break

                # Update Z to Z'
                Z = Z_prime

            # Set the pixel color based on whether the point belongs to the set or not
            if abs(Z[0]) ** 2 + abs(Z[1]) ** 2 <= lim:
                image[y][x] = [0, 0, 255]  # Blue pixel for in set
            else:
                image[y][x] = [255, 255, 255]  # White pixel for not in set

    return image

def write_pbm(width, height):
    header = f"P4\n{width} {height}\n"
    pixel_data = "".join([f"{i:08b}" for i in [0] * (width // 8) + [1] * width])

    output = header + pixel_data
    print(output)

if __name__ == "__main__":
    N = int(sys.argv[1]))
    image = mandelbrot(N, N))
    write_pbm(N, N))
