public class QuickSort {
    /**
     * Sorts the given array using QuickSort algorithm.
     * 
     * @param arr the array to be sorted
     */
    public static void sort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    /**
     * Recursive function to sort the array.
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
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    /**
     * Swaps two elements in the array.
     * 
     * @param arr   the array
     * @param i     the index of the first element
     * @param j     the index of the second element
     */
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        sort(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
