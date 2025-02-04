#
# @lc app=leetcode id=128 lang=python3
# @lcpr version=20005
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.36%)
# Likes:    20917
# Dislikes: 1099
# Total Accepted:    2.3M
# Total Submissions: 4.9M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        curr = 1
        mp = defaultdict(int)
        for i in nums:
            mp[i] = 1
            
        mp2 = defaultdict(int)
        res = 0
        for i in nums:
            if i-1 in mp:
                continue
            curr = i
            maxx = 1
            if i in mp2:
                continue
            while curr+1 in mp:
                maxx+=1
                if curr+1 in mp2:
                    maxx += mp2[curr+1]
                    break
                curr+=1
                #print(curr,maxx)
            mp2[i] = maxx-1
            res = max(res,maxx)
        
        return res
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#

