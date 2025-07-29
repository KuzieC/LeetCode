#
# @lc app=leetcode id=14 lang=python3
# @lcpr version=30202
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (45.79%)
# Likes:    19600
# Dislikes: 4765
# Total Accepted:    4.7M
# Total Submissions: 10.4M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
# 
# 
#

# @lc code=start
class trieNode:
    def __init__(self):
        self.isend = False
        self.child = {}
class trie:
    def __init__(self):
        self.root = trieNode()
    
    def add(self,x):
        curr = self.root
        for i in x:
            if i not in curr.child:
                curr.child[i] = trieNode()
            curr = curr.child[i]
        curr.isend = True
    
    def getLCP(self):
        res = ""
        curr = self.root
        while len(curr.child) == 1 and curr.isend == False:
            key = list(curr.child.keys())[0]
            res += key
            curr = curr.child[key]
        return res
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for col in range(len(strs[0])):
            for i in range(len(strs)-1):
                if col >= len(strs[i]):
                    return strs[i]
                if col >= len(strs[i+1]):
                    return strs[i+1]
                if strs[i][col] != strs[i+1][col]:
                    return strs[i][:col]
        return strs[0]
# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

