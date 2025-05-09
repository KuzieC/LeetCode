/*
 * @lc app=leetcode id=491 lang=cpp
 * @lcpr version=30200
 *
 * [491] Non-decreasing Subsequences
 *
 * https://leetcode.com/problems/non-decreasing-subsequences/description/
 *
 * algorithms
 * Medium (61.54%)
 * Likes:    3733
 * Dislikes: 232
 * Total Accepted:    187.7K
 * Total Submissions: 305.1K
 * Testcase Example:  '[4,6,7,7]'
 *
 * Given an integer array nums, return all the different possible
 * non-decreasing subsequences of the given array with at least two elements.
 * You may return the answer in any order.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [4,6,7,7]
 * Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [4,4,3,2,1]
 * Output: [[4,4]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 15
 * -100 <= nums[i] <= 100
 * 
 * 
 */

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"

using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> res;
    void dfs(vector<int>& nums, int ind, vector<int>& curr){
        unordered_set<int> used;
        for(int i = ind; i < nums.size(); ++i){
            if(used.find(nums[i]) != used.end()) continue;
            if(!curr.empty() && nums[i] < curr.back()) continue;
            used.insert(nums[i]);
            curr.push_back(nums[i]);
            if(curr.size() > 1) res.push_back(curr);
            dfs(nums,i+1,curr);
            curr.pop_back();
        }
    }
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<int> temp;
        dfs(nums,0,temp);
        return res;
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// [4,6,7,7]\n
// @lcpr case=end

// @lcpr case=start
// [4,4,3,2,1]\n
// @lcpr case=end

 */

