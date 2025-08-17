#
# @lc app=leetcode id=837 lang=python3
# @lcpr version=30202
#
# [837] New 21 Game
#
# https://leetcode.com/problems/new-21-game/description/
#
# algorithms
# Medium (44.77%)
# Likes:    2228
# Dislikes: 1909
# Total Accepted:    107.4K
# Total Submissions: 223K
# Testcase Example:  '10\n1\n10'
#
# Alice plays the following game, loosely based on the card game "21".
# 
# Alice starts with 0 points and draws numbers while she has less than k
# points. During each draw, she gains an integer number of points randomly from
# the range [1, maxPts], where maxPts is an integer. Each draw is independent
# and the outcomes have equal probabilities.
# 
# Alice stops drawing numbers when she gets k or more points.
# 
# Return the probability that Alice has n or fewer points.
# 
# Answers within 10^-5 of the actual answer are considered accepted.
# 
# 
# Example 1:
# 
# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000
# Explanation: Alice gets a single card, then stops.
# 
# 
# Example 2:
# 
# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.
# 
# 
# Example 3:
# 
# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278
# 
# 
# 
# Constraints:
# 
# 
# 0 <= k <= n <= 10^4
# 1 <= maxPts <= 10^4
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    # def new21Game(self, n: int, k: int, W: int) -> float:
        
    #     if k == 0 or n >= k + W - 1:
    #         return 1.0

    #     m = k + W  
    #     dp = [0.0] * m

    #     for x in range(k, min(n, m - 1) + 1):
    #         dp[x] = 1.0

    #     window_sum = sum(dp[x] for x in range(k, m)) 

    #     for x in range(k - 1, -1, -1):
    #         dp[x] = window_sum / W
    #         window_sum += dp[x] - dp[x + W]
    #     return dp[0]

    def new21Game(self, n: int, k: int, W: int) -> float:
        if k == 0 or n >= k + W - 1:
            return 1.0
        
        left = 0
        right = 1
        currSum = 1
        dp = [0.0] * (n+1)
        dp[0] = 1
        res = 0.0
        while right <= n:
            dp[right] = currSum/W
            
            if right < k:
                currSum += dp[right]
            
            right+=1
            
            if right - left > W:
                currSum -= dp[left]
                left+=1
        return sum([dp[i] for i in range(k,n+1)])

            
# @lc code=end



#
# @lcpr case=start
# 10\n1\n10\n
# @lcpr case=end

# @lcpr case=start
# 6\n1\n10\n
# @lcpr case=end

# @lcpr case=start
# 21\n17\n10\n
# @lcpr case=end

#

