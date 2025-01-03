#
# @lc app=leetcode id=889 lang=python3
# @lcpr version=20001
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (71.77%)
# Likes:    2760
# Dislikes: 117
# Total Accepted:    107.2K
# Total Submissions: 149.4K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# Given two integer arrays, preorder and postorder where preorder is the
# preorder traversal of a binary tree of distinct values and postorder is the
# postorder traversal of the same tree, reconstruct and return the binary
# tree.
# 
# If there exist multiple answers, you can return any of them.
# 
# 
# Example 1:
# 
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# 
# 
# Example 2:
# 
# Input: preorder = [1], postorder = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and
# postorder traversal of the same binary tree.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(postorder) == 0:
            return 
        
        if len(preorder) == 1 and len(postorder) == 1:
            return TreeNode(preorder[0])
        
        curr = preorder[0]
        root = TreeNode(curr)
        ind = 0
        currLeft = preorder[1]
        while postorder[ind] != currLeft:
            ind+=1
            
        root.left = self.constructFromPrePost(preorder[1:1+ind+1],postorder[:ind+1])
        root.right = self.constructFromPrePost(preorder[1+ind+1:],postorder[ind+1:-1])
        
        return root
        
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1]\n
# @lcpr case=end

#

