import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        int N = Integer.parseInt(args[0]);
        String ALU = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
                "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACT" +
                "AAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAG" +
                "GCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCA" +
                "CTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";

        Random random = new Random(42);
        String[] sequences = new String[3];

        // Repeat Fasta
        StringBuilder repeatFasta = new StringBuilder();
        for (int i = 0; i < N * 2; i++) {
            repeatFasta.append(ALU.charAt(i % ALU.length()));
        }
        sequences[0] = ">ONE\n" + repeatFasta.toString().substring(0, 60) + "\n";

        // Random Fasta
        StringBuilder randomFasta1 = new StringBuilder();
        for (int i = 0; i < N * 3; i++) {
            double r = random.nextDouble();
            if (r < 0.27) {
                randomFasta1.append('a');
            } else if (r < 0.39) {
                randomFasta1.append('c');
            } else if (r < 0.51) {
                randomFasta1.append('g');
            } else {
                randomFasta1.append('t');
            }
        }
        sequences[1] = ">TWO\n" + randomFasta1.toString().substring(0, 60) + "\n";

        StringBuilder randomFasta2 = new StringBuilder();
        double[] probabilities = {0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008};
        for (int i = 0; i < N * 5; i++) {
            double r = random.nextDouble();
            int index = 0;
            while (r > probabilities[index]) {
                r -= probabilities[index];
                index++;
            }
            switch (index) {
                case 0:
                    randomFasta2.append('a');
                    break;
                case 1:
                    randomFasta2.append('c');
                    break;
                case 2:
                    randomFasta2.append('g');
                    break;
                default:
                    randomFasta2.append('t');
            }
        }
        sequences[2] = ">THREE\n" + randomFasta2.toString().substring(0, 60) + "\n";

        StringBuilder output = new StringBuilder();
        for (String sequence : sequences) {
            output.append(sequence);
        }

        System.out.println(output);
    }
}
