#
# @lc app=leetcode id=518 lang=python3
# @lcpr version=30201
#
# [518] Coin Change II
#
# https://leetcode.com/problems/coin-change-ii/description/
#
# algorithms
# Medium (62.38%)
# Likes:    9785
# Dislikes: 213
# Total Accepted:    810.5K
# Total Submissions: 1.3M
# Testcase Example:  '5\n[1,2,5]'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the number of combinations that make up that amount. If that amount of
# money cannot be made up by any combination of the coins, return 0.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# The answer is guaranteed to fit into a signed 32-bit integer.
# 
# 
# Example 1:
# 
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# Example 2:
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# 
# Example 3:
# 
# Input: amount = 10, coins = [10]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000
# 
# 
#

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"


# @lc code=start
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for j in coins:
            for i in range(1,(amount)+1):
                if i - j >= 0:
                    dp[i] = dp[i] + dp[i-j]
        return dp[amount]
            
# @lc code=end



#
# @lcpr case=start
# 5\n[1,2,5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[10]\n
# @lcpr case=end

#

