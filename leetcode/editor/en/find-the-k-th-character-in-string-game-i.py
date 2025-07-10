#
# @lc app=leetcode id=3304 lang=python3
# @lcpr version=30201
#
# [3304] Find the K-th Character in String Game I
#
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/
#
# algorithms
# Easy (81.77%)
# Likes:    575
# Dislikes: 117
# Total Accepted:    186.5K
# Total Submissions: 228.1K
# Testcase Example:  '5'
#
# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
# 
# You are given a positive integer k.
# 
# Now Bob will ask Alice to perform the following operation forever:
# 
# 
# Generate a new string by changing each character in word to its next
# character in the English alphabet, and append it to the original word.
# 
# 
# For example, performing the operation on "c" generates "cd" and performing
# the operation on "zb" generates "zbac".
# 
# Return the value of the k^th character in word, after enough operations have
# been done for word to have at least k characters.
# 
# 
# Example 1:
# 
# 
# Input: k = 5
# 
# Output: "b"
# 
# Explanation:
# 
# Initially, word = "a". We need to do the operation three times:
# 
# 
# Generated string is "b", word becomes "ab".
# Generated string is "bc", word becomes "abbc".
# Generated string is "bccd", word becomes "abbcbccd".
# 
# 
# 
# Example 2:
# 
# 
# Input: k = 10
# 
# Output: "c"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= 500
# 
# 
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        curr = "a"
        while len(curr)<k:
            newstr = ""
            for i in curr:
                newstr += chr((ord(i)-ord("a"))%26 + ord("b"))
            curr += newstr
        return curr[k-1]
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

