#
# @lc app=leetcode id=986 lang=python3
# @lcpr version=30201
#
# [986] Interval List Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (72.72%)
# Likes:    5790
# Dislikes: 127
# Total Accepted:    520.8K
# Total Submissions: 716.1K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list
# of intervals is pairwise disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
# a <= x <= b.
# 
# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].
# 
# 
# Example 1:
# 
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 
# 
# Example 2:
# 
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 10^9
# endi < starti+1
# 0 <= startj < endj <= 10^9 
# endj < startj+1
# 
# 
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i= 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            if second[0] >= first[0] and second[0] <= first[1]:
                res.append([second[0],min(second[1],first[1])])
            elif first[0] >= second[0] and first[0] <= second[1]:
                res.append([first[0],min(first[1],second[1])])
            if first[1] > second[1]:
                j+=1
            else:
                i+=1
        return res
                    
                
                    
# @lc code=end



#
# @lcpr case=start
# [[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,9]]\n[]\n
# @lcpr case=end

#

