#
# @lc app=leetcode id=1314 lang=python3
# @lcpr version=30201
#
# [1314] Matrix Block Sum
#
# https://leetcode.com/problems/matrix-block-sum/description/
#
# algorithms
# Medium (76.00%)
# Likes:    2464
# Dislikes: 390
# Total Accepted:    99.9K
# Total Submissions: 131.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# Given a m x n matrix mat and an integer k, return a matrix answer where each
# answer[i][j] is the sum of all elements mat[r][c] for:
# 
# 
# i - k <= r <= i + k,
# j - k <= c <= j + k, and
# (r, c) is a valid position in the matrix.
# 
# 
# 
# Example 1:
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# Example 2:
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n, k <= 100
# 1 <= mat[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        self.presum = [[0] * (col+1) for _ in range(row+1)]
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                self.presum[r][c] = matrix[r][c] + self.presum[r+1][c] + self.presum[r][c+1] - self.presum[r+1][c+1]      

        for r in range(row):
            for c in range(col):
                topleftrow = max(r - k, 0)
                topleftcol = max( c - k, 0)
                botrightrow = min(r+k,row-1)
                botrightcol = min(c+k,col-1)
                matrix[r][c] = self.sumRegion(topleftrow,topleftcol,botrightrow,botrightcol)
        return matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row1][col1] - self.presum[row1][col2+1] - self.presum[row2+1][col1] + self.presum[row2+1][col2+1]
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n2\n
# @lcpr case=end

#

