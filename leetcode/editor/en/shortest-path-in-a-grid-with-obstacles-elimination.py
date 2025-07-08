#
# @lc app=leetcode id=1293 lang=python3
# @lcpr version=30201
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (45.66%)
# Likes:    4696
# Dislikes: 88
# Total Accepted:    245K
# Total Submissions: 536.5K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# You are given an m x n integer matrix grid where each cell is either 0
# (empty) or 1 (obstacle). You can move up, down, left, or right from and to an
# empty cell in one step.
# 
# Return the minimum number of steps to walk from the upper left corner (0, 0)
# to the lower right corner (m - 1, n - 1) given that you can eliminate at most
# k obstacles. If it is not possible to find such walk return -1.
# 
# 
# Example 1:
# 
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# 
# 
# Example 2:
# 
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a
# walk.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
# 
# 
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        res = 0
        q.append((0,0,k))
        curr = 0
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        visited = [[-1]*col for _ in range(row)]
        visited[0][0] = row*col
        while q:
            for _ in range(len(q)):
                x,y,obs = q.popleft()
                if x == row - 1 and y == col - 1:
                    return curr
                for a,b in dirs:
                    newr = x + a 
                    newc = y + b
                    if 0 <= newr < row and 0 <= newc < col :
                        if grid[newr][newc] == 1 and obs > 0 and obs - 1 > visited[newr][newc]:
                            q.append((newr,newc,obs-1))
                            visited[newr][newc] = obs -1
                        elif grid[newr][newc] == 0 and obs > visited[newr][newc]:
                            visited[newr][newc] = obs
                            q.append((newr,newc,obs))
            curr+=1
        return -1 
                            
                    
# @lc code=end



#
# @lcpr case=start
# [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1],[1,1,1],[1,0,0]]\n1\n
# @lcpr case=end

#

