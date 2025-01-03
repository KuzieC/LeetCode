#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=20001
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (43.86%)
# Likes:    18185
# Dislikes: 751
# Total Accepted:    1.5M
# Total Submissions: 3.4M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# 
# Example 1:
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        need = defaultdict(lambda: 0)
        window = defaultdict(lambda: 0)
        flag = False
        start = 0
        length = float('inf')
        for i in t:
            need[i] += 1
        count = 0
        while right < len(s):
            if s[right] in need:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    count += 1

            right+=1
            
            while count == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                if s[left] in need:
                    
                    if window[s[left]] == need[s[left]]:
                        count -= 1
                    window[s[left]] -= 1
                left += 1
                
        return s[start:start+length] if length != float('inf') else ""
                
                
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

