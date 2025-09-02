#
# @lc app=leetcode id=951 lang=python3
# @lcpr version=30202
#
# [951] Flip Equivalent Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1:
            return True if not root2 else False
        if not root2:
            return True if not root1 else False
        level = {}
        q = deque()
        q.append(root1)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                currlvl = set()
                if curr.left:
                    currlvl.add(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    currlvl.add(curr.right.val)
                    q.append(curr.right)
                level[curr.val] = currlvl
        q.append(root2)
        while q:
            for _ in range(len(q)):
                currlvl = set()
                curr = q.popleft()
                if not curr:
                    continue
                if curr.left:
                    currlvl.add(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    currlvl.add(curr.right.val)
                    q.append(curr.right)
                if curr.val not in level or currlvl != level[curr.val]:
                    return False
        return True        

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[1]\n
# @lcpr case=end

#

