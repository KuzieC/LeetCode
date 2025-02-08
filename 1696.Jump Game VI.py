#
# @lc app=leetcode id=1696 lang=python3
# @lcpr version=30002
#
# [1696] Jump Game VI
#
# https://leetcode.com/problems/jump-game-vi/description/
#
# algorithms
# Medium (45.78%)
# Likes:    3464
# Dislikes: 116
# Total Accepted:    114.2K
# Total Submissions: 249.3K
# Testcase Example:  '[1,-1,-2,4,-7,3]\n2'
#
# You are given a 0-indexed integer array nums and an integer k.
# 
# You are initially standing at index 0. In one move, you can jump at most k
# steps forward without going outside the boundaries of the array. That is, you
# can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
# inclusive.
# 
# You want to reach the last index of the array (index n - 1). Your score is
# the sum of all nums[j] for each index j you visited in the array.
# 
# Return the maximum score you can get.
# 
# 
# Example 1:
# 
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
# (underlined above). The sum is 7.
# 
# 
# Example 2:
# 
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3]
# (underlined above). The sum is 17.
# 
# 
# Example 3:
# 
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length, k <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        s = deque()
        dp[0] = nums[0]
        s.append(nums[0])
        left = 0
        right = 1
        while right < len(nums):
            if right - left > k:
                if dp[left] == s[0]:
                    s.popleft()
                left+=1
            if s:
                dp[right] = s[0] + nums[right]
            while s and s[-1] < dp[right]:
                s.pop()
            s.append(dp[right])
            right+=1
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# [1,-1,-2,4,-7,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [10,-5,-2,4,0,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,-5,-20,4,-1,3,-6,-3]\n2\n
# @lcpr case=end

#

