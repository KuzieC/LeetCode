/*
 * @lc app=leetcode id=131 lang=cpp
 * @lcpr version=30200
 *
 * [131] Palindrome Partitioning
 *
 * https://leetcode.com/problems/palindrome-partitioning/description/
 *
 * algorithms
 * Medium (71.78%)
 * Likes:    13471
 * Dislikes: 541
 * Total Accepted:    1.1M
 * Total Submissions: 1.5M
 * Testcase Example:  '"aab"'
 *
 * Given a string s, partition s such that every substring of the partition is
 * a palindrome. Return all possible palindrome partitioning of s.
 * 
 * 
 * Example 1:
 * Input: s = "aab"
 * Output: [["a","a","b"],["aa","b"]]
 * Example 2:
 * Input: s = "a"
 * Output: [["a"]]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 16
 * s contains only lowercase English letters.
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
    vector<vector<string>> res;
    bool isPalindrome(string& s, int start, int end){
        while(start<end){
            if(s[start++] != s[end--]) return false;
        }
        return true;
    }
    void dfs(string s, int ind, vector<string>& curr){
        if(ind == s.size()){
            res.push_back(curr);
            return;
        }

        for(int i = ind; i < s.size(); ++i){
            if(isPalindrome(s,ind,i)){
                curr.push_back(s.substr(ind,i-ind+1));
                dfs(s,i+1,curr);
                curr.pop_back();
            }
        }

    }
    vector<vector<string>> partition(string s) {
        res.clear();
        vector<string> curr;
        dfs(s,0,curr);
        return res;

    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// "aab"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n
// @lcpr case=end

 */

