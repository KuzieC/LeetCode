/*
 * @lc app=leetcode id=721 lang=cpp
 * @lcpr version=30201
 *
 * [721] Accounts Merge
 *
 * https://leetcode.com/problems/accounts-merge/description/
 *
 * algorithms
 * Medium (59.34%)
 * Likes:    7210
 * Dislikes: 1250
 * Total Accepted:    513.1K
 * Total Submissions: 864.7K
 * Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
 *
 * Given a list of accounts where each element accounts[i] is a list of
 * strings, where the first element accounts[i][0] is a name, and the rest of
 * the elements are emails representing emails of the account.
 * 
 * Now, we would like to merge these accounts. Two accounts definitely belong
 * to the same person if there is some common email to both accounts. Note that
 * even if two accounts have the same name, they may belong to different people
 * as people could have the same name. A person can have any number of accounts
 * initially, but all of their accounts definitely have the same name.
 * 
 * After merging the accounts, return the accounts in the following format: the
 * first element of each account is the name, and the rest of the elements are
 * emails in sorted order. The accounts themselves can be returned in any
 * order.
 * 
 * 
 * Example 1:
 * 
 * Input: accounts =
 * [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
 * Output:
 * [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
 * Explanation:
 * The first and second John's are the same person as they have the common
 * email "johnsmith@mail.com".
 * The third John and Mary are different people as none of their email
 * addresses are used by other accounts.
 * We could return these lists in any order, for example the answer [['Mary',
 * 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
 * ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
 * would still be accepted.
 * 
 * 
 * Example 2:
 * 
 * Input: accounts =
 * [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
 * Output:
 * [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= accounts.length <= 1000
 * 2 <= accounts[i].length <= 10
 * 1 <= accounts[i][j].length <= 30
 * accounts[i][0] consists of English letters.
 * accounts[i][j] (for j > 0) is a valid email.
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
    void dfs(vector<vector<string>>& accounts, unordered_map<string,vector<int>>& emailtoIndex, unordered_set<string>& visited, vector<string>& res, string curremail){
        res.push_back(curremail);
        const vector<int>& indexs = emailtoIndex[curremail];
        for(auto ind : indexs){
            const vector<string>& account = accounts[ind];
            for(int i = 1; i < account.size(); ++i){
                string nextemail = account[i];
                if(visited.find(nextemail) != visited.end()) continue;
                visited.insert(nextemail);
                dfs(accounts,emailtoIndex,visited,res,nextemail);
            }
        }
    }
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, vector<int>> emailtoIndex;
        for(int i = 0; i < accounts.size(); ++i){
            vector<string> account = accounts[i];
             for(int j = 1; j < account.size(); ++j){
                emailtoIndex[account[j]].push_back(i);
             }
        }

        vector<vector<string>> ress;
        unordered_set<string> visited;
        for(auto pair : emailtoIndex){
            cout<<pair.first<<endl;
            set<string> emails;
            string email = pair.first;
            set<string> res;
            if(visited.find(email) != visited.end()) continue;
            visited.insert(email);
            // dfs(accounts,emailtoIndex,visited,res,email);
            vector<int> indexs = pair.second;
            deque<string> q;
            q.push_back(email);
            while(!q.empty()){
                string curr = q.front(); q.pop_front();
                cout<<email<<" "<<curr<<endl;
                res.insert(curr);
                const vector<int>& ind = emailtoIndex[curr];
                for(int i = 0; i < ind.size(); ++i){
                    vector<string> account = accounts[ind[i]];
                    for(int j = 1; j < account.size(); ++j){
                        string nextemail = account[j];
                        if(visited.find(nextemail) != visited.end()) continue;
                        visited.insert(nextemail);
                        q.push_back(nextemail);
                    }

                }
            }
            
            // emails.insert(email);
            // visited.insert(email);
            // for(int ind : indexs){
            //     vector<string> account = accounts[ind];
            //     for(int i = 1; i < account.size(); ++i){
            //         emails.insert(account[i]);
            //         visited.insert(account[i]);
            //     }
            // }
            // vector<string> mergedemail(emails.begin(),emails.end());
            string name = accounts[indexs[0]][0];
            vector<string> temp;
            temp.push_back(name);
            temp.insert(temp.end(),res.begin(),res.end());
            ress.push_back(temp);
        }

        return ress;
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// \n[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]\n
// @lcpr case=end

// @lcpr case=start
// \n[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]\n
// @lcpr case=end

 */

