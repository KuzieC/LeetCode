#
# @lc app=leetcode id=875 lang=python3
# @lcpr version=30201
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (49.06%)
# Likes:    12358
# Dislikes: 814
# Total Accepted:    1.2M
# Total Submissions: 2.4M
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
# 
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
# 
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
# 
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
# 
# 
# Example 1:
# 
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# 
# 
# Example 2:
# 
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# 
# 
# Example 3:
# 
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#

# @lc code=start
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(piles,speed):
            res = 0
            for i in piles:
                res += ceil(i/speed)
            return res

        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = lo + (hi - lo)//2
            res = helper(piles,mid)
            if res > h:
                lo = mid + 1
            else:
                hi = mid
        return lo
# @lc code=end



#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

