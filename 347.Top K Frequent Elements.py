#
# @lc app=leetcode id=347 lang=python3
# @lcpr version=20004
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.91%)
# Likes:    17938
# Dislikes: 693
# Total Accepted:    2.6M
# Total Submissions: 4M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        q = []
        res = []
        vp = defaultdict(list)
        for val,freq in mp.items():
            vp[freq].append(val)
        vp = sorted(vp.items(),key = lambda i : i[0], reverse=True)
        for _,v in vp:
            res.extend(v)
            if len(res) == k:
                return res
        return None
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

