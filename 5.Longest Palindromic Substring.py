#
# @lc app=leetcode id=5 lang=python3
# @lcpr version=20004
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (35.11%)
# Likes:    30245
# Dislikes: 1862
# Total Accepted:    3.6M
# Total Submissions: 10.2M
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


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPan(s:str,i:int,j:int)->str:
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
                
            return s[i+1:j]
        res = ""

        for i in range(len(s)):
            a = isPan(s,i,i) 
            b = isPan(s,i,i+1)
    
            if len(a) > len(res):
                res = a
            if len(b) > len(res):
                res = b
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

