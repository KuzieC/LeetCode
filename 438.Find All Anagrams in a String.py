#
# @lc app=leetcode id=438 lang=python3
# @lcpr version=20001
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (51.40%)
# Likes:    12475
# Dislikes: 343
# Total Accepted:    929.8K
# Total Submissions: 1.8M
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
# 
# 
# Example 1:
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# Example 2:
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = defaultdict(lambda:0)
        window = defaultdict(lambda:0)

        for i in p:
            need[i] += 1
        count = len(need)       
        n = len(s)
        
        left,right = 0,0
        res = []
        while right < n:
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    print(c,"-1")
                    count -= 1
            
            while right - left > len(p):
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        print(c,"+1")
                        count += 1
                    window[c] -= 1
                
            if count == 0:
                print(left,right)
                res.append(left)
    
        return res
# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

