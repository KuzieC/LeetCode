#
# @lc app=leetcode id=2106 lang=python3
# @lcpr version=30202
#
# [2106] Maximum Fruits Harvested After at Most K k
#
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-k/description/
#
# algorithms
# Hard (61.46%)
# Likes:    945
# Dislikes: 42
# Total Accepted:    79.1K
# Total Submissions: 128.7K
# Testcase Example:  '[[2,8],[6,3],[8,6]]\n5\n4'
#
# Fruits are available at some positions on an infinite x-axis. You are given a
# 2D integer array fruits where fruits[i] = [positioni, amounti] depicts
# amounti fruits at the position positioni. fruits is already sorted by
# positioni in ascending order, and each positioni is unique.
# 
# You are also given a#printn integer startPos and an integer k. Initially, you are
# at the position startPos. From any position, you can either walk to the left
# or right. It takes one step to move one unit on the x-axis, and you can walk
# at most k k in total. For every position you reach, you harvest all the
# fruits at that position, and the fruits will disappear from that position.
# 
# Return the maximum total number of fruits you can harvest.
# 
# 
# Example 1:
# 
# Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
# Output: 9
# Explanation: 
# The optimal way is to:
# - Move right to position 6 and harvest 3 fruits
# - Move right to position 8 and harvest 6 fruits
# You moved 3 k and harvested 3 + 6 = 9 fruits in total.
# 
# 
# Example 2:
# 
# Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
# Output: 14
# Explanation: 
# You can move at most k = 4 k, so you cannot reach position 0 nor 10.
# The optimal way is to:
# - Harvest the 7 fruits at the starting position 5
# - Move left to position 4 and harvest 1 fruit
# - Move right to position 6 and harvest 2 fruits
# - Move right to position 7 and harvest 4 fruits
# You moved 1 + 3 = 4 k and harvested 7 + 1 + 2 + 4 = 14 fruits in total.
# 
# 
# Example 3:
# 
# Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
# Output: 0
# Explanation:
# You can move at most k = 2 k and cannot reach any position with
# fruits.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= fruits.length <= 10^5
# fruits[i].length == 2
# 0 <= startPos, positioni <= 2 * 10^5
# positioni-1 < positioni for any i > 0 (0-indexed)
# 1 <= amounti <= 10^4
# 0 <= k <= 2 * 10^5
# 
# 
#

# @lc code=start
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        preL = {}
        preR = {}
        left = bisect.bisect_left(fruits,[startPos,-inf])
        right = bisect.bisect_right(fruits,[startPos,inf])
        if left == right:
            if left != 0 :
                left -= 1
        else:
            right -= 1
        sumleft = 0
        sumright = 0
        while len(fruits) > left >= 0 and 0 <= startPos-fruits[left][0] <= k:
            sumleft += fruits[left][1]
            preL[startPos-fruits[left][0]] = sumleft
            left-=1
        while 0 <= right < len(fruits) and 0 <= fruits[right][0]-startPos <= k:
            sumright += fruits[right][1]
            preR[fruits[right][0]-startPos] = sumright
            right+=1
        preL= SortedDict(preL)
        preR = SortedDict(preR)
        print(preL,preR)
        res = 0
        curr = 0
        for dis, sum in preL.items():
            if k - dis >= 0:
                curr = sum
                if (k - dis*2) > 0:
                    pos = preR.bisect_right(k-dis*2) - 1
                    if pos >= 0:
                        curr += preR.peekitem(pos)[1]
                        if 0 in preR:
                            curr -= preR[0]
                res = max(res,curr)
            else:
                break
        curr = 0
        for dis, sum in preR.items():
            if k-dis >= 0:
                curr = sum 
                if (k - dis*2) > 0:
                    pos = preL.bisect_right(k-dis*2)-1
                    if pos >= 0:
                        curr += preL.peekitem(pos)[1]
                        if 0 in preL:
                            curr -= preL[0]
                res = max(res,curr)
            else:
                break
        return res
                        

# @lc code=end



#
# @lcpr case=start
# [[2,8],[6,3],[8,6]]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [[0,3],[6,4],[8,5]]\n3\n2\n
# @lcpr case=end

#

