/*
 * @lc app=leetcode id=1438 lang=cpp
 * @lcpr version=20004
 *
 * [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
 *
 * https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
 *
 * algorithms
 * Medium (56.65%)
 * Likes:    4179
 * Dislikes: 199
 * Total Accepted:    249.7K
 * Total Submissions: 440.7K
 * Testcase Example:  '[8,2,4,7]\n4'
 *
 * Given an array of integers nums and an integer limit, return the size of the
 * longest non-empty subarray such that the absolute difference between any two
 * elements of this subarray is less than or equal to limit.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [8,2,4,7], limit = 4
 * Output: 2 
 * Explanation: All subarrays are: 
 * [8] with maximum absolute diff |8-8| = 0 <= 4.
 * [8,2] with maximum absolute diff |8-2| = 6 > 4. 
 * [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
 * [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
 * [2] with maximum absolute diff |2-2| = 0 <= 4.
 * [2,4] with maximum absolute diff |2-4| = 2 <= 4.
 * [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
 * [4] with maximum absolute diff |4-4| = 0 <= 4.
 * [4,7] with maximum absolute diff |4-7| = 3 <= 4.
 * [7] with maximum absolute diff |7-7| = 0 <= 4. 
 * Therefore, the size of the longest subarray is 2.
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [10,1,2,4,7,2], limit = 5
 * Output: 4 
 * Explanation: The subarray [2,4,7,2] is the longest since the maximum
 * absolute diff is |2-7| = 5 <= 5.
 * 
 * 
 * Example 3:
 * 
 * Input: nums = [4,2,2,2,4,4,2,2], limit = 0
 * Output: 3
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * 0 <= limit <= 10^9
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
class Mqueue{
public:
    deque<int> maxq,minq;

    void push(int s){
        while(!maxq.empty() && maxq.back() < s) maxq.pop_back();
        while(!minq.empty() && minq.back() > s) minq.pop_back();
        maxq.push_back(s);
        minq.push_back(s);
    }

    int max(){
        return maxq.front();
    } 

    int min(){
        return minq.front();
    }  

    void pop(int s){
        if(maxq.front() == s) maxq.pop_front();
        if(minq.front() == s) minq.pop_front();
    }
};
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int left  = 0, right = 0, siz = 0, diff = 0, res = 0;
        Mqueue q;
        while(right < nums.size()){
            q.push(nums[right++]);
            siz++;
            //cout<<"p"<<endl;
            diff = q.max() - q.min();
            //cout<<diff<<endl;
            while(diff > limit){
                q.pop(nums[left++]);
                siz--;
                //cout<<"s"<<siz<<endl;
                //cout<<"pop"<<endl;
                diff = q.max() - q.min();
            }
            res = max(res,siz);
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [8,2,4,7]\n4\n
// @lcpr case=end

// @lcpr case=start
// [10,1,2,4,7,2]\n5\n
// @lcpr case=end

// @lcpr case=start
// [4,2,2,2,4,4,2,2]\n0\n
// @lcpr case=end

 */

