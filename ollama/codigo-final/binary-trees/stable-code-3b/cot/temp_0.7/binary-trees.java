import java.util.Scanner;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode(int val) {
        this.val = val;
    }
}

public class BinaryTrees {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in));
        int N = scanner.nextInt();
        scanner.close();

        int minDepth = 4;
        int maxDepth = Math.min(N, (1 << (minDepth + 2)))));
        int stretchDepth = maxDepth + 1;
        int iterations = 1 << (maxDepth - minDepth + 1));

        // Generate a stretch tree
        TreeNode stretchTreeRoot = generateStretchTree(stretchDepth));

        // Perform bottom-up tree generation and testing
        for (int depth = minDepth; depth <= maxDepth; depth += 2) {
            iterations /= 2; // Halve the number of iterations per tree
            int numTrees = 1 << (depth - minDepth + 1));
            System.out.println(depth + "\t" + numTrees + "\tcheck: " + countNodesAndDeallocateTree((TreeNode) null, depth))));
        }

        // Long-lived tree maintenance
        // Perform any necessary operations to maintain the long-lived tree consistently after allocations and deallocations.

    }

    private static TreeNode generateStretchTree(int depth) {
        if (depth == 0) {
            return null;
        }
        TreeNode node = new TreeNode((int) Math.random() * 10));
        node.left = generateStretchTree(depth - 1));
        node.right = generateStretchTree(depth - 1));
        return node;
    }

    private static int countNodesAndDeallocateTree(TreeNode root, int depth) {
        if (root == null) {
            return 0;
        }
        int numNodes = 1; // Count the current node
        numNodes += countNodesAndDeallocateTree(root.left, depth - 1)); // Traverse left subtree and count nodes
        numNodes += countNodesAndDeallocateTree(root.right, depth - 1)); // Traverse right subtree and count nodes
        if (depth == 0) {
            // Deallocate the tree node
            root = null;
        }
        return numNodes;
    }

}
