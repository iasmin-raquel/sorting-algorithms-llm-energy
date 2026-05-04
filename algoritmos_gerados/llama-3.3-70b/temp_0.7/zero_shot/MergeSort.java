public class MergeSort {

    /**
     * Sorts an array of integers using the MergeSort algorithm.
     *
     * @param arr the array to be sorted
     * @return the sorted array
     */
    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }

        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        System.arraycopy(arr, 0, left, 0, mid);
        System.arraycopy(arr, mid, right, 0, arr.length - mid);

        left = mergeSort(left);
        right = mergeSort(right);

        return merge(left, right);
    }

    /**
     * Merges two sorted arrays into a single sorted array.
     *
     * @param left  the first sorted array
     * @param right the second sorted array
     * @return the merged sorted array
     */
    private static int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0;
        int j = 0;
        int k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result[k] = left[i];
                i++;
            } else {
                result[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < left.length) {
            result[k] = left[i];
            i++;
            k++;
        }

        while (j < right.length) {
            result[k] = right[j];
            j++;
            k++;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 1, 9};
        int[] sortedArr = mergeSort(arr);

        System.out.println("Original Array:");
        printArray(arr);

        System.out.println("Sorted Array:");
        printArray(sortedArr);
    }

    /**
     * Prints an array of integers to the console.
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
