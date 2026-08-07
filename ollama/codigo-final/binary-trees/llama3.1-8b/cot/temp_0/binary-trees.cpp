#include <iostream>
#include <cstdlib>

// Define a tree node structure with left and right child pointers
struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) : value(val), left(nullptr), right(nullptr) {}
};

// Function to allocate a stretch tree of depth D
TreeNode* allocateStretchTree(int D) {
    if (D == 0) return nullptr;
    TreeNode* node = new TreeNode(D);
    node->left = allocateStretchTree(D - 1);
    node->right = allocateStretchTree(D - 1);
    return node;
}

// Function to check the existence of a tree
bool checkTree(TreeNode* root, int D) {
    if (root == nullptr || D < 0) return false;
    bool leftExist = checkTree(root->left, D - 1);
    bool rightExist = checkTree(root->right, D - 1);
    return leftExist && rightExist;
}

// Function to deallocate a tree
void deallocateTree(TreeNode* root) {
    if (root == nullptr) return;
    deallocateTree(root->left);
    deallocateTree(root->right);
    delete root;
}

int main(int argc, char** argv) {
    int N = std::stoi(argv[1]);
    int min_depth = 4;
    int max_depth = std::max(6, N);

    // Allocate a stretch tree of depth D
    for (int D = min_depth; D <= max_depth; D += 2) {
        TreeNode* stretchTree = allocateStretchTree(D);
        bool checkResult = checkTree(stretchTree, D);
        deallocateTree(stretchTree);
        std::cout << "stretch tree of depth " << D << "\t check: " << (checkResult ? "C" : "F") << std::endl;
    }

    // Allocate a long-lived tree
    TreeNode* longLivedTree = allocateStretchTree(max_depth);

    // Allocate, walk, and deallocate many bottom-up trees
    for (int D = min_depth; D <= max_depth; D += 2) {
        int iterations = 1 << (max_depth - D + min_depth);
        for (int i = 0; i < iterations; ++i) {
            TreeNode* tree = allocateStretchTree(D);
            deallocateTree(tree);
        }
    }

    // Ensure the long-lived tree still exists
    bool checkResult = checkTree(longLivedTree, max_depth);
    std::cout << "long lived tree of depth " << max_depth << "\t check: " << (checkResult ? "C" : "F") << std::endl;

    return 0;
}
