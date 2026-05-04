public class QuickSort {
    /**
     * Sorts an array of integers using the QuickSort algorithm.
     * 
     * @param arr the array to be sorted
     */
    public static void sort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    /**
     * Recursively sorts a sub-array using the QuickSort algorithm.
     * 
     * @param arr   the array to be sorted
     * @param low   the starting index of the sub-array
     * @param high  the ending index of the sub-array
     */
    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    /**
     * Partitions the array around a pivot element.
     * 
     * @param arr   the array to be partitioned
     * @param low   the starting index of the sub-array
     * @param high  the ending index of the sub-array
     * @return      the index of the pivot element
     */
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // Swap arr[i+1] and arr[high] (pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        sort(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
