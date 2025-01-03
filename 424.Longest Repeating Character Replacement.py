#
# @lc app=leetcode id=424 lang=python3
# @lcpr version=20002
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (55.55%)
# Likes:    11012
# Dislikes: 572
# Total Accepted:    900K
# Total Submissions: 1.6M
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = 0
        inWindow = {}
        maxCount = 0
        while right < len(s):
            if s[right] not in inWindow:
                inWindow[s[right]] = 1
            else:
                inWindow[s[right]] += 1
            right += 1
            maxCount = max(maxCount,inWindow[s[right-1]])
            while right - left - maxCount > k:
                inWindow[s[left]] -= 1
                left += 1
            res = max(res,right - left)

        return res
                    
# @lc code=end



#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#

