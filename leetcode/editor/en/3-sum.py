#
# @lc app=leetcode id=15 lang=python3
# @lcpr version=30201
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (37.17%)
# Likes:    33226
# Dislikes: 3115
# Total Accepted:    4.8M
# Total Submissions: 13M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def twoSum(nums,ind,target):
            res = []
            lo = ind
            hi = len(nums)-1
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    res.append([nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1    
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo+=1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi-=1
                elif nums[lo] + nums[hi] < target:
                    lo+=1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo+=1
                else:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi-=1
            return res
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            curr = nums[i]
            for pair in twoSum(nums,i+1,0-curr):
                pair.append(curr)
                res.append(pair[:])
        return res
            
            
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

