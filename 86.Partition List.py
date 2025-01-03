#
# @lc app=leetcode id=86 lang=python3
# @lcpr version=20001
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (57.39%)
# Likes:    7428
# Dislikes: 897
# Total Accepted:    681K
# Total Submissions: 1.2M
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# 
# Example 1:
# 
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# 
# 
# Example 2:
# 
# Input: head = [2,1], x = 2
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lower = ListNode(0,None)
        res = lower
        higher = ListNode(0,None)
        res2 = higher
        curr = head
        while curr is not None:
            if curr.val < x:
                lower.next = curr
                lower = lower.next
            
            else:
                higher.next = curr
                higher = higher.next
                
            temp = curr.next
            curr.next = None
            curr = temp
        lower.next = res2.next
        
        return res.next
# @lc code=end



#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

