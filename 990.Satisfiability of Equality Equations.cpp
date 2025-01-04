/*
 * @lc app=leetcode id=990 lang=cpp
 * @lcpr version=20004
 *
 * [990] Satisfiability of Equality Equations
 *
 * https://leetcode.com/problems/satisfiability-of-equality-equations/description/
 *
 * algorithms
 * Medium (50.83%)
 * Likes:    3810
 * Dislikes: 62
 * Total Accepted:    139K
 * Total Submissions: 273.5K
 * Testcase Example:  '["a==b","b!=a"]'
 *
 * You are given an array of strings equations that represent relationships
 * between variables where each string equations[i] is of length 4 and takes
 * one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are
 * lowercase letters (not necessarily different) that represent one-letter
 * variable names.
 * 
 * Return true if it is possible to assign integers to variable names so as to
 * satisfy all the given equations, or false otherwise.
 * 
 * 
 * Example 1:
 * 
 * Input: equations = ["a==b","b!=a"]
 * Output: false
 * Explanation: If we assign say, a = 1 and b = 1, then the first equation is
 * satisfied, but not the second.
 * There is no way to assign the variables to satisfy both equations.
 * 
 * 
 * Example 2:
 * 
 * Input: equations = ["b==a","a==b"]
 * Output: true
 * Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= equations.length <= 500
 * equations[i].length == 4
 * equations[i][0] is a lowercase letter.
 * equations[i][1] is either '=' or '!'.
 * equations[i][2] is '='.
 * equations[i][3] is a lowercase letter.
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
    vector<int> parent;
    int count;
    UF(int n){
        parent.resize(n);
        count = n;
        for(int i = 0; i < n; i++){
            parent[i] = i;
        }
    }

    int find(int x){
        if(parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void connect(int a, int b){
        int par_a = find(a);
        int par_b = find(b);
        if(par_a != par_b){
            parent[par_a] = par_b;
            count--;
        }
        
    }

    bool connected(int a, int b){
        return find(a) == find(b);
    }

    int get(){
        return count;
    }
};
class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        UF uf(256);
        for(int i = 0; i < equations.size();i++){
            char a = equations[i][0];
            char b = equations[i][3];
            char op = equations[i][1];
            if(op == '='){
                uf.connect(a,b);
            }
        }
        for(int i = 0; i < equations.size();i++){
            char a = equations[i][0];
            char b = equations[i][3];
            char op = equations[i][1];
            if(op == '!'){
                if(uf.connected(a,b)){
                    return false;
                }
            }
        }
        return true;
    }
};
// @lc code=end



/*
// @lcpr case=start
// b"\na"]\n
// @lcpr case=end

// @lcpr case=start
// a"\nb"]\n
// @lcpr case=end

 */

