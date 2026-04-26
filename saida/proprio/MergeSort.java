package proprio;

public class MergeSort {

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
        int repeticoes = 50000;
        for (int i = 0; i < repeticoes; i++) {
            int[] copia = numeros.clone();
            mergeSort(copia, 0, copia.length - 1);
        }
        System.out.println("MergeSort concluído: " + repeticoes + " execuções");
    }
}