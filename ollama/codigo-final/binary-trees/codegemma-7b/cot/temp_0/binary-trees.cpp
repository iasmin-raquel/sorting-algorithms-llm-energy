#include <cstdio>

struct TreeNode {
  int data;
  TreeNode* left;
  TreeNode* right;
};

int min_depth = 4;
int max_depth;
int stretch_depth;

TreeNode* create_stretch_tree(int depth) {
  if (depth == 0) {
    return nullptr;
  }
  TreeNode* root = new TreeNode();
  root->left = create_stretch_tree(depth - 1);
  root->right = create_stretch_tree(depth - 1);
  return root;
}

void deallocate_tree(TreeNode* root) {
  if (root == nullptr) {
    return;
  }
  deallocate_tree(root->left);
  deallocate_tree(root->right);
  delete root;
}

TreeNode* create_long_lived_tree(int depth) {
  static TreeNode* root = nullptr;
  if (root == nullptr) {
    root = create_stretch_tree(depth);
  }
  return root;
}

void create_bottom_up_trees(int depth) {
  int iterations = 1 << (max_depth - depth + min_depth);
  for (int i = 0; i < iterations; i++) {
    TreeNode* root = new TreeNode();
    root->left = create_bottom_up_trees(depth - 1);
    root->right = create_bottom_up_trees(depth - 1);
    deallocate_tree(root);
  }
}

int main() {
  int N;
  scanf("%d", &N);

  max_depth = max(min_depth + 2, N);
  stretch_depth = max_depth + 1;

  printf("stretch tree of depth %d\t check: C\n", stretch_depth);
  TreeNode* stretch_tree = create_stretch_tree(stretch_depth);
  deallocate_tree(stretch_tree);

  printf("I\t trees of depth %d\t check: C\n", max_depth);
  create_bottom_up_trees(max_depth);

  printf("long lived tree of depth %d\t check: C\n", max_depth);
  TreeNode* long_lived_tree = create_long_lived_tree(max_depth);

  return 0;
}
