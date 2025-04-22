#
# @lc app=leetcode id=234 lang=python3
# @lcpr version=30008
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (55.05%)
# Likes:    17126
# Dislikes: 918
# Total Accepted:    2.3M
# Total Submissions: 4.1M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
# 
# 
# Example 1:
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

