#
# @lc app=leetcode id=46 lang=python
# @lcpr version=30201
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (80.72%)
# Likes:    20016
# Dislikes: 357
# Total Accepted:    2.6M
# Total Submissions: 3.3M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,used,curr):
            if len(curr) == len(nums):
                self.res.append(curr[:])
                return
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    curr.append(nums[i])
                    dfs(nums,used,curr)
                    curr.pop()
                    used.remove(i)
        s = set()
        dfs(nums,s,[])
        return self.res
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

