# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/

import sys

def mandelbrot(n):
    lim = 4.0
    max_iter = 50
    for x in range(n):
        for y in range(n):
            zx, zy, c = 0.0, 0.0, x * 2.0 / n - 1.5 + (y * 2.0 / n - 1.0) * 1j
            for i in range(max_iter):
                if abs(zx*zx + zy*zy) > lim:
                    break
                zx, zy = zx*zx - zy*zy + c.real, 2*zx*zy + c.imag
            print((i < max_iter), end='')

if __name__ == '__main__':
    mandelbrot(int(sys.argv[1]))
