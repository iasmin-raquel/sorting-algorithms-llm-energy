package proprio;

public class QuickSort {

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
        int repeticoes = 50000;
        for (int i = 0; i < repeticoes; i++) {
            int[] copia = numeros.clone(); // evita ordenar array já ordenado
            quickSort(copia, 0, copia.length - 1);
        }
        System.out.println("QuickSort concluído: " + repeticoes + " execuções");
    }
}