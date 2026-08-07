#include <iostream>
#include <gmpxx.h>

using namespace std;

mpz_class q(1), r(0), t(1);
int k = 0;

void next_step() {
    k++;
    r = (2*q + r) * (2*k + 1);
    t *= (2*k + 1);
    q = q * k;
}

mpz_class extract(mpz_class x) {
    return (q * x + r) / t;
}

void produce(mpz_class d) {
    q *= 10;
    r = (r - t * d) * 10;
}

int main() {
    int N;

    // Parse input
    cin >> N;

    // Output header
    cout << "3.";

    // Generate digits
    while (true) {
        mpz_class d1 = extract(3);
        mpz_class d2 = extract(4);

        if (d1 == d2) {
            cout << d1;
            produce(d1);
            if (q > r) {
                break;
            }
        } else {
            next_step();
        }
    }

    // Output total digits
    cout << "\t:" << k << endl;

    return 0;
}
