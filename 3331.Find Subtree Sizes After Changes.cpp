/*
 * @lc app=leetcode id=3331 lang=cpp
 * @lcpr version=20004
 *
 * [3331] Find Subtree Sizes After Changes
 *
 * https://leetcode.com/problems/find-subtree-sizes-after-changes/description/
 *
 * algorithms
 * Medium (57.64%)
 * Likes:    85
 * Dislikes: 32
 * Total Accepted:    14.3K
 * Total Submissions: 24.8K
 * Testcase Example:  '[-1,0,0,1,1,1]\n"abaabc"'
 *
 * You are given a tree rooted at node 0 that consists of n nodes numbered from
 * 0 to n - 1. The tree is represented by an array parent of size n, where
 * parent[i] is the parent of node i. Since node 0 is the root, parent[0] ==
 * -1.
 * 
 * You are also given a string s of length n, where s[i] is the character
 * assigned to node i.
 * 
 * We make the following changes on the tree one time simultaneously for all
 * nodes x from 1 to n - 1:
 * 
 * 
 * Find the closest node y to node x such that y is an ancestor of x, and s[x]
 * == s[y].
 * If node y does not exist, do nothing.
 * Otherwise, remove the edge between x and its current parent and make node y
 * the new parent of x by adding an edge between them.
 * 
 * 
 * Return an array answer of size n where answer[i] is the size of the subtree
 * rooted at node i in the final tree.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: parent = [-1,0,0,1,1,1], s = "abaabc"
 * 
 * Output: [6,3,1,1,1,1]
 * 
 * Explanation:
 * 
 * The parent of node 3 will change from node 1 to node 0.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: parent = [-1,0,4,0,1], s = "abbba"
 * 
 * Output: [5,2,1,1,1]
 * 
 * Explanation:
 * 
 * The following changes will happen at the same time:
 * 
 * 
 * The parent of node 4 will change from node 1 to node 0.
 * The parent of node 2 will change from node 4 to node 1.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == parent.length == s.length
 * 1 <= n <= 10^5
 * 0 <= parent[i] <= n - 1 for all i >= 1.
 * parent[0] == -1
 * parent represents a valid tree.
 * s consists only of lowercase English letters.
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
class UF {
public:
    vector<int> r;

    UF(int n){
        r.resize(n,0);
        for(int i = 0; i < r.size(); i++){
            r[i] = i;
        }
    }

    int find(int curr){
        while(r[curr] != curr){
            r[curr] = find(r[curr]);
        }
        return curr;
    }

    void add(int x, int y){
        int a = find(x);
        int b = find(y);
        r[b] = a;
    }

    bool check(int x, int y){
        return r[y] == x;
    }
};
class Solution {
public:

    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        UF uf(parent.size());

        for(int i = 1; i < parent.size(); i++){
            if(parent[i] != 0){
                uf.add(i,parent[i]);
            }
        }
    }
};
// @lc code=end



/*
// @lcpr case=start
// [-1,0,0,1,1,1]\n"abaabc"\n
// @lcpr case=end

// @lcpr case=start
// [-1,0,4,0,1]\n"abbba"\n
// @lcpr case=end

 */

