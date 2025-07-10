#
# @lc app=leetcode id=3333 lang=python3
# @lcpr version=30201
#
# [3333] Find the Original Typed String II
#
# https://leetcode.com/problems/find-the-original-typed-string-ii/description/
#
# algorithms
# Hard (46.52%)
# Likes:    476
# Dislikes: 70
# Total Accepted:    66.3K
# Total Submissions: 142.6K
# Testcase Example:  '"aabbccdd"\n7'
#
# Alice is attempting to type a specific string on her computer. However, she
# tends to be clumsy and may press a key for too long, resulting in a character
# being typed multiple times.
# 
# You are given a string word, which represents the final output displayed on
# Alice's screen. You are also given a positive integer k.
# 
# Return the total number of possible original strings that Alice might have
# intended to type, if she was trying to type a string of size at least k.
# 
# Since the answer may be very large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: word = "aabbccdd", k = 7
# 
# Output: 5
# 
# Explanation:
# 
# The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and
# "abbccdd".
# 
# 
# Example 2:
# 
# 
# Input: word = "aabbccdd", k = 8
# 
# Output: 1
# 
# Explanation:
# 
# The only possible string is "aabbccdd".
# 
# 
# Example 3:
# 
# 
# Input: word = "aaabbb", k = 3
# 
# Output: 8
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 5 * 10^5
# word consists only of lowercase English letters.
# 1 <= k <= 2000
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def __init__(self):
        self.res = 0
    def dfs(self,currlen,k,mp):
        if currlen >= k:
            print(mp)
            self.res+=1
        else:
            return
        for key,v in mp.items():
            for i in range(v-1,0,-1):
                mp[key] = i
                self.dfs(currlen-1,k,mp)
            mp[key] = v
    def possibleStringCount(self, word: str, k: int) -> int:
        mp = Counter(word)
        curr = len(word)
        if curr < k:
            return 0
        

        self.dfs(curr,k,mp)
        return self.res
                
# @lc code=end



#
# @lcpr case=start
# "aabbccdd"\n7\n
# @lcpr case=end

# @lcpr case=start
# "aabbccdd"\n8\n
# @lcpr case=end

# @lcpr case=start
# "aaabbb"\n3\n
# @lcpr case=end

#

