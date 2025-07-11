#
# @lc app=leetcode id=300 lang=python3
# @lcpr version=30201
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (57.65%)
# Likes:    21797
# Dislikes: 481
# Total Accepted:    2.2M
# Total Submissions: 3.7M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# 
# Example 1:
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
# 
#

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        deck = [0]*len(nums)
        pile = 0
        
        for i in range(len(nums)):
            left, right = 0, pile
            curr = nums[i]
            if i == 0:
                deck[0] = curr
                pile=1
                continue
            while left < right:
                mid = left + (right - left) // 2
                if deck[mid] < curr:
                    left = mid + 1
                else:
                    right = mid
            if left == pile:
                deck[pile] = curr
                pile+=1
            elif deck[left] >= curr:
                deck[left] = curr
            else:
                pile += 1
                deck[pile] = curr
        return pile
                
                    
                
# @lc code=end


#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#

