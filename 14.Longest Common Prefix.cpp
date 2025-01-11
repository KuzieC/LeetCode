/*
 * @lc app=leetcode id=14 lang=cpp
 * @lcpr version=20004
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (44.50%)
 * Likes:    18529
 * Dislikes: 4656
 * Total Accepted:    4.1M
 * Total Submissions: 9.1M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * 
 * Example 1:
 * 
 * Input: strs = ["flower","flow","flight"]
 * Output: "fl"
 * 
 * 
 * Example 2:
 * 
 * Input: strs = ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] consists of only lowercase English letters if it is non-empty.
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
class TreNode{
public:
    char val;
    vector<TreNode*> mp;
    int size;
    bool isEnd;
    TreNode(char a): val(a){
        mp.resize(26,nullptr);
        size = 0;
        isEnd = false;
    }
};
class Tre{
public:
    TreNode* head;

    Tre(){
        head = new TreNode('@');
    }

    void insert(string& input){
        auto curr = head;
        for(auto i : input){
            if(curr->mp[i-'a'] == nullptr) {
                curr->mp[i-'a'] = new TreNode(i);
                curr->size++;
            }        
            curr = curr->mp[i-'a'];
        }
        curr->isEnd = true;
    }

    string get(string& input){
        string res  = "";
        auto curr = head;
        for(auto i : input){
            if(curr->mp[i-'a'] != nullptr && curr->size == 1 && curr->isEnd == false){
                res += i;
                curr = curr->mp[i-'a'];
            }
            else{
                return res;
            }
        }
        return res;
    }

};
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        Tre* t = new Tre();
        if(strs.size() == 1) return strs[0];
        for(int i = 0; i < strs.size(); i++){
            if(i == strs.size()-1){
                return t->get(strs[i]);
            }
            t->insert(strs[i]);
        }
        return "";
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["flower","flow","flight"]\n
// @lcpr case=end

// @lcpr case=start
// ["dog","racecar","car"]\n
// @lcpr case=end

 */

