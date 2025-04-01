/*
 * @lc app=leetcode id=303 lang=cpp
 * @lcpr version=30104
 *
 * [303] Range Sum Query - Immutable
 *
 * https://leetcode.com/problems/range-sum-query-immutable/description/
 *
 * algorithms
 * Easy (67.58%)
 * Likes:    3446
 * Dislikes: 1954
 * Total Accepted:    677.9K
 * Total Submissions: 1M
 * Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
  '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
 *
 * Given an integer array nums, handle multiple queries of the following
 * type:
 * 
 * 
 * Calculate the sum of the elements of nums between indices left and right
 * inclusive where left <= right.
 * 
 * 
 * Implement the NumArray class:
 * 
 * 
 * NumArray(int[] nums) Initializes the object with the integer array nums.
 * int sumRange(int left, int right) Returns the sum of the elements of nums
 * between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
 * ... + nums[right]).
 * 
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["NumArray", "sumRange", "sumRange", "sumRange"]
 * [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
 * Output
 * [null, 1, -1, -3]
 * 
 * Explanation
 * NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
 * numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
 * numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
 * numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^4
 * -10^5 <= nums[i] <= 10^5
 * 0 <= left <= right < nums.length
 * At most 10^4 calls will be made to sumRange.
 * 
 * 
 */

// @lc code=start
class NumArray {
public:
    vector<int> pre;
    NumArray(vector<int>& nums) {
        int cur = 0;
        for(int i : nums){
            pre.push_back(cur);
            cur+= i;            
        }
        pre.push_back(cur);
    }
    
    int sumRange(int left, int right) {
        return pre[right+1] - pre[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
// @lc code=end



