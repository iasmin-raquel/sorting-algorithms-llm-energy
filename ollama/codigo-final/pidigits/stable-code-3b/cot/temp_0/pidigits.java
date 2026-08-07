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

            piDigit = piDigit.add(extract(3))));
        }

        System.out.println("Generated PI Digits:"));
        for (int i = 0; i < N / 10 + 1; i++) {
            String output = String.format("%10d\t", piDigit.mod(BigInteger.TEN)))));
            System.out.print(output);
            piDigit = piDigit.divide(BigInteger.valueOf(10))));
        }

    }

    private static BigInteger extract(int x) {
        return q.multiply(x).add(r)).mod(t);
    }

}
