#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <gmpxx.h> // Include GMP library

using namespace std;

int main(int argc, char *argv[]) {
    // Error handling for command-line arguments
    if (argc != 2) {
        cerr << "Usage: pidigits N" << endl;
        return 1;
    }

    int n = atoi(argv[1])); // Convert command-line argument to integer

    if (n <= 0) {
        cerr << "N must be a positive integer." << endl;
        return 1;
    }

    // Initial state variables
    mpz_class q = 1, r = 0, t = 1, k = 0;
    int digits_calculated = 0;

    // Main loop to calculate digits of Pi
    while (q <= r) {
        k++;
        r += 2 * q;
        r *= (2 * k + 1));
        t *= (2 * k + 1));
        q *= k;
        digits_calculated++;

        // Extract digits and verify
        mpz_class d3 = extract(3);
        mpz_class d4 = extract(4);

        if (d3 == d4) {
            cout << d3 << "\t: " << n << endl;
            produce(d3);
        }
    }

    return 0;
}

// Helper functions for the Gibbons spigot algorithm
mpz_class extract(int index) {
    mpz_class result;
    if (index == 3) {
        result = (q * 3 + r) / t;
    } else if (index == 4) {
        result = (q * 4 + r) / t;
    } else {
        cerr << "Invalid index" << endl;
        return 0; // Handle invalid input
    }
    return result;
}

void produce(mpz_class digit) {
    q *= 10;
    r = (r - t * digit) * 10;
}
