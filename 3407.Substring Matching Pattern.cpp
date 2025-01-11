/*
 * @lc app=leetcode id=3407 lang=cpp
 * @lcpr version=20004
 *
 * [3407] Substring Matching Pattern
 *
 * https://leetcode.com/problems/substring-matching-pattern/description/
 *
 * algorithms
 * Easy (23.64%)
 * Likes:    58
 * Dislikes: 27
 * Total Accepted:    19.8K
 * Total Submissions: 83.6K
 * Testcase Example:  '"leetcode"\n"ee*e"'
 *
 * You are given a string s and a pattern string p, where p contains exactly
 * one '*' character.
 * 
 * The '*' in p can be replaced with any sequence of zero or more characters.
 * 
 * Return true if p can be made a substring of s, and false otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "leetcode", p = "ee*e"
 * 
 * Output: true
 * 
 * Explanation:
 * 
 * By replacing the '*' with "tcod", the substring "eetcode" matches the
 * pattern.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "car", p = "c*v"
 * 
 * Output: false
 * 
 * Explanation:
 * 
 * There is no substring matching the pattern.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "luck", p = "u*"
 * 
 * Output: true
 * 
 * Explanation:
 * 
 * The substrings "u", "uc", and "uck" match the pattern.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 50
 * 1 <= p.length <= 50 
 * s contains only lowercase English letters.
 * p contains only lowercase English letters and exactly one '*'
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
    bool hasMatch(string s, string p) {
        int curr = 0;
        int i;
        for(i = 0; i < p.size(); i++){
            if(p[i] == '*') break;
        }
        if(s.find(p.substr(0,i)) == string::npos) return false;
        if(s.rfind(p.substr(i+1)) == string::npos) return false;
        if(s.find(p.substr(0,i)) + i <= s.rfind(p.substr(i+1))) return true;
        return false;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "leetcode"\n"ee*e"\n
// @lcpr case=end

// @lcpr case=start
// "car"\n"c*v"\n
// @lcpr case=end

// @lcpr case=start
// "luck"\n"u*"\n
// @lcpr case=end

 */

