#
# @lc app=leetcode id=1254 lang=python3
# @lcpr version=30202
#
# [1254] Number of Closed Islands
#
# https://leetcode.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (66.79%)
# Likes:    4678
# Dislikes: 185
# Total Accepted:    259.8K
# Total Submissions: 389K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
# 4-directionally connected group of 0s and a closed island is an island
# totally (all left, top, right, bottom) surrounded by 1s.
# 
# Return the number of closed islands.
# 
# 
# Example 1:
# 
# 
# 
# Input: grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water
# (group of 1s).
# 
# Example 2:
# 
# 
# 
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# 
# 
# Example 3:
# 
# Input: grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠              [1,1,1,1,1,1,1]]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
# 
# 
#

# @lc code=start
class Solution:
    def dfs(self,grid,r,c):
        q = []
        q.append((r,c))
        while q:
            curr = q.pop()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr = curr[0] + i
                newc = curr[1] + j
                if 0<= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc] == 0:
                    grid[newr][newc] = 1
                    q.append((newr,newc))
    def closedIsland(self, grid: List[List[int]]) -> int:
        for i in (0,len(grid)-1):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    self.dfs(grid,i,j)
        for i in range(len(grid)):
            for j in (0,len(grid[0])-1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    self.dfs(grid,i,j)
        res = 0
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    self.dfs(grid,i,j)
                    res+=1
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,1,1,1],\n[1,0,0,0,0,0,1],\n[1,0,1,1,1,0,1],\n[1,0,1,0,1,0,1],\n[1,0,1,1,1,0,1],\n[1,0,0,0,0,0,1],\n[1,1,1,1,1,1,1]]\n
# @lcpr case=end

#

