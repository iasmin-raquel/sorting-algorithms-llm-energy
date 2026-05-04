public class MergeSort {

    /**
     * Sorts an array using the merge sort algorithm.
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
        int i = 0, j = 0, k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result[k++] = left[i++];
            } else {
                result[k++] = right[j++];
            }
        }

        while (i < left.length) {
            result[k++] = left[i++];
        }

        while (j < right.length) {
            result[k++] = right[j++];
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 3, 1, 6, 4};
        int[] sortedArr = mergeSort(arr);

        System.out.println("Original array: ");
        printArray(arr);

        System.out.println("Sorted array: ");
        printArray(sortedArr);
    }

    private static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
