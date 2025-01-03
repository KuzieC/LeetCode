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
        
        preArray = [_ for _ in nums]
        postArray = [_ for _ in nums]
        res = [_ for _ in nums]
        for i in range(len(nums)):
            if i == 0:
                preArray[i] = 1
            else:
                preArray[i] = preArray[i-1] * nums[i-1]
        print(preArray)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                postArray[i] = 1
            else:
                postArray[i] = postArray[i+1] * nums[i+1]
        print(postArray)
        for i in range(len(nums)):
            if i == 0:
                res[i] = 1 * postArray[i]
            elif i == len(nums)-1:
                res[i] = 1 * preArray[i]
            else:
                res[i] = preArray[i] * postArray[i]
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

