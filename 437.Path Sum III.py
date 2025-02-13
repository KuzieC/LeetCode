#
# @lc app=leetcode id=437 lang=python3
# @lcpr version=30005
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (46.03%)
# Likes:    11331
# Dislikes: 542
# Total Accepted:    656.7K
# Total Submissions: 1.4M
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
# 
# 
# Example 1:
# 
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# 
# 
# Example 2:
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
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
    def __init__():
        self.res = 0
    def dfs(self,root,targetSum):
        if root == None:
            return 0
        left = self.pathSum(root.left, targetSum)
        right = self.pathSum(root.right, targetSum)
        self.res = 0
        if root.val == targetSum:
            self.res +=1
        if left + root.val == targetSum:
            self.res +=1
        if right + root.val == tragetSum:
            sefl.res +=1 
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        

        
# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#

