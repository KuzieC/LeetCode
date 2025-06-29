#
# @lc app=leetcode id=16 lang=python
# @lcpr version=30201
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.93%)
# Likes:    11029
# Dislikes: 596
# Total Accepted:    1.5M
# Total Submissions: 3.2M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
# Example 2:
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twoSum(nums, target, ind):
            left = ind
            right = len(nums)-1
            diff = float('inf')
            res = 0
            while left < right:
                d = nums[left] + nums[right] - target
                if abs(d) < abs(diff):
                    diff = d
                    res = nums[left] + nums[right]
                if nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            return res
        nums.sort()
        res = 0
        diff = float('inf')
        for i in range(len(nums)-2):
            k =  twoSum(nums,target-nums[i],i+1)
            print(nums[i],k)
            if abs(nums[i] + k - target) < abs(diff):
                diff = k + nums[i] - target
                res = k+ nums[i]
        return res
            
# @lc code=end



#
# @lcpr case=start
# [-1,2,1,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

#

