#
# @lc app=leetcode id=220 lang=python3
# @lcpr version=20002
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Hard (23.07%)
# Likes:    1058
# Dislikes: 96
# Total Accepted:    264.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# You are given an integer array nums and two integers indexDiff and
# valueDiff.
# 
# Find a pair of indices (i, j) such that:
# 
# 
# i != j,
# abs(i - j) <= indexDiff.
# abs(nums[i] - nums[j]) <= valueDiff, and
# 
# 
# Return true if such pair exists or false otherwise.
# 
# 
# Example 1:
# 
# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true
# Explanation: We can choose (i, j) = (0, 3).
# We satisfy the three conditions:
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
# 
# 
# Example 2:
# 
# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false
# Explanation: After trying all the possible pairs (i, j), we cannot satisfy
# the three conditions, so we return false.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 1 <= indexDiff <= nums.length
# 0 <= valueDiff <= 10^9
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#

