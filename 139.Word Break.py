#
# @lc app=leetcode id=139 lang=python3
# @lcpr version=20001
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (47.36%)
# Likes:    17467
# Dislikes: 819
# Total Accepted:    1.8M
# Total Submissions: 3.9M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {}
        def helper(s: str) -> bool:
            if s in dp:
                return dp[s]
            if len(s) == 0:
                return True
            for i in range (len(s)+1):
                curr = s[:i]
                if curr in wordDict :
                    if helper(s[i:]):
                        dp[s] = True
                        return True
            dp[s] = False
            return False
        return helper(s)

# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet","code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple","pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

