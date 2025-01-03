#
# @lc app=leetcode id=82 lang=python3
# @lcpr version=20001
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (48.46%)
# Likes:    8929
# Dislikes: 247
# Total Accepted:    808.4K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
# 
# 
# Example 1:
# 
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# 
# 
# Example 2:
# 
# Input: head = [1,1,1,2,3]
# Output: [2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            while head.next is not None and head.next.val == head.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        

# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end


