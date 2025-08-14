#
# @lc app=leetcode id=997 lang=python3
# @lcpr version=30202
#
# [997] Find the Town Judge
#
# https://leetcode.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (50.13%)
# Likes:    6837
# Dislikes: 620
# Total Accepted:    689.7K
# Total Submissions: 1.4M
# Testcase Example:  '2\n[[1,2]]'
#
# In a town, there are n people labeled from 1 to n. There is a rumor that one
# of these people is secretly the town judge.
# 
# If the town judge exists, then:
# 
# 
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# 
# 
# You are given an array trust where trust[i] = [ai, bi] representing that the
# person labeled ai trusts the person labeled bi. If a trust relationship does
# not exist in trust array, then such a trust relationship does not exist.
# 
# Return the label of the town judge if the town judge exists and can be
# identified, or return -1 otherwise.
# 
# 
# Example 1:
# 
# Input: n = 2, trust = [[1,2]]
# Output: 2
# 
# 
# Example 2:
# 
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# 
# 
# Example 3:
# 
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 0 <= trust.length <= 10^4
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n
# 
# 
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        mp = defaultdict(int)
        for f,t in trust:
            mp[f] -= 1
            mp[t] += 1
        for k,v in mp.items():
            if v == n - 1:
                return k
        return -1
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,3],[2,3],[3,1]]\n
# @lcpr case=end

#

