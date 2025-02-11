#
# @lc app=leetcode id=735 lang=python3
# @lcpr version=30004
#
# [735] Asteroid Collision
#
# https://leetcode.com/problems/asteroid-collision/description/
#
# algorithms
# Medium (45.03%)
# Likes:    8452
# Dislikes: 1187
# Total Accepted:    697.8K
# Total Submissions: 1.5M
# Testcase Example:  '[5,10,-5]'
#
# We are given an array asteroids of integers representing asteroids in a row.
# The indices of the asteriod in the array represent their relative position in
# space.
# 
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# 
# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will
# explode. Two asteroids moving in the same direction will never meet.
# 
# 
# Example 1:
# 
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
# collide.
# 
# 
# Example 2:
# 
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# 
# 
# Example 3:
# 
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
# resulting in 10.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= asteroids.length <= 10^4
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0:
                q.append(asteroids[i])
                i+=1
            else: 
                while q and q[-1] > 0:
                    if q[-1] + asteroids[i] > 0:
                        i+=1
                        break
                    elif q[-1] + asteroids[i] == 0:
                        q.pop()
                        i+=1
                        break
                    else:
                        q.pop()
                if not q and i < len(asteroids):
                    q.append(asteroids[i])
                    i+=1
            
        return q
                
# @lc code=end



#
# @lcpr case=start
# [5,10,-5]\n
# @lcpr case=end

# @lcpr case=start
# [8,-8]\n
# @lcpr case=end

# @lcpr case=start
# [10,2,-5]\n
# @lcpr case=end

#

