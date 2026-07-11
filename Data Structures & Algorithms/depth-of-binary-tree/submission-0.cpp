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
private:
    int helper(TreeNode* node, int depth) {
        if (node == nullptr) return depth - 1;
        //if (node->left == nullptr && node->right == nullptr) return depth;
        return std::max(helper(node->left, depth+1), helper(node->right, depth+1));
    }
public:
    int maxDepth(TreeNode* root) {
        return helper(root, 1);
        
    }
};
