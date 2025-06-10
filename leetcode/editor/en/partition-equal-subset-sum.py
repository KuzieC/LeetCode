#
# @lc app=leetcode id=416 lang=python3
# @lcpr version=30201
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (48.39%)
# Likes:    13235
# Dislikes: 283
# Total Accepted:    1.2M
# Total Submissions: 2.5M
# Testcase Example:  '[1,5,11,5]'
#
# Given an integer array nums, return true if you can partition the array into
# two subsets such that the sum of the elements in both subsets is equal or
# false otherwise.
# 
# 
# Example 1:
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 
# 
#

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s = sum(nums)
        target = s//2
        if s / 2 != target:
            return False
        dp = [False] * (target+1)
        dp[0] = True
        for ind in range(0,len(nums)):
            for j in range(target,0,-1):
                if j - nums[ind] >= 0:
                    dp[j] = dp[j] or dp[j-nums[ind]]
        return dp[target]
# @lc code=end


#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

