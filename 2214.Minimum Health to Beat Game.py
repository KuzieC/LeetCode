#
# @lc app=leetcode id=2214 lang=python3
# @lcpr version=30003
#
# [2214] Minimum Health to Beat Game
#
# https://leetcode.com/problems/minimum-health-to-beat-game/description/
#
# algorithms
# Medium (57.92%)
# Likes:    318
# Dislikes: 235
# Total Accepted:    33.6K
# Total Submissions: 58K
# Testcase Example:  '[2,7,4,3]\n4'
#
# You are playing a game that has n levels numbered from 0 to n - 1. You are
# given a 0-indexed integer array damage where damage[i] is the amount of
# health you will lose to complete the i^th level.
# 
# You are also given an integer armor. You may use your armor ability at most
# once during the game on any level which will protect you from at most armor
# damage.
# 
# You must complete the levels in order and your health must be greater than 0
# at all times to beat the game.
# 
# Return the minimum health you need to start with to beat the game.
# 
# 
# Example 1:
# 
# Input: damage = [2,7,4,3], armor = 4
# Output: 13
# Explanation: One optimal way to beat the game starting at 13 health is:
# On round 1, take 2 damage. You have 13 - 2 = 11 health.
# On round 2, take 7 damage. You have 11 - 7 = 4 health.
# On round 3, use your armor to protect you from 4 damage. You have 4 - 0 = 4
# health.
# On round 4, take 3 damage. You have 4 - 3 = 1 health.
# Note that 13 is the minimum health you need to start with to beat the game.
# 
# 
# Example 2:
# 
# Input: damage = [2,5,3,4], armor = 7
# Output: 10
# Explanation: One optimal way to beat the game starting at 10 health is:
# On round 1, take 2 damage. You have 10 - 2 = 8 health.
# On round 2, use your armor to protect you from 5 damage. You have 8 - 0 = 8
# health.
# On round 3, take 3 damage. You have 8 - 3 = 5 health.
# On round 4, take 4 damage. You have 5 - 4 = 1 health.
# Note that 10 is the minimum health you need to start with to beat the game.
# 
# 
# Example 3:
# 
# Input: damage = [3,3,3], armor = 0
# Output: 10
# Explanation: One optimal way to beat the game starting at 10 health is:
# On round 1, take 3 damage. You have 10 - 3 = 7 health.
# On round 2, take 3 damage. You have 7 - 3 = 4 health.
# On round 3, take 3 damage. You have 4 - 3 = 1 health.
# Note that you did not use your armor ability.
# 
# 
# 
# Constraints:
# 
# 
# n == damage.length
# 1 <= n <= 10^5
# 0 <= damage[i] <= 10^5
# 0 <= armor <= 10^5
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        m = max(damage)
        return sum(damage) - m + max(0,(m-armor)) + 1
# @lc code=end



#
# @lcpr case=start
# [2,7,4,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,5,3,4]\n7\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3]\n0\n
# @lcpr case=end

#

