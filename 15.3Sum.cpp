/*
 * @lc app=leetcode id=15 lang=cpp
 * @lcpr version=20004
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (36.05%)
 * Likes:    31994
 * Dislikes: 3001
 * Total Accepted:    4.3M
 * Total Submissions: 11.8M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an integer array nums, return all the triplets [nums[i], nums[j],
 * nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
 * nums[k] == 0.
 * 
 * Notice that the solution set must not contain duplicate triplets.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 * Explanation: 
 * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
 * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
 * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
 * The distinct triplets are [-1,0,1] and [-1,-1,2].
 * Notice that the order of the output and the order of the triplets does not
 * matter.
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [0,1,1]
 * Output: []
 * Explanation: The only possible triplet does not sum up to 0.
 * 
 * 
 * Example 3:
 * 
 * Input: nums = [0,0,0]
 * Output: [[0,0,0]]
 * Explanation: The only possible triplet sums up to 0.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 3 <= nums.length <= 3000
 * -10^5 <= nums[i] <= 10^5
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
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end()); 
        for(int i = 0; i < nums.size();i++){
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int target = -nums[i]; 
            auto r = twoSum(nums,i+1,target);
            for(auto j : r){
                res.push_back({nums[i],j[0],j[1]});
            }
        }
        return res;
    }

    vector<vector<int>> twoSum(vector<int>& nums,int ind,int target){
        unordered_map<int,int> mp;
        vector<vector<int>> res;
        for(int i = ind; i < nums.size();i++){
            if(mp.find(target - nums[i]) != mp.end()){
                res.push_back({nums[i],target-nums[i]});
                while(i+1 < nums.size() && nums[i] == nums[i+1]) i++;
            }
            mp[nums[i]]++;
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [-1,0,1,2,-1,-4]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [0,0,0]\n
// @lcpr case=end

 */

