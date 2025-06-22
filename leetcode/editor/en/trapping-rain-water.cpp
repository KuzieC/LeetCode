/*
 * @lc app=leetcode id=42 lang=cpp
 * @lcpr version=30201
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (65.12%)
 * Likes:    34237
 * Dislikes: 605
 * Total Accepted:    2.9M
 * Total Submissions: 4.4M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it can trap after raining.
 * 
 * 
 * Example 1:
 * 
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * Explanation: The above elevation map (black section) is represented by array
 * [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
 * section) are being trapped.
 * 
 * 
 * Example 2:
 * 
 * Input: height = [4,2,0,3,2,5]
 * Output: 9
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
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
    int trap(vector<int>& height) {
        int left = 0, right = height.size()-1;
        int res= 0,curr = 0;
        int leftMax = height[left];
        int rightMax = height[right];
        left++;
        right--;
        while(left <= right){
            if(leftMax <= rightMax){
                curr = height[left];
                if(curr < leftMax){
                    res += leftMax - curr;
                }
                else{
                    leftMax = curr;
                }
                left++;
            }
            else{
                curr = height[right];
                if(curr < rightMax){
                    res += rightMax - curr;
                }
                else{
                    rightMax = curr;
                }
                right--;
            }
        }
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
// [0,1,0,2,1,0,1,3,2,1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [4,2,0,3,2,5]\n
// @lcpr case=end

 */

