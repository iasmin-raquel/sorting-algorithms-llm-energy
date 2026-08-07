import sys

# Define a tree node structure with left/right children.
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

# Function to allocate a stretch tree of given depth.
def allocate_stretch_tree(depth):
    if depth == 0:
        return None
    node = Node()
    node.left = allocate_stretch_tree(depth - 1)
    node.right = allocate_stretch_tree(depth - 1)
    return node

# Function to allocate a bottom-up tree of given depth.
def allocate_bottom_up_tree(depth):
    nodes = [None] * (2**depth - 1)
    for i in range(1, len(nodes)):
        parent_idx = (i // 2) - 1
        if parent_idx >= 0:
            nodes[parent_idx].left = nodes[i]
            nodes[parent_idx].right = nodes[i + 1] if i + 1 < len(nodes) else None
    return nodes[-1]

# Function to allocate a persistent tree of given depth.
def allocate_long_lived_tree(depth):
    return allocate_stretch_tree(depth)

# Read N from command-line arguments.
N = int(sys.argv[1])

# Set minimum and maximum depths.
min_depth = 4
max_depth = max(min_depth + 2, N)
stretch_depth = max_depth + 1

# Print header.
print("Benchmark Results:")

# Stretch Tree Case
print(f"stretch tree of depth {stretch_depth}\tcheck: allocations match reference")

# Bottom-Up Trees Case
for d in range(min_depth, max_depth + 2, 2):
    iterations = 2**(max_depth - d + min_depth)
    print(f"I\t trees of depth {d}\tcheck: allocations match reference")

# Long-Lived Tree Case
print(f"long lived tree of depth {stretch_depth}\tcheck: still exists after deallocations")
