/*
 * @lc app=leetcode id=1429 lang=cpp
 * @lcpr version=20004
 *
 * [1429] First Unique Number
 *
 * https://leetcode.com/problems/first-unique-number/description/
 *
 * algorithms
 * Medium (55.00%)
 * Likes:    585
 * Dislikes: 33
 * Total Accepted:    94.5K
 * Total Submissions: 171.9K
 * Testcase Example:  '["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]\n' +
  '[[[2,3,5]],[],[5],[],[2],[],[3],[]]'
 *
 * You have a queue of integers, you need to retrieve the first unique integer
 * in the queue.
 * 
 * Implement the FirstUnique class:
 * 
 * 
 * FirstUnique(int[] nums) Initializes the object with the numbers in the
 * queue.
 * int showFirstUnique() returns the value of the first unique integer of the
 * queue, and returns -1 if there is no such integer.
 * void add(int value) insert value to the queue.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: 
 * 
 * ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
 * [[[2,3,5]],[],[5],[],[2],[],[3],[]]
 * Output: 
 * [null,2,null,2,null,3,null,-1]
 * Explanation: 
 * FirstUnique firstUnique = new FirstUnique([2,3,5]);
 * firstUnique.showFirstUnique(); // return 2
 * firstUnique.add(5);            // the queue is now [2,3,5,5]
 * firstUnique.showFirstUnique(); // return 2
 * firstUnique.add(2);            // the queue is now [2,3,5,5,2]
 * firstUnique.showFirstUnique(); // return 3
 * firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
 * firstUnique.showFirstUnique(); // return -1
 * 
 * 
 * Example 2:
 * 
 * Input: 
 * 
 * ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
 * [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
 * Output: 
 * [null,-1,null,null,null,null,null,17]
 * Explanation: 
 * FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
 * firstUnique.showFirstUnique(); // return -1
 * firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
 * firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
 * firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
 * firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
 * firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
 * firstUnique.showFirstUnique(); // return 17
 * 
 * 
 * Example 3:
 * 
 * Input: 
 * ["FirstUnique","showFirstUnique","add","showFirstUnique"]
 * [[[809]],[],[809],[]]
 * Output: 
 * [null,809,null,-1]
 * Explanation: 
 * FirstUnique firstUnique = new FirstUnique([809]);
 * firstUnique.showFirstUnique(); // return 809
 * firstUnique.add(809);          // the queue is now [809,809]
 * firstUnique.showFirstUnique(); // return -1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^8
 * 1 <= value <= 10^8
 * At most 50000 calls will be made to showFirstUnique and add.
 * 
 * 
 */


// @lcpr-template-start
using namespace std;
#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
// @lcpr-template-end
// @lc code=start
class FirstUnique {
public:
    queue<int> q;
    unordered_map<int,int> mp;
    FirstUnique(vector<int>& nums) {
        for(auto i : nums){
            q.push(i);
            mp[i]++;
        }
    }
    
    int showFirstUnique() {
        while(!q.empty()){
            auto temp = q.front();
            if(mp[temp] != 1) q.pop();
            else return temp;
        }
        return -1;
    }
    
    void add(int value) {
        q.push(value);
        mp[value]++;
    }
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */
// @lc code=end



/*
// @lcpr case=start
// ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"][[[2,3,5]],[],[5],[],[2],[],[3],[]]\n
// @lcpr case=end

// @lcpr case=start
// ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"][[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]\n
// @lcpr case=end

// @lcpr case=start
// ["FirstUnique","showFirstUnique","add","showFirstUnique"][[[809]],[],[809],[]]\n
// @lcpr case=end

 */

