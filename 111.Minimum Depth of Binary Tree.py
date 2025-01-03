#
# @lc app=leetcode id=111 lang=python3
# @lcpr version=20001
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (49.13%)
# Likes:    7361
# Dislikes: 1315
# Total Accepted:    1.3M
# Total Submissions: 2.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# 
# 
# Example 2:
# 
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^5].
# -1000 <= Node.val <= 1000
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
            q = deque()
            if root is None:
                return 0
            q.append(root)
            depth = 0
            while q:
                l = len(q)
                depth += 1
                for i in range(l):
                    tmp = q.popleft()
                    print(tmp.val)
                    if tmp.left == None and tmp.right == None:
                        return depth
                    if tmp.left is not None:
                        q.append(tmp.left)
                    if tmp.right is not None:
                        q.append(tmp.right)
            return -1
                    
                
                

# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,null,3,null,4,null,5,null,6]\n
# @lcpr case=end

#

