#
# @lc app=leetcode id=78 lang=python3
# @lcpr version=30201
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (80.95%)
# Likes:    18306
# Dislikes: 309
# Total Accepted:    2.5M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
    def dfs(self,nums,curr,used,ind):
        self.res.append(curr[:])
        for i in range(ind,len(nums)):
            if i not in used:
                used.add(i)
                curr.append(nums[i])
                self.dfs(nums,curr,used,i+1)
                curr.pop()
                used.remove(i)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        used = set()
        self.dfs(nums,curr,used,0)
        return self.res
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

