#
# @lc app=leetcode id=140 lang=python3
# @lcpr version=20001
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (52.04%)
# Likes:    7258
# Dislikes: 539
# Total Accepted:    694.7K
# Total Submissions: 1.3M
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# 
# 
# Example 2:
# 
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed
# 10^5.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        res = []
        wordDict = set(wordDict)
        def helper(s):
            if s in dp:
                return dp[s]
            
            if len(s) == 0:
                return [""]
            
            result = []
            
            for i in range(1,len(s)+1):
                word = s[:i]
                if word in wordDict:
                    tmps = helper(s[i:])
                    for tmp in tmps:
                        if tmp == "":
                            result.append(word)
                        else:
                            result.append(word+" "+tmp)
            
            dp[s] = result
            return result
        return helper(s)
                    
            
# @lc code=end



#
# @lcpr case=start
# "catsanddog"\n["cat","cats","and","sand","dog"]\n
# @lcpr case=end

# @lcpr case=start
# "pineapplepenapple"\n["apple","pen","applepen","pine","pineapple"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

