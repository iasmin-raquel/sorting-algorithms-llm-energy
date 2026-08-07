import sys

def mandelbrot_set(N):
    lim_squared = 2.0 * 2.0
    max_iterations = 50
    
    # PBM header
    print("P4")
    print(f"{N} {N}")
    
    for y in range(N):
        for x in range(N):
            zr, zi = 0.0, 0.0
            cr = 2.0 * x / N - 1.5
            ci = 2.0 * y / N - 1.0
            iteration = 0
            
            while (zr*zr + zi*zi) <= lim_squared and iteration < max_iterations:
                zr_new = zr*zr - zi*zi + cr
                zi = 2.0 * zr * zi + ci
                zr, zi = zr_new, zi
                iteration += 1
            
            # Determine if the point is in the set
            pixel_value = 0 if iteration == max_iterations else 1
            print(chr(pixel_value), end='')
        
        # Pad row with zeros if N is not divisible by 8
        padding = (N % 8)
        if padding != 0:
            print(''.join(['\x00'] * (8 - padding)), end='')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot.py <N>")
        sys.exit(1)
    
    N = int(sys.argv[1])
    mandelbrot_set(N)
