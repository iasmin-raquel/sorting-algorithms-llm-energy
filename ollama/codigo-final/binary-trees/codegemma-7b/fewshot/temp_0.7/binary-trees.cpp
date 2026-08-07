#include <iostream>

struct TreeNode {
  TreeNode* left;
  TreeNode* right;
};

int main(int argc, char* argv[]) {
  int N = atoi(argv[1]);
  int min_depth = 4;
  int max_depth = max(6, N);
  int stretch_depth = max_depth + 1;

  // Stretch tree
  TreeNode* stretch_tree = new TreeNode();
  if (stretch_tree) {
    // ... validation logic here ...
  }
  delete stretch_tree;

  // Long-lived tree
  TreeNode* long_lived_tree = new TreeNode();

  // Bottom-up trees
  for (int current_depth = min_depth; current_depth <= max_depth; current_depth += 2) {
    int iterations = (1 << (max_depth - current_depth + min_depth));
    for (int i = 0; i < iterations; i++) {
      TreeNode* bottom_up_tree = new TreeNode();
      // ... walk and deallocate logic here ...
    }
  }

  return 0;
}
