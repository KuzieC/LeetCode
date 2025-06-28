#
# @lc app=leetcode id=51 lang=python
# @lcpr version=30201
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (72.93%)
# Likes:    13373
# Dislikes: 323
# Total Accepted:    1M
# Total Submissions: 1.4M
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
# 
# 
# Example 1:
# 
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: [["Q"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 9
# 
# 
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = []
    def isValid(self,board,r,c):
        n = len(board)
        for i in range(n):
            if board[r][i] == 'Q':
                return False
            if board[i][c] == 'Q':
                return False

        for x,y in zip(range(r-1,-1,-1),range(c-1,-1,-1)):
            if board[x][y] == 'Q':
                return False
        
        for x,y in zip(range(r,n),range(c,n)):
            if board[x][y] == 'Q':
                return False
        
        for x,y in zip(range(r-1,-1,-1),range(c+1,n)):
            if board[x][y] == 'Q':
                return False
        
        for x,y in zip(range(r+1,n),range(c-1,-1,-1)):
            if board[x][y] == 'Q':
                return False
        return True
    def dfs(self,board,n,k,row):
        if(k == 0):
            self.res.append(board[:])
            return
        for col in range(n):
            if board[row][col] == '.' and self.isValid(board,row,col):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.dfs(board,n,k-1,row+1)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                    
    def solveNQueens(self,n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = ['.'* n for _ in range(n)]
        self.dfs(board,n,n,0)
        return self.res
        
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

