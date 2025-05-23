#
# @lc app=leetcode id=918 lang=python3
# @lcpr version=30002
#
# [918] Maximum Sum Circular Subarray
#
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (46.66%)
# Likes:    6843
# Dislikes: 318
# Total Accepted:    313.2K
# Total Submissions: 671.3K
# Testcase Example:  '[1,-2,3,-2]'
#
# Given a circular integer array nums of length n, return the maximum possible
# sum of a non-empty subarray of nums.
# 
# A circular array means the end of the array connects to the beginning of the
# array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the
# previous element of nums[i] is nums[(i - 1 + n) % n].
# 
# A subarray may only include each element of the fixed buffer nums at most
# once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does
# not exist i <= k1, k2 <= j with k1 % n == k2 % n.
# 
# 
# Example 1:
# 
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# 
# 
# Example 2:
# 
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# 
# 
# Example 3:
# 
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l = len(nums)
        nums.extend(nums)
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        print(prefix)
        s = []
        res = -999990
        left = 0 
        right = 0
        s.append(0)
        while right+1 < len(prefix):
            
            right+=1
            res = max(res, prefix[right] - s[0])
            while s and right - left >= l:
                if s[0] == prefix[left]:
                    s.pop(0)
                left+=1

            while s and s[-1] > prefix[right]:
                s.pop()
            s.append(prefix[right])
  
        return res
# @lc code=end



#
# @lcpr case=start
# [1,-2,3,-2]\n
# @lcpr case=end

# @lcpr case=start
# [5,-3,5]\n
# @lcpr case=end

# @lcpr case=start
# [-3,-2,-3]\n
# @lcpr case=end

#

