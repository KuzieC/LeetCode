#
# @lc app=leetcode id=3195 lang=python3
# @lcpr version=30202
#
# [3195] Find the Minimum Area to Cover All Ones I
#

# @lc code=start
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        maxX=maxY = 0
        minX=minY = 1001
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i < minX:
                        minX = i
                    if i > maxX:
                        maxX = i
                    if j < minY:
                        minY = j
                    if j > maxY:
                        maxY = j
        return (maxY - minY + 1) * (maxX - minX + 1)
# @lc code=end



#
# @lcpr case=start
# [[0,1,0],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0],[0,0]]\n
# @lcpr case=end

#

