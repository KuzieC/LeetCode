#
# @lc app=leetcode id=974 lang=python3
# @lcpr version=20002
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (55.48%)
# Likes:    7314
# Dislikes: 322
# Total Accepted:    371.6K
# Total Submissions: 669.7K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an integer array nums and an integer k, return the number of non-empty
# subarrays that have a sum divisible by k.
# 
# A subarray is a contiguous part of an array.
# 
# 
# Example 1:
# 
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# Example 2:
# 
# Input: nums = [5], k = 9
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# 2 <= k <= 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums)+1)
        
        for i in range(1,len(preSum)):
            preSum[i] = preSum[i-1]+nums[i-1]
        mp = {0:1}
        res = 0
        for i in range(1,len(preSum)):
            if preSum[i] % k in mp:
                count = mp[preSum[i] % k]
                res += count
                mp[preSum[i] % k] += 1
            else:
                mp[preSum[i] % k] = 1
        return res     
        
# @lc code=end



#
# @lcpr case=start
# [4,5,0,-2,-3,1]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5]\n9\n
# @lcpr case=end

#

