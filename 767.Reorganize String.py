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
    def reorganizeString(self, str: str) -> str:
        mp = defaultdict(int)
        s = []
        res = ""
        for i in str:
            mp[i] += 1
        for k,v in mp.items():
            heappush(s,(-1 * v,k))
        print(s)
        while len(s) > 1:
            v1, k1 = heappop(s)
            v2, k2 = heappop(s)
            v1 = v1 * -1
            v2 = v2 * -1
            res+= k1
            res+= k2
            if v1 > 1:
                heappush(s,(-1 * (v1-1),k1))
            if v2 > 1:
                heappush(s,(-1 * (v2-1),k2))
        if len(s) == 1:
            v, k  = heappop(s)
            if v*-1 == 1 and (not res or res[-1] != k):
                res += k
            else:
                return ""
        return res    
        
            
        
            
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "aaab"\n
# @lcpr case=end

#

