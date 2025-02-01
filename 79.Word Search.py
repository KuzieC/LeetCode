#
# @lc app=leetcode id=79 lang=python3
# @lcpr version=20004
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (44.37%)
# Likes:    16384
# Dislikes: 694
# Total Accepted:    1.9M
# Total Submissions: 4.4M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    visited = []
    find = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = [[0 for _ in range (len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.dfs(i,j,board,word,0)
        return self.find
    
    def dfs(self,i,j,board,word,ind):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or ind >= len(word):
            return
        if self.visited[i][j] == 1:
            return
        if board[i][j] != word[ind]:
            return
        if self.find: 
            return
        if ind == len(word) - 1:
            self.find = True
        self.visited[i][j] = 1
        self.dfs(i+1,j,board,word,ind+1)
        self.dfs(i-1,j,board,word,ind+1)
        self.dfs(i,j+1,board,word,ind+1)
        self.dfs(i,j-1,board,word,ind+1)
        self.visited[i][j] = 0
        return
        


# @lc code=end



#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#

