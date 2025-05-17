/*
 * @lc app=leetcode id=433 lang=cpp
 * @lcpr version=30201
 *
 * [433] Minimum Genetic Mutation
 *
 * https://leetcode.com/problems/minimum-genetic-mutation/description/
 *
 * algorithms
 * Medium (55.31%)
 * Likes:    3130
 * Dislikes: 341
 * Total Accepted:    226.4K
 * Total Submissions: 409.3K
 * Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
 *
 * A gene string can be represented by an 8-character long string, with choices
 * from 'A', 'C', 'G', and 'T'.
 * 
 * Suppose we need to investigate a mutation from a gene string startGene to a
 * gene string endGene where one mutation is defined as one single character
 * changed in the gene string.
 * 
 * 
 * For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
 * 
 * 
 * There is also a gene bank bank that records all the valid gene mutations. A
 * gene must be in bank to make it a valid gene string.
 * 
 * Given the two gene strings startGene and endGene and the gene bank bank,
 * return the minimum number of mutations needed to mutate from startGene to
 * endGene. If there is no such a mutation, return -1.
 * 
 * Note that the starting point is assumed to be valid, so it might not be
 * included in the bank.
 * 
 * 
 * Example 1:
 * 
 * Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank =
 * ["AACCGGTA","AACCGCTA","AAACGGTA"]
 * Output: 2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= bank.length <= 10
 * startGene.length == endGene.length == bank[i].length == 8
 * startGene, endGene, and bank[i] consist of only the characters ['A', 'C',
 * 'G', 'T'].
 * 
 * 
 */

#include <iostream>
#include <vector>
#include <string>
#include "../common/ListNode.cpp"
#include "../common/TreeNode.cpp"
#include <unordered_set>
#include <deque>
using namespace std;

// @lc code=start
class Solution {
public:
    bool isNeighbours(string a, string b){
        bool diff = false;
        for(int i = 0; i < 8; ++i){
            if(a[i] != b[i]){
                if(diff) return false;
                diff = true;
            }
        }
        return true;
    }

    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> seen;
        deque<string> dq;      
        dq.push_back(startGene);
        int res = 0;
        while(!dq.empty()){
            int siz = dq.size();
            for(int i = 0; i < siz; ++i){
                string curr = dq.front(); dq.pop_front();
                seen.insert(curr);
                if(curr == endGene) return res;
                for(auto neig : bank){
                    if(isNeighbours(curr,neig) && seen.find(neig) == seen.end()){
                        dq.push_back(neig);
                    }
                }
            }
            res++;
        }
        return -1;
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// "AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]\n
// @lcpr case=end

// @lcpr case=start
// "AACCGGTT"\n"AAACGGTA"\n["AACCGGTA","AACCGCTA","AAACGGTA"]\n
// @lcpr case=end

 */

