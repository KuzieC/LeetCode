#
# @lc app=leetcode id=10 lang=python3
# @lcpr version=30201
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (29.34%)
# Likes:    12766
# Dislikes: 2302
# Total Accepted:    1.2M
# Total Submissions: 4M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.str = ""
        self.pattern = ""
        self.memo = []
    def isMatch(self, s: str, p: str) -> bool:
        self.str = s
        self.pattern = p
        self.memo = [[-1]*len(p) for _ in range(len(s))]
        def dp(i,j):
            res = 0
            if i == len(self.str):
                if (len(self.pattern) - j)%2 == 1:
                    return False
                while j < len(self.pattern):
                    if self.pattern[j+1] != "*":
                        return False
                    j+=2
                return True
            if j == len(self.pattern):
                return i == len(self.str)
            if self.memo[i][j] != -1:
                return self.memo[i][j]
            if self.str[i] == self.pattern[j] or self.pattern[j] == ".":
                if j + 1 < len(self.pattern) and self.pattern[j+1] == "*":
                    res = dp(i+1,j) or dp(i,j+2)
                else:
                    res = dp(i+1,j+1)
            else:
                if j + 1 < len(self.pattern) and self.pattern[j+1] == "*":
                    res = dp(i,j+2)
                else:
                    res = 0
            self.memo[i][j] = res
            return res
        return True if dp(0,0) else False
                    
                
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# @lcpr case=end

#

