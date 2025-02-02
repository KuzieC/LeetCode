#
# @lc app=leetcode id=22 lang=python3
# @lcpr version=20005
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.31%)
# Likes:    21780
# Dislikes: 1007
# Total Accepted:    2.2M
# Total Submissions: 2.9M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = n
        right = n
        res = []
        
        def gen(left, right,p):
            if left == 0 and right == 0:
                res.append(p)
                return
            if left > 0:
                p+="("
                left -= 1
                gen(left,right,p) 
                left+=1
                p = p[:-1]
            if right > 0 and right > left:
                p+=")"
                right -= 1
                gen(left,right,p)
                right+=1
                p = p[:-1]
        
        gen(left,right,"")
        return res
                
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

