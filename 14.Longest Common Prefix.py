#
# @lc app=leetcode id=14 lang=python3
# @lcpr version=20001
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.05%)
# Likes:    18115
# Dislikes: 4618
# Total Accepted:    3.8M
# Total Submissions: 8.7M
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
# strs[i] consists of only lowercase English letters.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for ind in range (len(strs[0])):
            for str in range (1,len(strs)):
                if ind >= len(strs[str]) or ind >= len(strs[str-1]) or strs[str][ind] != strs[str-1][ind]:
                    return "" if strs[str][0:ind] == None else strs[str][0:ind]
        
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

