#
# @lc app=leetcode id=36 lang=python3
# @lcpr version=30202
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def checker(self,board):
        s1 = set()
        s2 = set()
        s3 = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != "." and board[i][j] in s1:
                    return False
                if board[j][i] != "." and board[j][i] in s2:
                    return False
                si = (j // 3) + (i // 3) * 3
                sj = (j % 3) + (i % 3) * 3
                if board[si][sj] != "." and board[si][sj] in s3:
                    return False
                if board[si][sj] != ".": 
                    s3.add(board[si][sj])
                if board[j][i] != ".": 
                    s2.add(board[j][i])
                if board[i][j] != ".": 
                    s1.add(board[i][j])
            s1.clear()
            s2.clear()
            s3.clear()
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checker(board)
# @lc code=end



#
# @lcpr case=start
# \n[["5","3",".",".","7",".",".",".","."]\n,["6",".",".","1","9","5",".",".","."]\n,[".","9","8",".",".",".",".","6","."]\n,["8",".",".",".","6",".",".",".","3"]\n,["4",".",".","8",".","3",".",".","1"]\n,["7",".",".",".","2",".",".",".","6"]\n,[".","6",".",".",".",".","2","8","."]\n,[".",".",".","4","1","9",".",".","5"]\n,[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# \n[["8","3",".",".","7",".",".",".","."]\n,["6",".",".","1","9","5",".",".","."]\n,[".","9","8",".",".",".",".","6","."]\n,["8",".",".",".","6",".",".",".","3"]\n,["4",".",".","8",".","3",".",".","1"]\n,["7",".",".",".","2",".",".",".","6"]\n,[".","6",".",".",".",".","2","8","."]\n,[".",".",".","4","1","9",".",".","5"]\n,[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

