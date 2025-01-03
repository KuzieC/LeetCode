#
# @lc app=leetcode id=51 lang=python3
# @lcpr version=20001
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (70.29%)
# Likes:    12645
# Dislikes: 296
# Total Accepted:    825.3K
# Total Submissions: 1.2M
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


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [["." for _ in range (n)] for _ in range (n)]
        
        def helper(curr,board):
            if n == curr:
                self.res.append(["".join(row) for row in board])
                return
            
            for j in range(len(board[curr])):
                if isValid(curr,j,board):
                    board[curr][j] = 'Q'
                    helper(curr+1,board)
                    board[curr][j] = '.'
            return
                    
                    
        def isValid(row,col,board):
            for i in range(row,-1,-1):
                if board[i][col] == 'Q':
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
                if board[i][j] == 'Q':
                    return False
            for i,j in zip (range(row-1,-1,-1),range(col+1,n,1)):
                if board[i][j] == 'Q':
                    return False
            return True
        
        helper(0,board)
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

