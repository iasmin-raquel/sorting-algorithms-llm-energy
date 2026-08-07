import java.util.Arrays;

public class Main {
    static int N = 10;
    static int minDepth = 4;

    public static void main(String[] args) throws Exception {
        // Compute max_depth
        int maxDepth = Math.max(6, N);

        // Compute stretch_depth
        int stretchDepth = maxDepth + 1;

        // Allocate a "stretch tree" of depth stretchDepth
        TreeNode[] stretchTree = new TreeNode[stretchDepth * (1 << stretchDepth)];
        for (int i = 0; i < stretchTree.length; i++) {
            stretchTree[i] = new TreeNode();
        }
        System.out.println("stretch tree of depth " + stretchDepth + " check: C");

        // Check if the stretch tree is fully allocated
        boolean allNull = true;
        for (TreeNode node : stretchTree) {
            if (node != null) {
                allNull = false;
                break;
            }
        }
        System.out.println("stretch tree of depth " + stretchDepth + " check: C");
        if (!allNull) {
            throw new AssertionError("Stretch tree is not fully allocated");
        }

        // Deallocate the stretch tree
        Arrays.fill(stretchTree, null);
        for (TreeNode node : stretchTree) {
            node.left = node.right = null;
        }
        System.out.println("stretch tree of depth " + stretchDepth + " check: C");

        // Allocate a "long-lived tree"
        TreeNode[] longLivedTree = new TreeNode[1 << 10];
        for (int i = 0; i < longLivedTree.length; i++) {
            longLivedTree[i] = new TreeNode();
        }
        System.out.println("long-lived tree check: C");

        // Allocate, walk, and deallocate "bottom-up trees" (each of depth D for D from min_depth to max_depth in steps of 2)
        for (int depth = minDepth; depth <= maxDepth; depth += 2) {
            int iterations = 1 << (maxDepth - depth + minDepth);

            TreeNode[] tree = new TreeNode[iterations];
            for (int i = 0; i < tree.length; i++) {
                tree[i] = new TreeNode();
            }
            System.out.println("bottom-up trees of depths from " + depth + " to " + maxDepth + " check: C");

            // Walk the tree
            walkTree(tree, 0);

            // Deallocate the tree
            Arrays.fill(tree, null);
            for (TreeNode node : tree) {
                node.left = node.right = null;
            }
            System.out.println("bottom-up trees of depths from " + depth + " to " + maxDepth + " check: C");
        }

        // Check if the long-lived tree is still allocated
        boolean allNullLongLived = true;
        for (TreeNode node : longLivedTree) {
            if (node != null) {
                allNullLongLived = false;
                break;
            }
        }
        System.out.println("long-lived tree check: C");
        if (!allNullLongLived) {
            throw new AssertionError("Long-lived tree has been deallocated");
        }

        // Deallocate the long-lived tree
        Arrays.fill(longLivedTree, null);
        for (TreeNode node : longLivedTree) {
            node.left = node.right = null;
        }
    }

    static void walkTree(TreeNode[] tree, int depth) {
        if (depth >= tree.length) return;

        TreeNode current = tree[depth];
        if (current != null) {
            System.out.println("walked to depth " + depth);
            walkTree(tree, 2 * depth + 1); // Left child
            walkTree(tree, 2 * depth + 2); // Right child
        }
    }
}
