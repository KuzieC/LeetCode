/*
 * @lc app=leetcode id=1109 lang=cpp
 * @lcpr version=30104
 *
 * [1109] Corporate Flight Bookings
 *
 * https://leetcode.com/problems/corporate-flight-bookings/description/
 *
 * algorithms
 * Medium (63.71%)
 * Likes:    1752
 * Dislikes: 164
 * Total Accepted:    78.9K
 * Total Submissions: 123.9K
 * Testcase Example:  '[[1,2,10],[2,3,20],[2,5,25]]\n5'
 *
 * There are n flights that are labeled from 1 to n.
 * 
 * You are given an array of flight bookings bookings, where bookings[i] =
 * [firsti, lasti, seatsi] represents a booking for flights firsti through
 * lasti (inclusive) with seatsi seats reserved for each flight in the range.
 * 
 * Return an array answer of length n, where answer[i] is the total number of
 * seats reserved for flight i.
 * 
 * 
 * Example 1:
 * 
 * Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
 * Output: [10,55,45,25,25]
 * Explanation:
 * Flight labels:        1   2   3   4   5
 * Booking 1 reserved:  10  10
 * Booking 2 reserved:      20  20
 * Booking 3 reserved:      25  25  25  25
 * Total seats:         10  55  45  25  25
 * Hence, answer = [10,55,45,25,25]
 * 
 * 
 * Example 2:
 * 
 * Input: bookings = [[1,2,10],[2,2,15]], n = 2
 * Output: [10,25]
 * Explanation:
 * Flight labels:        1   2
 * Booking 1 reserved:  10  10
 * Booking 2 reserved:      15
 * Total seats:         10  25
 * Hence, answer = [10,25]
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 2 * 10^4
 * 1 <= bookings.length <= 2 * 10^4
 * bookings[i].length == 3
 * 1 <= firsti <= lasti <= n
 * 1 <= seatsi <= 10^4
 * 
 * 
 */

// @lc code=start
#include <vector>
class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> s(n+1,0);
        for(auto entry : bookings){
            s[entry[0]-1] += entry[2];
            s[entry[1]] -= entry[2];
        }
        int curr = 0;
        vector<int> res;

        for(size_t i = 0; i < s.size() - 1; i++){
            curr += s[i];
            res.push_back(curr);
        }
        return res;

    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2,10],[2,3,20],[2,5,25]]\n5\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,10],[2,2,15]]\n2\n
// @lcpr case=end

 */

