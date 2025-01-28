#
# @lc app=leetcode id=200 lang=python3
# @lcpr version=20004
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (61.27%)
# Likes:    23417
# Dislikes: 547
# Total Accepted:    3.2M
# Total Submissions: 5.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end

class Solution:
   
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res+=1
                    self.dfs(grid,i,j)
                    
        return res
    
    def dfs(self,grid: List[List[str]], row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return
        if grid[row][col] == "1":
            grid[row][col] = "0"
        self.dfs(grid,row+1,col)
        self.dfs(grid,row,col+1)
        self.dfs(grid,row-1,col)
        self.dfs(grid,row,col-1)
        return
# @lc code=end



#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#

