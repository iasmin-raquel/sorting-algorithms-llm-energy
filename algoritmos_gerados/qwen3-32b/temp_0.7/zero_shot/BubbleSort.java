public class BubbleSort {

    public static void bubbleSort(int[] arr) {
        // Return early if the input array is null
        if (arr == null) {
            return;
        }

        int n = arr.length;
        boolean swapped;

        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            // Each pass bubbles the largest unsorted element to the end
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no swaps occurred, the array is already sorted
            if (!swapped) {
                break;
            }
        }
    }

    // Optional main method for testing purposes
    public static void main(String[] args) {
        int[] arr = {5, 3, 8, 4, 2};

        System.out.println("Original array:");
        printArray(arr);

        bubbleSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }

    // Helper method to print the array
    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
