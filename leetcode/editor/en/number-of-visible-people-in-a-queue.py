#
# @lc app=leetcode id=1944 lang=python
# @lcpr version=30201
#
# [1944] Number of Visible People in a Queue
#
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/
#
# algorithms
# Hard (71.35%)
# Likes:    1961
# Dislikes: 60
# Total Accepted:    85.9K
# Total Submissions: 120.4K
# Testcase Example:  '[10,6,8,5,11,9]'
#
# There are n people standing in a queue, and they numbered from 0 to n - 1 in
# left to right order. You are given an array heights of distinct integers
# where heights[i] represents the height of the i^th person.
# 
# A person can see another person to their right in the queue if everybody in
# between is shorter than both of them. More formally, the i^th person can see
# the j^th person if i < j and min(heights[i], heights[j]) > max(heights[i+1],
# heights[i+2], ..., heights[j-1]).
# 
# Return an array answer of length n where answer[i] is the number of people
# the i^th person can see to their right in the queue.
# 
# 
# Example 1:
# 
# 
# 
# Input: heights = [10,6,8,5,11,9]
# Output: [3,1,2,1,1,0]
# Explanation:
# Person 0 can see person 1, 2, and 4.
# Person 1 can see person 2.
# Person 2 can see person 3 and 4.
# Person 3 can see person 4.
# Person 4 can see person 5.
# Person 5 can see no one since nobody is to the right of them.
# 
# 
# Example 2:
# 
# Input: heights = [5,1,2,3,10]
# Output: [4,1,1,1,0]
# 
# 
# 
# Constraints:
# 
# 
# n == heights.length
# 1 <= n <= 10^5
# 1 <= heights[i] <= 10^5
# All the values of heights are unique.
# 
# 
#

# @lc code=start
from collections import deque


class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        dq = deque()
        res = []
        for i in reversed(heights):
            if len(dq) == 0:
                res.append(0)
                dq.append(i)
            else:
                count = 0
                while dq and dq[-1] < i:
                    dq.pop()
                    count+=1
                if len(dq) != 0:
                    count+=1
                dq.append(i)
                res.append(count)
        res.reverse()
        return res
                
# @lc code=end



#
# @lcpr case=start
# [10,6,8,5,11,9]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,10]\n
# @lcpr case=end

#

