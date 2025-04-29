 /*
 * @lc app=leetcode id=1670 lang=cpp
 * @lcpr version=30200
 *
 * [1670] Design Front Middle Back Queue
 *
 * https://leetcode.com/problems/design-front-middle-back-queue/description/
 *
 * algorithms
 * Medium (56.20%)
 * Likes:    785
 * Dislikes: 109
 * Total Accepted:    34.8K
 * Total Submissions: 61.9K
 * Testcase Example:  '["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]\n' +
  '[[],[1],[2],[3],[4],[],[],[],[],[]]'
 *
 * Design a queue that supports push and pop operations in the front, middle,
 * and back.
 * 
 * Implement the FrontMiddleBack class:
 * 
 * 
 * FrontMiddleBack() Initializes the queue.
 * void pushFront(int val) Adds val to the front of the queue.
 * void pushMiddle(int val) Adds val to the middle of the queue.
 * void pushBack(int val) Adds val to the back of the queue.
 * int popFront() Removes the front element of the queue and returns it. If the
 * queue is empty, return -1.
 * int popMiddle() Removes the middle element of the queue and returns it. If
 * the queue is empty, return -1.
 * int popBack() Removes the back element of the queue and returns it. If the
 * queue is empty, return -1.
 * 
 * 
 * Notice that when there are two middle position choices, the operation is
 * performed on the frontmost middle position choice. For example:
 * 
 * 
 * Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4,
 * 5].
 * Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2,
 * 4, 5, 6].
 * 
 * 
 * 
 * Example 1:
 * 
 * Input:
 * ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle",
 * "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
 * [[], [1], [2], [3], [4], [], [], [], [], []]
 * Output:
 * [null, null, null, null, null, 1, 3, 4, 2, -1]
 * 
 * Explanation:
 * FrontMiddleBackQueue q = new FrontMiddleBackQueue();
 * q.pushFront(1);   // [1]
 * q.pushBack(2);    // [1, 2]
 * q.pushMiddle(3);  // [1, 3, 2]
 * q.pushMiddle(4);  // [1, 4, 3, 2]
 * q.popFront();     // return 1 -> [4, 3, 2]
 * q.popMiddle();    // return 3 -> [4, 2]
 * q.popMiddle();    // return 4 -> [2]
 * q.popBack();      // return 2 -> []
 * q.popFront();     // return -1 -> [] (The queue is empty)
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= val <= 10^9
 * At most 1000 calls will be made to pushFront, pushMiddle, pushBack,
 * popFront, popMiddle, and popBack.
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
class FrontMiddleBackQueue {
public:
    deque<int> left;
    deque<int> right;
    FrontMiddleBackQueue() {
        
    }
    
    void referesh(){
        if(left.size() > right.size()){
            int temp = left.back();
            left.pop_back();
            right.push_front(temp);    
        }
        else if( right.size() > left.size()+1){
            int temp = right.front();
            right.pop_front();
            left.push_back(temp);
        }
    }

    void pushFront(int val) {
        left.push_front(val);
        referesh();
    }
    
    void pushMiddle(int val) {
        if(left.size() == right.size()){
            right.push_front(val);
        }
        else{
            left.push_back(val);
        }
        referesh();
    }
    
    void pushBack(int val) {
        right.push_back(val);
        referesh();
    }
    
    int popFront() {
        if(left.empty() && right.empty()) return -1;
        int t = -1;
        if(!left.empty()){
            t = left.front();
            left.pop_front();
        }
        else{
            t = right.front();
            right.pop_front();
        }
        referesh();
        return t;
    }
    
    int popMiddle() {
        if(left.empty() && right.empty()) return -1;
        int t = -1;
        if(left.size() == right.size()){
            t = left.back();
            left.pop_back();
        }
        else{
            t = right.front();
            right.pop_front();
        }
        referesh();
        return t;
    }
    
    int popBack() {
        if(left.empty() && right.empty()) return -1;
        int t = -1;
        if(!right.empty()){
            t = right.back();
            right.pop_back();
        }
        else{
            t = left.back();
            left.pop_back();
        }
        referesh();
        return t;
    }
};

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = new FrontMiddleBackQueue();
 * obj->pushFront(val);
 * obj->pushMiddle(val);
 * obj->pushBack(val);
 * int param_4 = obj->popFront();
 * int param_5 = obj->popMiddle();
 * int param_6 = obj->popBack();
 */
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle",\n"popBack", "popFront"]\n[[], [1], [2], [3], [4], [], [], [], [], []]\n
// @lcpr case=end

 */

