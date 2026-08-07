#include <cstdio>
#include <cstdlib>

struct Node {
    int data;
    Node* left;
    Node* right;
};

Node* allocate_perfect_binary_tree(int depth) {
    if (depth == 0) {
        return NULL;
    }
    Node* root = new Node;
    root->left = allocate_perfect_binary_tree(depth - 1);
    root->right = allocate_perfect_binary_tree(depth - 1);
    return root;
}

Node* allocate_long_lived_tree(int depth) {
    static Node* root = NULL;
    if (root == NULL) {
        root = allocate_perfect_binary_tree(depth);
    }
    return root;
}

int main(int argc, char* argv[]) {
    int N = atoi(argv[1]);
    int min_depth = 4;
    int max_depth = max(min_depth + 2, N);
    int stretch_depth = max_depth + 1;

    // --- Stretch Tree ---
    Node* stretch_tree = allocate_perfect_binary_tree(stretch_depth);
    printf("stretch tree of depth %d\tcheck: C\n", stretch_depth);

    // --- Long-Lived Tree ---
    Node* long_lived_tree = allocate_long_lived_tree(max_depth);
    printf("long lived tree of depth %d\tcheck: C\n", max_depth);

    // --- Bottom-Up Trees (Iterations) ---
    for (int depth = min_depth; depth <= max_depth; depth += 2) {
        int iterations = (1 << (max_depth - depth + min_depth));
        for (int i = 0; i < iterations; ++i) {
            Node* temp_tree = allocate_perfect_binary_tree(depth);
            // Walk and deallocate (e.g., `free(temp_tree)`).
        }
        printf("I\t trees of depth %d\tcheck: C\n", depth);
    }

    return 0;
}
