public class MergeSort {

    /**
     * Public method to initiate merge sort on an array.
     * @param array The array to be sorted.
     * @throws IllegalArgumentException if the array is null.
     */
    public static void mergeSort(int[] array) {
        if (array == null) {
            throw new IllegalArgumentException("Array cannot be null.");
        }
        mergeSort(array, 0, array.length - 1);
    }

    /**
     * Recursively divides the array into halves and sorts them.
     * @param array The array to sort.
     * @param left  The starting index of the subarray.
     * @param right The ending index of the subarray.
     */
    private static void mergeSort(int[] array, int left, int right) {
        if (left >= right) {
            return; // Base case: subarray of size 0 or 1 is already sorted
        }

        int mid = left + (right - left) / 2; // Avoids integer overflow

        // Recursively sort both halves
        mergeSort(array, left, mid);
        mergeSort(array, mid + 1, right);

        // Merge the sorted halves
        merge(array, left, mid, right);
    }

    /**
     * Merges two sorted subarrays into a single sorted subarray.
     * @param array The array containing the two sorted subarrays.
     * @param left  The starting index of the left subarray.
     * @param mid   The ending index of the left subarray.
     * @param right The ending index of the right subarray.
     */
    private static void merge(int[] array, int left, int mid, int right) {
        int leftSize = mid - left + 1;
        int rightSize = right - mid;

        // Create temporary arrays for left and right subarrays
        int[] leftArray = new int[leftSize];
        int[] rightArray = new int[rightSize];

        // Copy data into the temporary arrays
        for (int i = 0; i < leftSize; i++) {
            leftArray[i] = array[left + i];
        }
        for (int j = 0; j < rightSize; j++) {
            rightArray[j] = array[mid + 1 + j];
        }

        // Merge the temporary arrays back into the original array
        int i = 0, j = 0, k = left;
        while (i < leftSize && j < rightSize) {
            if (leftArray[i] <= rightArray[j]) {
                array[k++] = leftArray[i++];
            } else {
                array[k++] = rightArray[j++];
            }
        }

        // Copy any remaining elements from the left subarray
        while (i < leftSize) {
            array[k++] = leftArray[i++];
        }

        // Copy any remaining elements from the right subarray
        while (j < rightSize) {
            array[k++] = rightArray[j++];
        }
    }

    // Optional: Main method for testing
    public static void main(String[] args) {
        int[] array = {38, 27, 43, 3, 9, 82, 10};
        mergeSort(array);

        System.out.println("Sorted array:");
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}
