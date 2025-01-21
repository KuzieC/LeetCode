/*
 * @lc app=leetcode id=346 lang=cpp
 * @lcpr version=20004
 *
 * [346] Moving Average from Data Stream
 *
 * https://leetcode.com/problems/moving-average-from-data-stream/description/
 *
 * algorithms
 * Easy (79.39%)
 * Likes:    1696
 * Dislikes: 183
 * Total Accepted:    446.8K
 * Total Submissions: 562.8K
 * Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
 *
 * Given a stream of integers and a window size, calculate the moving average
 * of all integers in the sliding window.
 * 
 * Implement the MovingAverage class:
 * 
 * 
 * MovingAverage(int size) Initializes the object with the size of the window
 * size.
 * double next(int val) Returns the moving average of the last size values of
 * the stream.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["MovingAverage", "next", "next", "next", "next"]
 * [[3], [1], [10], [3], [5]]
 * Output
 * [null, 1.0, 5.5, 4.66667, 6.0]
 * 
 * Explanation
 * MovingAverage movingAverage = new MovingAverage(3);
 * movingAverage.next(1); // return 1.0 = 1 / 1
 * movingAverage.next(10); // return 5.5 = (1 + 10) / 2
 * movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
 * movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= size <= 1000
 * -10^5 <= val <= 10^5
 * At most 10^4 calls will be made to next.
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
class MovingAverage {
public:
    int siz;
    queue<int> q;
    int sum;
    MovingAverage(int size) {
        siz = size;
        sum = 0;
    }
    
    double next(int val) {
        q.push(val);
        sum += val;
        while(q.size() > siz){
            sum -= q.front();
            q.pop();
        }
        return sum / (double)q.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
// @lc code=end



