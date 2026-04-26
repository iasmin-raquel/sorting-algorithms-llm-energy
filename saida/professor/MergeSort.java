package professor;

public class MergeSort {

    static int[] numeros = { 74, 12, 88, 5, 43, 21, 97, 66, 30, 52, 11, 8, 99, 34, 19,
                              47, 82, 60, 2, 75, 14, 91, 33, 58, 26, 4, 68, 81, 10, 55,
                              39, 72, 17, 94, 63, 29, 41, 87, 50, 6, 23, 85, 13, 90, 37,
                              70, 44, 9, 78, 100 };

    static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1, n2 = right - mid;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; i++) L[i] = arr[left + i];
        for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    public static void main(String[] args) {
        int repeticoes = 10000;
        for (int i = 0; i < repeticoes; i++) {
            int[] copia = numeros.clone();
            mergeSort(copia, 0, copia.length - 1);
        }
        System.out.println("MergeSort concluído: " + repeticoes + " execuções");
    }
}
