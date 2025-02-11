#
# @lc app=leetcode id=238 lang=python3
# @lcpr version=20001
#
# [238] Product of Array Except Self
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = [ 0 for _ in range(len(nums))]
        postProduct = [ 0 for _ in range(len(nums))]
        preProduct[0] = 1
        for i in range(1,len(nums)):
            preProduct[i] = preProduct[i-1] * nums[i-1]
        
        postProduct[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            postProduct[i] = postProduct[i+1] * nums[i+1]
        
        res = []
        for x,y in zip(preProduct,postProduct):
            res.append(x*y)
        return res
            
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

