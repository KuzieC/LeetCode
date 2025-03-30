/*
 * @lc app=leetcode id=1658 lang=cpp
 * @lcpr version=30104
 *
 * [1658] Minimum Operations to Reduce X to Zero
 *
 * https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
 *
 * algorithms
 * Medium (39.96%)
 * Likes:    5561
 * Dislikes: 124
 * Total Accepted:    208.2K
 * Total Submissions: 520.9K
 * Testcase Example:  '[1,1,4,2,3]\n5'
 *
 * You are given an integer array nums and an integer x. In one operation, you
 * can either remove the leftmost or the rightmost element from the array nums
 * and subtract its value from x. Note that this modifies the array for future
 * operations.
 * 
 * Return the minimum number of operations to reduce x to exactly 0 if it is
 * possible, otherwise, return -1.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,1,4,2,3], x = 5
 * Output: 2
 * Explanation: The optimal solution is to remove the last two elements to
 * reduce x to zero.
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [5,6,7,8,9], x = 4
 * Output: -1
 * 
 * 
 * Example 3:
 * 
 * Input: nums = [3,2,20,1,1,3], x = 10
 * Output: 5
 * Explanation: The optimal solution is to remove the last three elements and
 * the first two elements (5 operations in total) to reduce x to zero.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^4
 * 1 <= x <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
public:

    int helper(vector<int>& nums, int left, int right, int x, int count){
        if(x == 0) return count;
        if(left > right || x < 0) return 999999;
        return min(helper(nums,left+1,right,x-nums[left],count+1),
        helper(nums,left,right-1,x-nums[right],count+1));
    }
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size();
        int s = std::accumulate(nums.begin(),nums.end(),0);
        if(s < x) return -1;
        int target = s - x;
        cout<<target<<endl;
        int left = 0, right = 0;
        int sum = 0;
        int res = INT_MAX;
        while(right < n){
            sum += nums[right];
            right++;
            while(sum > target && left < right){
                sum -= nums[left];
                left++;
            }
            if(sum == target){
                res = min(res,n - (right-left));
            }
            
        }
        return res == INT_MAX ? -1 : res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,1,4,2,3]\n5\n
// @lcpr case=end

// @lcpr case=start
// [5,6,7,8,9]\n4\n
// @lcpr case=end

// @lcpr case=start
// [3,2,20,1,1,3]\n10\n
// @lcpr case=end

 */

