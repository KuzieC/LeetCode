#
# @lc app=leetcode id=407 lang=python3
# @lcpr version=30201
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (58.90%)
# Likes:    4534
# Dislikes: 145
# Total Accepted:    181.9K
# Total Submissions: 308.8K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n integer matrix heightMap representing the height of each unit
# cell in a 2D elevation map, return the volume of water it can trap after
# raining.
# 
# 
# Example 1:
# 
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
# 
# 
# Example 2:
# 
# Input: heightMap =
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
# 
# 
# 
# Constraints:
# 
# 
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pq = []
        row = len(heightMap)
        res = 0
        col = len(heightMap[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        visited = set()
        for i in range(col):
            heapq.heappush(pq,(heightMap[0][i],0,i))
            heapq.heappush(pq,(heightMap[row-1][i],row-1,i))
            visited.add((0,i))
            visited.add((row-1,i))
        for i in range(1,row-1):
            heapq.heappush(pq,(heightMap[i][0],i,0))
            heapq.heappush(pq,(heightMap[i][col-1],i,col-1))
            visited.add((i,0))
            visited.add((i,col-1))
        while pq:
            val,r,c = heapq.heappop(pq)

            visited.add((r,c))
            for a,b in dirs:
                newr = r + a
                newc = c + b
                if 0 <= newr < row and 0 <= newc < col and (newr,newc) not in visited:
                    if heightMap[newr][newc] < val:
                        res += val - heightMap[newr][newc]
                        heightMap[newr][newc] = val                    
                    heapq.heappush(pq,(heightMap[newr][newc],newr,newc))
                    visited.add((newr,newc))
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]\n
# @lcpr case=end

#

