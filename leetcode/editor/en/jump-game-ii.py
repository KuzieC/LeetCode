#
# @lc app=leetcode id=45 lang=python3
# @lcpr version=30202
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (41.71%)
# Likes:    15763
# Dislikes: 670
# Total Accepted:    1.8M
# Total Submissions: 4.3M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
# 
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
# 
# 
# 0 <= j <= nums[i] and
# i + j < n
# 
# 
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
# 
# 
# Example 1:
# 
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# Input: nums = [2,3,0,1,4]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
# 
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        maxstep = 0
        currmax = 0
        for i in range(len(nums)-1):
            currmax = max(currmax,i +  nums[i])
            if maxstep == i:
                res+=1
                maxstep = currmax
            if maxstep >= len(nums)-1:
                return res
        return res
    
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

