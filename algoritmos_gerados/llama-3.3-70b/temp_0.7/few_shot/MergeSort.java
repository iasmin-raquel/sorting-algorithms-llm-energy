public class MergeSort {
    /**
     * Sorts an array using the Merge Sort algorithm.
     *
     * @param arr the input array to be sorted
     */
    public static void sort(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
    }

    /**
     * Recursively sorts a subarray using the Merge Sort algorithm.
     *
     * @param arr the input array to be sorted
     * @param low the starting index of the subarray
     * @param high the ending index of the subarray
     */
    private static void mergeSort(int[] arr, int low, int high) {
        if (low < high) {
            int mid = low + (high - low) / 2;

            // Recursively sort the left and right subarrays
            mergeSort(arr, low, mid);
            mergeSort(arr, mid + 1, high);

            // Merge the sorted subarrays
            merge(arr, low, mid, high);
        }
    }

    /**
     * Merges two sorted subarrays into a single sorted subarray.
     *
     * @param arr the input array to be merged
     * @param low the starting index of the left subarray
     * @param mid the ending index of the left subarray
     * @param high the ending index of the right subarray
     */
    private static void merge(int[] arr, int low, int mid, int high) {
        // Create temporary arrays to store the left and right subarrays
        int[] left = new int[mid - low + 1];
        int[] right = new int[high - mid];

        // Copy the left and right subarrays into the temporary arrays
        System.arraycopy(arr, low, left, 0, mid - low + 1);
        System.arraycopy(arr, mid + 1, right, 0, high - mid);

        // Merge the temporary arrays into the original array
        int i = 0, j = 0, k = low;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy any remaining elements from the temporary arrays
        while (i < left.length) {
            arr[k] = left[i];
            i++;
            k++;
        }
        while (j < right.length) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        sort(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
