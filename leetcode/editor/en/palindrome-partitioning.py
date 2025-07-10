#
# @lc app=leetcode id=131 lang=python3
# @lcpr version=30201
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (72.32%)
# Likes:    13671
# Dislikes: 550
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
    
    def isPal(self,s,start,end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True
    def dfs(self,s,curr,lis):
        if curr == len(s):
            self.res.append(lis.copy())
            return
        for i in range(curr,len(s)):
            if self.isPal(s,curr,i):
                lis.append(s[curr:i+1])
                self.dfs(s,i+1,lis)
                lis.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        self.dfs(s,0,[])
        return self.res
        
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

