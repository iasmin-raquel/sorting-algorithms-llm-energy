package professor;

public class QuickSort {

    static int[] numeros = { 74, 12, 88, 5, 43, 21, 97, 66, 30, 52, 11, 8, 99, 34, 19,
                              47, 82, 60, 2, 75, 14, 91, 33, 58, 26, 4, 68, 81, 10, 55,
                              39, 72, 17, 94, 63, 29, 41, 87, 50, 6, 23, 85, 13, 90, 37,
                              70, 44, 9, 78, 100 };

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
            }
        }
        int tmp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = tmp;
        return i + 1;
    }

    public static void main(String[] args) {
        int repeticoes = 10000;
        for (int i = 0; i < repeticoes; i++) {
            int[] copia = numeros.clone();
            quickSort(copia, 0, copia.length - 1);
        }
        System.out.println("QuickSort concluído: " + repeticoes + " execuções");
    }
}
