#
# @lc app=leetcode id=3516 lang=python3
# @lcpr version=30202
#
# [3516] Find Closest Person
#

# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 1 if abs(z-x) < abs(z-y) else 0 if abs(z-x) == abs(z-y) else 2
# @lc code=end



#
# @lcpr case=start
# 2\n7\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n5\n6\n
# @lcpr case=end

# @lcpr case=start
# 1\n5\n3\n
# @lcpr case=end

#

