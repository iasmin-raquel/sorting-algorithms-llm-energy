import java.util.Scanner;

public class BinaryTreeOperations {

    static class TreeNode {
        TreeNode left, right;
        TreeNode() {}
    }

    static int min_depth = 4;
    static int max_depth;
    static int stretch_depth;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read N from command line
        int N = Integer.parseInt(args[0]);

        // Calculate max_depth
        max_depth = Math.max(min_depth + 2, N);
        stretch_depth = max_depth + 1;

        // Stretch Tree
        TreeNode stretchTree = createTree(stretch_depth);
        verifyNode(stretchTree);
        deleteTree(stretchTree);

        // Iterative Trees
        for (int depth = min_depth; depth <= max_depth; depth += 2) {
            int iterations = 1 << (max_depth - depth + min_depth);
            for (int i = 0; i < iterations; i++) {
                TreeNode iterativeTree = createTree(depth);
                countNodes(iterativeTree);
                deleteTree(iterativeTree);
            }
        }

        // Long-Lived Tree
        TreeNode longLivedTree = createTree(stretch_depth);
        verifyNode(longLivedTree);
        deleteTree(longLivedTree);
    }

    // Create a binary tree of the given depth
    private static TreeNode createTree(int depth) {
        if (depth == 0) {
            return null;
        }
        TreeNode node = new TreeNode();
        node.left = createTree(depth - 1);
        node.right = createTree(depth - 1);
        return node;
    }

    // Verify that the tree node exists
    private static void verifyNode(TreeNode node) {
        if (node == null) {
            System.out.println("check: false");
        } else {
            System.out.println("check: true");
        }
    }

    // Delete the binary tree
    private static void deleteTree(TreeNode node) {
        if (node == null) {
            return;
        }
        deleteTree(node.left);
        deleteTree(node.right);
        node = null;
    }

    // Count the nodes in the binary tree
    private static int countNodes(TreeNode node) {
        if (node == null) {
            return 0;
        }
        return 1 + countNodes(node.left) + countNodes(node.right);
    }
}
