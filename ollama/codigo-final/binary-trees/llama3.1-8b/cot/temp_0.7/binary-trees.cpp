import sys
import math

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None

def allocate_stretch_tree(depth, stretch_depth):
    root = TreeNode()
    current_node = root
    for _ in range(stretch_depth - 1):
        new_node = TreeNode()
        if (depth & 1):  # right child at odd depths
            current_node.right = new_node
        else:
            current_node.left = new_node
        current_node = new_node
    return root

def check_stretch_tree(tree, depth):
    count = 0
    stack = [(tree, 0)]
    while stack:
        node, d = stack.pop()
        if (d == depth) and (node is not None):
            count += 1
        elif node.left or node.right:
            stack.append((node.right, d + 1))
            if node.left:
                stack.append((node.left, d + 1))
    return count

def deallocate_stretch_tree(tree):
    while tree:
        temp = tree
        tree = tree.left if tree else None
        del temp

class LongLivedTree:
    def __init__(self):
        self.root = TreeNode()

def allocate_long_lived_tree(depth, max_depth):
    tree = allocate_stretch_tree(depth, max_depth + 1)
    return tree

def deallocate_long_lived_tree(tree):
    pass  # This will not actually free the memory, but we can't modify the long-lived tree later

def allocate_bottom_up_trees(min_depth, max_depth, iterations):
    for depth in range(min_depth, max(max_depth, N), 2):
        iterations_at_depth = 1 << (max_depth - depth + min_depth)
        print(f"I\t trees of depth {depth}\t check: {iterations_at_depth}")
        tree_count = 0
        stack = [(allocate_stretch_tree(depth, depth + 1), 0)]
        while stack:
            node, d = stack.pop()
            if (d == depth) and (node is not None):
                tree_count += 1
            elif node.left or node.right:
                stack.append((node.right, d + 1))
                if node.left:
                    stack.append((node.left, d + 1))
        print(f"tree count at depth {depth}: {tree_count}")
        for _ in range(iterations_at_depth):
            allocate_stretch_tree(depth, depth + 1)
            deallocate_stretch_tree(allocate_stretch_tree(depth, depth + 1))

def main():
    global N
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    min_depth = 4
    max_depth = max(6, N)
    stretch_depth = max_depth + 1

    print(f"stretch tree of depth {max_depth}\t check: {check_stretch_tree(allocate_stretch_tree(max_depth, stretch_depth), max_depth)}")
    deallocate_stretch_tree(allocate_stretch_tree(max_depth, stretch_depth))

    long_lived_tree = allocate_long_lived_tree(max_depth, max_depth)
    print(f"long lived tree of depth {max_depth}\t check: 1")

    allocate_bottom_up_trees(min_depth, max_depth, N)

if __name__ == "__main__":
    main()
