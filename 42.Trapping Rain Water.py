#
# @lc app=leetcode id=42 lang=python3
# @lcpr version=20004
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (63.98%)
# Likes:    33286
# Dislikes: 571
# Total Accepted:    2.6M
# Total Submissions: 4M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftm = height[0]
        res = 0
        rightm = height[len(height)-1]
        while left < right: 
            if leftm < rightm:
                res += leftm - height[left]
                print(res,left)
                left+=1
                leftm = max(leftm,height[left])
            else:
                res += rightm - height[right]
                print(res,right)
                right-=1
                rightm = max(rightm,height[right])
        
        return res
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

