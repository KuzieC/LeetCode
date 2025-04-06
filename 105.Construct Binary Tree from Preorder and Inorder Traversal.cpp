/*
 * @lc app=leetcode id=105 lang=cpp
 * @lcpr version=30104
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (66.33%)
 * Likes:    15740
 * Dislikes: 565
 * Total Accepted:    1.5M
 * Total Submissions: 2.3M
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * Given two integer arrays preorder and inorder where preorder is the preorder
 * traversal of a binary tree and inorder is the inorder traversal of the same
 * tree, construct and return the binary tree.
 * 
 * 
 * Example 1:
 * 
 * Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 * Output: [3,9,20,null,null,15,7]
 * 
 * 
 * Example 2:
 * 
 * Input: preorder = [-1], inorder = [-1]
 * Output: [-1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= preorder.length <= 3000
 * inorder.length == preorder.length
 * -3000 <= preorder[i], inorder[i] <= 3000
 * preorder and inorder consist of unique values.
 * Each value of inorder also appears in preorder.
 * preorder is guaranteed to be the preorder traversal of the tree.
 * inorder is guaranteed to be the inorder traversal of the tree.
 * 
 * 
 */

// @lc code=start
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {

        unordered_map<int,int> inordermap;
        for(size_t i =  0; i < inorder.size(); i++){
            inordermap[inorder[i]] = i;
        }
        return help(preorder,0,preorder.size(),inorder,0,inorder.size(),inordermap);
    }

    TreeNode* help(vector<int>& preorder,int p1, int p2, vector<int>& inorder, int i1, int i2, unordered_map<int,int>& inordermap){

        if(p2 - p1 <= 0 || i2 - i1 <= 0){
            return nullptr;
        }

        TreeNode* head = new TreeNode(preorder[p1]);

        int ind = inordermap[preorder[p1]];

        auto left = help(preorder,p1+1,p1+(ind-i1)+1,inorder,i1,ind,inordermap);
        auto right = help(preorder,p1+(ind-i1)+1,p2,inorder,ind+1,i2,inordermap);
        head->left = left;
        head->right = right;
        return head;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,9,20,15,7]\n[9,3,15,20,7]\n
// @lcpr case=end

// @lcpr case=start
// [-1]\n[-1]\n
// @lcpr case=end

 */

