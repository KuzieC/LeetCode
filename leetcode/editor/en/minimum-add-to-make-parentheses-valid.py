#
# @lc app=leetcode id=921 lang=python3
# @lcpr version=30202
#
# [921] Minimum Add to Make Parentheses Valid
#
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (74.57%)
# Likes:    4799
# Dislikes: 243
# Total Accepted:    636.4K
# Total Submissions: 853.4K
# Testcase Example:  '"())"'
#
# A parentheses string is valid if and only if:
# 
# 
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# You are given a parentheses string s. In one move, you can insert a
# parenthesis at any position of the string.
# 
# 
# For example, if s = "()))", you can insert an opening parenthesis to be
# "(()))" or a closing parenthesis to be "())))".
# 
# 
# Return the minimum number of moves required to make s valid.
# 
# 
# Example 1:
# 
# Input: s = "())"
# Output: 1
# 
# 
# Example 2:
# 
# Input: s = "((("
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
# 
# 
#

# @lc code=start
from collections import deque
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        curr = 0
        count = deque()
        for i in s:
            if i == '(':
                count.append('(')
            else:
                if count and count[-1] == '(':
                    count.pop()
                else:
                    count.append(')')

        return len(count)
# @lc code=end



#
# @lcpr case=start
# "())"\n
# @lcpr case=end

# @lcpr case=start
# "((("\n
# @lcpr case=end

#

