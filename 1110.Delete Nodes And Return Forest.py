#
# @lc app=leetcode id=1110 lang=python3
# @lcpr version=30202
#
# [1110] Delete Nodes And Return Forest
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
        self.de = {}
    def helper(self,root):
        if not root:
            return None
        leftSub = self.helper(root.left)
        rightSub = self.helper(root.right)
        root.left = leftSub
        root.right = rightSub
        if root.val in self.de:
            if leftSub == rightSub == None:
                return None
            else:
                if leftSub:
                    self.res.append(leftSub)
                if rightSub:
                    self.res.append(rightSub)
                return None
        else:
            return root
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.de = set(to_delete)
        self.helper(root)
        if root and root.val not in self.de:
            self.res.append(root)
        return self.res
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n[3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,null,3]\n[3]\n
# @lcpr case=end

#

