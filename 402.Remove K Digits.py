#
# @lc app=leetcode id=402 lang=python3
# @lcpr version=30003
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (34.33%)
# Likes:    9802
# Dislikes: 512
# Total Accepted:    555.9K
# Total Submissions: 1.6M
# Testcase Example:  '"1432219"\n3'
#
# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.
# 
# 
# Example 1:
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# 
# 
# Example 2:
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
# 
# 
# Example 3:
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= num.length <= 10^5
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        s = []
        i = 0
        for i in range(len(num)):
            while s and k > 0 and s[-1] > num[i]:
                s.pop()
                k-=1
            s.append(num[i])
        while k > 0:
            s.pop()
            k-=1
        res = "".join(s)
        return "0" if sum(int(i) for i in s) == 0 else res.lstrip("0")
        

        
        
# @lc code=end



#
# @lcpr case=start
# "1432219"\n3\n
# @lcpr case=end

# @lcpr case=start
# "10200"\n1\n
# @lcpr case=end

# @lcpr case=start
# "10"\n2\n
# @lcpr case=end

#

