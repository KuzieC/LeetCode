

#
# @lc app=leetcode id=3021 lang=python3
# @lcpr version=30202
#
# [3021] Alice and Bob Playing Flower Game
#

# @lc code=start
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddN = n // 2 if n % 2 == 0 else n // 2 + 1
        oddM = m // 2 if m % 2 == 0 else m // 2 + 1
        return oddN * (m - oddM) + oddM * (n - oddN)
        
# @lc code=end



#
# @lcpr case=start
# 3\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

