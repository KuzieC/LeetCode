#
# @lc app=leetcode id=322 lang=python3
# @lcpr version=20001
#
# [322] Coin Change
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# class Solution:
#     def helper(self,coins:List[int],amount: int) -> int:
#         if amount == 0:
#             return 0
        
#         if amount < 0:
#             return -1
        
#         if self.dp[amount] is not None:
#             return self.dp[amount]

#         count = float('inf')
#         for coin in coins:
#             res = self.helper(coins,amount-coin)
#             if res != -1:
#                 count = min(count,res+1)
                

        
        
#         self.dp[amount] = count if count != float('inf') else -1
#         return self.dp[amount]



#     def coinChange(self, coins: List[int], amount: int) -> int:
#         self.dp = [None]*(amount+1)
#         return self.helper(coins,amount)

class Solution:
    def coinChange(self,coins,amount)->int:
        if amount == 0:
            return 0
        dp = [0 for _ in range(amount+1)]
        for i in coins:
            if i <= amount:
                dp[i] = 1   
        
        for i in range(1,amount+1):
            for j in coins:
                if i - j > 0 and dp[i-j] != 0:
                    val = dp[i-j] + 1
                    if dp[i] == 0:
                        dp[i] = val
                    else:
                        dp[i] = min(dp[i], val)
        return -1 if dp[amount] == 0 else dp[amount]
        
                    
    
# @lc code=end



#
# @lcpr case=start
# [1,2,5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

