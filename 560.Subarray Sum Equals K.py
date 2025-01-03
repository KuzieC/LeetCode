#
# @lc app=leetcode id=560 lang=python3
# @lcpr version=20002
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.27%)
# Likes:    22064
# Dislikes: 689
# Total Accepted:    1.4M
# Total Submissions: 3.3M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums)+1)
        
        
        for i in range(1,len(nums)+1):
            preSum[i] = preSum[i-1]+nums[i-1]
        
        SumToIndex = {}
        res = 0
        for i in range(len(preSum)):
            if preSum[i] - k in SumToIndex:
                res += SumToIndex[preSum[i] - k]
            if preSum[i] not in SumToIndex:
                SumToIndex[preSum[i]] = 1
            else:
                SumToIndex[preSum[i]] += 1

        return res
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

