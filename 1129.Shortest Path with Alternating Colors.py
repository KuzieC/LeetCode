#
# @lc app=leetcode id=1129 lang=python3
# @lcpr version=30003
#
# [1129] Shortest Path with Alternating Colors
#
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (47.15%)
# Likes:    3569
# Dislikes: 193
# Total Accepted:    129.1K
# Total Submissions: 273.8K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# You are given an integer n, the number of nodes in a directed graph where the
# nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph,
# and there could be self-edges and parallel edges.
# 
# You are given two arrays redEdges and blueEdges where:
# 
# 
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node
# ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from
# node uj to node vj in the graph.
# 
# 
# Return an array answer of length n, where each answer[x] is the length of the
# shortest path from node 0 to node x such that the edge colors alternate along
# the path, or -1 if such a path does not exist.
# 
# 
# Example 1:
# 
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# 
# 
# Example 2:
# 
# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]
        res = [-1 for _ in range(n)]
        for a,b in redEdges:
            red[a].append(b)

        for a,b in blueEdges:
            blue[a].append(b)
        
        def bfs(color:bool):
            r = 0
            while q:
                s = len(q)
                for _ in range(s):
                    curr = q.popleft()
                    if res[curr] == -1:
                        res[curr] = r
                    else:
                        res[curr] = min(res[curr],r)
                        
                    if color:
                        for neig in blue[curr]:
                            if (curr,neig,color) not in visited:
                                visited.add((curr,neig,color))
                                q.append(neig)
                    else:
                        for neig in red[curr]:
                            if (curr,neig,color) not in visited:
                                visited.add((curr,neig,color))
                                q.append(neig)
                color = not color
                r+=1
            return -1

        q = deque()
        q.append(0)
        visited = set()
        bfs(False)
        q.clear()
        q.append(0)
        visited.clear()
        bfs(True)
        return res
            
            
# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[1,2]]\n[]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1]]\n[[2,1]]\n
# @lcpr case=end

#

