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

        /* 
            u: 
                diameter = max( depth of left subtree, depth of right subtree)
                
            m:
                dfs problem because dealing with depth

            p:

            dfs(node, res)
                if node is null
                    return 0

                left tree = recursive call left
                right tree = recursive call right

                diameter = left + right

                res = max(res, diameter)
                return 1 + res
        */


public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
        dfs(root, maxDiameter);
        return maxDiameter;

    }
private:
    int dfs(TreeNode* root, int &maxDiameter) {
        // base case
        if (root == nullptr) {
            return 0;
        }

        // search left subtree
        int left = dfs(root->left, maxDiameter);

        // search right subtree
        int right = dfs(root->right, maxDiameter);

        // calculate diameter
        int diameter = left + right;

        maxDiameter = max(diameter, maxDiameter);

        // return height of current subtree
        return 1 + max(left, right);
    }
};
