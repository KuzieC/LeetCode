#
# @lc app=leetcode id=37 lang=python3
# @lcpr version=30202
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (64.07%)
# Likes:    10340
# Dislikes: 305
# Total Accepted:    808.9K
# Total Submissions: 1.3M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
# of the grid.
# 
# 
# The '.' character indicates empty cells.
# 
# 
# Example 1:
# 
# Input: board =
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output:
# [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is
# shown below:
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
# 
# 
#

# @lc code=start
class Solution:
    def checker(self,board,r,c,v):
        for i in range(0,len(board)):
            if board[r][i] == str(v) or board[i][c] == str(v) or board[r//3*3+i//3][c//3*3+i%3] == str(v):
                return False
        return True

    def helper(self, board: List[List[str]],n):
        """
        Do not return anything, modify board in-place instead.
        """
        row = n // 9
        col = n % 9
        if n == 81:
            return True
        if board[row][col] != ".":
            return self.helper(board,n+1)
        
        for i in range(1,10):
            if self.checker(board,row,col,i):
                board[row][col] = str(i)
                if self.helper(board,n+1):
                    return True
        board[row][col] = "."
        return False
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.helper(board,0)
                        
# @lc code=end



#
# @lcpr case=start
# \n[["5","3","."],["9",".","."],[".",".","."]]\n
# @lcpr case=end

#

