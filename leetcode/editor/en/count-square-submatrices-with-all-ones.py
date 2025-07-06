#
# @lc app=leetcode id=1277 lang=python3
# @lcpr version=30201
#
# [1277] Count Square Submatrices with All Ones
#
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
#
# algorithms
# Medium (78.75%)
# Likes:    5468
# Dislikes: 101
# Total Accepted:    348.4K
# Total Submissions: 442.4K
# Testcase Example:  '[[0,1,1,1],[1,1,1,1],[0,1,1,1]]'
#
# Given a m * n matrix of ones and zeros, return how many square submatrices
# have all ones.
# 
# 
# Example 1:
# 
# Input: matrix =
# [
# [0,1,1,1],
# [1,1,1,1],
# [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# 
# 
# Example 2:
# 
# Input: matrix = 
# [
# ⁠ [1,0,1],
# ⁠ [1,1,0],
# ⁠ [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
# 
# 
#

# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [ 0] * (col+1)
        res = prev = 0
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if matrix[r][c] == 1:
                    temp = dp[c]
                    dp[c] = min(dp[c],dp[c+1],prev) + 1
                    prev = temp
                    res += dp[c] 
                else:
                    dp[c] = 0
        return res
# @lc code=end



#
# @lcpr case=start
# \n[\n[0,1,1,1],\n[1,1,1,1],\n[0,1,1,1]\n]\n
# @lcpr case=end

# @lcpr case=start
# \n[\n[1,0,1],\n[1,1,0],\n[1,1,0]\n]\n
# @lcpr case=end

#

