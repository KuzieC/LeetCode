#
# @lc app=leetcode id=1373 lang=python3
# @lcpr version=30202
#
# [1373] Maximum Sum BST in Binary Tree
#
# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
#
# algorithms
# Hard (44.97%)
# Likes:    2869
# Dislikes: 198
# Total Accepted:    106.7K
# Total Submissions: 237.1K
# Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
#
# Given a binary tree root, return the maximum sum of all keys of any sub-tree
# which is also a Binary Search Tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root
# node with key equal to 3.
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a
# single root node with key equal to 2.
# 
# 
# Example 3:
# 
# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 4 * 10^4].
# -4 * 10^4 <= Node.val <= 4 * 10^4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def helper(self,root):
        if not root:
            return 0,float('inf'),float('-inf')
        
        leftSub,leftMin,leftMax = self.helper(root.left)
        rightSub,rightMin,rightMax  = self.helper(root.right)
            
        if leftSub != float('-inf') and rightSub != float('-inf') and root.val > leftMax and root.val < rightMin:
            self.res = max(leftSub+rightSub+root.val,self.res)
            return leftSub+rightSub+root.val, min(leftMin,root.val), max(rightMax,root.val)
        else:
            #self.res = max([leftSub,rightSub,self.res])
            return float('-inf'),float('-inf'),float('-inf')

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res
# @lc code=end



#
# @lcpr case=start
# [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,null,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [-4,-2,-5]\n
# @lcpr case=end

#

