#
# @lc app=leetcode id=40 lang=python3
# @lcpr version=20001
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (56.57%)
# Likes:    11136
# Dislikes: 325
# Total Accepted:    1.2M
# Total Submissions: 2.1M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(curr, ava,sum):
            if sum == target:
                res.append(curr[:])
                return

            if sum > target:
                return
            
            for i in range(len(ava)):
                if i > 0 and ava[i] == ava[i-1]:
                    continue
                curr.append(ava[i])
                
                helper(curr,ava[i+1:],sum+ava[i])
                curr.pop()
        helper([],candidates,0)
        return res
# @lc code=end



#
# @lcpr case=start
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,5,2,1,2]\n5\n
# @lcpr case=end

#

