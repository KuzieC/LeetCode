#
# @lc app=leetcode id=417 lang=python3
# @lcpr version=30201
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (57.63%)
# Likes:    7903
# Dislikes: 1620
# Total Accepted:    611.7K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
# 
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
# 
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
# 
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
# 
# 
# Example 1:
# 
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans,
# as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
# [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
# [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
# [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
# [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
# [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
# [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
# ⁠      [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the
# Pacific and Atlantic oceans.
# 
# 
# Example 2:
# 
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and
# Atlantic oceans.
# 
# 
# 
# Constraints:
# 
# 
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        pac = set()
        atl = set()
        def dfs(visited : set(),curr_r,curr_c):
            visited.add((curr_r,curr_c))
            for a,b in dirs:
                nr = a + curr_r
                nc = b + curr_c
                
                if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in visited and heights[nr][nc] >= heights[curr_r][curr_c]:
                    dfs(visited,nr,nc)
        for i in range(col):
            dfs(pac,0,i)
            dfs(atl,row-1,i)
        for i in range(row):
            dfs(pac,i,0)
            dfs(atl,i,col-1)
        res = [i for i in pac if i in atl]
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#

