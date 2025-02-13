#
# @lc app=leetcode id=1104 lang=python3
# @lcpr version=30005
#
# [1104] Path In Zigzag Labelled Binary Tree
#
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/
#
# algorithms
# Medium (75.49%)
# Likes:    1508
# Dislikes: 324
# Total Accepted:    48.8K
# Total Submissions: 64.6K
# Testcase Example:  '14'
#
# In an infinite binary tree where every node has two children, the nodes are
# labelled in row order.
# 
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is
# left to right, while in the even numbered rows (second, fourth, sixth,...),
# the labelling is right to left.
# 
# 
# 
# Given the label of a node in this tree, return the labels in the path from
# the root of the tree to the node with that label.
# 
# 
# Example 1:
# 
# Input: label = 14
# Output: [1,3,4,14]
# 
# 
# Example 2:
# 
# Input: label = 26
# Output: [1,2,6,10,26]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= label <= 10^6
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        n = 0
        while not (label >= pow(2,n) and label < pow(2,n+1)):
            n+=1
        if n % 2 == 1:
            newlabel = pow(2,n+1)-1 - label + pow(2,n)
        else:
            newlabel = label
        res = []
        while newlabel >= 1:
            res.append(newlabel)
            newlabel //= 2
        res.reverse()
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = pow(2,i+1)-1 - res[i] + pow(2,i)
        return res
# @lc code=end



#
# @lcpr case=start
# 14\n
# @lcpr case=end

# @lcpr case=start
# 26\n
# @lcpr case=end

#

