/*
 * @lc app=leetcode id=322 lang=cpp
 * @lcpr version=30201
 *
 * [322] Coin Change
 *
 * https://leetcode.com/problems/coin-change/description/
 *
 * algorithms
 * Medium (46.44%)
 * Likes:    19936
 * Dislikes: 502
 * Total Accepted:    2.3M
 * Total Submissions: 5.1M
 * Testcase Example:  '[1,2,5]\n11'
 *
 * You are given an integer array coins representing coins of different
 * denominations and an integer amount representing a total amount of money.
 * 
 * Return the fewest number of coins that you need to make up that amount. If
 * that amount of money cannot be made up by any combination of the coins,
 * return -1.
 * 
 * You may assume that you have an infinite number of each kind of coin.
 * 
 * 
 * Example 1:
 * 
 * Input: coins = [1,2,5], amount = 11
 * Output: 3
 * Explanation: 11 = 5 + 5 + 1
 * 
 * 
 * Example 2:
 * 
 * Input: coins = [2], amount = 3
 * Output: -1
 * 
 * 
 * Example 3:
 * 
 * Input: coins = [1], amount = 0
 * Output: 0
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= coins.length <= 12
 * 1 <= coins[i] <= 2^31 - 1
 * 0 <= amount <= 10^4
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

    // int coinChange(vector<int>& coins, int amount) {
    //     if (amount == 0) return 0;
    //     deque<int> q;
    //     q.push_back(amount);
    //     unordered_set<int> visited;
    //     visited.insert(amount);
    //     int count = 0;
    //     while(!q.empty()){
    //         int size = q.size();
    //         for(int i = 0; i < size; ++i){
    //             int curr = q.front(); q.pop_front();
    //             if(curr == 0) return count;
    //             for(int j = 0; j < coins.size(); ++j){
    //                 int next = curr - coins[j];
    //                 if(next < 0) continue;
    //                 if(visited.find(next) == visited.end()){
    //                     visited.insert(next);
    //                     q.push_back(next);
    //                 }
    //             }
    //         }
    //         count++;
    //     }
    //     return -1;
    // }
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX-1);
        dp[0] = 0;
        for(int i = 0; i < coins.size(); ++i){
            for(int j = coins[i]; j <= amount; ++j){
                dp[j] = min(dp[j],dp[j-coins[i]]+1);
            }
        }
        return dp[amount] == INT_MAX-1 ? -1 : dp[amount];
    }

};

// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// [1,2,5]\n11\n
// @lcpr case=end

// @lcpr case=start
// [2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n0\n
// @lcpr case=end

 */

