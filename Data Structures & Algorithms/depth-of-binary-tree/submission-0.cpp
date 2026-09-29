/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {

public:
    int maxDepth(TreeNode* root) {
        /*
        m: dfs, at each iteration, keep track of max depth
        */

        if (root == nullptr) {
            return 0;
        }

        // + 1 to compute depth every return
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
        
    }
};
