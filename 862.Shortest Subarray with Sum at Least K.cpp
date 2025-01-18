/*
 * @lc app=leetcode id=862 lang=cpp
 * @lcpr version=20004
 *
 * [862] Shortest Subarray with Sum at Least K
 *
 * https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
 *
 * algorithms
 * Hard (32.17%)
 * Likes:    4970
 * Dislikes: 137
 * Total Accepted:    181.6K
 * Total Submissions: 564.6K
 * Testcase Example:  '[1]\n1'
 *
 * Given an integer array nums and an integer k, return the length of the
 * shortest non-empty subarray of nums with a sum of at least k. If there is no
 * such subarray, return -1.
 * 
 * A subarray is a contiguous part of an array.
 * 
 * 
 * Example 1:
 * Input: nums = [1], k = 1
 * Output: 1
 * Example 2:
 * Input: nums = [1,2], k = 4
 * Output: -1
 * Example 3:
 * Input: nums = [2,-1,2], k = 3
 * Output: 3
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * -10^5 <= nums[i] <= 10^5
 * 1 <= k <= 10^9
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
class MQueue {
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

    long long min(){
        return minq.front();
    }

    bool empty(){
        return maxq.empty();
    }
};
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int sum = 0, left = 0, right = 0, siz = 0, res = INT_MAX;

        vector<long long> presum (nums.size()+1,0);

        for(int i = 0; i < nums.size(); i++){
            presum[i+1] = presum[i] + nums[i]; 
        }
        MQueue mq;
        while(right < presum.size()){
            mq.push(presum[right]);
            right++;
            while(right < presum.size() && !mq.empty() && mq.min() <= presum[right] - k){
                res = min(res, right - left);
                mq.pop(presum[left]);
                left++;
            }
            
        }
        return res == INT_MAX ? -1 : res ;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n4\n
// @lcpr case=end

// @lcpr case=start
// [2,-1,2]\n3\n
// @lcpr case=end

 */

