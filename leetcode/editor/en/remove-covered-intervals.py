#
# @lc app=leetcode id=1288 lang=python3
# @lcpr version=30201
#
# [1288] Remove Covered Intervals
#
# https://leetcode.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (56.17%)
# Likes:    2284
# Dislikes: 61
# Total Accepted:    133.5K
# Total Submissions: 237.6K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# Given an array intervals where intervals[i] = [li, ri] represent the interval
# [li, ri), remove all intervals that are covered by another interval in the
# list.
# 
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a
# and b <= d.
# 
# Return the number of remaining intervals.
# 
# 
# Example 1:
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# 
# Example 2:
# 
# Input: intervals = [[1,4],[2,3]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= li < ri <= 10^5
# All the given intervals are unique.
# 
# 
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : ( x[0],x[1]))
        res = []
        for start,end in intervals:
            if not res or end > res[-1][1]:
                if res and res[-1][0] == start:
                    res[-1][1] = max(res[-1][1],end)
                else:
                    res.append([start,end])
        return len(res)
# @lc code=end



#
# @lcpr case=start
# [[1,4],[3,6],[2,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[2,3]]\n
# @lcpr case=end

#
