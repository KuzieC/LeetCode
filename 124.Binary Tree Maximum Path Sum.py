#
# @lc app=leetcode id=124 lang=python3
# @lcpr version=30202
#
# [124] Binary Tree Maximum Path Sum
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
        self.res = float('-inf')
    def dfs(self,root):
        leftSum = self.dfs(root.left) if root.left else 0
        rightSum = self.dfs(root.right) if root.right else 0
        self.res = max(self.res, leftSum + rightSum + root.val, leftSum + root.val, rightSum+ root.val, root.val)
        return root.val + (max(leftSum,rightSum,0) if root.left and root.right else max(leftSum,0) if root.left else max(rightSum,0))
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#

