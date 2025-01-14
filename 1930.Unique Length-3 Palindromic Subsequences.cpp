/*
 * @lc app=leetcode id=1930 lang=cpp
 * @lcpr version=20004
 *
 * [1930] Unique Length-3 Palindromic Subsequences
 *
 * https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
 *
 * algorithms
 * Medium (70.77%)
 * Likes:    2447
 * Dislikes: 99
 * Total Accepted:    237.6K
 * Total Submissions: 335.7K
 * Testcase Example:  '"aabca"'
 *
 * Given a string s, return the number of unique palindromes of length three
 * that are a subsequence of s.
 * 
 * Note that even if there are multiple ways to obtain the same subsequence, it
 * is still only counted once.
 * 
 * A palindrome is a string that reads the same forwards and backwards.
 * 
 * A subsequence of a string is a new string generated from the original string
 * with some characters (can be none) deleted without changing the relative
 * order of the remaining characters.
 * 
 * 
 * For example, "ace" is a subsequence of "abcde".
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: s = "aabca"
 * Output: 3
 * Explanation: The 3 palindromic subsequences of length 3 are:
 * - "aba" (subsequence of "aabca")
 * - "aaa" (subsequence of "aabca")
 * - "aca" (subsequence of "aabca")
 * 
 * 
 * Example 2:
 * 
 * Input: s = "adc"
 * Output: 0
 * Explanation: There are no palindromic subsequences of length 3 in "adc".
 * 
 * 
 * Example 3:
 * 
 * Input: s = "bbcbaba"
 * Output: 4
 * Explanation: The 4 palindromic subsequences of length 3 are:
 * - "bbb" (subsequence of "bbcbaba")
 * - "bcb" (subsequence of "bbcbaba")
 * - "bab" (subsequence of "bbcbaba")
 * - "aba" (subsequence of "bbcbaba")
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 3 <= s.length <= 10^5
 * s consists of only lowercase English letters.
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
    int count = 0;
    unordered_set<string> vis;
    int countPalindromicSubsequence(string& s) {
        vector<int> first(26,-1);
        vector<int> last(26,-1);

        for(int i = 0; i < s.size();i++){
            if(first[s[i] - 'a'] == -1) first[s[i]-'a'] = i;
            last[s[i]-'a'] = i;
        }

        for(int i = 0; i < 26; i++){
            if(first[i] != -1 && last[i] != -1){
                for(int j = first[i]+1; j < last[i]; j++){
                    string temp = string(1,'a'+i) + s[j] + string(1,'a'+i);
                    vis.insert(temp);
                }
            }
        }
        return vis.size();

    }

};
// @lc code=end



/*
// @lcpr case=start
// "aabca"\n
// @lcpr case=end

// @lcpr case=start
// "adc"\n
// @lcpr case=end

// @lcpr case=start
// "bbcbaba"\n
// @lcpr case=end

 */

