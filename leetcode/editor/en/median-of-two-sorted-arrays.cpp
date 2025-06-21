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
        int m = nums1.size(), n = nums2.size();

        int target = (m + n) / 2;
        if(target == 0 && (m== 0 || n == 0)){
            return m == 0 ? double(nums2[0]) : double(nums1[0]);
        }
        if( m < n) return findMedianSortedArrays(nums2,nums1);
        int firstHalf = m / 2;
        while(firstHalf >= 0 && firstHalf <= m){
            int secondHalf = target - firstHalf;
            int maxLeft = firstHalf > 0 ? nums1[firstHalf-1] : INT_MIN;
            int minLeft = firstHalf < m ? nums1[firstHalf] : INT_MAX;
            int maxRight = secondHalf > 0 ? nums2[secondHalf-1]: INT_MIN;
            int minRight = secondHalf < n ? nums2[secondHalf] : INT_MAX;
            if(maxLeft <= minRight && maxRight <= minLeft){
                if((m+n)%2 == 0){
                    return (max(maxLeft,maxRight) + min(minLeft,minRight))/2.0;
                } 
                else{
                    return double(min(minLeft,minRight));
                }
            }
            else if(maxLeft > minRight){
                firstHalf--;
            }
            else{
                firstHalf++;
            }
        }
        return 0.0;
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

