#
# @lc app=leetcode id=61 lang=python3
# @lcpr version=30202
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right = left = head
        prev = None
        if not head:
            return None

        count = 0
        while right:
            count += 1
            right = right.next
        k = k % count
        right = head
        while k > 1:
            right = right.next
            k -= 1
        if k == 0:
            return head
        while right.next:
            right = right.next
            prev = left
            left = left.next
        if prev != None: 
            prev.next = None
            right.next = head
        return left
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#

