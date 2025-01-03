#
# @lc app=leetcode id=525 lang=python3
# @lcpr version=20002
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (48.95%)
# Likes:    8074
# Dislikes: 397
# Total Accepted:    497.9K
# Total Submissions: 1M
# Testcase Example:  '[0,1]'
#
# Given a binary array nums, return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.
# 
# 
# Example 1:
# 
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number
# of 0 and 1.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Constraints:
# 
# 
 # 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        preSum =  [0] * (len(nums)+1)
        preSum[0]  = 0
        for i in range(1,len(nums)+1):
            preSum[i] = preSum[i-1] + (1 if nums[i-1] == 1 else -1)
            
        SumToIndex = {}
        res = 0
        for i in range(len(preSum)):
            if preSum[i] not in SumToIndex:
                SumToIndex[preSum[i]] = i
            else:
                res = max(res,i - SumToIndex[preSum[i]])
        
        return res
            
# @lc code=end



#
# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

#

