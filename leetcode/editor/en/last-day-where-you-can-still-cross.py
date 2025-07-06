#
# @lc app=leetcode id=1970 lang=python3
# @lcpr version=30201
#
# [1970] Last Day Where You Can Still Cross
#
# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/
#
# algorithms
# Hard (62.34%)
# Likes:    1970
# Dislikes: 37
# Total Accepted:    63.7K
# Total Submissions: 102.2K
# Testcase Example:  '2\n2\n[[1,1],[2,1],[1,2],[2,2]]'
#
# There is a 1-based binary matrix where 0 represents land and 1 represents
# water. You are given integers row and col representing the number of rows and
# columns in the matrix, respectively.
# 
# Initially on day 0, the entire matrix is land. However, each day a new cell
# becomes flooded with water. You are given a 1-based 2D array cells, where
# cells[i] = [ri, ci] represents that on the i^th day, the cell on the ri^th
# row and ci^th column (1-based coordinates) will be covered with water (i.e.,
# changed to 1).
# 
# You want to find the last day that it is possible to walk from the top to the
# bottom by only walking on land cells. You can start from any cell in the top
# row and end at any cell in the bottom row. You can only travel in the four
# cardinal directions (left, right, up, and down).
# 
# Return the last day where it is possible to walk from the top to the bottom
# by only walking on land cells.
# 
# 
# Example 1:
# 
# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting
# from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.
# 
# 
# Example 2:
# 
# Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# Output: 1
# Explanation: The above image depicts how the matrix changes each day starting
# from day 0.
# The last day where it is possible to cross from top to bottom is on day 1.
# 
# 
# Example 3:
# 
# Input: row = 3, col = 3, cells =
# [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# Output: 3
# Explanation: The above image depicts how the matrix changes each day starting
# from day 0.
# The last day where it is possible to cross from top to bottom is on day
# 3.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= row, col <= 2 * 10^4
# 4 <= row * col <= 2 * 10^4
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# All the values of cells are unique.
# 
# 
#

# @lc code=start
class UF:
    def __init__(self,n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[1] * col for _ in range(row)]
        uf = UF(row*col+2)
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for ind,[r,c] in enumerate(reversed(cells)):
            grid[r-1][c-1] = 0
            
            if r-1 == 0:
                uf.union((r-1) * col + c,0)
            if r-1 == row - 1:
                uf.union((r-1) * col + c,row*col+1)
            for dirr,dirc in dirs:
                if 0<= r + dirr - 1 < row and 0 <= c + dirc - 1 < col and grid[r + dirr - 1][c + dirc - 1] == 0:
                    uf.union((r-1) * col + c, (r + dirr - 1) * col + c + dirc)
            if uf.find(0) == uf.find(row*col+1):
                return row*col - ind - 1
        return 0
            
                    
        
# @lc code=end



#
# @lcpr case=start
# 2\n2\n[[1,1],[2,1],[1,2],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n2\n[[1,1],[1,2],[2,1],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]\n
# @lcpr case=end

#

