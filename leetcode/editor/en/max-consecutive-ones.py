#
# @lc app=leetcode id=485 lang=python3
# @lcpr version=30201
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (62.62%)
# Likes:    6287
# Dislikes: 471
# Total Accepted:    1.7M
# Total Submissions: 2.7M
# Testcase Example:  '[1,1,0,1,1,1]'
#
# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
# 
# 
# Example 1:
# 
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s. The maximum number of consecutive 1s is 3.
# 
# 
# Example 2:
# 
# Input: nums = [1,0,1,1,0,1]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCon = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            else:
                count = 0
            maxCon = max(maxCon, count)
        return maxCon
# @lc code=end



#
# @lcpr case=start
# [1,1,0,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1,0,1]\n
# @lcpr case=end

#

