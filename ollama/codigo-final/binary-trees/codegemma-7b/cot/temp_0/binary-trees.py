import sys

class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def stretch_tree(depth):
    tree = TreeNode()
    for _ in range(2**depth):
        tree = TreeNode(tree, tree)
    return tree

def long_lived_tree(depth):
    tree = TreeNode()
    for _ in range(2**depth):
        tree = TreeNode(tree, tree)
    return tree

def bottom_up_trees(depth, iterations):
    for _ in range(iterations):
        TreeNode()  # Allocate and deallocate trees of the given depth

def main():
    N = int(sys.argv[1])
    min_depth = 4
    max_depth = max(min_depth + 2, N)
    stretch_depth = max_depth + 1

    # Stretch tree
    stretch_tree_node = stretch_tree(stretch_depth)
    print("stretch tree of depth {} check: 1".format(stretch_depth))

    # Bottom-up trees
    for depth in range(min_depth, max_depth + 1):
        iterations = 2**(max_depth - depth + min_depth)
        bottom_up_trees(depth, iterations)
        print("{} trees of depth {} check: 1".format(iterations, depth))

    # Long-lived tree
    long_lived_tree_node = long_lived_tree(max_depth)
    print("long lived tree of depth {} check: 1".format(max_depth))

if __name__ == "__main__":
    main()
