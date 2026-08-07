import java.util.Random;

public class DNASequenceGenerator {
    private static final String ALU_SEQUENCE = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
            "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT" +
            "AAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG" +
            "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCG" +
            "CCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";
    private static final double[] IUB_PROBABILITIES = {0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02};
    private static final double[] HOMO_SAPIENS_PROBABILITIES = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};
    private static final int IM = 139968;
    private static final int IA = 3877;
    private static final int IC = 29573;
    private static final int SEED = 42;

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java DNASequenceGenerator <N>");
            return;
        }

        int N = Integer.parseInt(args[0]);
        Random random = new Random(SEED);

        // Generate ALU sequence
        StringBuilder aluSequence = new StringBuilder();
        for (int i = 0; i < N; ) {
            int index = random.nextInt(ALU_SEQUENCE.length());
            char nucleotide = ALU_SEQUENCE.charAt(index);
            if (nucleotide != ' ') { // Ignore spaces in the ALU sequence
                aluSequence.append(nucleotide);
                i++;
            }
        }

        // Generate IUB sequence
        StringBuilder iubSequence = new StringBuilder();
        for (int i = 0; i < N; ) {
            double randomValue = random.nextDouble();
            int index = 0;
            while (randomValue > IUB_PROBABILITIES[index]) {
                randomValue -= IUB_PROBABILITIES[index];
                index++;
            }
            char nucleotide = "ACGTBDHKMNRYSVWY".charAt(index);
            iubSequence.append(nucleotide);
        }

        // Generate Homo sapiens sequence
        StringBuilder homoSapiensSequence = new StringBuilder();
        for (int i = 0; i < N; ) {
            double randomValue = random.nextDouble();
            int index = 0;
            while (randomValue > HOMO_SAPIENS_PROBABILITIES[index]) {
                randomValue -= HOMO_SAPIENS_PROBABILITIES[index];
                index++;
            }
            char nucleotide = "ACGT".charAt(index);
            homoSapiensSequence.append(nucleotide);
        }

        // Output sequences
        System.out.println(">ALU");
        for (int i = 0; i < aluSequence.length(); i += 60) {
            System.out.println(aluSequence.substring(i, Math.min(i + 60, aluSequence.length())));
        }
        System.out.println(">IUB");
        for (int i = 0; i < iubSequence.length(); i += 60) {
            System.out.println(iubSequence.substring(i, Math.min(i + 60, iubSequence.length())));
        }
        System.out.println(">Homo sapiens");
        for (int i = 0; i < homoSapiensSequence.length(); i += 60) {
            System.out.println(homoSapiensSequence.substring(i, Math.min(i + 60, homoSapiensSequence.length())));
        }
    }
}
