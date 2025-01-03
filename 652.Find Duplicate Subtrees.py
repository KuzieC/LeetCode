#
# @lc app=leetcode id=652 lang=python3
# @lcpr version=20001
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (59.72%)
# Likes:    5879
# Dislikes: 478
# Total Accepted:    275.5K
# Total Submissions: 461.4K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
# 
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
# 
# Two trees are duplicate if they have the same structure with the same node
# values.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# 
# 
# Example 2:
# 
# Input: root = [2,1,1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200
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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,null,2,4,null,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,3,null,3,null]\n
# @lcpr case=end

#

