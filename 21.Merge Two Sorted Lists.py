#
# @lc app=leetcode id=21 lang=python3
# @lcpr version=20001
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (65.44%)
# Likes:    22224
# Dislikes: 2174
# Total Accepted:    4.6M
# Total Submissions: 7M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# 
# Example 1:
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# 
# Example 3:
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
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
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0,None)
        curr = dummyhead
        p1 = list1
        p2 = list2
        
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                curr.next = p2
                p2 = p2.next

            else:
                curr.next = p1
                p1 = p1.next
            curr = curr.next
        
        if p1 is not None:
            curr.next = p1
        
        if p2 is not None:
            curr.next = p2
        
        return dummyhead.next
        
                
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

