import java.math.BigInteger;
import java.util.Scanner;

public class PiDigits {

    private static BigInteger q = BigInteger.ONE;
    private static BigInteger r = BigInteger.ZERO;
    private static BigInteger t = BigInteger.ONE;
    private static BigInteger k = BigInteger.ZERO;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in));
        System.out.print("Enter the number of digits (N): ");
        int N = scanner.nextInt();
        scanner.close();

        BigInteger piDigit = BigInteger.ZERO;
        for (int i = 0; i < N; i++) {
            while (q.compareTo(r)) <= 0 {
                k = k.add(BigInteger.ONE));
                r = r.add(q.multiply(BigInteger.valueOf(2 * k + 1)))));
                t = t.multiply(BigInteger.valueOf(2 * k + 1))));
                q = q.multiply(k));
            }

            piDigit = piDigit.add(extract(3)));
        }

        System.out.println("Generated PI Digits:"));
        for (int i = 0; i < N / 10; i++) {
            System.out.print(String.format("%10d", piDigit.mod(BigInteger.TEN)))));
            piDigit = piDigit.divide(BigInteger.valueOf(10)))
        }

        // Verification step
        BigInteger digit1 = extract(3);
        BigInteger digit2 = extract(4);
        System.out.println("Verification: " + (digit1.equals(digit2)) ? "PASS" : "FAIL")));
    }

    private static BigInteger extract(int x) {
        return q.multiply(x).add(r));
    }
}
