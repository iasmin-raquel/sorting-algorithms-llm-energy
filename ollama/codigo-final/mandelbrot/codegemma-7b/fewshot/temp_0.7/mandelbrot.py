import sys

N = int(sys.argv[1])
max_iterations = 50
lim = 4.0

print("P4\n{N} {N}".format(N=N))

for y in range(N):
    row = 0
    for x in range(N):
        c = complex(2 * x / N - 1.5, 2 * y / N - 1)
        z = 0
        for i in range(max_iterations):
            if abs(z) > lim:
                row += 2**i
                break
            z = z**2 + c

    while row % 256:
        print(row & 255, end=" ")
        row >>= 8
    print(row)
