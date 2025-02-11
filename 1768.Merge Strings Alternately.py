#
# @lc app=leetcode id=1768 lang=python3
# @lcpr version=30003
#
# [1768] Merge Strings Alternately
#
# https://leetcode.com/problems/merge-strings-alternately/description/
#
# algorithms
# Easy (81.67%)
# Likes:    4301
# Dislikes: 116
# Total Accepted:    1.4M
# Total Submissions: 1.7M
# Testcase Example:  '"abc"\n"pqr"'
#
# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer than
# the other, append the additional letters onto the end of the merged string.
# 
# Return the merged string.
# 
# 
# Example 1:
# 
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# 
# 
# Example 2:
# 
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# 
# 
# Example 3:
# 
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for a, b in zip(word1, word2):
            res += a + b
        res += word1[len(word2):] + word2[len(word1):]
        return res
        
# @lc code=end



#
# @lcpr case=start
# "abc"\n"pqr"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"pqrs"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"pq"\n
# @lcpr case=end

#

