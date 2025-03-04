/*
 * @lc app=leetcode id=30 lang=cpp
 * @lcpr version=30008
 *
 * [30] Substring with Concatenation of All Words
 *
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
 *
 * algorithms
 * Hard (32.79%)
 * Likes:    2126
 * Dislikes: 339
 * Total Accepted:    549.1K
 * Total Submissions: 1.7M
 * Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
 *
 * You are given a string s and an array of strings words. All the strings of
 * words are of the same length.
 * 
 * A concatenated string is a string that exactly contains all the strings of
 * any permutation of words concatenated.
 * 
 * 
 * For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
 * "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is
 * not a concatenated string because it is not the concatenation of any
 * permutation of words.
 * 
 * 
 * Return an array of the starting indices of all the concatenated substrings
 * in s. You can return the answer in any order.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "barfoothefoobarman", words = ["foo","bar"]
 * 
 * Output: [0,9]
 * 
 * Explanation:
 * 
 * The substring starting at 0 is "barfoo". It is the concatenation of
 * ["bar","foo"] which is a permutation of words.
 * The substring starting at 9 is "foobar". It is the concatenation of
 * ["foo","bar"] which is a permutation of words.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "wordgoodgoodgoodbestword", words =
 * ["word","good","best","word"]
 * 
 * Output: []
 * 
 * Explanation:
 * 
 * There is no concatenated substring.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
 * 
 * Output: [6,9,12]
 * 
 * Explanation:
 * 
 * The substring starting at 6 is "foobarthe". It is the concatenation of
 * ["foo","bar","the"].
 * The substring starting at 9 is "barthefoo". It is the concatenation of
 * ["bar","the","foo"].
 * The substring starting at 12 is "thefoobar". It is the concatenation of
 * ["the","foo","bar"].
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * 1 <= words.length <= 5000
 * 1 <= words[i].length <= 30
 * s and words[i] consist of lowercase English letters.
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
    vector<int> findSubstring(string s, vector<string>& words) {
        if (words.empty()) return {};
        int wordlen = words[0].size();
        int wordsize = words.size();
        vector<int> res; 
        unordered_map<string,int> mp;
        unordered_map<string,int> ori;
        for(string& i : words){
            ori[i] += 1;
        }
        for(int i = 0; i < wordlen;  i ++){
            mp.clear();
            int left = i;
            int right = i;
            while(right+wordlen <= s.size()){
                string temp = s.substr(right,wordlen);
                right += wordlen;
                if( ori.find(temp) != ori.end()){
                    mp[temp] ++;
                    
                    while(left <= right && mp[temp] > ori[temp]){
                        string t = s.substr(left,wordlen);
                        if(mp.find(t) != mp.end()) {
                            mp[t]--;
                        }
                        left+=wordlen;
                    }
                    if(wordsize * wordlen == right - left){
                        res.push_back(left);
                    }
                }
                else{
                    left = right;
                    mp.clear();
                }
            }
        }
        return res;
    }
    
};

// @lc code=end



/*
// @lcpr case=start
// "barfoothefoobarman"\n["foo","bar"]\n
// @lcpr case=end

// @lcpr case=start
// "wordgoodgoodgoodbestword"\n["word","good","best","word"]\n
// @lcpr case=end

// @lcpr case=start
// "barfoofoobarthefoobarman"\n["bar","foo","the"]\n
// @lcpr case=end

 */

