/*
 * @lc app=leetcode id=1406 lang=cpp
 * @lcpr version=30201
 *
 * [1406] Stone Game III
 *
 * https://leetcode.com/problems/stone-game-iii/description/
 *
 * algorithms
 * Hard (63.23%)
 * Likes:    2265
 * Dislikes: 75
 * Total Accepted:    101.5K
 * Total Submissions: 160.6K
 * Testcase Example:  '[1,2,3,7]'
 *
 * Alice and Bob continue their games with piles of stones. There are several
 * stones arranged in a row, and each stone has an associated value which is an
 * integer given in the array stoneValue.
 * 
 * Alice and Bob take turns, with Alice starting first. On each player's turn,
 * that player can take 1, 2, or 3 stones from the first remaining stones in
 * the row.
 * 
 * The score of each player is the sum of the values of the stones taken. The
 * score of each player is 0 initially.
 * 
 * The objective of the game is to end with the highest score, and the winner
 * is the player with the highest score and there could be a tie. The game
 * continues until all the stones have been taken.
 * 
 * Assume Alice and Bob play optimally.
 * 
 * Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they
 * will end the game with the same score.
 * 
 * 
 * Example 1:
 * 
 * Input: stoneValue = [1,2,3,7]
 * Output: "Bob"
 * Explanation: Alice will always lose. Her best move will be to take three
 * piles and the score become 6. Now the score of Bob is 7 and Bob wins.
 * 
 * 
 * Example 2:
 * 
 * Input: stoneValue = [1,2,3,-9]
 * Output: "Alice"
 * Explanation: Alice must choose all the three piles at the first move to win
 * and leave Bob with negative score.
 * If Alice chooses one pile her score will be 1 and the next move Bob's score
 * becomes 5. In the next move, Alice will take the pile with value = -9 and
 * lose.
 * If Alice chooses two piles her score will be 3 and the next move Bob's score
 * becomes 3. In the next move, Alice will take the pile with value = -9 and
 * also lose.
 * Remember that both play optimally so here Alice will choose the scenario
 * that makes her win.
 * 
 * 
 * Example 3:
 * 
 * Input: stoneValue = [1,2,3,6]
 * Output: "Tie"
 * Explanation: Alice cannot win this game. She can end the game in a draw if
 * she decided to choose all the first three piles, otherwise she will
 * lose.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= stoneValue.length <= 5 * 10^4
 * -1000 <= stoneValue[i] <= 1000
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
    string stoneGameIII(vector<int>& stoneValue) {
        vector<long> dp(stoneValue.size()+1,INT_MIN);
        dp[stoneValue.size()] = 0;
        for(int i = stoneValue.size()-1; i >= 0; i--){
            int sum = 0;
            for(int take = 1; take <= 3 && take + i <= stoneValue.size(); take++){
                sum += stoneValue[i+take-1];
                dp[i] = max(dp[i],sum - dp[i+take]);
            }
        }
        if(dp[0] == 0) return "Tie";
        else if(dp[0] > 0) return "Alice";
        else return "Bob";
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// [1,2,3,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,-9]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,6]\n
// @lcpr case=end

 */

