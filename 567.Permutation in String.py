#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=20001
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (46.36%)
# Likes:    11906
# Dislikes: 451
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        
        count = 0
        need = defaultdict(lambda:0)
        have = defaultdict(lambda:0)
        for i in s1:
            need[i] += 1
        count = len(need)
        while right < len(s2):
            if s2[right] not in need:
                right +=1
                left = right
                count = len(need)
                have.clear()
            else:
                have[s2[right]]+=1
                if have[s2[right]] == need[s2[right]]:
                    print(s2[right],have[s2[right]])
                    count -=1
                right += 1
            
            while right - left + 1 > len(s1):
                if count == 0:
                    return True
                if s2[left] in need:
                    if have[s2[left]] == need[s2[left]]:
                        count += 1
                    have[s2[left]] -= 1
                left += 1
        return False
                
# @lc code=end



#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

