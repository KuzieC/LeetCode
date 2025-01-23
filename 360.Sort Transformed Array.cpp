/*
 * @lc app=leetcode id=360 lang=cpp
 * @lcpr version=20004
 *
 * [360] Sort Transformed Array
 *
 * https://leetcode.com/problems/sort-transformed-array/description/
 *
 * algorithms
 * Medium (56.55%)
 * Likes:    687
 * Dislikes: 216
 * Total Accepted:    69K
 * Total Submissions: 122K
 * Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
 *
 * Given a sorted integer array nums and three integers a, b and c, apply a
 * quadratic function of the form f(x) = ax^2 + bx + c to each element nums[i]
 * in the array, and return the array in a sorted order.
 * 
 * 
 * Example 1:
 * Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
 * Output: [3,9,15,33]
 * Example 2:
 * Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
 * Output: [-23,-5,1,7]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 200
 * -100 <= nums[i], a, b, c <= 100
 * nums is sorted in ascending order.
 * 
 * 
 * 
 * Follow up: Could you solve it in O(n) time?
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

    int f(int x, int a, int b, int c){
        return a * x * x + b * x + c;
    }
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        int left = 0, right = nums.size() - 1;

        int p = a > 0 ? nums.size()-1 : 0;
        vector<int> res(nums.size(),0);
        while(left <= right){
            int x = f(nums[left],a,b,c);
            int y = f(nums[right],a,b,c);
            if(a > 0){
                if(x > y){
                    res[p--] = x;
                    left++;
                }
                else{
                    res[p--] =y;
                    right--;
                }
            }
            else{
                if(x > y){
                    res[p++] = y;
                    right--;
                }
                else{
                    res[p++] = x;
                    left++;
                }
            }
        }
        return res;
        }
};
// @lc code=end



/*
// @lcpr case=start
// [-4,-2,2,4]\n1\n3\n5\n
// @lcpr case=end

// @lcpr case=start
// [-4,-2,2,4]\n-1\n3\n5\n
// @lcpr case=end

 */

