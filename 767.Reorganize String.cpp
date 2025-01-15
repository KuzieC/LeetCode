/*
 * @lc app=leetcode id=767 lang=cpp
 * @lcpr version=20004
 *
 * [767] Reorganize String
 *
 * https://leetcode.com/problems/reorganize-string/description/
 *
 * algorithms
 * Medium (55.55%)
 * Likes:    8721
 * Dislikes: 268
 * Total Accepted:    457.7K
 * Total Submissions: 823.9K
 * Testcase Example:  '"aab"'
 *
 * Given a string s, rearrange the characters of s so that any two adjacent
 * characters are not the same.
 * 
 * Return any possible rearrangement of s or return "" if not possible.
 * 
 * 
 * Example 1:
 * Input: s = "aab"
 * Output: "aba"
 * Example 2:
 * Input: s = "aaab"
 * Output: ""
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 500
 * s consists of lowercase English letters.
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
    string reorganizeString(string s) {
        sort(s.begin(), s.end());
        string res;
        int n = s.size();
        int i = 0;
        unordered_map<char, int> mp;
        priority_queue<pair<int, char>> pq;
        for(auto c: s){
            mp[c]++;
        }
        for(auto [c, f]: mp){
            pq.push({f, c});
        }
        while(pq.size() >= 2){
            auto [f1, c1] = pq.top(); pq.pop();
            auto [f2, c2] = pq.top(); pq.pop();
            res.push_back(c1);
            res.push_back(c2);
            if(--f1 > 0) pq.push({f1, c1});
            if(--f2 > 0) pq.push({f2, c2});
        }
        if(pq.size() > 0){
            auto [f, c] = pq.top(); pq.pop();
            if(f > 1) return "";
            res.push_back(c);
        }
        return res;
        
    }
};
// @lc code=end



/*
// @lcpr case=start
// "aab"\n
// @lcpr case=end

// @lcpr case=start
// "aaab"\n
// @lcpr case=end

 */

