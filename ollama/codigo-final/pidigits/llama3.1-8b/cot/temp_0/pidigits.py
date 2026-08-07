import sys
from decimal import Decimal, getcontext

def next_step(q, r, t, k):
    """Increment k, update r and t, then q."""
    k += 1
    r = (r * 10 + 1) // t
    t *= 3
    q = (q * 10 + r * 8) // t
    return q, r, t, k

def extract(q, x):
    """Compute floor((q*x + r)/t) for x=3 and x=4 to verify correctness."""
    r = q * x
    t = 1
    while r % t == 0:
        r //= t
        t *= x
    return r

def produce(q, r):
    """Adjust q and r based on the extracted digits."""
    if q > r:
        return False
    digit = (r * 10) // q
    q *= 10
    r = (r * 10 + 1) // q
    return digit

def main():
    N = int(sys.argv[1])
    getcontext().prec = N + 5  # Set precision to ensure enough digits
    q, r, t, k = Decimal(1), Decimal(0), Decimal(1), 0
    running_total = 0
    
    while True:
        digit = produce(q, r)
        if digit is False:
            break
        
        running_total += digit
        print(f"{digit:10d}", end='')
        
        # Verify the output with extract(3) and extract(4)
        assert extract(int(q), 3) == int(digit)
        assert extract(int(q), 4) == int(digit)
        
        q, r, t, k = next_step(q, r, t, k)
    
    print("\t:N", N)

if __name__ == "__main__":
    main()
