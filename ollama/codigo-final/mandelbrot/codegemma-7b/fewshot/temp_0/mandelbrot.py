import sys

def mandelbrot_pbm(N):
    lim = 2.0 * 2.0
    max_iter = 50

    # Header
    sys.stdout.write("P4\n")
    sys.stdout.write(f"{N} {N}\n")

    # Coordinate mapping and iteration
    for y in range(N):
        for x in range(N):
            c_real = 2.0 * x / N - 1.5
            c_imag = 2.0 * y / N - 1.0

            z_real, z_imag = 0.0, 0.0
            iter_count = 0
            while (z_real*z_real + z_imag*z_imag <= lim) and (iter_count < max_iter):
                new_z_real = z_real * z_real - z_imag * z_imag + c_real
                new_z_imag = 2.0 * z_real * z_imag + c_imag
                z_real, z_imag = new_z_real, new_z_imag
                iter_count += 1

            # Pack bits
            pixel_byte = (iter_count == max_iter) << 7
            sys.stdout.buffer.write(pixel_byte.to_bytes(1, byteorder='big'))

        # Padding
        padding = (N % 8) * 0xFF
        sys.stdout.buffer.write(padding.to_bytes((N + 7) // 8, byteorder='big'))

if __name__ == "__main__":
    N = int(sys.argv[1])
    mandelbrot_pbm(N)
