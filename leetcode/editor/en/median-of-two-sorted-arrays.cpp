/*
 * @lc app=leetcode id=4 lang=cpp
 * @lcpr version=30201
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (43.83%)
 * Likes:    30199
 * Dislikes: 3393
 * Total Accepted:    3.4M
 * Total Submissions: 7.9M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return
 * the median of the two sorted arrays.
 * 
 * The overall run time complexity should be O(log (m+n)).
 * 
 * 
 * Example 1:
 * 
 * Input: nums1 = [1,3], nums2 = [2]
 * Output: 2.00000
 * Explanation: merged array = [1,2,3] and median is 2.
 * 
 * 
 * Example 2:
 * 
 * Input: nums1 = [1,2], nums2 = [3,4]
 * Output: 2.50000
 * Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
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
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        int x = 0, y = 0;
        int sumSize = nums1.size() + nums2.size();
        while(res.size() < sumSize/2 + 1){
            if(x < nums1.size() && y < nums2.size()){
                if(nums1[x] < nums2[y]){
                    res.push_back(nums1[x++]);
                }
                else{
                    res.push_back(nums2[y++]);
                }
            }
            else if(x < nums1.size()){
                res.push_back(nums1[x++]);
            }
            else if(y < nums2.size()){
                res.push_back(nums2[y++]);
            }
        }
        if(sumSize % 2){
            return res[sumSize/2];
        }
        else{
            return ((res[sumSize/2-1]) + res[sumSize/2]) / 2.0;
        }
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// [1,3]\n[2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n[3,4]\n
// @lcpr case=end

 */

