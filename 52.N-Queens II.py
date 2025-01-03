#
# @lc app=leetcode id=52 lang=python3
# @lcpr version=20001
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (75.13%)
# Likes:    3923
# Dislikes: 267
# Total Accepted:    429.1K
# Total Submissions: 571.2K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# 
# Example 1:
# 
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
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
    def totalNQueens(self, n: int) -> int:
        board = [[ "." for _ in range(n)]for _ in range (n)]
        res = 0
        
        def helper(curr):
            nonlocal res
            if curr == n:
                res += 1
                return
            
            for col in range(n):
                if isValid(curr,col):
                    board[curr][col] = 'Q'
                    helper(curr+1)
                    board[curr][col] = ','
            
            return
        
        def isValid(row,col):
            for i in range(row,-1,-1):
                if board[i][col] == 'Q':
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
                if board[i][j] == 'Q':
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col+1,n,1)):
                if board[i][j] == 'Q':
                    return False
            return True

        helper(0)
        return res
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

