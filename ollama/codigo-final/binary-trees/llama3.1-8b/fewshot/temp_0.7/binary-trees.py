import sys
from random import shuffle
class Node:
    def __init__(self):
        self.left = None
        self.right = None

def build_tree(depth, data):
    if depth == 0: return None
    half = len(data) // 2
    node = Node()
    node.left = build_tree(depth - 1, data[:half])
    node.right = build_tree(depth - 1, data[half:])
    return node

def walk(node, depth, out):
    if node is None: return
    walk(node.right, depth + 1, out)
    out.write(f"long lived tree of depth {depth}\t check: ")

def stretch_tree(stretch_depth):
    data = [i for i in range(2**stretch_depth)]
    shuffle(data)
    return build_tree(stretch_depth - 1, data)

min_depth = int(sys.argv[1])
max_depth = max(min_depth + 2, min(int(sys.argv[1]) + 1, 16))
iterations = 0

for depth in range(min_depth, max_depth+1, 2):
    iterations += (1 << (max_depth - depth + min_depth))

stretch_tree_data = stretch_tree(max_depth+1)
if stretch_tree_data is None:
    print("fail")
else:
    print(f"stretch tree of depth {max_depth+1}\t check: True")

long_lived_tree = build_tree(4, [i for i in range(16)])
walk(long_lived_tree, 0, sys.stdout)

for depth in range(min_depth, max_depth + 1, 2):
    tree_data = [i for i in range(iterations)]
    shuffle(tree_data)
    tree = build_tree(depth - 1, tree_data)
    walk(tree, 0, sys.stdout.write('I\t trees of depth '))
    del tree
    print(file=sys.stderr)

walk(long_lived_tree, 0, sys.stdout)
print("True", file=sys.stderr)
