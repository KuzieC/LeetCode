#
# @lc app=leetcode id=792 lang=python3
# @lcpr version=30005
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (50.72%)
# Likes:    5581
# Dislikes: 239
# Total Accepted:    243.3K
# Total Submissions: 479.7K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
# 
# 
# For example, "ace" is a subsequence of "abcde".
# 
# 
# 
# Example 1:
# 
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".
# 
# 
# Example 2:
# 
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def bs(l:List[int], x: int):
            left = 0
            right = len(l)-1
            while left <= right:
                mid = left + (right - left)//2
                if l[mid] <= x:
                    left = mid + 1
                else:
                    right = mid - 1
            return l[left] if left < len(l) else None
        mp = defaultdict(list)
        for i in range(len(s)):
            mp[s[i]].append(i)
        ans = 0
        for word in words:
            curr = -1
            for char in word:
                res = None
                if char not in mp:
                    break
                res = bs(mp[char],curr)
                if res == None:
                    break
                else:
                    curr = res
            if res != None:
                ans+=1
        return ans
                    
        
# @lc code=end



#
# @lcpr case=start
# "abcde"\n["a","bb","acd","ace"]\n
# @lcpr case=end

# @lcpr case=start
# "dsahjpjauf"\n["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]\n
# @lcpr case=end

#

