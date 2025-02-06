#
# @lc app=leetcode id=862 lang=python3
# @lcpr version=30002
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (32.17%)
# Likes:    4977
# Dislikes: 138
# Total Accepted:    182.7K
# Total Submissions: 567.8K
# Testcase Example:  '[1]\n1'
#
# Given an integer array nums and an integer k, return the length of the
# shortest non-empty subarray of nums with a sum of at least k. If there is no
# such subarray, return -1.
# 
# A subarray is a contiguous part of an array.
# 
# 
# Example 1:
# Input: nums = [1], k = 1
# Output: 1
# Example 2:
# Input: nums = [1,2], k = 4
# Output: -1
# Example 3:
# Input: nums = [2,-1,2], k = 3
# Output: 3
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= 10^9
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        res = 99999
        for i in nums:
            prefix.append(prefix[-1]+i)
        q = []
        for i in range(len(prefix)):
            while q and prefix[q[-1]] > prefix[i]:
                q.pop()
            q.append(i)
            while q and prefix[i] - prefix[q[0]] >= k:
                res = min(res,i - q[0])
                q.pop(0)
        return -1 if res == 99999 else res
            
# @lc code=end



#
# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

#

