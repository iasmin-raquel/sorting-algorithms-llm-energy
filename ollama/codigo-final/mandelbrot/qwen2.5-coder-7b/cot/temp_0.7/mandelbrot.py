import sys

def mandelbrot_set(N):
    lim_squared = 2.0 * 2.0
    max_iterations = 50
    
    # Calculate PBM header
    header = f"P4\n{N} {N}\n"
    print(header, end='')
    
    for y in range(N):
        for x in range(N):
            zr, zi = 0, 0
            cr, ci = (2.0 * x / N - 1.5), (2.0 * y / N - 1.0)
            iteration = 0
            
            while zr*zr + zi*zi <= lim_squared and iteration < max_iterations:
                zr_new = zr*zr - zi*zi + cr
                zi_new = 2*zr*zi + ci
                zr, zi = zr_new, zi_new
                iteration += 1
            
            # Write binary pixel data to stdout
            if iteration == max_iterations:
                print('0', end='', flush=True)  # Black pixel (inset)
            else:
                print('1', end='', flush=True)  # White pixel (outside set)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot.py <N>")
        sys.exit(1)
    
    N = int(sys.argv[1])
    mandelbrot_set(N)
