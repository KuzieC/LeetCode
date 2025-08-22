#
# @lc app=leetcode id=1504 lang=python3
# @lcpr version=30202
#
# [1504] Count Submatrices With All Ones
#

# @lc code=start
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        down = [[0] * col for _ in range(row)]
        res = 0
        for i in range(col):
            for j in range(row):
                if mat[j][i] == 1:
                    down[j][i] = down[j-1][i] + 1 if j > 0 else 1
        
        for r in range(row):
            for c in range(col):
                i = c
                currm = down[r][i]
                while i < col and down[r][i] > 0:
                    currm = min(currm,down[r][i])
                    res += currm
                    i+=1
        return res

# @lc code=end



#
# @lcpr case=start
# [[1,0,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1,0],[0,1,1,1],[1,1,1,0]]\n
# @lcpr case=end

#
