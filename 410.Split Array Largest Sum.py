#
# @lc app=leetcode id=410 lang=python3
# @lcpr version=20002
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (56.65%)
# Likes:    10027
# Dislikes: 232
# Total Accepted:    400.8K
# Total Submissions: 707.6K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an integer array nums and an integer k, split nums into k non-empty
# subarrays such that the largest sum of any subarray is minimized.
# 
# Return the minimized largest sum of the split.
# 
# A subarray is a contiguous part of the array.
# 
# 
# Example 1:
# 
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum
# among the two subarrays is only 18.
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum
# among the two subarrays is only 9.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= k <= min(50, nums.length)
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def f(nums,x):
            count = 1
            total = 0
            for i in range(len(nums)):
                if total + nums[i] > x:
                    total = nums[i] 
                    count += 1
                else:
                    total += nums[i]
            
            return count

        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = left + (right - left)//2
            res = f(nums,mid)
            
            if res > k:
                left = mid + 1
            else:
                right = mid
            
        return left

            
# @lc code=end



#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#

