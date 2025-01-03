#
# @lc app=leetcode id=1011 lang=python3
# @lcpr version=20002
#
# [1011] Capacity To Ship Packages Within D Days
#
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (70.64%)
# Likes:    9706
# Dislikes: 237
# Total Accepted:    454.7K
# Total Submissions: 643.7K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5'
#
# A conveyor belt has packages that must be shipped from one port to another
# within days days.
# 
# The i^th package on the conveyor belt has a weight of weights[i]. Each day,
# we load the ship with packages on the conveyor belt (in the order given by
# weights). We may not load more weight than the maximum weight capacity of the
# ship.
# 
# Return the least weight capacity of the ship that will result in all the
# packages on the conveyor belt being shipped within days days.
# 
# 
# Example 1:
# 
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in
# 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# 
# Note that the cargo must be shipped in the order given, so using a ship of
# capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6,
# 7), (8), (9), (10) is not allowed.
# 
# 
# Example 2:
# 
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in
# 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# 
# 
# Example 3:
# 
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= days <= weights.length <= 5 * 10^4
# 1 <= weights[i] <= 500
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def f(weights,x):
            count = 1
            total  = 0
            for i in range(len(weights)):
                if total + weights[i] > x:
                    total = weights[i]
                    count += 1
                else:
                    total += weights[i]
            print(x,count)
            return count

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left)//2
            res = f(weights,mid)
            if res < days:
                right = mid
            elif res > days:
                left = mid + 1
            elif res == days:
                right = mid
        return left

             
                   
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#

