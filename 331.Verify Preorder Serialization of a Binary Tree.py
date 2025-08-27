#
# @lc app=leetcode id=331 lang=python3
# @lcpr version=30202
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def __init__(self):
        self.pre = []
        self.idx = 0
    def helper(self):
        if self.idx >= len(self.pre):
            return False
        
        if self.pre[self.idx] == "#":
            return 
        self.idx+=1
        self.helper()
        self.idx+=1
        self.helper()
        return
    
    def isValidSerialization(self, preorder: str) -> bool:
        self.pre = preorder.split(",")
        self.helper()
        if self.idx == len(self.pre)-1:
            return True
        return False


# @lc code=end



#
# @lcpr case=start
# "9,3,4,#,#,1,#,#,2,#,6,#,#"\n
# @lcpr case=end

# @lcpr case=start
# "1,#"\n
# @lcpr case=end

# @lcpr case=start
# "9,#,#,1"\n
# @lcpr case=end

#

