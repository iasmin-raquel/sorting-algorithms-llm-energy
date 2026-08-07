import sys
import numpy as np

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z*z + c
    return max_iter

def generate_bitmap(N):
    bitmap = np.zeros((N,N), dtype=np.uint8)
    
    for x in range(N):
        for y in range(N):
            c = complex(2.0 * x / N - 1.5, 2.0 * y / N - 1.0)
            bitmap[y,x] = mandelbrot(c, 50)
            
    return bitmap

def output_pbm(bitmap, filename):
    with open(filename, 'wb') as f:
        f.write(b"P4\n")
        f.write(f"{bitmap.shape[0]} {bitmap.shape[1]}\n".encode())
        
        for row in bitmap:
            # Pad the row to a multiple of 8
            padded_row = np.pad(row, (0, 7 - len(row) % 8), mode='constant')
            
            # Convert to bytes and write to file
            f.write(padded_row.astype(np.uint8).tobytes())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mandelbrot.py <N>")
        sys.exit(1)
        
    N = int(sys.argv[1])
    
    bitmap = generate_bitmap(N)
    
    # Validate output for N=200
    if N == 200:
        reference_filename = "mandelbrot_200.pbm"
        output_pbm(bitmap, reference_filename)
        cmp_output(reference_filename)
        
    output_pbm(bitmap, f"mandelbrot_{N}.pbm")

def cmp_output(filename):
    # This function is not implemented as it's not clear what the comparison should be
    # You may need to implement a custom comparison function based on your specific requirements
    pass
