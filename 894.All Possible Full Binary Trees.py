#
# @lc app=leetcode id=894 lang=python3
# @lcpr version=30202
#
# [894] All Possible Full Binary Trees
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
        self.memo = defaultdict(list)
    def helper(self,n):
        if n == 1:
            return [TreeNode()]
        if n in self.memo:
            return self.memo[n]
        
        res = []
        for left in range(1,n-1,2):
            right = n - 1 - left

            leftsub = self.helper(left)
            rightsub = self.helper(right)
            for l in leftsub:
                for r in rightsub:
                    curr = TreeNode()
                    curr.left = l
                    curr.right = r
                    res.append(curr)
        self.memo[n] = res
        return res
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        return self.helper(n)
# @lc code=end



#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

