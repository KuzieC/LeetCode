#
# @lc app=leetcode id=2203 lang=python3
# @lcpr version=30201
#
# [2203] Minimum Weighted Subgraph With the Required Paths
#
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/description/
#
# algorithms
# Hard (38.79%)
# Likes:    742
# Dislikes: 23
# Total Accepted:    17K
# Total Submissions: 43.8K
# Testcase Example:  '6\n' +
  '[[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]\n' +
  '0\n' +
  '1\n' +
  '5'
#
# You are given an integer n denoting the number of nodes of a weighted
# directed graph. The nodes are numbered from 0 to n - 1.
# 
# You are also given a 2D integer array edges where edges[i] = [fromi, toi,
# weighti] denotes that there exists a directed edge from fromi to toi with
# weight weighti.
# 
# Lastly, you are given three distinct integers src1, src2, and dest denoting
# three distinct nodes of the graph.
# 
# Return the minimum weight of a subgraph of the graph such that it is possible
# to reach dest from both src1 and src2 via a set of edges of this subgraph. In
# case such a subgraph does not exist, return -1.
# 
# A subgraph is a graph whose vertices and edges are subsets of the original
# graph. The weight of a subgraph is the sum of weights of its constituent
# edges.
# 
# 
# Example 1:
# 
# Input: n = 6, edges =
# [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]],
# src1 = 0, src2 = 1, dest = 5
# Output: 9
# Explanation:
# The above figure represents the input graph.
# The blue edges represent one of the subgraphs that yield the optimal answer.
# Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It
# is not possible to get a subgraph with less weight satisfying all the
# constraints.
# 
# 
# Example 2:
# 
# Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
# Output: -1
# Explanation:
# The above figure represents the input graph.
# It can be seen that there does not exist any path from node 1 to node 2,
# hence there are no subgraphs satisfying all the constraints.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= n <= 10^5
# 0 <= edges.length <= 10^5
# edges[i].length == 3
# 0 <= fromi, toi, src1, src2, dest <= n - 1
# fromi != toi
# src1, src2, and dest are pairwise distinct.
# 1 <= weight[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        INF = float('inf')
        shortest = [[INF,INF,INF] for _ in range(n)]
        shortest[src1][0] = 0
        shortest[src2][1] = 0
        shortest[dest][2] = 0
        adj = [[] for _ in range(n)]
        rev_adj = [[] for _ in range(n)]
        for f,t,wei in edges:
          adj[f].append((t,wei))
          rev_adj[t].append((f,wei))
        def bfs(curr,lis,start):
          q = []
          heapq.heappush(q,(0,curr))  
          while q:
            sum,curr = heapq.heappop(q)
            if sum != shortest[curr][start]:
              continue
            for neig,w in lis[curr]:
              if shortest[neig][start] > w+sum:
                heapq.heappush(q,(w+sum,neig))
                shortest[neig][start] = w+sum
        bfs(src1,adj,0)
        bfs(src2,adj,1)
        bfs(dest,rev_adj,2)
        res = INF
        for i in range(n):
            res = min(res,sum(shortest[i]))
        return res if res != INF else -1
            
          
          
# @lc code=end



#
# @lcpr case=start
# 6\n[[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]\n0\n1\n5\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1,1],[2,1,1]]\n0\n1\n2\n
# @lcpr case=end

#

