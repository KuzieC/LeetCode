#
# @lc app=leetcode id=326 lang=python3
# @lcpr version=30202
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (48.33%)
# Likes:    3560
# Dislikes: 302
# Total Accepted:    1.2M
# Total Submissions: 2.4M
# Testcase Example:  '27'
#
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.
# 
# An integer n is a power of three, if there exists an integer x such that n ==
# 3^x.
# 
# 
# Example 1:
# 
# Input: n = 27
# Output: true
# Explanation: 27 = 3^3
# 
# 
# Example 2:
# 
# Input: n = 0
# Output: false
# Explanation: There is no x where 3^x = 0.
# 
# 
# Example 3:
# 
# Input: n = -1
# Output: false
# Explanation: There is no x where 3^x = (-1).
# 
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
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3**19 % n == 0
# @lc code=end



#
# @lcpr case=start
# 27\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# -1\n
# @lcpr case=end

#

