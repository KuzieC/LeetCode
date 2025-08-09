#
# @lc app=leetcode id=3479 lang=python3
# @lcpr version=30202
#
# [3479] Fruits Into Baskets III
#
# https://leetcode.com/problems/fruits-into-baskets-iii/description/
#
# algorithms
# Medium (38.88%)
# Likes:    527
# Dislikes: 78
# Total Accepted:    77.8K
# Total Submissions: 200K
# Testcase Example:  '[4,2,5]\n[3,5,4]'
#
# You are given two arrays of integers, fruits and baskets, each of length n,
# where fruits[i] represents the quantity of the i^th type of fruit, and
# baskets[j] represents the capacity of the j^th basket.
# 
# From left to right, place the fruits according to these rules:
# 
# 
# Each fruit type must be placed in the leftmost available basket with a
# capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# 
# 
# Return the number of fruit types that remain unplaced after all possible
# allocations are made.
# 
# 
# Example 1:
# 
# 
# Input: fruits = [4,2,5], baskets = [3,5,4]
# 
# Output: 1
# 
# Explanation:
# 
# 
# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# 
# 
# Since one fruit type remains unplaced, we return 1.
# 
# 
# Example 2:
# 
# 
# Input: fruits = [3,6,1], baskets = [6,4,7]
# 
# Output: 0
# 
# Explanation:
# 
# 
# fruits[0] = 3 is placed in baskets[0] = 6.
# fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but
# can be placed in the next available basket, baskets[2] = 7.
# fruits[2] = 1 is placed in baskets[1] = 4.
# 
# 
# Since all fruits are successfully placed, we return 0.
# 
# 
# 
# Constraints:
# 
# 
# n == fruits.length == baskets.length
# 1 <= n <= 10^5
# 1 <= fruits[i], baskets[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, baskets , fruits) -> int:
        count = 0
        n = len(baskets)
        leafSize = 1
        while leafSize < n:
            leafSize = leafSize * 2
        
        segTree = [-1] * (2 * leafSize)
        left, right = 0, n-1
        def buildTree(l,r,ind):
            if l == r:
                segTree[ind] = fruits[l]
                return
            mid = l + (r-l)//2
            buildTree(l,mid,2*ind)
            buildTree(mid+1,r,2*ind+1)
            segTree[ind] = max(segTree[ind*2],segTree[ind*2+1])
            return 
        buildTree(left,right,1)
        def findFruit(ind,f,l,r):
            if segTree[ind] < f:
                return -1
            if l == r:
                #print("fount {}".format(f))
                segTree[ind] = -1
                return 1

            mid = (r + l)//2
            ret = findFruit(2*ind,f,l,mid)
            #print("from {} look left, got {}".format(ind,ret))
            if ret == -1:
                ret = findFruit(2*ind+1,f,mid+1,r)
                #print("from {} look right, got {}".format(ind,ret))

            if ret:
                segTree[ind] = max(segTree[2*ind],segTree[2*ind+1])
            #print(l,r,ind,f,ret)
            return ret    
        
        for fruit in baskets:
            if findFruit(1,fruit,0,n-1) == 1:
                count+=1
        
        return len(fruits) - count
            
# @lc code=end



#
# @lcpr case=start
# [4,2,5]\n[3,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,6,1]\n[6,4,7]\n
# @lcpr case=end

#

