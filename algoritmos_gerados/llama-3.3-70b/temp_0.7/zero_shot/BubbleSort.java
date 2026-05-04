public class BubbleSort {

    /**
     * Sorts an array of integers using the Bubble Sort algorithm.
     * 
     * @param array the array to be sorted
     */
    public static void bubbleSort(int[] array) {
        int n = array.length;
        boolean swapped;

        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    // Swap array[j] and array[j + 1]
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no two elements were swapped in the inner loop, the array is sorted
            if (!swapped) {
                break;
            }
        }
    }

    /**
     * Prints the elements of an array.
     * 
     * @param array the array to be printed
     */
    public static void printArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] array = {64, 34, 25, 12, 22, 11, 90};

        System.out.println("Original array:");
        printArray(array);

        bubbleSort(array);

        System.out.println("Sorted array:");
        printArray(array);
    }
}
