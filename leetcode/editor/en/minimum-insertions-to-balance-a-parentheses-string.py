#
# @lc app=leetcode id=1541 lang=python3
# @lcpr version=30202
#
# [1541] Minimum Insertions to Balance a Parentheses String
#
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/
#
# algorithms
# Medium (53.25%)
# Likes:    1218
# Dislikes: 286
# Total Accepted:    77.3K
# Total Submissions: 145.2K
# Testcase Example:  '"(()))"'
#
# Given a parentheses string s containing only the characters '(' and ')'. A
# parentheses string is balanced if:
# 
# 
# Any left parenthesis '(' must have a corresponding two consecutive right
# parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right
# parenthesis '))'.
# 
# 
# In other words, we treat '(' as an opening parenthesis and '))' as a closing
# parenthesis.
# 
# 
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))"
# and "(()))" are not balanced.
# 
# 
# You can insert the characters '(' and ')' at any position of the string to
# balance it if needed.
# 
# Return the minimum number of insertions needed to make s balanced.
# 
# 
# Example 1:
# 
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only
# ')' matching. We need to add one more ')' at the end of the string to be
# "(())))" which is balanced.
# 
# 
# Example 2:
# 
# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
# 
# 
# Example 3:
# 
# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last
# '('.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of '(' and ')' only.
# 
# 
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = deque()
        res = i = need = 0
        for i in s:
            if i == '(':
                need += 2
                if need % 2 == 1:
                    need -= 1
                    res += 1
            else:
                need -= 1
                if need == -1:
                    need = 1
                    res += 1
        return res + need
# @lc code=end



#
# @lcpr case=start
# "(()))"\n
# @lcpr case=end

# @lcpr case=start
# "())"\n
# @lcpr case=end

# @lcpr case=start
# "))())("\n
# @lcpr case=end

#

