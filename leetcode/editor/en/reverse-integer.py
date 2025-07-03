#
# @lc app=leetcode id=7 lang=python3
# @lcpr version=30201
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (30.37%)
# Likes:    14257
# Dislikes: 13790
# Total Accepted:    4.1M
# Total Submissions: 13.7M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# 
# Example 1:
# 
# Input: x = 123
# Output: 321
# 
# 
# Example 2:
# 
# Input: x = -123
# Output: -321
# 
# 
# Example 3:
# 
# Input: x = 120
# Output: 21
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        str_s = 0
        if x < 0:
            str_s = -1*int(str(x*-1)[::-1])
        else:
            str_s = int(str(x)[::-1])
        if -2**31 <= str_s <= 2**31 - 1:
            return str_s
        return 0
# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# -123\n
# @lcpr case=end

# @lcpr case=start
# 120\n
# @lcpr case=end

#

