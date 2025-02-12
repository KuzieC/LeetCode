#
# @lc app=leetcode id=92 lang=python3
# @lcpr version=30005
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (48.97%)
# Likes:    12044
# Dislikes: 682
# Total Accepted:    1M
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
# 
# 
# Example 1:
# 
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# 
# 
# Example 2:
# 
# Input: head = [5], left = 1, right = 1
# Output: [5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# 
# 
# 
# Follow up: Could you do it in one pass?
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(head: Optional[ListNode], siz: int):
            if siz == 0:
                return head
            if head.next == None or siz == 1:
                return head
            else:
                newhead = reverse(head.next,siz-1)
                head.next.next = head
                head.next = None
                return newhead
        curr = head
        dummy = ListNode()
        dummy.next = curr
        prev = dummy
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        newtail = curr
        for _ in range(right-left+1):
            curr = curr.next
        after = curr
        newhead = reverse(newtail,right-left+1)
        prev.next = newhead
        newtail.next = after
        return dummy.next
        
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

