#
# @lc app=leetcode id=239 lang=python3
# @lcpr version=30201
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (47.65%)
# Likes:    19321
# Dislikes: 762
# Total Accepted:    1.3M
# Total Submissions: 2.8M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
from  collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = deque()
        i = 0
        left = 0
        for i in range(min(len(nums),k)):
            while pq and pq[-1] < nums[i]:
                pq.pop()
            pq.append(nums[i])
        res = []
        while i < len(nums)-1:
            res.append(pq[0])
            i+=1
            while pq and pq[-1] < nums[i]:
                pq.pop()
            pq.append(nums[i])
            if pq[0] == nums[left]:
                pq.popleft()
            left+=1
        res.append(pq[0])
        return res
            
# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

