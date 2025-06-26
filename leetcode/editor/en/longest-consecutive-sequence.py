#
# @lc app=leetcode id=128 lang=python3
# @lcpr version=30201
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.04%)
# Likes:    21535
# Dislikes: 1160
# Total Accepted:    2.6M
# Total Submissions: 5.5M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# Example 3:
# 
# Input: nums = [1,0,1,2]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
        res = 0
        for num in nums:
            if num-1 not in mp:
                count = 1
                while num + 1 in mp:
                    num = num+1
                    count += 1
                res = max(count,res)
        return res
# @lc code=end




#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#

