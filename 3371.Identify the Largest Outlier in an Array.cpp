/*
 * @lc app=leetcode id=3371 lang=cpp
 * @lcpr version=20004
 *
 * [3371] Identify the Largest Outlier in an Array
 *
 * https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/
 *
 * algorithms
 * Medium (29.70%)
 * Likes:    133
 * Dislikes: 19
 * Total Accepted:    25K
 * Total Submissions: 84.2K
 * Testcase Example:  '[2,3,5,10]'
 *
 * You are given an integer array nums. This array contains n elements, where
 * exactly n - 2 elements are special numbers. One of the remaining two
 * elements is the sum of these special numbers, and the other is an outlier.
 * 
 * An outlier is defined as a number that is neither one of the original
 * special numbers nor the element representing the sum of those numbers.
 * 
 * Note that special numbers, the sum element, and the outlier must have
 * distinct indices, but may share the same value.
 * 
 * Return the largest potential outlier in nums.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [2,3,5,10]
 * 
 * Output: 10
 * 
 * Explanation:
 * 
 * The special numbers could be 2 and 3, thus making their sum 5 and the
 * outlier 10.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [-2,-1,-3,-6,4]
 * 
 * Output: 4
 * 
 * Explanation:
 * 
 * The special numbers could be -2, -1, and -3, thus making their sum -6 and
 * the outlier 4.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,1,1,1,1,5,5]
 * 
 * Output: 5
 * 
 * Explanation:
 * 
 * The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and
 * the other 5 as the outlier.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 3 <= nums.length <= 10^5
 * -1000 <= nums[i] <= 1000
 * The input is generated such that at least one potential outlier exists in
 * nums.
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
#include <numeric>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int getLargestOutlier(vector<int>& nums) {
        int sum = 0;
        unordered_map<float,int> mp;
        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]] ++;
            sum += nums[i];
        }
        sort(nums.begin(),nums.end());
        for(int i = nums.size()-1; i > -1; i--){
            float target = (sum - nums[i])/2.0;
            if(nums[i] == target){
                if(mp[target] > 1) return target;
            }
            else{
                if(mp[target]>0) return nums[i];
            }
        }
        return 0;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,3,5,10]\n
// @lcpr case=end

// @lcpr case=start
// [-2,-1,-3,-6,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1,1,5,5]\n
// @lcpr case=end

 */

