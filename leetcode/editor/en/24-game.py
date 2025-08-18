#
# @lc app=leetcode id=679 lang=python3
# @lcpr version=30202
#
# [679] 24 Game
#
# https://leetcode.com/problems/24-game/description/
#
# algorithms
# Hard (50.15%)
# Likes:    1628
# Dislikes: 266
# Total Accepted:    110.3K
# Total Submissions: 205.6K
# Testcase Example:  '[4,1,8,7]'
#
# You are given an integer array cards of length 4. You have four cards, each
# containing a number in the range [1, 9]. You should arrange the numbers on
# these cards in a mathematical expression using the operators ['+', '-', '*',
# '/'] and the parentheses '(' and ')' to get the value 24.
# 
# You are restricted with the following rules:
# 
# 
# The division operator '/' represents real division, not integer
# division.
# 
# 
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# 
# 
# Every operation done is between two numbers. In particular, we cannot use '-'
# as a unary operator.
# 
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not
# allowed.
# 
# 
# You cannot concatenate numbers together
# 
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not
# valid.
# 
# 
# 
# 
# Return true if you can get such expression that evaluates to 24, and false
# otherwise.
# 
# 
# Example 1:
# 
# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24
# 
# 
# Example 2:
# 
# Input: cards = [1,2,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# cards.length == 4
# 1 <= cards[i] <= 9
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = False
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(lists):
            if self.res:
                return
            if len(lists) == 1:
                if abs(lists[0] - 24.0) <= 1e-6:
                    self.res = True
                return
            for i in range(len(lists)):
                for j in range(i+1,len(lists)):
                    rest = [ lists[k] for k in range(len(lists)) if k != i and k != j]
                    candidates = [lists[i] + lists[j], lists[i] * lists[j], lists[i] - lists[j],lists[j] - lists[i]]
                    if lists[i] != 0:
                        candidates.append(lists[j] / lists[i])
                    if lists[j] != 0:
                        candidates.append(lists[i] / lists[j])
                    for can in candidates:
                        dfs(rest + [can])
        dfs([float(card) for card in cards])
        return self.res
# @lc code=end



#
# @lcpr case=start
# [4,1,8,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2]\n
# @lcpr case=end

#

