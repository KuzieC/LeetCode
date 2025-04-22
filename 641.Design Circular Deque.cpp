/*
 * @lc app=leetcode id=641 lang=cpp
 * @lcpr version=30104
 *
 * [641] Design Circular Deque
 *
 * https://leetcode.com/problems/design-circular-deque/description/
 *
 * algorithms
 * Medium (64.56%)
 * Likes:    1612
 * Dislikes: 102
 * Total Accepted:    172.9K
 * Total Submissions: 267.8K
 * Testcase Example:  '["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n' +
  '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
 *
 * Design your implementation of the circular double-ended queue (deque).
 * 
 * Implement the MyCircularDeque class:
 * 
 * 
 * MyCircularDeque(int k) Initializes the deque with a maximum size of k.
 * boolean insertFront() Adds an item at the front of Deque. Returns true if
 * the operation is successful, or false otherwise.
 * boolean insertLast() Adds an item at the rear of Deque. Returns true if the
 * operation is successful, or false otherwise.
 * boolean deleteFront() Deletes an item from the front of Deque. Returns true
 * if the operation is successful, or false otherwise.
 * boolean deleteLast() Deletes an item from the rear of Deque. Returns true if
 * the operation is successful, or false otherwise.
 * int getFront() Returns the front item from the Deque. Returns -1 if the
 * deque is empty.
 * int getRear() Returns the last item from Deque. Returns -1 if the deque is
 * empty.
 * boolean isEmpty() Returns true if the deque is empty, or false
 * otherwise.
 * boolean isFull() Returns true if the deque is full, or false otherwise.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["MyCircularDeque", "insertLast", "insertLast", "insertFront",
 * "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
 * [[3], [1], [2], [3], [4], [], [], [], [4], []]
 * Output
 * [null, true, true, true, false, 2, true, true, true, 4]
 * 
 * Explanation
 * MyCircularDeque myCircularDeque = new MyCircularDeque(3);
 * myCircularDeque.insertLast(1);  // return True
 * myCircularDeque.insertLast(2);  // return True
 * myCircularDeque.insertFront(3); // return True
 * myCircularDeque.insertFront(4); // return False, the queue is full.
 * myCircularDeque.getRear();      // return 2
 * myCircularDeque.isFull();       // return True
 * myCircularDeque.deleteLast();   // return True
 * myCircularDeque.insertFront(4); // return True
 * myCircularDeque.getFront();     // return 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= k <= 1000
 * 0 <= value <= 1000
 * At most 2000 calls will be made to insertFront, insertLast, deleteFront,
 * deleteLast, getFront, getRear, isEmpty, isFull.
 * 
 * 
 */

// @lc code=start
class MyCircularDeque {
public:
    deque<int> d;
    int start, end, siz, capacity;
    MyCircularDeque(int k):capacity(k),start(0),end(0),siz(0) {
        d.resize(k);
    }
    
    bool insertFront(int value) {
        if(isFull()) return false;
        start = (start-1+capacity)%capacity;
        d[start] = value;
        siz++;
        return true;
    }
    
    bool insertLast(int value) {
        if(isFull()) return false;
        d[end] = value;
        end = (end+1)%capacity;
        siz++;
        return true;
    }
    
    bool deleteFront() {
        if(isEmpty()) return false;
        start = (start + 1)%capacity;
        siz--;
        return true;
    }
    
    bool deleteLast() {
        if(isEmpty()) return false;
        end = (end - 1 + capacity)%capacity;
        siz--;
        return true;
    }
    
    int getFront() {
        if(isEmpty()) return -1;
        return d[start];
    }
    
    int getRear() {
        if(isEmpty()) return -1;
        return d[(end - 1 + capacity)%capacity];
    }
    
    bool isEmpty() {
        return siz == 0;
    }
    
    bool isFull() {
        return siz == capacity;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
// @lc code=end



