package professor;

public class BubbleSort {

    static int[] numeros = { 74, 12, 88, 5, 43, 21, 97, 66, 30, 52, 11, 8, 99, 34, 19,
                              47, 82, 60, 2, 75, 14, 91, 33, 58, 26, 4, 68, 81, 10, 55,
                              39, 72, 17, 94, 63, 29, 41, 87, 50, 6, 23, 85, 13, 90, 37,
                              70, 44, 9, 78, 100 };

    static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j] > arr[j + 1]) {
                    int tmp = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = tmp;
                }
    }

    public static void main(String[] args) {
        int repeticoes = 10000;
        for (int i = 0; i < repeticoes; i++) {
            int[] copia = numeros.clone();
            bubbleSort(copia);
        }
        System.out.println("BubbleSort concluído: " + repeticoes + " execuções");
    }
}
