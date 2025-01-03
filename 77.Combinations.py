#
# @lc app=leetcode id=77 lang=python3
# @lcpr version=20001
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (71.47%)
# Likes:    8327
# Dislikes: 230
# Total Accepted:    990.6K
# Total Submissions: 1.4M
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
# 
# You may return the answer in any order.
# d
# 
# Example 1:
# 
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
# be the same combination.
# 
# 
# Example 2:
# 
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= k <= n
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def helper(curr, possible):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range (len(possible)):
                curr.append(possible[i])
                helper(curr,possible[i+1:])                
                curr.pop()
        helper([],[i for i in range(1,n+1)])
        return res
                
# @lc code=end



#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

