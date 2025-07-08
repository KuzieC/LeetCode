#
# @lc app=leetcode id=827 lang=python3
# @lcpr version=30201
#
# [827] Making A Large Island
#
# https://leetcode.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (55.10%)
# Likes:    4764
# Dislikes: 95
# Total Accepted:    356.4K
# Total Submissions: 646.8K
# Testcase Example:  '[[1,0],[0,1]]'
#
# You are given an n x n binary matrix grid. You are allowed to change at most
# one 0 to be 1.
# 
# Return the size of the largest island in grid after applying this operation.
# 
# An island is a 4-directionally connected group of 1s.
# 
# 
# Example 1:
# 
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
# area = 3.
# 
# 
# Example 2:
# 
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island
# with area = 4.
# 
# Example 3:
# 
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        q = deque()
        dirs = ((-1,0),(1,0),(0,1),(0,-1))
        size = [0 for _ in range(row*col+2)]
        
        curr_ind = 2
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    q = deque()
                    q.append((r,c))
                    grid[r][c] = curr_ind
                    while q:
                        x,y = q.popleft()
                        size[curr_ind] += 1
                        for a,b in dirs:
                            newr = x + a
                            newc = y + b
                            if 0 <= newr < row and 0 <= newc < col and grid[newr][newc] == 1:
                                grid[newr][newc] = curr_ind
                                q.append((newr,newc))
                    curr_ind+=1

        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    curr = 0
                    visited = set()
                    for a,b in dirs:
                        newr,newc = r + a,c + b
                        if 0 <= newr < row and 0 <= newc < col and grid[newr][newc] not in visited and grid[newr][newc] > 1:
                            curr += size[grid[newr][newc]]
                            visited.add(grid[newr][newc])
                    curr+=1
                    res = max(res,curr)
        return max(res,max(size))        
                    
                                        
                                
# @lc code=end



#
# @lcpr case=start
# [[1,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1]]\n
# @lcpr case=end

#

