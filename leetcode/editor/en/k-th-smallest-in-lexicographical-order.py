#
# @lc app=leetcode id=440 lang=python
# @lcpr version=30201
#
# [440] K-th Smallest in Lexicographical Order
#
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (45.89%)
# Likes:    1614
# Dislikes: 145
# Total Accepted:    160.7K
# Total Submissions: 350.2K
# Testcase Example:  '13\n2'
#
# Given two integers n and k, return the k^th lexicographically smallest
# integer in the range [1, n].
# 
# 
# Example 1:
# 
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6,
# 7, 8, 9], so the second smallest number is 10.
# 
# 
# Example 2:
# 
# Input: n = 1, k = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution(object):
    def count(self,ffrom,to,n):
        c = 0
        curr = ffrom
        while curr <= n:
            c += min(to,n+1) - curr
            curr *= 10
            to *= 10
        return c
    
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        curr = 1
        k-=1
        steps = 0
        while k != 0:
            steps = self.count(curr,curr+1,n)
            if steps <= k:
                curr+=1
                k-= steps
            else:
                curr*=10
                k-=1
        return curr
                
# @lc code=end



#
# @lcpr case=start
# 13\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

