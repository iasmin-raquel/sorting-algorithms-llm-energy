import sys

class Node:
    def __init__(self, depth):
        self.depth = depth
        self.left = None
        self.right = None

def allocate_stretch_tree(depth):
    if depth <= 0:
        return None
    node = Node(depth)
    node.left = allocate_stretch_tree(depth - 1)
    node.right = allocate_stretch_tree(depth - 1)
    return node

def deallocate_stretch_tree(node):
    if node is not None:
        deallocate_stretch_tree(node.left)
        deallocate_stretch_tree(node.right)
        del node

def allocate_long_lived_tree():
    long_lived_node = Node(max_depth + 1)
    long_lived_node.left = allocate_stretch_tree(max_depth - 1)
    return long_lived_node

def walk_long_lived_tree(node, depth):
    if node is not None:
        print(f"depth: {node.depth}")
        walk_long_lived_tree(node.left, node.depth - 1)
        walk_long_lived_tree(node.right, node.depth + 1)

def allocate_bottom_up_trees(min_depth, max_depth):
    for depth in range(min_depth, max_depth + 1, 2):
        iterations = 1 << (max_depth - depth + min_depth)
        print(f"allocate: {iterations} trees of depth {depth}")
        bottom_up_node = Node(depth)
        for _ in range(iterations):
            bottom_up_node.left = allocate_stretch_tree(depth - 1)
            bottom_up_node.right = allocate_stretch_tree(depth - 1)
        walk_bottom_up_tree(bottom_up_node, depth)

def deallocate_bottom_up_trees(min_depth, max_depth):
    for depth in range(max_depth, min_depth - 1, -2):
        iterations = 1 << (max_depth - depth + min_depth)
        print(f"deallocate: {iterations} trees of depth {depth}")
        bottom_up_node = Node(depth)
        deallocate_stretch_tree(bottom_up_node.left)
        deallocate_stretch_tree(bottom_up_node.right)

def walk_bottom_up_tree(node, depth):
    if node is not None:
        print(f"depth: {node.depth}")
        walk_bottom_up_tree(node.left, node.depth - 1)
        walk_bottom_up_tree(node.right, node.depth + 1)

if __name__ == "__main__":
    N = int(sys.argv[1])
    min_depth = 4
    max_depth = max(6, N)
    stretch_depth = max_depth + 1

    print(f"stretch tree of depth {stretch_depth}\t check: {allocate_stretch_tree(stretch_depth) is not None}")
    deallocate_stretch_tree(allocate_stretch_tree(stretch_depth))

    long_lived_node = allocate_long_lived_tree()
    walk_long_lived_tree(long_lived_node, stretch_depth)
    print(f"long lived tree of depth {stretch_depth}\t check: {long_lived_node is not None}")

    allocate_bottom_up_trees(min_depth, max_depth)

    deallocate_bottom_up_trees(min_depth, max_depth)
