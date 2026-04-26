package proprio;

public class BubbleSort {

    static int[] gerarArray() {
        int[] arr = new int[1000];
        for (int i = 0; i < 1000; i++) arr[i] = i + 1;
        java.util.Random rng = new java.util.Random(42);
        for (int i = 999; i > 0; i--) {
            int j = rng.nextInt(i + 1);
            int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
        }
        return arr;
    }

    static int[] numeros = gerarArray();

    static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j] > arr[j + 1]) {
                    int tmp = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = tmp;
                }
    }

    public static void main(String[] args) {
        int repeticoes = 50000;
        for (int i = 0; i < repeticoes; i++) {
            int[] copia = numeros.clone();
            bubbleSort(copia);
        }
        System.out.println("BubbleSort concluído: " + repeticoes + " execuções");
    }
}