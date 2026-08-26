import sys

def mandelbrot(n):
    lim = 4.0  # Escape threshold squared
    max_iter = 50  # Maximum number of iterations
    header = f"P4\n{n} {n}\n"
    print(header, end='')
    
    for y in range(n):
        for x in range(n):
            zx, zy = 0.0, 0.0
            cx = 2.0 * x / n - 1.5
            cy = 2.0 * y / n - 1.0
            iter_count = 0
            
            while (zx*zx + zy*zy <= lim) and (iter_count < max_iter):
                zx, zy = zx*zx - zy*zy + cx, 2.0*zx*zy + cy
                iter_count += 1
            
            # Determine if the pixel is in the set
            pixel_value = 0 if iter_count == max_iter else 1
            print(chr(pixel_value), end='', flush=False)
        
        # Pad with zeros if necessary to ensure 8 bits per byte
        padding = (n % 8) or 8
        for _ in range(padding):
            print('\x00', end='', flush=False)

if __name__ == '__main__':
    mandelbrot(int(sys.argv[1]))
