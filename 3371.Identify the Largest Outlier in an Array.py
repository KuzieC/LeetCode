#
# @lc app=leetcode id=3371 lang=python3
# @lcpr version=20004
#
# [3371] Identify the Largest Outlier in an Array
#
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/
#
# algorithms
# Medium (30.93%)
# Likes:    140
# Dislikes: 20
# Total Accepted:    28.5K
# Total Submissions: 92.2K
# Testcase Example:  '[2,3,5,10]'
#
# You are given an integer array nums. This array contains n elements, where
# exactly n - 2 elements are special numbers. One of the remaining two elements
# is the sum of these special numbers, and the other is an outlier.
# 
# An outlier is defined as a number that is neither one of the original special
# numbers nor the element representing the sum of those numbers.
# 
# Note that special numbers, the sum element, and the outlier must have
# distinct indices, but may share the same value.
# 
# Return the largest potential outlier in nums.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,5,10]
# 
# Output: 10
# 
# Explanation:
# 
# The special numbers could be 2 and 3, thus making their sum 5 and the outlier
# 10.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2,-1,-3,-6,4]
# 
# Output: 4
# 
# Explanation:
# 
# The special numbers could be -2, -1, and -3, thus making their sum -6 and the
# outlier 4.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1,1,1,5,5]
# 
# Output: 5
# 
# Explanation:
# 
# The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and
# the other 5 as the outlier.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 10^5
# -1000 <= nums[i] <= 1000
# The input is generated such that at least one potential outlier exists in
# nums.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        dict = {}
        sum = 0
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
            sum += i
        for i in range(len(nums)-1,-1,-1):
            tar = (sum - nums[i])/2.0
            if tar == nums[i]:
                if dict[tar] > 1:
                    return nums[i]
            elif tar in dict:
               return nums[i] 
                
        return -1
# @lc code=end



#
# @lcpr case=start
# [2,3,5,10]\n
# @lcpr case=end

# @lcpr case=start
# [-2,-1,-3,-6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1,5,5]\n
# @lcpr case=end

#

