#
# @lc app=leetcode id=962 lang=python3
# @lcpr version=30002
#
# [962] Maximum Width Ramp
#
# https://leetcode.com/problems/maximum-width-ramp/description/
#
# algorithms
# Medium (55.54%)
# Likes:    2647
# Dislikes: 89
# Total Accepted:    181.9K
# Total Submissions: 327.4K
# Testcase Example:  '[6,0,8,2,1,5]'
#
# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i]
# <= nums[j]. The width of such a ramp is j - i.
# 
# Given an integer array nums, return the maximum width of a ramp in nums. If
# there is no ramp in nums, return 0.
# 
# 
# Example 1:
# 
# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] =
# 0 and nums[5] = 5.
# 
# 
# Example 2:
# 
# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] =
# 1 and nums[9] = 1.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5 * 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxRight = [0 for _ in range(len(nums))]
        maxRight[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            maxRight[i] = max(nums[i], maxRight[i+1])
        maxRamp = 0
        i = 0; j = 1
        print(maxRight)
        while j < len(nums):
            
            if nums[i] <= maxRight[j]:
                while j < len(nums) and maxRight[j] == maxRight[j-1]:
                    j+=1
                maxRamp = max(j - i - 1,maxRamp)
            else:
                while i < len(nums) and nums[i] > maxRight[j]:
                    i+=1
            
                
        return maxRamp
            
# @lc code=end



#
# @lcpr case=start
# [6,0,8,2,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [9,8,1,0,1,9,4,0,4,1]\n
# @lcpr case=end

#

