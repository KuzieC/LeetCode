#
# @lc app=leetcode id=257 lang=python3
# @lcpr version=30202
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (67.06%)
# Likes:    7008
# Dislikes: 333
# Total Accepted:    909.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,null,5]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# 
# 
# Example 2:
# 
# Input: root = [1]
# Output: ["1"]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
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
        self.res = []
    def helper(self,curr):
        if not curr:
            return []
        temp = []
        if not curr.left and not curr.right:
            temp.append(str(curr.val))
            return temp
        if curr.left:
            leftPath = self.helper(curr.left)
            for l in leftPath:
                temp.append(str(curr.val) + "->" + l)
        if curr.right:
            rightPath = self.helper(curr.right)
            for r in rightPath:
                temp.append(str(curr.val) + "->" + r)
        return temp
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.helper(root)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

