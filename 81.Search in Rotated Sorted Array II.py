#
# @lc app=leetcode id=81 lang=python3
# @lcpr version=30005
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (38.52%)
# Likes:    8840
# Dislikes: 1074
# Total Accepted:    894.8K
# Total Submissions: 2.3M
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).
# 
# Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
# [4,5,6,6,7,0,1,2,4,4].
# 
# Given the array nums after the rotation and an integer target, return true if
# target is in nums, or false if it is not in nums.
# 
# You must decrease the overall operation steps as much as possible.
# 
# 
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# 
# 
# 
# Follow up: This problem is similar to Search in Rotated Sorted Array, but
# nums may contain duplicates. Would this affect the runtime complexity? How
# and why?
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left <= right:
            while left+1 < len(nums) and nums[left] == nums[left+1]:
                left += 1
            while right-1 >-1 and nums[right] == nums[right-1]:
                right-=1
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
# @lc code=end



#
# @lcpr case=start
# [2,5,6,0,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,5,6,0,0,1,2]\n3\n
# @lcpr case=end

#

