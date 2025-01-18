/*
 * @lc app=leetcode id=1425 lang=cpp
 * @lcpr version=20004
 *
 * [1425] Constrained Subsequence Sum
 *
 * https://leetcode.com/problems/constrained-subsequence-sum/description/
 *
 * algorithms
 * Hard (56.46%)
 * Likes:    2160
 * Dislikes: 104
 * Total Accepted:    82.2K
 * Total Submissions: 145.5K
 * Testcase Example:  '[10,2,-10,5,20]\n2'
 *
 * Given an integer array nums and an integer k, return the maximum sum of a
 * non-empty subsequence of that array such that for every two consecutive
 * integers in the subsequence, nums[i] and nums[j], where i < j, the condition
 * j - i <= k is satisfied.
 * 
 * A subsequence of an array is obtained by deleting some number of elements
 * (can be zero) from the array, leaving the remaining elements in their
 * original order.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [10,2,-10,5,20], k = 2
 * Output: 37
 * Explanation: The subsequence is [10, 2, 5, 20].
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [-1,-2,-3], k = 1
 * Output: -1
 * Explanation: The subsequence must be non-empty, so we choose the largest
 * number.
 * 
 * 
 * Example 3:
 * 
 * Input: nums = [10,-2,-10,-5,20], k = 2
 * Output: 23
 * Explanation: The subsequence is [10, -2, -5, 20].
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= k <= nums.length <= 10^5
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

    long long min(){
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
    int constrainedSubsetSum(vector<int>& nums, int k) {
        vector<int> dp(nums.size(),0);
        dp[0] = nums[0];
        int res = dp[0];
        int left = 0, right = 0;
        MonoQueue m;
        while(right < nums.size()){
            dp[right] = max(nums[right],m.max()+nums[right]);
            res = max(res,dp[right]);
            m.push(dp[right++]);
            if(right - left > k){
                m.pop(dp[left++]);
            }
        }
        return res;

    }
};
// @lc code=end



/*
// @lcpr case=start
// [10,2,-10,5,20]\n2\n
// @lcpr case=end

// @lcpr case=start
// [-1,-2,-3]\n1\n
// @lcpr case=end

// @lcpr case=start
// [10,-2,-10,-5,20]\n2\n
// @lcpr case=end

 */

