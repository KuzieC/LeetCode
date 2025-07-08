#
# @lc app=leetcode id=777 lang=python3
# @lcpr version=30201
#
# [777] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (37.55%)
# Likes:    1297
# Dislikes: 944
# Total Accepted:    88.1K
# Total Submissions: 234.5K
# Testcase Example:  '"RXXLRXRXL"\n"XRLXXRRLX"'
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string result, return True if and only if there exists a
# sequence of moves to transform start to result.
# 
# 
# Example 1:
# 
# Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to result following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# Example 2:
# 
# Input: start = "X", result = "L"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= start.length <= 10^4
# start.length == result.length
# Both start and result will only consist of characters in 'L', 'R', and 'X'.
# 
# 
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        p1 = 0
        p2 = 0
        if start.replace("X","") != result.replace("X",""):
            return False
        while p1 < len(start) and p2 < len(result):
            while p1 < len(start) and start[p1] == "X":
                p1 += 1
            while p2 < len(result) and result[p2] == "X":
                p2 += 1
            if p1 < len(start) and p2 < len(result):
                if start[p1] == "R" and p2 < p1:
                    return False
                elif start[p1] == "L" and p2 > p1:
                    return False
                else:
                    p1+=1
                    p2+=1
            else:
                return p1 == len(start) and p2 == len(result)
        return True
# @lc code=end



#
# @lcpr case=start
# "RXXLRXRXL"\n"XRLXXRRLX"\n
# @lcpr case=end

# @lcpr case=start
# "X"\n"L"\n
# @lcpr case=end

#

