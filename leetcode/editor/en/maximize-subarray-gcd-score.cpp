/*
 * @lc app=leetcode id=3574 lang=cpp
 * @lcpr version=30201
 *
 * [3574] Maximize Subarray GCD Score
 *
 * https://leetcode.com/problems/maximize-subarray-gcd-score/description/
 *
 * algorithms
 * Hard (20.74%)
 * Likes:    34
 * Dislikes: 4
 * Total Accepted:    4.3K
 * Total Submissions: 20.7K
 * Testcase Example:  '[2,4]\n1'
 *
 * You are given an array of positive integers nums and an integer k.
 * 
 * You may perform at most k operations. In each operation, you can choose one
 * element in the array and double its value. Each element can be doubled at
 * most once.
 * 
 * The score of a contiguous subarray is defined as the product of its length
 * and the greatest common divisor (GCD) of all its elements.
 * 
 * Your task is to return the maximum score that can be achieved by selecting a
 * contiguous subarray from the modified array.
 * 
 * Note:
 * 
 * 
 * The greatest common divisor (GCD) of an array is the largest integer that
 * evenly divides all the array elements.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [2,4], k = 1
 * 
 * Output: 8
 * 
 * Explanation:
 * 
 * 
 * Double nums[0] to 4 using one operation. The modified array becomes [4,
 * 4].
 * The GCD of the subarray [4, 4] is 4, and the length is 2.
 * Thus, the maximum possible score is 2 × 4 = 8.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [3,5,7], k = 2
 * 
 * Output: 14
 * 
 * Explanation:
 * 
 * 
 * Double nums[2] to 14 using one operation. The modified array becomes [3, 5,
 * 14].
 * The GCD of the subarray [14] is 14, and the length is 1.
 * Thus, the maximum possible score is 1 × 14 = 14.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [5,5,5], k = 1
 * 
 * Output: 15
 * 
 * Explanation:
 * 
 * 
 * The subarray [5, 5, 5] has a GCD of 5, and its length is 3.
 * Since doubling any element doesn't improve the score, the maximum score is 3
 * × 5 = 15.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n == nums.length <= 1500
 * 1 <= nums[i] <= 10^9
 * 1 <= k <= n
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
    long long maxGCDScore(vector<int>& nums, int k) {
        
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// [2,4]\n1\n
// @lcpr case=end

// @lcpr case=start
// [3,5,7]\n2\n
// @lcpr case=end

// @lcpr case=start
// [5,5,5]\n1\n
// @lcpr case=end

 */

