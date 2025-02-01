#
# @lc app=leetcode id=767 lang=python3
# @lcpr version=20004
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (55.61%)
# Likes:    8738
# Dislikes: 270
# Total Accepted:    463.3K
# Total Submissions: 833.1K
# Testcase Example:  '"aab"'
#
# Given a string s, rearrange the characters of s so that any two adjacent
# characters are not the same.
# 
# Return any possible rearrangement of s or return "" if not possible.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of lowercase English letters.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        mp = defaultdict(int)
        for i in s:
            mp[i] += 1
        for val in mp.values():
            if val > (n+1)//2:
                return ""
        res = [""] * n
        ind = 0
        for val, rep in sorted(mp.items(),key = lambda x: -x[1]):
            for _ in range(rep):
                if ind >= n:
                    ind = 1
                res[ind] = val
                ind += 2
        return "".join(res)
            
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "aaab"\n
# @lcpr case=end

#

