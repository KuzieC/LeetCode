#
# @lc app=leetcode id=231 lang=python3
# @lcpr version=30202
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (49.12%)
# Likes:    7602
# Dislikes: 480
# Total Accepted:    1.9M
# Total Submissions: 3.8M
# Testcase Example:  '1'
#
# Given an integer n, return true if it is a power of two. Otherwise, return
# false.
# 
# An integer n is a power of two, if there exists an integer x such that n ==
# 2^x.
# 
# 
# Example 1:
# 
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
# 
# 
# Example 2:
# 
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
# 
# 
# Example 3:
# 
# Input: n = 3
# Output: false
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
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        binary = ""
        base = math.floor(math.log2(n))
        while base >= 0:
            if 2 ** base <= n:
                n -= 2**base
                binary += "1"
            else:
                binary += "0"
            base -= 1

        return True if binary.count('1') == 1 else False
                
            
# @lc code=end



#
# @lcpr case=start
# 8\n
# @lcpr case=end

# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

