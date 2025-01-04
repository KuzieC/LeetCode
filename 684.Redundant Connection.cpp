/*
 * @lc app=leetcode id=684 lang=cpp
 * @lcpr version=20004
 *
 * [684] Redundant Connection
 *
 * https://leetcode.com/problems/redundant-connection/description/
 *
 * algorithms
 * Medium (63.82%)
 * Likes:    6326
 * Dislikes: 409
 * Total Accepted:    415.9K
 * Total Submissions: 651.6K
 * Testcase Example:  '[[1,2],[1,3],[2,3]]'
 *
 * In this problem, a tree is an undirected graph that is connected and has no
 * cycles.
 * 
 * You are given a graph that started as a tree with n nodes labeled from 1 to
 * n, with one additional edge added. The added edge has two different vertices
 * chosen from 1 to n, and was not an edge that already existed. The graph is
 * represented as an array edges of length n where edges[i] = [ai, bi]
 * indicates that there is an edge between nodes ai and bi in the graph.
 * 
 * Return an edge that can be removed so that the resulting graph is a tree of
 * n nodes. If there are multiple answers, return the answer that occurs last
 * in the input.
 * 
 * 
 * Example 1:
 * 
 * Input: edges = [[1,2],[1,3],[2,3]]
 * Output: [2,3]
 * 
 * 
 * Example 2:
 * 
 * Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
 * Output: [1,4]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == edges.length
 * 3 <= n <= 1000
 * edges[i].length == 2
 * 1 <= ai < bi <= edges.length
 * ai != bi
 * There are no repeated edges.
 * The given graph is connected.
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
#include "uf.cpp"
// @lcpr-template-end
// @lc code=start
class UF {
private:
    std::vector<int> parent;
    int count;

public:
    UF(int n) {
        parent.resize(n);
        count = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void connect(int a, int b) {
        int par_a = find(a);
        int par_b = find(b);
        if (par_a != par_b) {
            parent[par_a] = par_b;
            count--;
        }
    }

    bool connected(int a, int b) {
        return find(a) == find(b);
    }

    int get() {
        return count;
    }
};
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        UF uf(edges.size());
        for(int i =0; i < edges.size(); i++){
            if(uf.connected(edges[i][0]-1,edges[i][1]-1)){
                return edges[i];
            }
            uf.connect(edges[i][0]-1,edges[i][1]-1);
        }
        return {};
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2],[1,3],[2,3]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2],[2,3],[3,4],[1,4],[1,5]]\n
// @lcpr case=end

 */

