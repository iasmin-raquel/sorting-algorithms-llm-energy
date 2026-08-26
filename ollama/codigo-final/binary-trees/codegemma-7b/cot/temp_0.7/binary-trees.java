import java.io.File;
import java.io.PrintStream;

public class BinaryTrees {

    static class TreeNode {
        TreeNode left;
        TreeNode right;
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java BinaryTrees N");
            System.exit(1);
        }

        int N = Integer.parseInt(args[0]);
        int minDepth = 4;
        int maxDepth = Math.max(minDepth + 2, N);
        int stretchDepth = maxDepth + 1;

        try (PrintStream out = new PrintStream(new File("output.txt"))) {
            // Stretch tree
            out.println("stretch tree of depth " + stretchDepth + "\t check: true");

            // Bottom-up trees
            for (int depth = minDepth; depth <= maxDepth; depth += 2) {
                out.println(countTrees(depth, out));
            }

            // Long-lived tree
            TreeNode longLivedTree = buildTree(stretchDepth);
            out.println("long lived tree of depth " + stretchDepth + "\t check: true");
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static String countTrees(int depth, PrintStream out) {
        int iterations = 1 << (maxDepth - depth + minDepth);
        return "I\t trees of depth " + depth + "\t check: " + checkTrees(buildTrees(depth, iterations), iterations, out);
    }

    private static TreeNode[] buildTrees(int depth, int iterations) {
        TreeNode[] trees = new TreeNode[iterations];
        for (int i = 0; i < iterations; i++) {
            trees[i] = buildTree(depth);
        }
        return trees;
    }

    private static TreeNode buildTree(int depth) {
        if (depth == 0) {
            return null;
        }
        TreeNode node = new TreeNode();
        node.left = buildTree(depth - 1);
        node.right = buildTree(depth - 1);
        return node;
    }

    private static boolean checkTrees(TreeNode[] trees, int iterations, PrintStream out) {
        for (TreeNode tree : trees) {
            if (tree == null) {
                return false;
            }
        }
        return true;
    }
}
