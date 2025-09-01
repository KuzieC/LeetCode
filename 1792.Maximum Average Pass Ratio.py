

#
# @lc app=leetcode id=1792 lang=python3
# @lcpr version=30202
#
# [1792] Maximum Average Pass Ratio
#

# @lc code=start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        Ratio = 0.0
        q = []
        for p , t in classes:
            heapq.heappush(q, (-((p+1)/(t+1) - (p/t)),p,t))
        
        while extraStudents > 0:
            extraStudents -= 1
            _, p, t = heapq.heappop(q)
            p+=1
            t+=1
            heapq.heappush(q,(-((p+1)/(t+1) - (p/t)),p,t))
        while(q):
            _ , a, b = heapq.heappop(q)
            Ratio += (a/b)
        return Ratio / len(classes)

# @lc code=end



#
# @lcpr case=start
# [[1,2],[3,5],[2,2]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,4],[3,9],[4,5],[2,10]]\n4\n
# @lcpr case=end

#

