#
# @lc app=leetcode id=342 lang=python3
# @lcpr version=30202
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (50.61%)
# Likes:    4283
# Dislikes: 409
# Total Accepted:    923.2K
# Total Submissions: 1.8M
# Testcase Example:  '16'
#
# Given an integer n, return true if it is a power of four. Otherwise, return
# false.
# 
# An integer n is a power of four, if there exists an integer x such that n ==
# 4^x.
# 
# 
# Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true
# 
# 
# Constraints:
# 
# 
# -2^31 <= n <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1:
            return True
        if n <= 0:
            return False
        ni = 4
        while ni <= n:
            if ni == n:
                return True
            ni *= 4
        return False
        
# @lc code=end



#
# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

