#
# @lc app=leetcode id=1584 lang=python3
# @lcpr version=30202
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (69.34%)
# Likes:    5389
# Dislikes: 141
# Total Accepted:    397.5K
# Total Submissions: 573.3K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
# 
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
# 
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
# 
# 
# Example 1:
# 
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# 
# 
# Example 2:
# 
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
# 
# 
#

# @lc code=start
class UF:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [0] * n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def connect(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            px,py = py,px
        self.parent[py] = px
        self.size[px] += self.size[py]
        
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        q = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                heapq.heappush(q,(abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]),i,j))
        uf = UF(len(points))
        res = 0
        while q:
            dis,f,t = heapq.heappop(q)
            if uf.isConnected(f,t):
                continue
            uf.connect(f,t)
            res += dis
        return res
        
            
# @lc code=end



#
# @lcpr case=start
# [[0,0],[2,2],[3,10],[5,2],[7,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,12],[-2,5],[-4,1]]\n
# @lcpr case=end

#

