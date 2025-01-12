/*
 * @lc app=leetcode id=22 lang=cpp
 * @lcpr version=20004
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (76.15%)
 * Likes:    21688
 * Dislikes: 1002
 * Total Accepted:    2.1M
 * Total Submissions: 2.8M
 * Testcase Example:  '3'
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * 
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 8
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
    vector<string> res;
    vector<string> generateParenthesis(int n) {
        int left = n, right = n;
        dfs("",left,right);
        return res;

    }

    void dfs(string curr, int left, int right){

        if(left == 0 && right == 0){
            res.push_back(curr);
            return;
        }
        if(left > 0){
            curr += '(';
            dfs(curr,left-1,right);
            curr.pop_back();
        }
        if(left < right){
            curr += ')';
            dfs(curr,left,right-1);
            curr.pop_back();
        }
        
    }
};
// @lc code=end



/*
// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

