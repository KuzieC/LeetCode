#
# @lc app=leetcode id=1019 lang=python3
# @lcpr version=30003
#
# [1019] Next Greater Node In Linked List
#
# https://leetcode.com/problems/next-greater-node-in-linked-list/description/
#
# algorithms
# Medium (61.77%)
# Likes:    3370
# Dislikes: 120
# Total Accepted:    177.8K
# Total Submissions: 287.8K
# Testcase Example:  '[2,1,5]'
#
# You are given the head of a linked list with n nodes.
# 
# For each node in the list, find the value of the next greater node. That is,
# for each node, find the value of the first node that is next to it and has a
# strictly larger value than it.
# 
# Return an integer array answer where answer[i] is the value of the next
# greater node of the i^th node (1-indexed). If the i^th node does not have a
# next greater node, set answer[i] = 0.
# 
# 
# Example 1:
# 
# Input: head = [2,1,5]
# Output: [5,5,0]
# 
# 
# Example 2:
# 
# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= n <= 10^4
# 1 <= Node.val <= 10^9
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        q = deque()
        while head:
            res.append(head.val)
            head = head.next
        ans = [0 for _ in range(len(res))]
        for i in range(len(res)-1,-1,-1):
            while q and res[i] >= q[-1]:
                q.pop()
            if not q:
                ans[i] = 0
            else:
                ans[i] = q[-1]
            q.append(res[i])
        return ans
                
                
               
# @lc code=end



#
# @lcpr case=start
# [2,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,4,3,5]\n
# @lcpr case=end

#

