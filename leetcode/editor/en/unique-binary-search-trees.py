#
# @lc app=leetcode id=96 lang=python3
# @lcpr version=30202
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (62.58%)
# Likes:    10747
# Dislikes: 434
# Total Accepted:    778.8K
# Total Submissions: 1.2M
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
# 
# 
# Example 1:
# 
# Input: n = 3
# Output: 5
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 19
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.memo = {}
    def numTrees(self, n: int) -> int:
        return self.helper(1,n+1)
    def helper(self,left,right):
        if right - left <= 1:
            return 1
        if (left,right) in self.memo:
            return self.memo[(left,right)]

        res = 0
        for i in range(left,right):
            l = self.helper(left,i)
            r = self.helper(i+1,right)
            res += l * r
        self.memo[(left,right)] = res
        return self.memo[(left,right)]       
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

