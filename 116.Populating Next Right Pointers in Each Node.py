#
# @lc app=leetcode id=116 lang=python3
# @lcpr version=20001
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (63.86%)
# Likes:    9844
# Dislikes: 309
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# Example 1:
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# Example 2:
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2^12 - 1].
# -1000 <= Node.val <= 1000
# 
# 
# 
# Follow-up:
# 
# 
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        def helper(node):
            if node is None or node.left is None:
                return None
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            helper(node.left)
            helper(node.right)
        helper(root)
            
            
                
        return root
            
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

