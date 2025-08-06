#
# @lc app=leetcode id=904 lang=python3
# @lcpr version=30202
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (49.23%)
# Likes:    5647
# Dislikes: 493
# Total Accepted:    660.4K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,1]'
#
# You are visiting a farm that has a single row of fruit trees arranged from
# left to right. The trees are represented by an integer array fruits where
# fruits[i] is the type of fruit the i^th tree produces.
# 
# You want to collect as much fruit as possible. However, the owner has some
# strict rules that you must follow:
# 
# 
# You only have two baskets, and each basket can only hold a single type of
# fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from
# every tree (including the start tree) while moving to the right. The picked
# fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must
# stop.
# 
# 
# Given the integer array fruits, return the maximum number of fruits you can
# pick.
# 
# 
# Example 1:
# 
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# 
# 
# Example 2:
# 
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# 
# 
# Example 3:
# 
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
# 
# 
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, curr = 0, 0
        left, right = 0, 0
        inWindow = {}
        numCount = 0
        while right < len(fruits):
            curr += 1
            if fruits[right] not in inWindow:
                numCount+=1
                inWindow[fruits[right]] = 1
            else:
                inWindow[fruits[right]] += 1
            right+=1
            while left < right and numCount > 2:
                curr -= 1
                if inWindow[fruits[left]] == 1:
                    inWindow.pop(fruits[left])
                    numCount -= 1
                else:
                    inWindow[fruits[left]] -= 1
                left+=1
            res = max(res,curr)
        return res
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,2,2]\n
# @lcpr case=end

#

