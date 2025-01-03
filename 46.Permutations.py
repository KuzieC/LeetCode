#
# @lc app=leetcode id=46 lang=python3
# @lcpr version=20001
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (79.41%)
# Likes:    19332
# Dislikes: 337
# Total Accepted:    2.3M
# Total Submissions: 2.9M
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


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        mp = defaultdict(lambda:0)
        for i in nums:
            mp[i] = 1
        
        def helper(num: List[int],avaiable: List[int]):
            if len(num) == len(nums):
                res.append(num.copy())
                return
            for i in range(len(avaiable)):
                    num.append(avaiable[i])
                    tmp = avaiable[:]
                    del tmp[i]
                    helper(num,tmp)
                    num.pop()
            return
        helper([],nums)
        return res
            
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

