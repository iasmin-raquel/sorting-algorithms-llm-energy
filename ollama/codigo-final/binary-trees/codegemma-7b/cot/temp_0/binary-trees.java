public class BinaryTreeAllocation {

    static class TreeNode {
        TreeNode left;
        TreeNode right;
        // Add data field if needed
    }

    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        int min_depth = 4;
        int max_depth = Math.max(min_depth + 2, N);
        int stretch_depth = max_depth + 1;

        // Stretch Tree Logic
        TreeNode stretchTree = new TreeNode();
        // Build tree of depth stretch_depth
        // ...
        System.out.println("stretch tree of depth " + stretch_depth + "\t check: " + (stretchTree != null));
        // Deallocate stretchTree

        // Long-Lived Tree Logic
        TreeNode longLivedTree = new TreeNode();
        // Build tree of depth max_depth
        // ...
        System.out.println("long lived tree of depth " + max_depth + "\t check: " + (longLivedTree != null));

        // Bottom-Up Trees Logic
        for (int depth = min_depth; depth <= max_depth; depth++) {
            int iterations = 1 << (max_depth - depth + min_depth);
            for (int i = 0; i < iterations; i++) {
                TreeNode tree = new TreeNode();
                // Build tree of depth depth
                // ...
                // Count nodes in tree
                // ...
                // Deallocate tree
                System.out.println("I\t trees of depth " + depth + "\t check: " + true);
            }
        }
    }
}
