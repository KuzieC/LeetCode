#
# @lc app=leetcode id=994 lang=python3
# @lcpr version=20004
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (55.74%)
# Likes:    13544
# Dislikes: 424
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
# 
# 
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
# 
# 
# Example 1:
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# Example 2:
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# Example 3:
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot(i:int, j: int):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
                return
            if grid[i][j] == 1:
                grid[i][j] = 3
            return
        res = 0
        prevRot = -1
        newRot = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    newRot+=1

        while prevRot != newRot:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        rot(i+1,j)
                        rot(i,j+1)
                        rot(i-1,j)
                        rot(i,j-1)
            temp = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
                    elif grid[i][j] == 1:
                        temp += 1
            prevRot = newRot
            newRot = temp
            res+=1
        return -1 if newRot != 0 else res-1
            
                    
# @lc code=end



#
# @lcpr case=start
# [[2,1,1],[1,1,0],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,1],[0,1,1],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2]]\n
# @lcpr case=end

#

