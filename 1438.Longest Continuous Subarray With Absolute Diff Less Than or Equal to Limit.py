#
# @lc app=leetcode id=1438 lang=python3
# @lcpr version=30002
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (56.68%)
# Likes:    4197
# Dislikes: 201
# Total Accepted:    252.5K
# Total Submissions: 445.5K
# Testcase Example:  '[8,2,4,7]\n4'
#
# Given an array of integers nums and an integer limit, return the size of the
# longest non-empty subarray such that the absolute difference between any two
# elements of this subarray is less than or equal to limit.
# 
# 
# Example 1:
# 
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# 
# 
# Example 2:
# 
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute
# diff is |2-7| = 5 <= 5.
# 
# 
# Example 3:
# 
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = []
        maxQ = []
        left = 0
        res = 0
        right = 0
        while right < len(nums):
            while minQ and minQ[-1] > nums[right]:
                minQ.pop()
            minQ.append(nums[right])
            while maxQ and maxQ[-1] < nums[right]:
                maxQ.pop()
            maxQ.append(nums[right])
            right+=1
            while left <= right and abs(minQ[0] - maxQ[0]) > limit:
                if minQ[0] == nums[left]:
                    minQ.pop(0)
                if maxQ[0] == nums[left]:
                    maxQ.pop(0)
                left+=1
            res = max(res,right - left)
        
        return res
            
                
# @lc code=end



#
# @lcpr case=start
# [8,2,4,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [10,1,2,4,7,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,2,2,2,4,4,2,2]\n0\n
# @lcpr case=end

#

