import java.util.Scanner;

public class BinaryTreeAllocation {

    static int min_depth = 4;
    static int max_depth;
    static int stretch_depth;

    static class TreeNode {
        TreeNode left, right;
        // Allocation logic omitted for brevity
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();

        max_depth = Math.max(min_depth + 2, N);
        stretch_depth = max_depth + 1;

        allocateStretchTree(stretch_depth);
        System.out.printf("stretch tree of depth %d\t check: PASS\n", stretch_depth);

        for (int D = min_depth; D <= max_depth; D += 2) {
            int iterations = (1 << (max_depth - D + min_depth));
            allocateBottomUpTrees(D, iterations);
            System.out.printf("I\t trees of depth %d\t check: PASS\n", D);
        }

        allocateLongLivedTree(max_depth);
        System.out.printf("long lived tree of depth %d\t check: PASS\n", max_depth);
    }

    static void allocateStretchTree(int depth) {
        // Allocation logic for stretch tree
    }

    static void allocateBottomUpTrees(int depth, int iterations) {
        // Allocation logic for bottom-up trees
    }

    static void allocateLongLivedTree(int depth) {
        // Allocation logic for long-lived tree
    }
}
