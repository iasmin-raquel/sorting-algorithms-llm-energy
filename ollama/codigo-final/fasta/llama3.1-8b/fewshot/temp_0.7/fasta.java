import java.util.Random;
import java.io.*;

public class Fasta {
    static final Random rand = new Random(42);

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(args[0]);

        String alu = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
                "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

        String iub = "acgtbdfhmnsprvwyk";
        double[] iubProb = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02};

        String human = "acgt";
        double[] humanProb = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};

        PrintWriter out = new PrintWriter(System.out);

        for (int n=1; n <= N; n *= 10) {
            String aluSeq = repeatFasta(alu, n * 2);
            String iubSeq = randomFasta(iub, n * 3, iubProb);
            String humanSeq = randomFasta(human, n * 5, humanProb);

            out.println(">ONE Homo sapiens alu");
            out.println(aluSeq);
            out.println();

            out.println(">TWO IUB ambiguity codes");
            out.println(iubSeq);
            out.println();

            out.println(">THREE Homo sapiens frequency");
            out.println(humanSeq);
            out.println();
        }

        out.close();
    }

    static String repeatFasta(String s, int n) {
        StringBuilder sb = new StringBuilder(n);
        for (int i=0; i < n / s.length(); i++) {
            sb.append(s);
        }
        if ((n % s.length()) != 0) {
            sb.append(s.substring(0, n % s.length()));
        }

        return sb.toString();
    }

    static String randomFasta(String s, int n, double[] prob) {
        StringBuilder sb = new StringBuilder(n);

        for (int i=0; i < n; i++) {
            int r = rand.nextInt(s.length());
            if (s.charAt(r) == 'B' || s.charAt(r) == 'D' ||
                    s.charAt(r) == 'H' || s.charAt(r) == 'K' ||
                    s.charAt(r) == 'M' || s.charAt(r) == 'N' ||
                    s.charAt(r) == 'R' || s.charAt(r) == 'S' ||
                    s.charAt(r) == 'V' || s.charAt(r) == 'W') {
                r = rand.nextInt(s.length());
            }
            sb.append(s.charAt(r));
        }

        return sb.toString();
    }

    static long lcg(long seed, int im, int ia, int ic) {
        return (ia * seed + ic) % im;
    }
}
