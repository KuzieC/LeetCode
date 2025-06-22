/*
 * @lc app=leetcode id=14 lang=cpp
 * @lcpr version=30201
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (45.50%)
 * Likes:    19303
 * Dislikes: 4738
 * Total Accepted:    4.6M
 * Total Submissions: 10.1M
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

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"

using namespace std;

// @lc code=start

struct Node{
    bool end = false;
    char val = '\0';
    array<Node*,26> neigh{};
    Node() = default;
    Node(char i):val(i){}
};
class Solution {
public:
    void constructNode(string input, Node* head){
        auto curr = head;
        for(auto i : input){
            if(curr->neigh[i-'a'] == nullptr){
                curr->neigh[i-'a'] = new Node(i);
            }
            curr = curr->neigh[i-'a'];
        }
        curr->end = true;
    }
    string LCP(Node* head){
        string res = "";
        auto curr = head;
        while(true){
            int count = 0;
            auto next = curr;
            if(curr->end){
                res+=curr->val;
                return res.substr(1);
            }
            for(auto i : curr->neigh){
                if(i!= nullptr){
                    count++;
                    next = i;
                    if(count > 1) break;
                }
            }
            res+=curr->val;
            curr = next;    
            if(count != 1){
                return res.substr(1);
            }

        }
    }
    string longestCommonPrefix(vector<string>& strs) {
        Node* head = new Node();
        for(auto i : strs){
            constructNode(i,head);
        }
        return LCP(head);
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// ["flower","flow","flight"]\n
// @lcpr case=end

// @lcpr case=start
// ["dog","racecar","car"]\n
// @lcpr case=end

 */

