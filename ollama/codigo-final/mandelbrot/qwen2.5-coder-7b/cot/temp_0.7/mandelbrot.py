import sys
import struct

# Function to calculate if a point belongs to the Mandelbrot set
def mandelbrot(c, max_iter):
    zr, zi = 0.0, 0.0
    lim_sq = 2.0 * 2.0
    for n in range(max_iter):
        zr_new = zr*zr - zi*zi + c[0]
        zi_new = 2*zr*zi + c[1]
        if zr_new*zr_new + zi_new*zi_new > lim_sq:
            return n
        zr, zi = zr_new, zi_new
    return max_iter

# Main function to generate Mandelbrot set and output PBM P4 format
def main():
    N = int(sys.argv[1])
    max_iter = 50
    lim_sq = 2.0 * 2.0
    
    # Generate the bitmap data
    bitmap = bytearray()
    for y in range(N):
        for x in range(N):
            c = (2.0 * x / N - 1.5, 2.0 * y / N - 1.0)
            iter_count = mandelbrot(c, max_iter)
            pixel_value = 0 if iter_count == max_iter else 1
            bitmap.append(pixel_value)
        
        # Pad the last byte of each row with zeros on the right if needed
        if N % 8 != 0:
            padding = 8 - (N % 8)
            bitmap.extend([0] * padding)

    # Output PBM P4 header and binary pixel data to stdout
    sys.stdout.write(f"P4\n{N} {N}\n")
    sys.stdout.buffer.write(bitmap)

if __name__ == "__main__":
    main()
