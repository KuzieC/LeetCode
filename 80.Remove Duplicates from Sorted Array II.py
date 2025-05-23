#
# @lc app=leetcode id=80 lang=python3
# @lcpr version=20001
#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (60.58%)
# Likes:    7163
# Dislikes: 1380
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[1,1,1,2,2,3]'
#
# Given an integer array nums sorted in non-decreasing order, remove some
# duplicates in-place such that each unique element appears at most twice. The
# relative order of the elements should be kept the same.
# 
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.
# 
# Return k after placing the final result in the first k slots of nums.
# 
# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Custom Judge:
# 
# The judge will test your solution with the following code:
# 
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# 
# int k = removeDuplicates(nums); // Calls your implementation
# 
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
# ⁠   assert nums[i] == expectedNums[i];
# }
# 
# 
# If all assertions pass, then your solution will be accepted.
# 
# 
# Example 1:
# 
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
# 
# 
# Example 2:
# 
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements
# of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 0, 1
        count = 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
                
                count = 0
            elif count < 2:
                left += 1
                nums[left] = nums[right]
                
            count += 1
            right += 1
        return (left+1)
                    
                
            
            
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

