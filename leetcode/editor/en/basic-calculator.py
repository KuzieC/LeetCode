#
# @lc app=leetcode id=224 lang=python3
# @lcpr version=30202
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (45.87%)
# Likes:    6723
# Dislikes: 541
# Total Accepted:    619K
# Total Submissions: 1.3M
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
# 
# 
# Example 1:
# 
# Input: s = "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# Input: s = " 2-1 + 2 "
# Output: 3
# 
# 
# Example 3:
# 
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is
# invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is
# valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.
# 
# 
#

# @lc code=start
from collections import deque
class Solution:
    def __init__(self):
        self.mp = {}
    
    def calculate(self, s: str) -> int:
        q = deque()
        for i in range(len(s)):
            if s[i] == "(":
                q.append(i)
            elif s[i] == ")":
                t = q.pop()
                self.mp[t] = i
        return self.helper(s,0,len(s))
    def helper(self,s,f,t):
        op = deque()
        opr = deque()
        i = f
        curr = 0
        while i < t:
            if s[i] == " ":
                i+=1
                continue
            elif s[i].isdigit():
                curr = curr * 10 + int(s[i])
                i+=1
            elif s[i] in ("+","-"):
                opr.append(curr)
                curr = 0
                op.append(s[i])
                i+=1
            else:
                curr = (self.helper(s,i+1,self.mp[i]))
                i = self.mp[i] + 1

        opr.append(curr)
        while len(opr) > 1:
            num1 = opr.popleft()
            num2 = opr.popleft()
            if op.popleft() == "+":
                opr.appendleft(num1 + num2)
            else:
                opr.appendleft(num1 - num2)
        if op:
            return opr.pop() * -1
        return opr.pop()
    
# @lc code=end



#
# @lcpr case=start
# "1 + 1"\n
# @lcpr case=end

# @lcpr case=start
# " 2-1 + 2 "\n
# @lcpr case=end

# @lcpr case=start
# "(1+(4+5+2)-3)+(6+8)"\n
# @lcpr case=end

#

