#
# @lc app=leetcode id=35 lang=python3
# @lcpr version=20002
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (47.47%)
# Likes:    16568
# Dislikes: 770
# Total Accepted:    3.3M
# Total Submissions: 6.9M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# 
# Example 2:
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# 
# 
# Example 3:
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        def left_most(nums,x):
            left = 0
            right = len(nums)-1
            
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] >= x:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left
        
        pos = left_most(nums,target)
        print(pos)
        return pos
        
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

