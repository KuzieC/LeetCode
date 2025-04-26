/*
 * @lc app=leetcode id=155 lang=cpp
 * @lcpr version=30200
 *
 * [155] Min Stack
 *
 * https://leetcode.com/problems/min-stack/description/
 *
 * algorithms
 * Medium (56.15%)
 * Likes:    14982
 * Dislikes: 943
 * Total Accepted:    2.1M
 * Total Submissions: 3.8M
 * Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element in constant time.
 * 
 * Implement the MinStack class:
 * 
 * 
 * MinStack() initializes the stack object.
 * void push(int val) pushes the element val onto the stack.
 * void pop() removes the element on the top of the stack.
 * int top() gets the top element of the stack.
 * int getMin() retrieves the minimum element in the stack.
 * 
 * 
 * You must implement a solution with O(1) time complexity for each
 * function.
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["MinStack","push","push","push","getMin","pop","top","getMin"]
 * [[],[-2],[0],[-3],[],[],[],[]]
 * 
 * Output
 * [null,null,null,null,-3,null,0,-2]
 * 
 * Explanation
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin(); // return -3
 * minStack.pop();
 * minStack.top();    // return 0
 * minStack.getMin(); // return -2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * -2^31 <= val <= 2^31 - 1
 * Methods pop, top and getMin operations will always be called on non-empty
 * stacks.
 * At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
 * 
 * 
 */

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"

using namespace std;

// @lc code=start
class MinStack {
public:
    deque<int> dq;
    deque<int> minq;
    int mi;
    MinStack() {
        mi = INT_MAX;
    }
    
    void push(int val) {
        dq.push_back(val);
        mi = min(val,mi);
        minq.push_back(mi);
    }
    
    void pop() {
        dq.pop_back();
        minq.pop_back();
        if(dq.empty()) mi = INT_MAX;
        else mi = minq.back();
    }
    
    int top() {
        return dq.back();
    }
    
    int getMin() {
        return minq.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



