import sys

def mandelbrot(c, lim=4.0):
    z = complex(0, 0)
    for i in range(50):
        z = z*z + c
        if abs(z) > lim:
            return i
    return 50

def generate_image(N):
    width = N
    height = int(1.33 * N)  # aspect ratio of Mandelbrot set is approximately 3:2
    image_data = bytearray(width*height)

    for y in range(height):
        for x in range(width):
            c = complex(2.0*x/N - 1.5, 2.0*y/N - 1.0)
            pixel_value = mandelbrot(c)
            if pixel_value == 50:
                # pixel is not part of the Mandelbrot set
                image_data[y*width+x] = 0
            else:
                # pack 8 bits per byte, MSB first
                byte_value = (pixel_value & 1) | ((pixel_value >> 1) & 2) | ((pixel_value >> 2) & 4) | ((pixel_value >> 3) & 8)
                image_data[y*width+x] = byte_value

    # pad with zeros if N is not divisible by 8
    padding_bytes = (width % 8) * height
    image_data += b'\x00' * padding_bytes

    return image_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot.py <N>")
        sys.exit(1)

    N = int(sys.argv[1])
    image_data = generate_image(N)

    # write PBM P4 header and binary pixel data to stdout
    print("P4\n", N, " ", int(1.33 * N), "\n")
    sys.stdout.buffer.write(image_data)
