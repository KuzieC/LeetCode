 #
# @lc app=leetcode id=1124 lang=python3
# @lcpr version=20002
#
# [1124] Longest Well-Performing Interval
#
# https://leetcode.com/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (35.47%)
# Likes:    1445
# Dislikes: 119
# Total Accepted:    35.3K
# Total Submissions: 99.5K
# Testcase Example:  '[9,9,6,0,6,6,9]'
#
# We are given hours, a list of the number of hours worked per day for a given
# employee.
# 
# A day is considered to be a tiring day if and only if the number of hours
# worked is (strictly) greater than 8.
# 
# A well-performing interval is an interval of days for which the number of
# tiring days is strictly larger than the number of non-tiring days.
# 
# Return the length of the longest well-performing interval.
# 
# 
# Example 1:
# 
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
# 
# 
# Example 2:
# 
# Input: hours = [6,6,6]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hours.length <= 10^4
# 0 <= hours[i] <= 16
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        preSum = [0] * (len(hours)+1)
        mp = {}
        res = 0
        for i in range(1,len(preSum)):
            preSum[i] = preSum[i-1] + (1 if hours[i-1] > 8 else -1)
            
            if preSum[i] not in mp:
                mp[preSum[i]] = i
                
            if preSum[i] > 0:
                res = max(res,i)
            else:
                tmp = preSum[i] - 1
                if tmp in mp:
                    res = max(res,i - mp[tmp])
        return res
            
            
# @lc code=end



#
# @lcpr case=start
# [9,9,6,0,6,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,6]\n
# @lcpr case=end

#

