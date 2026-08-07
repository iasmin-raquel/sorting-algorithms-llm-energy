import java.io.PrintStream;

public class BinaryTrees {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java BinaryTrees N");
            System.exit(1);
        }

        int N = Integer.parseInt(args[0]);
        if (N < 6) {
            System.err.println("Invalid input: N must be >= 6");
            System.exit(1);
        }

        int min_depth = 4;
        int max_depth = Math.max(min_depth + 2, N);
        int stretch_depth = max_depth + 1;

        // Stretch tree
        TreeNode stretchTree = createTree(stretch_depth);
        System.out.printf("stretch tree of depth %d\t check: %b\n", stretch_depth, verifyMemory(stretchTree));

        // Bottom-up trees
        for (int depth = min_depth; depth <= max_depth; depth += 2) {
            int iterations = 1 << (max_depth - depth + min_depth);
            System.out.printf("I\t trees of depth %d\t check: %b\n", depth, verifyMemory(createTrees(depth, iterations)));
        }

        // Long-lived tree
        TreeNode longLivedTree = createTree(max_depth);
        System.out.printf("long lived tree of depth %d\t check: %b\n", max_depth, verifyMemory(longLivedTree));
    }

    private static TreeNode createTree(int depth) {
        if (depth == 0) {
            return null;
        }
        return new TreeNode(createTree(depth - 1), createTree(depth - 1));
    }

    private static TreeNode[] createTrees(int depth, int iterations) {
        TreeNode[] trees = new TreeNode[iterations];
        for (int i = 0; i < iterations; i++) {
            trees[i] = createTree(depth);
        }
        return trees;
    }

    private static boolean verifyMemory(TreeNode tree) {
        return tree != null;
    }

    static class TreeNode {
        TreeNode left;
        TreeNode right;

        TreeNode(TreeNode left, TreeNode right) {
            this.left = left;
            this.right = right;
        }
    }
}
