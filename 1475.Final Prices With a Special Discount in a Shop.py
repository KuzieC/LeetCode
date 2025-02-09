#
# @lc app=leetcode id=1475 lang=python3
# @lcpr version=30003
#
# [1475] Final Prices With a Special Discount in a Shop
#
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
#
# algorithms
# Easy (83.15%)
# Likes:    2686
# Dislikes: 137
# Total Accepted:    300.4K
# Total Submissions: 361.3K
# Testcase Example:  '[8,4,6,2,3]'
#
# You are given an integer array prices where prices[i] is the price of the
# i^th item in a shop.
# 
# There is a special discount for items in the shop. If you buy the i^th item,
# then you will receive a discount equivalent to prices[j] where j is the
# minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will
# not receive any discount at all.
# 
# Return an integer array answer where answer[i] is the final price you will
# pay for the i^th item of the shop, considering the special discount.
# 
# 
# Example 1:
# 
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to
# prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to
# prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to
# prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.
# 
# 
# Example 2:
# 
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount
# at all.
# 
# 
# Example 3:
# 
# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 500
# 1 <= prices[i] <= 1000
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [0 for _ in range(len(prices))]
        q = []
        for i in range(len(prices)-1,-1,-1):
            while q and q[-1] > prices[i]:
                q.pop()
            if q:
                res[i] = prices[i] - q[-1]
            else:
                res[i] = prices[i]
            q.append(prices[i])

        return res   
            
# @lc code=end



#
# @lcpr case=start
# [8,4,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [10,1,1,6]\n
# @lcpr case=end

#

