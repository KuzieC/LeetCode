/*
 * @lc app=leetcode id=93 lang=cpp
 * @lcpr version=30201
 *
 * [93] Restore IP Addresses
 *
 * https://leetcode.com/problems/restore-ip-addresses/description/
 *
 * algorithms
 * Medium (52.85%)
 * Likes:    5411
 * Dislikes: 805
 * Total Accepted:    533.1K
 * Total Submissions: 1M
 * Testcase Example:  '"25525511135"'
 *
 * A valid IP address consists of exactly four integers separated by single
 * dots. Each integer is between 0 and 255 (inclusive) and cannot have leading
 * zeros.
 * 
 * 
 * For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
 * "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
 * addresses.
 * 
 * 
 * Given a string s containing only digits, return all possible valid IP
 * addresses that can be formed by inserting dots into s. You are not allowed
 * to reorder or remove any digits in s. You may return the valid IP addresses
 * in any order.
 * 
 * 
 * Example 1:
 * 
 * Input: s = "25525511135"
 * Output: ["255.255.11.135","255.255.111.35"]
 * 
 * 
 * Example 2:
 * 
 * Input: s = "0000"
 * Output: ["0.0.0.0"]
 * 
 * 
 * Example 3:
 * 
 * Input: s = "101023"
 * Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 20
 * s consists of digits only.
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
    vector<string> res;
    void dfs(string s, int ind, string curr,int left){
        if(ind == s.size() && left == 0) {
            res.push_back(curr);
            return;
        }
        if(ind >= s.size() || left < 0) return;
        
        for(int i = 0; i < 3; ++i){
            if(ind + i >= s.size()) return;
            string part = s.substr(ind,i+1);
            if(part.size() > 1 && part[0] == '0')return;
            if(stoi(part) <= 255){
                if(curr.empty()){
                    dfs(s,ind+i+1,part,left);
                }
                else{
                    dfs(s,ind+i+1,curr+'.'+part,left-1);
                }
            }

        }

    }

    vector<string> restoreIpAddresses(string s) {
        string temp = "";
        dfs(s,0,temp,3);
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
// "25525511135"\n
// @lcpr case=end

// @lcpr case=start
// "0000"\n
// @lcpr case=end

// @lcpr case=start
// "101023"\n
// @lcpr case=end

 */

