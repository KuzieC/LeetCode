#
# @lc app=leetcode id=354 lang=python3
# @lcpr version=30201
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (37.32%)
# Likes:    6239
# Dislikes: 158
# Total Accepted:    255.7K
# Total Submissions: 685K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
# 
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
# 
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
# 
# Note: You cannot rotate an envelope.
# 
# 
# Example 1:
# 
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# Example 2:
# 
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5
# 
# 
#

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"



# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0],-x[1]) )
        height = [i[1] for i in envelopes]
        
        deck = [0] * len(height)
        pile = 0
        for curr in height:
            left , right = 0, pile
            while left < right:
                mid = (right+left) // 2
                val = deck[mid]
                if val < curr:
                    left = mid + 1
                else:
                    right = mid
            if left == pile:
                pile+=1
            deck[left] = curr
        return pile
# @lc code=end




#
# @lcpr case=start
# [[5,4],[6,4],[6,7],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1],[1,1]]\n
# @lcpr case=end

#

