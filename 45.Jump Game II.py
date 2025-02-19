#
# @lc app=leetcode id=45 lang=python3
# @lcpr version=30004
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (41.06%)
# Likes:    15237
# Dislikes: 625
# Total Accepted:    1.6M
# Total Submissions: 3.9M
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


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        ma = 0
        curr = 0
        for i in range(len(nums)-1):
            ma = max(ma,i+nums[i])
            if i >= curr:
                res += 1
                curr = ma
            
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

