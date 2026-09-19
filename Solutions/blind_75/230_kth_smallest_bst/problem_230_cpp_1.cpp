/**
    Definition for a binary tree node.
 */
 #include <unordered_set>
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    int smallest = 1;
    std::unordered_set<int> visited;

public:
    int kthSmallest(TreeNode* root, int k) {
        if(!root->left || visited.find(root->left->val) != visited.end()) {
            smallest += 1;
            if(smallest > k) {
                return root->val;
            }
        }

        int val = root->val;
        if(smallest < k && root->left) {
            val = kthSmallest(root->left, k);
        } 

        if(smallest < k && root->right) {
            val = kthSmallest(root->right, k);
        }

        return val;
    }
};