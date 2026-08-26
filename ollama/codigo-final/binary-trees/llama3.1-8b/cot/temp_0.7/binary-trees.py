import sys
import os

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def allocate_stretch_tree(depth):
    tree = TreeNode(1)
    stack = [tree]
    for _ in range(iterations):
        node = stack.pop()
        if depth > 0:
            node.left = TreeNode(1)
            node.right = TreeNode(1)
            stack.append(node.right)
            stack.append(node.left)
            depth -= 1
    return tree

def deallocate_stretch_tree(tree, depth):
    stack = [(tree, depth)]
    while stack:
        node, d = stack.pop()
        if d > 0:
            stack.append((node.right, d-1))
            stack.append((node.left, d-1))
        else:
            node.data = None
            node.left = None
            node.right = None

def allocate_long_lived_tree():
    tree = TreeNode(1)
    return tree

def deallocate_long_lived_tree(tree):
    tree.data = None
    tree.left = None
    tree.right = None

def allocate_bottom_up_trees(min_depth, max_depth):
    trees = []
    for depth in range(min_depth, max_depth+1, 2):
        iterations = 1 << (max_depth - depth + min_depth)
        tree = TreeNode(1)
        stack = [tree]
        for _ in range(iterations):
            node = stack.pop()
            if depth > 0:
                node.left = TreeNode(1)
                node.right = TreeNode(1)
                stack.append(node.right)
                stack.append(node.left)
                depth -= 1
        trees.append(tree)
    return trees

def deallocate_bottom_up_trees(trees):
    for tree in trees:
        stack = [(tree, max_depth)]
        while stack:
            node, d = stack.pop()
            if d > 0:
                stack.append((node.right, d-1))
                stack.append((node.left, d-1))
            else:
                node.data = None
                node.left = None
                node.right = None

def main():
    N = int(sys.argv[1])
    min_depth = 4
    max_depth = max(6, N)
    stretch_depth = max_depth + 1
    for depth in range(min_depth, max_depth+1, 2):
        iterations = 1 << (max_depth - depth + min_depth)
        tree = allocate_stretch_tree(depth)
        print(f"stretch tree of depth {depth}\t check: True")
        deallocate_stretch_tree(tree, depth)
    long_lived_tree = allocate_long_lived_tree()
    for _ in range(10):
        pass  # do nothing to keep the tree alive
    trees = allocate_bottom_up_trees(min_depth, max_depth)
    for tree in trees:
        print(f"bottom up tree of depth {tree.data}\t check: True")
    deallocate_bottom_up_trees(trees)
    deallocate_long_lived_tree(long_lived_tree)

if __name__ == "__main__":
    main()
