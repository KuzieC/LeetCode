#
# @lc app=leetcode id=1425 lang=python3
# @lcpr version=30002
#
# [1425] Constrained Subsequence Sum
#
# https://leetcode.com/problems/constrained-subsequence-sum/description/
#
# algorithms
# Hard (56.48%)
# Likes:    2162
# Dislikes: 104
# Total Accepted:    82.7K
# Total Submissions: 146.4K
# Testcase Example:  '[10,2,-10,5,20]\n2'
#
# Given an integer array nums and an integer k, return the maximum sum of a
# non-empty subsequence of that array such that for every two consecutive
# integers in the subsequence, nums[i] and nums[j], where i < j, the condition
# j - i <= k is satisfied.
# 
# A subsequence of an array is obtained by deleting some number of elements
# (can be zero) from the array, leaving the remaining elements in their
# original order.
# 
# 
# Example 1:
# 
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
# 
# 
# Example 2:
# 
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest
# number.
# 
# 
# Example 3:
# 
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        s= []
        left = 0
        right = 0
        res = -99999
        while right < len(nums):
            if right - left > k:
                if s[0] == dp[left]:
                    s.pop(0)
                left+=1
            if s:
                dp[right] = max(nums[right],nums[right]+s[0])
            else:
                dp[right] = nums[right]
            while s and s[-1] < dp[right]:
                s.pop()
            s.append(dp[right])
            right+=1 
            #print(dp)
        for i in dp:
            res = max(res,i)
        return res
                
            

# @lc code=end



#
# @lcpr case=start
# [10,2,-10,5,20]\n2\n
# @lcpr case=end

# @lcpr case=start
# [-1,-2,-3]\n1\n
# @lcpr case=end

# @lcpr case=start
# [10,-2,-10,-5,20]\n2\n
# @lcpr case=end

#

