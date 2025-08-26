#
# @lc app=leetcode id=988 lang=python3
# @lcpr version=30202
#
# [988] Smallest String Starting From Leaf
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
        self.res = ""
    
    def dfs(self,node,curr):
        if not node:
            return
        if node.left == None and node.right == None:
            if not self.res or curr < self.res:
                self.res = curr
            return
        if node.left:
            self.dfs(node.left, chr(ord('a') + node.left.val) + curr)
        if node.right:
            self.dfs(node.right, chr(ord('a') + node.right.val) + curr)
        
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        self.dfs(root, chr(ord('a')+root.val))
        return self.res
# @lc code=endr



#
# @lcpr case=start
# [0,1,2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [25,1,3,1,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,null,1,0,null,0]\n
# @lcpr case=end

#

