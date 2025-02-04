#
# @lc app=leetcode id=239 lang=python3
# @lcpr version=20005
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (47.16%)
# Likes:    18834
# Dislikes: 719
# Total Accepted:    1.2M
# Total Submissions: 2.6M
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


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = list()
        for i in range(k):
            while len(q) > 0 and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        
        res = list()
        for i in range(k,len(nums)):
            res.append(q[0])
            while len(q) > 0 and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            if q[0] == nums[i-k]:
                q.pop(0)
        res.append(q[0])
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

