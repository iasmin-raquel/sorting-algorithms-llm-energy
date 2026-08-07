import java.util.Random;

public class FastaGenerator {

    private static final String ALU_SEQUENCE = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
            "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAA" +
            "TACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGA" +
            "AATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGG" +
            "CGACAGAGCGAGACTCCGTCTCAAAAA";

    private static final double[] IUB_PROBABILITIES = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02,
            0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02};

    private static final double[] HOMO_SAPIENS_PROBABILITIES = {0.3029549426680, 0.1979883004921,
            0.1975473066391, 0.3015094502008};

    public static void main(String[] args) {
        int N = 1000;
        Random random = new Random(42);
        LCG lcg = new LCG(random.nextInt(), 139968, 3877, 29573);

        double[] cumulativeProbabilitiesIUB = calculateCumulativeProbabilities(IUB_PROBABILITIES);
        double[] cumulativeProbabilitiesHomoSapiens = calculateCumulativeProbilities(HOMO_SAPIENS_PROBABILITIES);

        String repeatFastaALU = generateRepeatFasta(ALU_SEQUENCE, N * 2);
        String randomFastaIUB = generateRandomFasta(cumulativeProbabilitiesIUB, lcg, N * 3);
        String randomFastaHomoSapiens = generateRandomFasta(cumulativeProbabilitiesHomoSapiens, lcg, N * 5);

        System.out.println(">ONE Homo sapiens alu");
        System.out.println(repeatFastaALU);
        System.out.println(">TWO IUB alphabet random");
        System.out.println(randomFastaIUB);
        System.out.println(">THREE Homo sapiens random");
        System.out.println(randomFastaHomoSapiens);
    }

    private static String generateRepeatFasta(String sequence, int length) {
        StringBuilder repeatFasta = new StringBuilder();
        for (int i = 0; i < length / sequence.length(); i++) {
            repeatFasta.append(sequence).append("\n");
        }
        if (length % sequence.length() != 0) {
            repeatFasta.append(sequence.substring(0, length % sequence.length())).append("\n");
        }
        return repeatFasta.toString();
    }

    private static String generateRandomFasta(double[] cumulativeProbabilities, LCG lcg, int length) {
        StringBuilder randomFasta = new StringBuilder();
        for (int i = 0; i < length / 4; i++) {
            double randomNumber = lcg.next();
            int nucleotideIndex = getNucleotideIndex(cumulativeProbabilities, randomNumber);
            String nucleotide = getNucleotide(nucleotideIndex);
            randomFasta.append(nucleotide).append("\n");
        }
        if (length % 4 != 0) {
            double randomNumber = lcg.next();
            int nucleotideIndex = getNucleotideIndex(cumulativeProbabilities, randomNumber);
            String nucleotide = getNucleotide(nucleotideIndex);
            randomFasta.append(nucleotide).append("\n");
        }
        return randomFasta.toString();
    }

    private static double[] calculateCumulativeProbabilities(double[] probabilities) {
        double cumulativeProbability = 0;
        for (int i = 0; i < probabilities.length; i++) {
            cumulativeProbability += probabilities[i];
            probabilities[i] = cumulativeProbability;
        }
        return probabilities;
    }

    private static int getNucleotideIndex(double[] cumulativeProbabilities, double randomNumber) {
        for (int i = 0; i < cumulativeProbabilities.length; i++) {
            if (randomNumber <= cumulativeProbabilities[i]) {
                return i;
            }
        }
        throw new RuntimeException("Random number out of range");
    }

    private static String getNucleotide(int index) {
        switch (index) {
            case 0:
                return "a";
            case 1:
                return "c";
            case 2:
                return "g";
            case 3:
                return "t";
            default:
                return String.valueOf((char) ('B' + index));
        }
    }

    private static class LCG {
        private int state;

        public LCG(int seed, int im, int ia, int ic) {
            this.state = seed;
        }

        public double next() {
            state = (int) ((ia * state + ic) % im);
            return state / (double) im;
        }
    }
}
