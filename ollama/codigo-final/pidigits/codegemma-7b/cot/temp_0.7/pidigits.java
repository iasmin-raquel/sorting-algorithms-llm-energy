import java.math.BigInteger;

public class Pidigits {

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        BigInteger q = BigInteger.ONE;
        BigInteger r = BigInteger.ZERO;
        BigInteger t = BigInteger.ONE;
        int k = 0;
        int count = 0;

        while (true) {
            next_step(q, r, t, k);
            int d = extract(3, q, r, t);
            if (d == extract(4, q, r, t)) {
                System.out.print(d);
                produce(d, q, r, t);
                count++;
                if (count % 10 == 0) {
                    System.out.print("\t:" + N);
                    if (count == N) {
                        break;
                    }
                    System.out.println();
                }
            }
        }
    }

    private static void next_step(BigInteger q, BigInteger r, BigInteger t, int k) {
        k++;
        r = r.multiply(BigInteger.TWO).add(q);
        r = r.multiply(BigInteger.valueOf(2 * k + 1));
        t = t.multiply(BigInteger.valueOf(2 * k + 1));
        q = q.multiply(BigInteger.valueOf(k));
    }

    private static int extract(int x, BigInteger q, BigInteger r, BigInteger t) {
        return (int) ((q.multiply(BigInteger.valueOf(x)).add(r)).divide(t)).longValue();
    }

    private static void produce(int d, BigInteger q, BigInteger r, BigInteger t) {
        q = q.multiply(BigInteger.TEN);
        r = r.subtract(t.multiply(BigInteger.valueOf(d))).multiply(BigInteger.TEN);
    }
}
