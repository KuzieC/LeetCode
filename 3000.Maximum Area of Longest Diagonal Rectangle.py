#
# @lc app=leetcode id=3000 lang=python3
# @lcpr version=30202
#
# [3000] Maximum Area of Longest Diagonal Rectangle
#

# @lc code=start
import math


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        prevMax = 0.0
        for length, width in dimensions:
            temp = math.sqrt(length**2 + width**2)
            if temp > prevMax:
                prevMax = temp
                res = length*width
            elif temp == prevMax:
                res = max(res, length*width)
        return res
# @lc code=end



#
# @lcpr case=start
# [[9,3],[8,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,4],[4,3]]\n
# @lcpr case=end

#

