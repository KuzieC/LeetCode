/*
 * @lc app=leetcode id=1696 lang=cpp
 * @lcpr version=20004
 *
 * [1696] Jump Game VI
 *
 * https://leetcode.com/problems/jump-game-vi/description/
 *
 * algorithms
 * Medium (45.79%)
 * Likes:    3460
 * Dislikes: 116
 * Total Accepted:    113.7K
 * Total Submissions: 248.2K
 * Testcase Example:  '[1,-1,-2,4,-7,3]\n2'
 *
 * You are given a 0-indexed integer array nums and an integer k.
 * 
 * You are initially standing at index 0. In one move, you can jump at most k
 * steps forward without going outside the boundaries of the array. That is,
 * you can jump from index i to any index in the range [i + 1, min(n - 1, i +
 * k)] inclusive.
 * 
 * You want to reach the last index of the array (index n - 1). Your score is
 * the sum of all nums[j] for each index j you visited in the array.
 * 
 * Return the maximum score you can get.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,-1,-2,4,-7,3], k = 2
 * Output: 7
 * Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
 * (underlined above). The sum is 7.
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [10,-5,-2,4,0,3], k = 3
 * Output: 17
 * Explanation: You can choose your jumps forming the subsequence [10,4,3]
 * (underlined above). The sum is 17.
 * 
 * 
 * Example 3:
 * 
 * Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
 * Output: 0
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length, k <= 10^5
 * -10^4 <= nums[i] <= 10^4
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
class MonoQueue {
public:
    deque<long long> maxq;
    deque<long long> minq;

    void push(long long s){
        while(!maxq.empty() && maxq.back() < s){
            maxq.pop_back();
        }
        while(!minq.empty() && minq.back() > s){
            minq.pop_back();
        }
        maxq.push_back(s);
        minq.push_back(s);
    }

    void pop(long long s){
        if(maxq.front() == s){
            maxq.pop_front();
        }
        if(minq.front() == s){
            minq.pop_front();
        }
    }

    int min(){
        return minq.front();
    }

    int max(){
        return maxq.front();
    }

    bool empty(){
        return maxq.empty();
    }
};
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        vector<int> dp(nums);

        MonoQueue m;
        int left = 0, right = 1;
        m.push(dp[0]);
        while(right < nums.size()){
            dp[right] = m.max()+dp[right];
            m.push(dp[right++]);
            if(right - left > k){
                m.pop(dp[left++]);
            }
        }
        return dp[nums.size()-1];
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,-1,-2,4,-7,3]\n2\n
// @lcpr case=end

// @lcpr case=start
// [10,-5,-2,4,0,3]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,-5,-20,4,-1,3,-6,-3]\n2\n
// @lcpr case=end

 */

