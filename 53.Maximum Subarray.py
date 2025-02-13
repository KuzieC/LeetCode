#
# @lc app=leetcode id=53 lang=python3
# @lcpr version=30005
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (51.64%)
# Likes:    35149
# Dislikes: 1490
# Total Accepted:    4.6M
# Total Submissions: 9M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
# 
# 
# Example 1:
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# 
# 
# Example 2:
# 
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# 
# 
# Example 3:
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        mini = presum[0]
        res = float('-inf')
        for i in presum[1:]:
            res = max(res, i - mini)
            mini = min(mini,i)
        return res
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

