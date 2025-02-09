#
# @lc app=leetcode id=581 lang=python3
# @lcpr version=30003
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Medium (37.23%)
# Likes:    7833
# Dislikes: 268
# Total Accepted:    348.5K
# Total Submissions: 936.3K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array nums, you need to find one continuous subarray such
# that if you only sort this subarray in non-decreasing order, then the whole
# array will be sorted in non-decreasing order.
# 
# Return the shortest such subarray and output its length.
# 
# 
# Example 1:
# 
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: 0
# 
# 
# Example 3:
# 
# Input: nums = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
# 
# Follow up: Can you solve it in O(n) time complexity?
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums)
        left = -1
        right = -1
        for i in range(len(nums)):
            if temp[i] != nums[i]:
                left = i
                break
        for i in range(len(nums)-1,-1,-1):
            if temp[i] != nums[i]:
                right = i
                break
        return 0 if left == -1 and right == -1 else right - left + 1
# @lc code=end



#
# @lcpr case=start
# [2,6,4,8,10,9,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

