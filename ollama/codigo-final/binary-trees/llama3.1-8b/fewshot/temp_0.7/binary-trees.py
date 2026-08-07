import sys

min_depth = 4
N = int(sys.argv[1])
max_depth = max(min_depth + 2, N)
stretch_depth = max_depth + 1

class Node:
    def __init__(self):
        self.left = None
        self.right = None

def stretch(depth):
    node = Node()
    for i in range(depth - 1):
        node = node._set_child(node, i % 2 == 0)
    return node

def _set_child(node, left):
    if left:
        node.left = Node()
    else:
        node.right = Node()
    return node

def walk_tree(node, depth=0):
    if not node:
        return
    print("I\t trees of depth %d\t check: 1" % (depth))
    walk_tree(node.left, depth + 1)
    walk_tree(node.right, depth + 1)

long_lived = stretch(max_depth)
print("stretch tree of depth %d\t check: 1" % max_depth)
walk_tree(long_lived)

for depth in range(min_depth, max_depth + 1, 2):
    iterations = 1 << (max_depth - depth + min_depth)
    for i in range(iterations):
        node = stretch(depth)
        walk_tree(node)
    long_lived.check()
    print("stretch tree of depth %d\t check: 1" % depth)

print("long lived tree of depth %d\t check: 1" % max_depth)
