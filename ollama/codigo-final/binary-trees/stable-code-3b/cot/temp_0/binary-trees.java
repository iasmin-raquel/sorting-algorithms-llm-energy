import java.util.Scanner;

class TreeNode {
    TreeNode left;
    TreeNode right;

    public TreeNode() {
        this.left = null;
        this.right = null;
    }
}

public class BinaryTrees {

    private static void stretchTree(int depth) {
        // Implement the stretch tree generation logic here
    }

    private static void longLivedTree(int depth) {
        // Implement the long-lived binary tree creation logic here
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in));
        System.out.print("Enter the value of N: ");
        int N = scanner.nextInt();

        // Calculate max_depth and stretch_depth based on min_depth, max_depth, and N
        int min_depth = 4;
        int max_depth = Math.min(N, (1 << (min_depth + 2))) >>> 0;
        int stretch_depth = max_depth + 1;

        // Generate output in the specified format for each depth
        for (int depth = min_depth; depth <= max_depth; depth++) {
            System.out.println("stretch tree of depth " + depth + "\t check: C");
        }

        // Generate output in the specified format for the long-lived tree
        longLivedTree(max_depth);
        System.out.println("long lived tree of depth " + max_depth + "\t check: C");
    }
}
