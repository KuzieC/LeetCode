#
# @lc app=leetcode id=62 lang=python3
# @lcpr version=30201
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (65.82%)
# Likes:    17574
# Dislikes: 471
# Total Accepted:    2.4M
# Total Submissions: 3.6M
# Testcase Example:  '3\n7'
#
# There is a robot on an m x n grid. The robot is initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
# 
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
# 
# The test cases are generated so that the answer will be less than or equal to
# 2 * 10^9.
# 
# 
# Example 1:
# 
# Input: m = 3, n = 7
# Output: 28
# 
# 
# Example 2:
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def __init__(self):
        self.res : int = 0
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * (n+1) for _ in range(m+1)]

        grid[1][1] = 1
        for row in range(m):
            for col in range(n):
                grid[row+1][col+1] = max(grid[row+1][col+1],grid[row][col+1] + grid[row+1][col])
        print(grid)
        return grid[m][n]
            
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#

