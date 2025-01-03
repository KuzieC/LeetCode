#
# @lc app=leetcode id=523 lang=python3
# @lcpr version=20002
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (30.44%)
# Likes:    6370
# Dislikes: 667
# Total Accepted:    610.2K
# Total Submissions: 2M
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given an integer array nums and an integer k, return true if nums has a good
# subarray or false otherwise.
# 
# A good subarray is a subarray where:
# 
# 
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# 
# 
# Note that:
# 
# 
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n
# * k. 0 is always a multiple of k.
# 
# 
# 
# Example 1:
# 
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up
# to 6.
# 
# 
# Example 2:
# 
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose
# elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# 
# 
# Example 3:
# 
# Input: nums = [23,2,6,4,7], k = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum  = [0] * (len(nums)+1)
        if len(nums) == 1:
            return False
        for i in range(1,len(nums)+1):
            preSum[i] = (preSum[i-1] + nums[i-1]) %k
        SumToIndex = {}
        for i in range(len(preSum)):
            if preSum[i] not in SumToIndex:
                SumToIndex[preSum[i]] = i
            else:
                if i - SumToIndex[preSum[i]] >= 2:
                    return True
        
        return False
            
        
# @lc code=end



#
# @lcpr case=start
# [23,2,4,6,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n13\n
# @lcpr case=end

#

