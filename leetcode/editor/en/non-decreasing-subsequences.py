#
# @lc app=leetcode id=491 lang=python3
# @lcpr version=30201
#
# [491] Non-decreasing Subsequences
#
# https://leetcode.com/problems/non-decreasing-subsequences/description/
#
# algorithms
# Medium (61.74%)
# Likes:    3757
# Dislikes: 233
# Total Accepted:    191.8K
# Total Submissions: 310.7K
# Testcase Example:  '[4,6,7,7]'
#
# Given an integer array nums, return all the different possible non-decreasing
# subsequences of the given array with at least two elements. You may return
# the answer in any order.
# 
# 
# Example 1:
# 
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# 
# 
# Example 2:
# 
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
    def dfs(self,nums,ind,curr):
        if len(curr) >= 2:
            self.res.append(curr[:])
        used = set()
        for i in range(ind,len(nums)):
            if nums[i] in used:
                continue
            if curr and nums[i] < curr[-1]:
                continue
            used.add(nums[i])
            curr.append(nums[i])
            self.dfs(nums,i+1,curr)
            curr.pop()                
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums,0,[])
        return self.res
# @lc code=end



#
# @lcpr case=start
# [4,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,3,2,1]\n
# @lcpr case=end

#

