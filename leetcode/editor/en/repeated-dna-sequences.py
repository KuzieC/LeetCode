#
# @lc app=leetcode id=187 lang=python3
# @lcpr version=30202
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (51.67%)
# Likes:    3515
# Dislikes: 558
# Total Accepted:    468.5K
# Total Submissions: 906.8K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A',
# 'C', 'G', and 'T'.
# 
# 
# For example, "ACGAATTCCG" is a DNA sequence.
# 
# 
# When studying DNA, it is useful to identify repeated sequences within the
# DNA.
# 
# Given a string s that represents a DNA sequence, return all the
# 10-letter-long sequences (substrings) that occur more than once in a DNA
# molecule. You may return the answer in any order.
# 
# 
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either 'A', 'C', 'G', or 'T'.
# 
# 
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
        left = 0
        right = 10
        while right <= len(s):
            curr = s[left:right]
            if curr in seen:
                res.add(curr)
            else:
                seen.add(curr)
            left+=1
            right+=1
        return list(res)
# @lc code=end



#
# @lcpr case=start
# "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"\n
# @lcpr case=end

# @lcpr case=start
# "AAAAAAAAAAAAA"\n
# @lcpr case=end

#

