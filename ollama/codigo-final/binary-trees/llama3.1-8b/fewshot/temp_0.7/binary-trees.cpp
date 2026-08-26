#include <iostream>
#include <vector>

// Define TreeNode struct with left and right pointers
struct TreeNode {
    int value;
    TreeNode* left = nullptr;
    TreeNode* right = nullptr;

    TreeNode() : value(0) {}
};

int main(int argc, char** argv) {
    // Get N from command-line argument
    int N = std::stoi(argv[1]);

    // Compute max_depth and stretch_depth
    int min_depth = 4;
    int max_depth = std::max(min_depth, N);
    int stretch_depth = max_depth + 1;

    // Allocate a stretch tree of depth max_depth + 1
    TreeNode* root = nullptr;
    for (int i = 0; i < stretch_depth - 1; ++i) {
        root = new TreeNode();
        if (i > 0) {
            root->left = new TreeNode();
            root->right = new TreeNode();
        }
    }

    // Verify memory allocation
    std::cout << "stretch tree of depth " << stretch_depth - 1 << "\t check: C" << std::endl;

    // Create a long-lived tree that persists beyond other allocations
    TreeNode* long_lived_root = nullptr;
    for (int i = min_depth; i <= max_depth; ++i) {
        long_lived_root = new TreeNode();
    }

    // Output the existence of the long-lived tree
    std::cout << "long lived tree of depth " << max_depth << "\t check: C" << std::endl;

    // Implement bottom-up tree allocation, walking, and deallocation for depths from min_depth to max_depth (step 2)
    for (int depth = min_depth; depth <= max_depth; depth += 2) {
        int iterations = 1 << (max_depth - depth + min_depth);
        TreeNode* current_root = nullptr;
        for (int i = 0; i < iterations; ++i) {
            current_root = new TreeNode();
            if (i > 0) {
                // Bottom-up allocation: allocate left and right children
                current_root->left = new TreeNode();
                current_root->right = new TreeNode();
            }
        }

        // Walk the tree to check its existence
        TreeNode* walker = current_root;
        while (walker != nullptr) {
            std::cout << "bottom-up tree of depth " << depth << "\t check: C" << std::endl;
            if (walker->left != nullptr) {
                walker = walker->left;
            } else if (walker->right != nullptr) {
                walker = walker->right;
            } else {
                break;
            }
        }

        // Deallocate the tree
        TreeNode* node = current_root;
        while (node != nullptr) {
            TreeNode* next_node = node->left ? node->left : node->right;
            delete node;
            node = next_node;
        }
    }

    return 0;
}
