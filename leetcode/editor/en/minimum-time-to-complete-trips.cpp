/*
 * @lc app=leetcode id=2187 lang=cpp
 * @lcpr version=30201
 *
 * [2187] Minimum Time to Complete Trips
 *
 * https://leetcode.com/problems/minimum-time-to-complete-trips/description/
 *
 * algorithms
 * Medium (39.05%)
 * Likes:    2953
 * Dislikes: 190
 * Total Accepted:    135.1K
 * Total Submissions: 346K
 * Testcase Example:  '[1,2,3]\n5'
 *
 * You are given an array time where time[i] denotes the time taken by the i^th
 * bus to complete one trip.
 * 
 * Each bus can make multiple trips successively; that is, the next trip can
 * start immediately after completing the current trip. Also, each bus operates
 * independently; that is, the trips of one bus do not influence the trips of
 * any other bus.
 * 
 * You are also given an integer totalTrips, which denotes the number of trips
 * all buses should make in total. Return the minimum time required for all
 * buses to complete at least totalTrips trips.
 * 
 * 
 * Example 1:
 * 
 * Input: time = [1,2,3], totalTrips = 5
 * Output: 3
 * Explanation:
 * - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
 * ⁠ The total number of trips completed is 1 + 0 + 0 = 1.
 * - At time t = 2, the number of trips completed by each bus are [2,1,0]. 
 * ⁠ The total number of trips completed is 2 + 1 + 0 = 3.
 * - At time t = 3, the number of trips completed by each bus are [3,1,1]. 
 * ⁠ The total number of trips completed is 3 + 1 + 1 = 5.
 * So the minimum time needed for all buses to complete at least 5 trips is
 * 3.
 * 
 * 
 * Example 2:
 * 
 * Input: time = [2], totalTrips = 1
 * Output: 2
 * Explanation:
 * There is only one bus, and it will complete its first trip at t = 2.
 * So the minimum time needed to complete 1 trip is 2.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= time.length <= 10^5
 * 1 <= time[i], totalTrips <= 10^7
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
    long long cal(vector<int>& time, long long totalTime){
        long long res = 0;
        for(auto i : time){
            res += totalTime / i;
        }
        return res;
    }
    long long minimumTime(vector<int>& time, int totalTrips) {
        long long trip = 0;
        long long lo = 1, hi = (long long)*min_element(time.begin(),time.end()) * totalTrips;
        while(lo < hi){
            long long res = lo + (hi - lo) / 2;
            trip = cal(time,res);
            if(trip == totalTrips){
                hi = res;
            }
            else if(trip > totalTrips){
                hi = res;
            }
            else{
                lo = res + 1;
            }
        }
        return lo;
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// [1,2,3]\n5\n
// @lcpr case=end

// @lcpr case=start
// [2]\n1\n
// @lcpr case=end

 */

