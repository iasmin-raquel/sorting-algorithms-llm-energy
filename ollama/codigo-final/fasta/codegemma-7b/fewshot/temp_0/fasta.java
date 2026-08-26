import java.util.Random;

public class FastaGenerator {
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);

        // LCG constants
        long IM = 139968;
        long IA = 3877;
        long IC = 29573;
        long Seed = 42;

        // ALU sequence
        String alu = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
                "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT" +
                "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG" +
                "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG" +
                "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

        // IUB ambiguity codes and probabilities
        double[] iub = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02};

        // Homo sapiens probabilities
        double[] sapiens = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};

        // Random number generator
        Random random = new Random((int) Seed);

        // Generate sequences
        System.out.println(">ONE Homo sapiens alu");
        for (int i = 0; i < N * 2; i++) {
            System.out.print(alu.charAt(random.nextInt(alu.length())));
            if (i % 60 == 59) {
                System.out.println();
            }
        }

        System.out.println(">TWO IUB ambiguity codes");
        for (int i = 0; i < N * 3; i++) {
            double r = random.nextDouble();
            int index = 0;
            for (double p : iub) {
                if (r < p) {
                    System.out.print(indexToNucleotide(index));
                    break;
                }
                r -= p;
                index++;
            }
            if (i % 60 == 59) {
                System.out.println();
            }
        }

        System.out.println(">THREE Homo sapiens frequency");
        for (int i = 0; i < N * 5; i++) {
            double r = random.nextDouble();
            int index = 0;
            for (double p : sapiens) {
                if (r < p) {
                    System.out.print(indexToNucleotide(index));
                    break;
                }
                r -= p;
                index++;
            }
            if (i % 60 == 59) {
                System.out.println();
            }
        }
    }

    // Convert integer index to nucleotide
    private static char indexToNucleotide(int index) {
        switch (index) {
            case 0: return 'a';
            case 1: return 'c';
            case 2: return 'g';
            case 3: return 't';
            case 4: return 'B';
            case 5: return 'D';
            case 6: return 'H';
            case 7: return 'K';
            case 8: return 'M';
            case 9: return 'N';
            case 10: return 'R';
            case 11: return 'S';
            case 12: return 'V';
            case 13: return 'W';
            case 14: return 'Y';
            default: throw new IllegalStateException("Invalid index");
        }
    }
}
