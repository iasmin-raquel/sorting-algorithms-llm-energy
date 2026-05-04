import java.util.Random;

public class QuickSort {

    // Public method to initiate QuickSort
    public static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    // Recursive QuickSort implementation
    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // Partition the array and get the pivot index
            int pivotIndex = partition(arr, low, high);

            // Recursively sort elements before and after the pivot
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    // Partition method using a random pivot
    private static int partition(int[] arr, int low, int high) {
        // Randomly select a pivot index
        Random rand = new Random();
        int pivotIndex = low + rand.nextInt(high - low + 1);

        // Move the pivot to the end for ease of partitioning
        swap(arr, pivotIndex, high);

        int pivot = arr[high]; // Pivot value
        int i = low - 1; // Index of smaller element

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        // Place the pivot in its correct position
        swap(arr, i + 1, high);

        return i + 1; // Return the pivot index
    }

    // Helper method to swap two elements in the array
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Main method to test the QuickSort implementation
    public static void main(String[] args) {
        int[] arr = {5, 3, 8, 4, 2, 7, 1, 10};

        System.out.println("Original array:");
        printArray(arr);

        quickSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }

    // Helper method to print array
    private static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
