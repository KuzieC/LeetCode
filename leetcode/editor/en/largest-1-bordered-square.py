#
# @lc app=leetcode id=1139 lang=python3
# @lcpr version=30201
#
# [1139] Largest 1-Bordered Square
#
# https://leetcode.com/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (51.14%)
# Likes:    751
# Dislikes: 117
# Total Accepted:    29.6K
# Total Submissions: 57.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D grid of 0s and 1s, return the number of elements in the largest
# square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
# exist in the grid.
# 
# 
# Example 1:
# 
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
# 
# 
# Example 2:
# 
# Input: grid = [[1,1,0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] is 0 or 1
# 
#

# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        right = [[0] * col for _ in  range(row)]
        down = [[0] * col for _ in  range(row)]
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if c == col-1:
                    right[r][c] = grid[r][c]
                else:
                    right[r][c] = right[r][c+1] + 1 if grid[r][c] == 1 else 0
                if r == row-1:
                    down[r][c] = grid[r][c]
                else:
                    down[r][c] = down[r+1][c] + 1 if grid[r][c] == 1 else 0
        
        
        res = 0
        for r in range(row):
            for c in range(col):
                side = min(right[r][c],down[r][c])
                for i in range(side,0,-1):
                    if down[r][c + i - 1] >= i and right[r + i - 1][c] >= i:
                        res = max(res,i)
                        break
        return res*res
                    
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,0,0]]\n
# @lcpr case=end

#

