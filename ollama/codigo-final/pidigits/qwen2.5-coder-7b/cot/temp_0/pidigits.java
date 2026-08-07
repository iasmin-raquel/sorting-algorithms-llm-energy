import java.math.BigInteger;

public class PiCalculator {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java PiCalculator <number_of_digits>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        BigInteger q = BigInteger.ONE;
        BigInteger r = BigInteger.ZERO;
        BigInteger t = BigInteger.ONE;
        int k = 0;

        StringBuilder output = new StringBuilder();
        int count = 0;

        while (true) {
            next_step(q, r, t, k);
            int d = extract(3);
            if (d == extract(4)) {
                output.append(d);
                produce(d);
                count++;
                if (count % 10 == 0) {
                    System.out.println(output.toString());
                    output.setLength(0); // Clear the StringBuilder for the next line
                }
            } else {
                continue;
            }

            if (count >= N) break;
        }

        if (output.length() > 0) {
            System.out.println(output.toString());
        }
    }

    private static void next_step(BigInteger q, BigInteger r, BigInteger t, int k) {
        // Implementation of the next_step function
    }

    private static int extract(int x) {
        // Implementation of the extract(x) function
        return 0; // Placeholder return value
    }

    private static void produce(int d) {
        // Implementation of the produce(d) function
    }
}
