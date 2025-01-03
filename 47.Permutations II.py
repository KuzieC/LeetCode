#
# @lc app=leetcode id=47 lang=python3
# @lcpr version=20001
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (60.23%)
# Likes:    8605
# Dislikes: 148
# Total Accepted:    1M
# Total Submissions: 1.7M
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
# 
# 
# Example 1:
# 
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        mp = [0 for i in range (len(nums))]
        for i in range (len(nums)):
            mp[i] = 1
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range (len(nums)):
                if mp[i] == 0:
                    continue
                if i > 0 and nums[i] == nums[i-1] and mp[i-1] == 1:
                    continue
                
                mp[i] = 0
                curr.append(nums[i])
                helper(curr)
                curr.pop()
                mp[i] = 1
        
        helper([])
        return res
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

