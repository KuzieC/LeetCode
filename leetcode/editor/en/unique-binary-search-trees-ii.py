#
# @lc app=leetcode id=95 lang=python3
# @lcpr version=30202
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (60.71%)
# Likes:    7808
# Dislikes: 568
# Total Accepted:    524.4K
# Total Submissions: 863.8K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
# 
# 
# Example 1:
# 
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
# Definition for a binary tree node.

class Solution:
    def helper(self,f,t):
        res = []
        if f > t:
            return [None]
        if f==t:
            curr = TreeNode(f)
            return [curr]
        for i in range(f,t+1):
            left = self.helper(f,i-1)
            right = self.helper(i+1,t)
            for l in left:
                for r in right:
                    curr = TreeNode(i)
                    curr.left = l
                    curr.right = r
                    res.append(curr)
        return res
            
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(1,n)
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

