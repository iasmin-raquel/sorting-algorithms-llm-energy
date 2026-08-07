import java.util.*;

public class Main {
    private static final String ALU = "GGCCGGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGCGGA" +
            "TCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCGTCTCTACTAAAAATACAAAAATTAGCCGGGCGTGGTGGCGCGCGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCGGAGGTTGCAGTGAGCCGAGATCGCGCCACTGCACTCCAGCCTGGGCGACAGAGCGAGACTCCGTCTCAAAAA";
    private static final double[] IUB = { 0.27, 0.12, 0.12, 0.27, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
            0.02, 0.02, 0.02 };
    private static final double[] HUMAN = { 0.3029549426680, 0.1979883004921, 0.1975473066391, 0.3015094502008 };

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        int length1 = 2 * N;
        int length2 = 3 * N;
        int length3 = 5 * N;

        // Repeat Fasta
        String sequence1 = repeatFasta(ALU, length1);
        System.out.println(">ONE Homo sapiens alu");
        printSequence(sequence1);

        // Random Fasta
        String sequence2 = randomFasta(IUB, length2);
        System.out.println("\n>TWO IUB ambiguity codes");
        printSequence(sequence2);

        // Human Random Fasta
        String sequence3 = humanRandomFasta(HUMAN, length3);
        System.out.println("\n>THREE Homo sapiens frequency");
        printSequence(sequence3);
    }

    private static String repeatFasta(String dna, int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(dna);
        }
        return sb.toString();
    }

    private static void printSequence(String sequence) {
        for (String s : splitToLines(sequence)) {
            System.out.println(s);
        }
    }

    private static List<String> splitToLines(String str, int lineLength) {
        List<String> lines = new ArrayList<>();
        StringBuilder currentLine = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            if (currentLine.length() >= lineLength - 1 && (i + 1 == str.length() || str.charAt(i + 1) != str.charAt(i))) {
                lines.add(currentLine.toString());
                currentLine.setLength(0);
            }
            currentLine.append(str.charAt(i));
        }
        lines.add(currentLine.toString());
        return lines;
    }

    private static String randomFasta(double[] alphabet, int n) {
        Random r = new Random(System.currentTimeMillis());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            double rand = nextRandom(r);
            int index = 0;
            while (index == -1 || index >= alphabet.length) {
                if (rand < alphabet[index]) {
                    sb.append(getChar(index));
                    break;
                }
                rand -= alphabet[index];
                index++;
            }
        }
        return sb.toString();
    }

    private static double nextRandom(Random r) {
        long s = System.currentTimeMillis() + 42;
        s ^= s << 21;
        s ^= s >> 35;
        s ^= s << 4;
        return (double) (s & 0x7fffffff) / (double) 0x7fffffffl;
    }

    private static char getChar(int i) {
        switch (i) {
            case 0:
                return 'a';
            case 1:
                return 'c';
            case 2:
                return 'g';
            case 3:
                return 't';
            default:
                if (i >= 4 && i <= 15)
                    return "BCHGKMRSVW".charAt(i - 4);
                else
                    return 'N';
        }
    }

    private static String humanRandomFasta(double[] alphabet, int n) {
        Random r = new Random(System.currentTimeMillis());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            double rand = nextRandom(r);
            int index = 0;
            while (index == -1 || index >= alphabet.length) {
                if (rand < alphabet[index]) {
                    sb.append(getChar(index));
                    break;
                }
                rand -= alphabet[index];
                index++;
            }
        }
        return sb.toString();
    }
}
