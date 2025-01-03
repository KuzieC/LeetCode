#
# @lc app=leetcode id=337 lang=python3
# @lcpr version=20001
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (54.49%)
# Likes:    8596
# Dislikes: 144
# Total Accepted:    403.3K
# Total Submissions: 740.1K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called root.
# 
# Besides the root, each house has one and only one parent house. After a tour,
# the smart thief realized that all houses in this place form a binary tree. It
# will automatically contact the police if two directly-linked houses were
# broken into on the same night.
# 
# Given the root of the binary tree, return the maximum amount of money the
# thief can rob without alerting the police.
# 
# 
# Example 1:
# 
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# 
# Example 2:
# 
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^4
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
    def __init__(self):
        # Use an instance variable for memoization
        self.dp = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root in self.dp:
            return self.dp[root]
        a = root.val + \
            (0 if root.left is None else self.rob(root.left.left) + self.rob(root.left.right)) + \
            (0 if root.right is None else self.rob(root.right.left) + self.rob(root.right.right))
        b = self.rob(root.left) + self.rob(root.right)
        self.dp[root] = max(a,b)
        return self.dp[root]
# @lc code=end



#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

#

