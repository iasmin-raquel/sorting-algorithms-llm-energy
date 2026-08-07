import os

class Node:
    def __init__(self):
        self.left = None
        self.right = None

def allocate_stretch_tree(depth, max_depth):
    if depth > max_depth:
        return None
    node = Node()
    node.left = allocate_stretch_tree(depth + 1, max_depth)
    node.right = allocate_stretch_tree(depth + 1, max_depth)
    return node

def check_long_lived_tree(tree):
    return tree is not None

def walk_bottom_up_tree(node, depth):
    if node is None:
        return
    print(f"Depth: {depth}")
    walk_bottom_up_tree(node.left, depth + 1)
    walk_bottom_up_tree(node.right, depth + 1)

def allocate_long_lived_tree():
    tree = Node()
    return tree

def main(min_depth=4, max_depth=max(6, N), stretch_depth=max_depth + 1):
    iterations = 1 << (max_depth - min_depth)
    
    # Allocate a long-lived tree
    long_lived_tree = allocate_long_lived_tree()

    for depth in range(min_depth, max_depth + 1, 2):
        print(f"Allocating stretch tree of depth {depth}")
        stretch_tree = allocate_stretch_tree(0, stretch_depth)
        
        # Check that the long-lived tree still exists
        assert check_long_lived_tree(long_lived_tree)

        # Walk and deallocate bottom-up trees
        for i in range(iterations):
            print(f"Allocating bottom-up tree of depth {depth}")
            node = Node()
            walk_bottom_up_tree(node, 0)
            
            print(f"Deallocating bottom-up tree of depth {depth}")

    # Check that the long-lived tree still exists after all allocations
    assert check_long_lived_tree(long_lived_tree)

if __name__ == "__main__":
    N = int(os.environ.get("N", "10"))  # Get value from environment variable or default to 10
    main(min_depth=4, max_depth=max(6, N), stretch_depth=max_depth + 1)
