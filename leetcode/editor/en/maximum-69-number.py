#
# @lc app=leetcode id=1323 lang=python3
# @lcpr version=30202
#
# [1323] Maximum 69 Number
#
# https://leetcode.com/problems/maximum-69-number/description/
#
# algorithms
# Easy (81.91%)
# Likes:    3194
# Dislikes: 235
# Total Accepted:    422.1K
# Total Submissions: 501.5K
# Testcase Example:  '9669'
#
# You are given a positive integer num consisting only of digits 6 and 9.
# 
# Return the maximum number you can get by changing at most one digit (6
# becomes 9, and 9 becomes 6).
# 
# 
# Example 1:
# 
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# 
# 
# Example 2:
# 
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# 
# 
# Example 3:
# 
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 10^4
# num consists of only 6 and 9 digits.
# 
# 
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
             if num[i] == '6':
                 return int(num[:i] + '9' + num[i+1:])
        return int(num)
                
                
# @lc code=end



#
# @lcpr case=start
# 9669\n
# @lcpr case=end

# @lcpr case=start
# 9996\n
# @lcpr case=end

# @lcpr case=start
# 9999\n
# @lcpr case=end

#

