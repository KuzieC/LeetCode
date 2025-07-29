#
# @lc app=leetcode id=451 lang=python3
# @lcpr version=30202
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (74.33%)
# Likes:    8827
# Dislikes: 320
# Total Accepted:    951.6K
# Total Submissions: 1.3M
# Testcase Example:  '"tree"'
#
# Given a string s, sort it in decreasing order based on the frequency of the
# characters. The frequency of a character is the number of times it appears in
# the string.
# 
# Return the sorted string. If there are multiple answers, return any of
# them.
# 
# 
# Example 1:
# 
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# 
# Example 2:
# 
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and
# "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
# Example 3:
# 
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^5
# s consists of uppercase and lowercase English letters and digits.
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sortedlist = sorted(count.items(),key = lambda x : (-x[1],x[0]))
        return "".join(i[0] * i[1] for i in sortedlist)
# @lc code=end



#
# @lcpr case=start
# "tree"\n
# @lcpr case=end

# @lcpr case=start
# "cccaaa"\n
# @lcpr case=end

# @lcpr case=start
# "Aabb"\n
# @lcpr case=end

#

