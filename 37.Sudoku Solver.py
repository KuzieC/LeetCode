#
# @lc app=leetcode id=37 lang=python3
# @lcpr version=30202
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:

    def __init__(self):
        self.found = False
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.box = defaultdict(set)
    def checker(self,board,r,c,val):
        if val in self.rows[r] or val in self.cols[c] or val in self.box[(r//3)*3 + (c//3)]:
                return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                self.rows[r].add(board[r][c])
                self.cols[c].add(board[r][c])
                self.box[(r//3)* 3 + (c//3)].add(board[r][c])

        self.dfs(0,board)
    def dfs(self,ind,board):
        if self.found:
            return
        if ind == 81:
            self.found = True
            return
        r = ind // 9
        c = ind % 9
        if board[r][c] != ".":
            self.dfs(ind+1,board)
            return 
            
        for val in '123456789':
            if self.checker(board,r,c,val):
                board[r][c] = val
                self.rows[r].add(val)
                self.cols[c].add(val)
                self.box[(r//3)*3 + (c//3)].add(val)
                self.dfs(ind+1,board)
                if self.found:
                    return 
                board[r][c] = "."
                self.rows[r].remove(val)
                self.cols[c].remove(val)
                self.box[(r//3)*3 + (c//3)].remove(val)

                        

        
# @lc code=end



#
# @lcpr case=start
# \n[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

