import java.util.Scanner;

public class BinaryTreeOperations {

    static class TreeNode {
        TreeNode left, right;

        TreeNode() {
            left = right = null;
        }
    }

    static int maxDepth(int N) {
        return Math.max(4, N);
    }

    static int stretchDepth(int maxDepth) {
        return maxDepth + 1;
    }

    static long iterations(int maxDepth, int minDepth, int depth) {
        return 1L << (maxDepth - depth + minDepth);
    }

    static TreeNode constructTree(int depth) {
        if (depth == 0) {
            return null;
        }
        TreeNode root = new TreeNode();
        root.left = constructTree(depth - 1);
        root.right = constructTree(depth - 1);
        return root;
    }

    static int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + countNodes(root.left) + countNodes(root.right);
    }

    static void deallocateTree(TreeNode root) {
        if (root == null) {
            return;
        }
        deallocateTree(root.left);
        deallocateTree(root.right);
        root = null;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(args[0]);
        int minDepth = 4;
        int maxDepth = maxDepth(N);
        int stretchDepth = stretchDepth(maxDepth);

        System.out.println("stretch tree of depth " + stretchDepth + "\t check: " + (constructTree(stretchDepth) != null));
        deallocateTree(constructTree(stretchDepth));

        for (int depth = minDepth; depth <= maxDepth; depth += 2) {
            TreeNode[] trees = new TreeNode[(int) iterations(maxDepth, minDepth, depth)];
            for (int i = 0; i < trees.length; i++) {
                trees[i] = constructTree(depth);
            }
            System.out.println("I\t trees of depth " + depth + "\t check: " + countNodes(trees[trees.length - 1]));
            for (TreeNode tree : trees) {
                deallocateTree(tree);
            }
        }

        System.out.println("long lived tree of depth " + maxDepth + "\t check: " + (constructTree(maxDepth) != null));
    }
}
