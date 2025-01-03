#
# @lc app=leetcode id=39 lang=python3
# @lcpr version=20001
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (72.98%)
# Likes:    19159
# Dislikes: 441
# Total Accepted:    2.2M
# Total Submissions: 3M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
# 
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.
# 
# 
# Example 1:
# 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# 
# Example 2:
# 
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 
# Example 3:
# 
# Input: candidates = [2], target = 1
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = [[]]
        candidates.sort()
        curr = []
        currSum = 0
        lastModeified = []
        
        for i in candidates:
            
            lastModeified = []
            for j in track:
                curr = j + [i]
                currSum = sum(curr)
                
                while currSum <= target:
                    if currSum == target:
                        res.append(curr[:])
                        break
                    lastModeified.append(curr)
                    curr = curr + [i]
                    currSum += i
                
            track.extend(lastModeified)
                
                    

        return res
        
        
# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

