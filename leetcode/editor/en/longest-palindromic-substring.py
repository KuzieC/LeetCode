#
# @lc app=leetcode id=5 lang=python
# @lcpr version=30201
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (35.89%)
# Likes:    30937
# Dislikes: 1905
# Total Accepted:    3.9M
# Total Submissions: 10.9M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution(object):
    def helper(self,s,left,right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left-=1
            right+=1
        return (right - left - 1,s[left+1:right])    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        count = 0
        for i in range(len(s)):
            length,st = self.helper(s,i,i)
            print(length,st)
            if length > count:
                count = length
                res = st
            length,st = self.helper(s,i,i+1)
            print(length,st)
            if length > count:
                count = length
                res = st
        return res
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

