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

        // Stretch Tree
        TreeNode stretchTree = createTree(stretch_depth);
        verifyTree(stretchTree);
        System.out.println("stretch tree of depth " + stretch_depth + "\t check: " + stretchTree != null);
        deleteTree(stretchTree);

        // Long-Lived Tree
        TreeNode longLivedTree = createTree(max_depth);
        System.out.println("long lived tree of depth " + max_depth + "\t check: " + longLivedTree != null);

        // Bottom-Up Trees
        for (int depth = min_depth; depth <= max_depth; depth++) {
            TreeNode bottomUpTree = createTree(depth);
            countNodes(bottomUpTree);
            deleteTree(bottomUpTree);
            System.out.println("I\t trees of depth " + depth + "\t check: " + bottomUpTree == null);
        }
    }

    private static TreeNode createTree(int depth) {
        if (depth == 0) {
            return null;
        }
        TreeNode root = new TreeNode();
        root.left = createTree(depth - 1);
        root.right = createTree(depth - 1);
        return root;
    }

    private static void verifyTree(TreeNode tree) {
        if (tree == null) {
            throw new IllegalStateException("Tree does not exist");
        }
    }

    private static void deleteTree(TreeNode tree) {
        if (tree == null) {
            return;
        }
        deleteTree(tree.left);
        deleteTree(tree.right);
        tree = null;
    }

    private static int countNodes(TreeNode tree) {
        if (tree == null) {
            return 0;
        }
        return 1 + countNodes(tree.left) + countNodes(tree.right);
    }
}
