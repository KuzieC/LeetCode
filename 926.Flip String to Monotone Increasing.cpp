/*
 * @lc app=leetcode id=926 lang=cpp
 * @lcpr version=20004
 *
 * [926] Flip String to Monotone Increasing
 *
 * https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
 *
 * algorithms
 * Medium (61.56%)
 * Likes:    4470
 * Dislikes: 179
 * Total Accepted:    199.2K
 * Total Submissions: 323.6K
 * Testcase Example:  '"00110"'
 *
 * A binary string is monotone increasing if it consists of some number of 0's
 * (possibly none), followed by some number of 1's (also possibly none).
 * 
 * You are given a binary string s. You can flip s[i] changing it from 0 to 1
 * or from 1 to 0.
 * 
 * Return the minimum number of flips to make s monotone increasing.
 * 
 * 
 * Example 1:
 * 
 * Input: s = "00110"
 * Output: 1
 * Explanation: We flip the last digit to get 00111.
 * 
 * 
 * Example 2:
 * 
 * Input: s = "010110"
 * Output: 2
 * Explanation: We flip to get 011111, or alternatively 000111.
 * 
 * 
 * Example 3:
 * 
 * Input: s = "00011000"
 * Output: 2
 * Explanation: We flip to get 00000000.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s[i] is either '0' or '1'.
 * 
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
    int minFlipsMonoIncr(string s) {
        vector<vector<int>> dp(s.size(),vector<int>(2,0));
        dp[0][0] = s[0] == '0'? 0 : 1;
        dp[0][1] = 1 - dp[0][0];
        for(int i = 1; i < s.size(); i++){
            dp[i][0] = dp[i-1][0]+ (s[i] == '0'? 0 : 1);
            dp[i][1] = min(dp[i-1][0],dp[i-1][1])+ (s[i] == '0'? 1 : 0);
        }
        return min(dp[s.size()-1][0],dp[s.size()-1][1]);
    }
};
// @lc code=end



/*
// @lcpr case=start
// "00110"\n
// @lcpr case=end

// @lcpr case=start
// "010110"\n
// @lcpr case=end

// @lcpr case=start
// "00011000"\n
// @lcpr case=end

 */

