import java.util.Random;
import java.io.*;
import java.nio.charset.StandardCharsets;

public class Main {

    static final int IM = 139968, IA = 3877, IC = 29573, Seed = 42;
    static final String ALU_SEQ = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
            "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAATACAAA" +
            "AATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACC" +
            "CGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAA" +
            "AAA";
    static final double[] IUB_PROBS = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
            0.02, 0.02, 0.02, 0.02, 0.02};
    static final double[] HUMAN_PROBS = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};

    public static void main(String[] args) throws Exception {
        int N = Integer.parseInt(args[0]);
        Random rand = new Random(Seed);

        // Repeat Fasta
        System.out.println("Repeat Fasta");
        double[] probs = {0.25, 0.25, 0.25, 0.25};
        System.out.print(generateSeq(ALU_SEQ, N * 2));
        for (int i = 1; i < 4; i++) {
            System.out.print("\n" + generateSeq(ALU_SEQ, N * 3));
        }

        // Random Fasta IUB
        System.out.println("\nRandom Fasta IUB");
        probs = IUB_PROBS;
        for (int i = 0; i < 2; i++) {
            System.out.print("\n" + generateSeq(probs, N * 5));
        }

        // Random Fasta Homo sapiens
        System.out.println("\nRandom Fasta Homo sapiens");
        probs = HUMAN_PROBS;
        for (int i = 0; i < 1; i++) {
            System.out.print("\n" + generateSeq(probs, N * 2));
        }
    }

    private static String generateSeq(String seq, int n) throws Exception {
        double[] probs = getProbs(seq);
        int length = (int) Math.ceil((double) n / 60); // Ensure output is at least 60 characters long
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            String s = generateNucleotide(probs, rand.nextLong());
            sb.append(s);
            if ((i + 1) * 60 <= n) {
                sb.append("\n");
            }
        }

        return sb.toString();
    }

    private static double[] getProbs(String seq) {
        double sum = 0;
        for (int i = 0; i < seq.length(); i++) {
            switch (seq.charAt(i)) {
                case 'G':
                case 'C':
                    sum += HUMAN_PROBS[1]; // Add c and g probabilities
                    break;
                case 'T':
                case 'A':
                    sum += HUMAN_PROBS[3]; // Add t and a probabilities
                    break;
            }
        }

        double[] probs = new double[HUMAN_PROBS.length];
        for (int i = 0; i < HUMAN_PROBS.length; i++) {
            probs[i] = HUMAN_PROBS[i] / sum;
        }
        return probs;
    }

    private static String generateNucleotide(double[] probs, long seed) {
        double r = rand.nextDouble();
        for (int i = 0; i < probs.length; i++) {
            if (r <= probs[i]) {
                switch (i) {
                    case 0:
                        return "A";
                    case 1:
                        return "C";
                    case 2:
                        return "G";
                    case 3:
                        return "T";
                }
            } else {
                r -= probs[i];
            }
        }

        throw new RuntimeException("Invalid probabilities");
    }

    private static Random rand = new Random();

}
