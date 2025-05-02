/*
 * @lc app=leetcode id=895 lang=cpp
 * @lcpr version=30200
 *
 * [895] Maximum Frequency Stack
 *
 * https://leetcode.com/problems/maximum-frequency-stack/description/
 *
 * algorithms
 * Hard (66.07%)
 * Likes:    4811
 * Dislikes: 77
 * Total Accepted:    196.1K
 * Total Submissions: 296.9K
 * Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' +
  '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
 *
 * Design a stack-like data structure to push elements to the stack and pop the
 * most frequent element from the stack.
 * 
 * Implement the FreqStack class:
 * 
 * 
 * FreqStack() constructs an empty frequency stack.
 * void push(int val) pushes an integer val onto the top of the stack.
 * int pop() removes and returns the most frequent element in the
 * stack.
 * 
 * If there is a tie for the most frequent element, the element closest to the
 * stack's top is removed and returned.
 * 
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop",
 * "pop", "pop"]
 * [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
 * Output
 * [null, null, null, null, null, null, null, 5, 7, 5, 4]
 * 
 * Explanation
 * FreqStack freqStack = new FreqStack();
 * freqStack.push(5); // The stack is [5]
 * freqStack.push(7); // The stack is [5,7]
 * freqStack.push(5); // The stack is [5,7,5]
 * freqStack.push(7); // The stack is [5,7,5,7]
 * freqStack.push(4); // The stack is [5,7,5,7,4]
 * freqStack.push(5); // The stack is [5,7,5,7,4,5]
 * freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
 * [5,7,5,7,4].
 * freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is
 * closest to the top. The stack becomes [5,7,5,4].
 * freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
 * [5,7,4].
 * freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is
 * closest to the top. The stack becomes [5,7].
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= val <= 10^9
 * At most 2 * 10^4 calls will be made to push and pop.
 * It is guaranteed that there will be at least one element in the stack before
 * calling pop.
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
class FreqStack {
public:
    unordered_map<int,list<int>> mp;
    unordered_map<int,int> freqmp;
    unordered_map<int,list<list<int>::iterator>> itemp;
    int maxFreq;
    list<int> lis;
    FreqStack(): maxFreq(0) {
        
    }
    
    void push(int val) {
        lis.push_back(val);
        freqmp[val]+=1;
        itemp[freqmp[val]].push_back(prev(lis.end()));
        maxFreq = max(freqmp[val],maxFreq);
    }
    
    int pop() {        
        int val = *itemp[maxFreq].back();
        lis.erase(itemp[maxFreq].back());
        itemp[maxFreq].pop_back();
        if(itemp[maxFreq].empty()) maxFreq--;
        freqmp[val]--;
        return val;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



