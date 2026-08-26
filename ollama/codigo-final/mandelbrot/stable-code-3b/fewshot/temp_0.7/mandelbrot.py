import sys

def mandelbrot(width, height):
    # Initialize a 2D array for storing the pixel values
    pixels = [[0] * 256 for _ in range(height)]

    for y in range(height):
        for x in range(width):
            real = 2.0 * x / width - 1.5
            imag = 2.0 * y / height - 1.0

            z_r, z_i = 0.0, 0.0
            for _ in range(50):
                z_r_next, z_i_next = z_r * z_r + real * z_r + imag * z_i, 2.0 * z_i + imag

                if z_r_next ** 2 + z_i_next ** 2 > lim:
                    break

                z_r, z_i = z_r_next, z_i_next

            # Calculate the squared magnitude to avoid computing square roots
            magnitude = z_r * z_r + z_i * z_i

            # Convert the squared magnitude to a color value in RGB format
            red, green, blue = 0.0, 0.0, 0.0

            if magnitude >= lim:
                red = 255.0
            elif magnitude >= 1.0:
                green = int(255.0 * (magnitude - 1.0) / (lim - 1.0))))
            else:
                blue = int(255.0 * magnitude))

            # Convert the RGB values to bytes and store them in the 2D array
            red_byte, green_byte, blue_byte = int(red), int(green), int(blue))
            pixels[y][x] = [red_byte, green_byte, blue_byte]

    # Write the header "P4\n" followed by "N N\n" to stdout
    sys.stdout.write("P4\n")
    sys.stdout.write(f"{width} {height}\n"))

    # Iterate over each row and column of the 2D array, convert the RGB values to bytes, and write them byte-by-byte to stdout
    for y in range(height):
        for x in range(width):
            red_byte, green_byte, blue_byte = pixels[y][x]
            sys.stdout.buffer.write(bytes([red_byte, green_byte, blue_byte])))


if __name__ == "__main__":
    # Get the command-line argument N (integer)
    N = int(input("Enter an integer for N: "))))

    # Call the mandelbrot function with the specified width and height
    mandelbrot(N, N))
