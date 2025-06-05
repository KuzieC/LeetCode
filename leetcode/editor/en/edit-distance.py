#
# @lc app=leetcode id=72 lang=python3
# @lcpr version=30201
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Medium (58.71%)
# Likes:    15634
# Dislikes: 281
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# 
# Example 1:
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
# 
# Constraints:
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# 
# 
#

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
# @lc code=end




#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

