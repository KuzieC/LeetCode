#
# @lc app=leetcode id=18 lang=python3
# @lcpr version=30202
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (38.67%)
# Likes:    12298
# Dislikes: 1480
# Total Accepted:    1.4M
# Total Submissions: 3.6M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# Example 2:
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self,start,nums,target):
        left = start
        right = len(nums)-1
        res = []
        while left < right:

            if nums[left] + nums[right] == target:
                res.append([nums[left],nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
            while right > left > start and nums[left] == nums[left-1]:
                left+=1
            while left < right < len(nums) - 1 and nums[right] == nums[right+1]:
                right -=1
        return res
    def solveSum(self,start,nums,target,n):        
        f = []
        if n > 2:
            for i in range(start,len(nums)-n+1):
                if nums[i] * n > target:
                    break
                if nums[i] + nums[-1] * (n-1) < target:
                    continue
                if i > start and nums[i] == nums[i-1]:
                    continue
                res = self.solveSum(i+1,nums,target-nums[i],n-1)
                for g in res:
                    f.append(g + [nums[i]])
        else:
            return self.twoSum(start,nums,target)
        return f
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.solveSum(0,nums,target,4)
        
# @lc code=end



#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

