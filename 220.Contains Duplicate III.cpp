/*
 * @lc app=leetcode id=220 lang=cpp
 * @lcpr version=30104
 *
 * [220] Contains Duplicate III
 *
 * https://leetcode.com/problems/contains-duplicate-iii/description/
 *
 * algorithms
 * Hard (23.45%)
 * Likes:    1130
 * Dislikes: 115
 * Total Accepted:    276.9K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,3,1]\n3\n0'
 *
 * You are given an integer array nums and two integers indexDiff and
 * valueDiff.
 * 
 * Find a pair of indices (i, j) such that:
 * 
 * 
 * i != j,
 * abs(i - j) <= indexDiff.
 * abs(nums[i] - nums[j]) <= valueDiff, and
 * 
 * 
 * Return true if such pair exists or false otherwise.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
 * Output: true
 * Explanation: We can choose (i, j) = (0, 3).
 * We satisfy the three conditions:
 * i != j --> 0 != 3
 * abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
 * abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
 * 
 * 
 * Example 2:
 * 
 * Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
 * Output: false
 * Explanation: After trying all the possible pairs (i, j), we cannot satisfy
 * the three conditions, so we return false.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 1 <= indexDiff <= nums.length
 * 0 <= valueDiff <= 10^9
 * 
 * 
 */

// @lc code=start
#include <set>
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        int left = 0, right = 0;
        std::set<int> s;
        while(right < nums.size()){


            auto high = s.lower_bound(nums[right]);
            if(high != s.end() && (abs(*high - nums[right]) <= valueDiff)){
                cout<<"a"<<*high<<nums[right]<<right<<endl;
                return true;
            }
            if(high != s.begin()) {
                auto low = prev(high);
                if(true ){
                    if(abs(nums[right] - *low) <= valueDiff){
                        cout<<"b"<<*low<<right<<endl;
                        return true;
                    }
                }
            }   
            s.insert(nums[right]);
            right++;
            if(right - left >indexDiff){
                s.erase(nums[left]);
                left++;
            }
        }
        return false;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,1]\n3\n0\n
// @lcpr case=end

// @lcpr case=start
// [1,5,9,1,5,9]\n2\n3\n
// @lcpr case=end

 */

