import sys
from math import *
import array

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z.real*z.real + z.imag*z.imag) > 4.0:
            return n
        z = complex(z.real**2 - z.imag**2 + c.real, 2*z.real*z.imag + c.imag)
    return max_iter

def main():
    N = int(sys.argv[1])
    output = open('output.pbm', 'wb')
    if N == 200:
        reference = open('reference.pbm', 'rb').read()

    output.write(b'P4\n%d %d\n'% (N, N))
    padding = (8 - N%8)%8
    for y in range(N):
        for x in range(N):
            c = complex(2.0 * x / N - 1.5, 2.0 * y / N - 1.0)
            output.write(bytes([mandelbrot(c, 50)]))
        if padding: output.write(b'\x00'*padding)

    output.close()
    if N == 200:
        import filecmp
        assert(filecmp.cmp('output.pbm', 'reference.pbm'))

if __name__ == "__main__":
    main()
