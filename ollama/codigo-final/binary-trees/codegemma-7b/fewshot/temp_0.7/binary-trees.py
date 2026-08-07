import sys

class TreeNode:
    def __init__(self):
        self.left = TreeNode()
        self.right = TreeNode()

    def __del__(self):
        del self.left
        del self.right

def stretch_tree(depth):
    root = TreeNode()
    for _ in range(2 ** (depth - 1)):
        node = root
        for _ in range(depth - 1):
            node = node.left
        del node
    return True

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def bottom_up_trees(depth, iterations):
    trees = [TreeNode() for _ in range(iterations)]
    for tree in trees:
        count_nodes(tree)
    del trees
    return True

def long_lived_tree(depth):
    root = TreeNode()
    for _ in range(2 ** (depth - 1)):
        node = root
        for _ in range(depth - 1):
            node = node.left
        del node
    return True

if __name__ == "__main__":
    N = int(sys.argv[1])
    min_depth = 4
    max_depth = max(min_depth + 2, N)
    stretch_depth = max_depth + 1

    for D in range(min_depth, max_depth + 1):
        iterations = (1 << (max_depth - D + min_depth))
        print(f"stretch tree of depth {D}\t check: {stretch_tree(stretch_depth)}")
        print(f"I\t trees of depth {D}\t check: {bottom_up_trees(D, iterations)}")

    print(f"long lived tree of depth {max_depth}\t check: {long_lived_tree(max_depth)}")
