public class QuickSort {

    /**
     * Sorts an array of integers using QuickSort algorithm.
     *
     * @param arr the array to be sorted
     */
    public static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    /**
     * Recursively sorts a sub-array of integers using QuickSort algorithm.
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
     * @return the index of the pivot element
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
     * @param arr the array
     * @param i   the index of the first element
     * @param j   the index of the second element
     */
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 3, 1, 6, 4};
        System.out.println("Original array:");
        printArray(arr);
        quickSort(arr);
        System.out.println("Sorted array:");
        printArray(arr);
    }

    /**
     * Prints the elements of the array.
     *
     * @param arr the array to be printed
     */
    private static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
