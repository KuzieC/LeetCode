#
# @lc app=leetcode id=998 lang=python3
# @lcpr version=30202
#
# [998] Maximum Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if not root:
            return []
        leftSub = self.helper(root.left)
        rightSub = self.helper(root.right)
        return leftSub + [root.val] + rightSub
    def helper2(self,lis:list[int],left,right):
        if left >= right:
            return None
        if left+1 == right:
            return TreeNode(lis[left])
        mid = lis.index(max(lis[left:right]))
        midNode = TreeNode(lis[mid])
        midNode.left = self.helper2(lis,left,mid)
        midNode.right = self.helper2(lis,mid+1,right)
        return midNode
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = self.helper(root) + [val]
        return self.helper2(temp,0,len(temp))
# @lc code=end



#
# @lcpr case=start
# [4,1,3,null,null,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,2,4,null,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,2,3,null,1]\n4\n
# @lcpr case=end

#

