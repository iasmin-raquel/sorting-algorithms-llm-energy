#include <iostream>

struct TreeNode {
  TreeNode* left;
  TreeNode* right;
};

int main() {
  int N;
  std::cin >> N;

  int min_depth = 4;
  int max_depth = std::max(6, N);
  int stretch_depth = max_depth + 1;

  // Stretch tree
  TreeNode* stretch_tree = new TreeNode();
  // ... validation logic ...
  delete stretch_tree;

  // Long-lived tree
  TreeNode* long_lived_tree = new TreeNode();
  // ... validation logic ...

  // Bottom-up trees
  for (int current_depth = min_depth; current_depth <= max_depth; current_depth += 2) {
    int iterations = (1 << (max_depth - current_depth + min_depth));
    for (int i = 0; i < iterations; i++) {
      TreeNode* bottom_up_tree = new TreeNode();
      // ... validation logic ...
      delete bottom_up_tree;
    }
  }

  // Output
  std::cout << "stretch tree of depth " << stretch_depth << "\t check: C" << std::endl;
  for (int depth = min_depth; depth <= max_depth; depth += 2) {
    std::cout << "I\t trees of depth " << depth << "\t check: C" << std::endl;
    std::cout << "long lived tree of depth " << depth << "\t check: C" << std::endl;
  }

  return 0;
}
