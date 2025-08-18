#
# @lc app=leetcode id=503 lang=python3
# @lcpr version=30202
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (66.91%)
# Likes:    8717
# Dislikes: 221
# Total Accepted:    636.6K
# Total Submissions: 951.5K
# Testcase Example:  '[1,2,1]'
#
# Given a circular integer array nums (i.e., the next element of
# nums[nums.length - 1] is nums[0]), return the next greater number for every
# element in nums.
# 
# The next greater number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, return -1 for this
# number.
# 
# 
# Example 1:
# 
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also
# 2.
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res= [0] * len(nums)
        stack = []
        nums += nums
        
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            res[i%n] = -1 if not stack else stack[-1]
            stack.append(nums[i%n])
        return res
                
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,3]\n
# @lcpr case=end

#

