#
# @lc app=leetcode id=136 lang=python3
# @lcpr version=30201
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (76.08%)
# Likes:    17697
# Dislikes: 817
# Total Accepted:    3.8M
# Total Submissions: 5M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
# 
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,2,1]
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,1,2,1,2]
# 
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [1]
# 
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.
# 
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
# @lc code=end



#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

