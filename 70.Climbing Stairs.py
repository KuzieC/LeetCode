#
# @lc app=leetcode id=70 lang=python3
# @lcpr version=30002
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (53.31%)
# Likes:    22756
# Dislikes: 918
# Total Accepted:    3.9M
# Total Submissions: 7.3M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(46)]
        memo[0] = 1
        memo[1] = 1
        if n < 2:
            return memo[n]
        for i in range(2,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

