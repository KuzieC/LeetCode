/*
 * @lc app=leetcode id=918 lang=cpp
 * @lcpr version=20004
 *
 * [918] Maximum Sum Circular Subarray
 *
 * https://leetcode.com/problems/maximum-sum-circular-subarray/description/
 *
 * algorithms
 * Medium (46.52%)
 * Likes:    6822
 * Dislikes: 315
 * Total Accepted:    308.7K
 * Total Submissions: 663.7K
 * Testcase Example:  '[1,-2,3,-2]'
 *
 * Given a circular integer array nums of length n, return the maximum possible
 * sum of a non-empty subarray of nums.
 * 
 * A circular array means the end of the array connects to the beginning of the
 * array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the
 * previous element of nums[i] is nums[(i - 1 + n) % n].
 * 
 * A subarray may only include each element of the fixed buffer nums at most
 * once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there
 * does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,-2,3,-2]
 * Output: 3
 * Explanation: Subarray [3] has maximum sum 3.
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [5,-3,5]
 * Output: 10
 * Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
 * 
 * 
 * Example 3:
 * 
 * Input: nums = [-3,-2,-3]
 * Output: -2
 * Explanation: Subarray [-2] has maximum sum -2.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == nums.length
 * 1 <= n <= 3 * 10^4
 * -3 * 10^4 <= nums[i] <= 3 * 10^4
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

    bool empty(){
        return maxq.empty();
    }
};
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n = nums.size();
        nums.insert(nums.end(), nums.begin(), nums.end());
        vector<long long> sum(n * 2 + 1, 0);
        for(int i = 1; i <= n * 2; i++){
            sum[i] = sum[i - 1] + nums[i - 1];
        }

        MonoQueue mq;
        mq.push(sum[0]);
        int left = 0, right = 1, res = INT_MIN;
        while(right < sum.size()){
            res = max(static_cast<long long>(res), sum[right] - mq.min());
            mq.push(sum[right]);
            right++;
            if(right - left > n){
                mq.pop(sum[left]);
                left++;
            }
            
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,-2,3,-2]\n
// @lcpr case=end

// @lcpr case=start
// [5,-3,5]\n
// @lcpr case=end

// @lcpr case=start
// [-3,-2,-3]\n
// @lcpr case=end

 */

