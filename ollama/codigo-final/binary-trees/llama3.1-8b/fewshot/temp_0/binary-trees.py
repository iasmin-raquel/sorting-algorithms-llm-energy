import sys
import random

class Node:
    def __init__(self):
        self.left = None
        self.right = None

def stretch_tree(depth):
    if depth == 0:
        return Node()
    else:
        node = Node()
        node.left = stretch_tree(depth - 1)
        node.right = stretch_tree(depth - 1)
        return node

def check_tree(node, depth):
    if node is None or depth <= 0:
        return True
    return (check_tree(node.left, depth - 1) and
            check_tree(node.right, depth - 1))

def long_lived_tree():
    root = Node()
    for _ in range(10000):  # allocate a large number of nodes
        node = Node()
        if random.random() < 0.5:
            node.left = root
        else:
            node.right = root
        root = node
    return root

def bottom_up_trees(min_depth, max_depth):
    for depth in range(min_depth, max_depth + 1, 2):
        iterations = 1 << (max_depth - depth + min_depth)
        tree = Node()
        for _ in range(iterations):
            node = Node()
            if random.random() < 0.5:
                node.left = tree
            else:
                node.right = tree
            tree = node
        print(f"stretch tree of depth {depth}\t check: {check_tree(tree, depth)}")
        del tree

def main():
    N = int(sys.argv[1])
    min_depth = 4
    max_depth = max(6, N)
    stretch_depth = max_depth + 1
    long_lived_root = long_lived_tree()

    for depth in range(min_depth, max_depth + 1, 2):
        iterations = 1 << (max_depth - depth + min_depth)
        tree = Node()
        for _ in range(iterations):
            node = Node()
            if random.random() < 0.5:
                node.left = tree
            else:
                node.right = tree
            tree = node

    bottom_up_trees(min_depth, max_depth)

    # check the long-lived tree's validity
    print(f"long-lived tree valid: {check_tree(long_lived_root, max_depth)}")

if __name__ == "__main__":
    main()
