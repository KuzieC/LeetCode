#
# @lc app=leetcode id=895 lang=python3
# @lcpr version=30005
#
# [895] Maximum Frequency Stack
#
# https://leetcode.com/problems/maximum-frequency-stack/description/
#
# algorithms
# Hard (66.65%)
# Likes:    4765
# Dislikes: 76
# Total Accepted:    189.8K
# Total Submissions: 284.8K
# Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' +
  '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
#
# Design a stack-like data structure to push elements to the stack and pop the
# most frequent element from the stack.
# 
# Implement the FreqStack class:
# 
# 
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the
# stack.
# 
# If there is a tie for the most frequent element, the element closest to the
# stack's top is removed and returned.
# 
# 
# 
# 
# 
# Example 1:
# 
# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop",
# "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]
# 
# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
# [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is
# closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
# [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is
# closest to the top. The stack becomes [5,7].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= val <= 10^9
# At most 2 * 10^4 calls will be made to push and pop.
# It is guaranteed that there will be at least one element in the stack before
# calling pop.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class FreqStack:

    def __init__(self):
        self.valFreq = {}
        self.FreqVal = {}
        self.FreqVal[1]= []
        return
    def push(self, val: int) -> None:
      print(f"insert {val}")
      if val not in self.valFreq:
        self.valFreq[val] = 1
        self.FreqVal[1].append(val)
      else:
        preFreq = self.valFreq[val]
        if preFreq+1 not in self.FreqVal:
            self.FreqVal[preFreq+1] = []
        self.FreqVal[preFreq+1].append(val)
        self.valFreq[val] = preFreq+1

    def pop(self) -> int:
      maxFreq = max(self.FreqVal)
      val = self.FreqVal[maxFreq].pop()
      if maxFreq > 1:
        self.valFreq[val] = maxFreq-1
      else:
        self.valFreq.pop(val)
      if len(self.FreqVal[maxFreq]) == 0:
        self.FreqVal.pop(maxFreq)
      return val
      
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end



