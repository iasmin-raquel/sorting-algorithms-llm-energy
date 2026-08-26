import sys
import random

class Node:
    def __init__(self):
        self.left = None
        self.right = None

def stretch_tree(depth):
    node = Node()
    for _ in range(depth - 1):
        if random.random() < 0.5:
            node.left = Node()
        else:
            node.right = Node()
    return node

def check_tree(node, depth):
    if node is None or depth == 0:
        return True
    return (check_tree(node.left, depth - 1) and
            check_tree(node.right, depth - 1))

def long_lived_tree():
    root = Node()
    for _ in range(10000):  # allocate a large tree to persist
        node = Node()
        if random.random() < 0.5:
            node.left = root
        else:
            node.right = root

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
        print(f"stretch tree of depth {depth}\t check: {check_tree(tree, depth)}")
        long_lived_tree()

def main():
    N = int(sys.argv[1])
    min_depth = 4
    max_depth = max(6, N)
    stretch_depth = max_depth + 1

    print(f"stretch tree of depth {stretch_depth}\t check: {check_tree(stretch_tree(stretch_depth), stretch_depth)}")
    long_lived_tree()

    bottom_up_trees(min_depth, max_depth)

if __name__ == "__main__":
    main()
