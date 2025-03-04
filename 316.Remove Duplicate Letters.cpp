/*
 * @lc app=leetcode id=316 lang=cpp
 * @lcpr version=30008
 *
 * [316] Remove Duplicate Letters
 *
 * https://leetcode.com/problems/remove-duplicate-letters/description/
 *
 * algorithms
 * Medium (50.83%)
 * Likes:    8859
 * Dislikes: 655
 * Total Accepted:    369.7K
 * Total Submissions: 727.3K
 * Testcase Example:  '"bcabc"'
 *
 * Given a string s, remove duplicate letters so that every letter appears once
 * and only once. You must make sure your result is the smallest in
 * lexicographical order among all possible results.
 * 
 * 
 * Example 1:
 * 
 * Input: s = "bcabc"
 * Output: "abc"
 * 
 * 
 * Example 2:
 * 
 * Input: s = "cbacdcbc"
 * Output: "acdb"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of lowercase English letters.
 * 
 * 
 * 
 * Note: This question is the same as 1081:
 * https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
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
    string removeDuplicateLetters(string s) {
        unordered_map<char,int> count;
        for (char i : s){
            count[i]++;
        }
        stack<char> stk;
        unordered_map<char,int> in;
        for(char i : s){
            count[i]--;
            if(in[i] == 1) continue;
            while (!stk.empty() && stk.top() > i && count[stk.top()] > 0){
                in[stk.top()] = 0;
                stk.pop();

            }
            if(in[i] == 0) {
                stk.push(i);
                in[i] = 1;
            }
        }
        string res = "";
        while(!stk.empty()){
            res += stk.top();
            stk.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "bcabc"\n
// @lcpr case=end

// @lcpr case=start
// "cbacdcbc"\n
// @lcpr case=end

 */

