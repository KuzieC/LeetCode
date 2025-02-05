#
# @lc app=leetcode id=399 lang=python3
# @lcpr version=30002
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (62.64%)
# Likes:    9596
# Dislikes: 998
# Total Accepted:    556K
# Total Submissions: 887.7K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
  '[2.0,3.0]\n' +
  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
# equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
# single variable.
# 
# You are also given some queries, where queries[j] = [Cj, Dj] represents the
# j^th query where you must find the answer for Cj / Dj = ?.
# 
# Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.
# 
# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.
# 
# Note: The variables that do not occur in the list of equations are undefined,
# so the answer cannot be determined for them.
# 
# 
# Example 1:
# 
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# 
# Example 2:
# 
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# 
# 
# Example 3:
# 
# Input: equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mp = defaultdict(lambda: defaultdict(lambda:0))
        for [a,b],c in zip(equations,values):
          mp[a][b] = c
          mp[b][a] = 1/c

        ans = []
        for src, tar in queries:
          if src not in mp or tar not in mp:
            ans.append(-1.0)
            continue
          print("-------")
          s = []
          vp = defaultdict(int)
          curr = src
          s.append((src,1)) 
          vis = set()
          vis.add(src)
          found = False
          while s:
            for _ in range (len(s)):
              curr,val = s.pop(0)
              if curr == tar:
                ans.append(val)
                s.clear()
                found = True
                break
              for neig in mp[curr].keys():
                if neig not in vis:
                  s.append((neig,val*mp[curr][neig]))          
                  vis.add(neig) 
          if not found:
            ans.append(-1)
        return ans

# @lc code=end



#
# @lcpr case=start
# [["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["b","c"],["bc","cd"]]\n[1.5,2.5,5.0]\n[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"]]\n[0.5]\n[["a","b"],["b","a"],["a","c"],["x","y"]]\n
# @lcpr case=end

#

