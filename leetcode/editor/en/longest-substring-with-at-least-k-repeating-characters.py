#
# @lc app=leetcode id=395 lang=python3
# @lcpr version=30202
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (45.55%)
# Likes:    6545
# Dislikes: 555
# Total Accepted:    269.4K
# Total Submissions: 591.6K
# Testcase Example:  '"aaabb"\n3'
#
# Given a string s and an integer k, return the length of the longest substring
# of s such that the frequency of each character in this substring is greater
# than or equal to k.
# 
# if no such substring exists, return 0.
# 
# 
# Example 1:
# 
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# Example 2:
# 
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and
# 'b' is repeated 3 times.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^5
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = Counter(s)
        legit = {ke for ke,v in count.items() if v >= k}
        left = 0
        right = 0
        inWindow = defaultdict(int)
        res = 0
        while right < len(s):
            if s[right] not in legit:
                right += 1
                left = right
                inWindow.clear()
                continue
            inWindow[s[right]] += 1
            right += 1
            
            templeft = left
            tempinWindow = inWindow.copy()
            for key in tempinWindow.keys():
                while templeft < right and 0 < tempinWindow[key] < k:
                    tempinWindow[s[templeft]] -= 1
                    templeft += 1
            flag = True
            for a,b in tempinWindow.items():
                if b != 0 and b < k:
                    flag = False
                    break
            if flag:
                
                res = max(res,right - templeft)
        return res

# @lc code=end



#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#

