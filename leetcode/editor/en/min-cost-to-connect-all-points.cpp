/*
 * @lc app=leetcode id=1584 lang=cpp
 * @lcpr version=30200
 *
 * [1584] Min Cost to Connect All Points
 *
 * https://leetcode.com/problems/min-cost-to-connect-all-points/description/
 *
 * algorithms
 * Medium (68.68%)
 * Likes:    5303
 * Dislikes: 138
 * Total Accepted:    371.1K
 * Total Submissions: 540.2K
 * Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
 *
 * You are given an array points representing integer coordinates of some
 * points on a 2D-plane, where points[i] = [xi, yi].
 * 
 * The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
 * distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
 * absolute value of val.
 * 
 * Return the minimum cost to make all points connected. All points are
 * connected if there is exactly one simple path between any two points.
 * 
 * 
 * Example 1:
 * 
 * Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
 * Output: 20
 * Explanation: 
 * 
 * We can connect the points as shown above to get the minimum cost of 20.
 * Notice that there is a unique path between every pair of points.
 * 
 * 
 * Example 2:
 * 
 * Input: points = [[3,12],[-2,5],[-4,1]]
 * Output: 18
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= points.length <= 1000
 * -10^6 <= xi, yi <= 10^6
 * All pairs (xi, yi) are distinct.
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
class UF{
public:
    vector<int> parent;
    UF(int n){
        parent.resize(n);
        for(int i = 0; i < n; ++i){
            parent[i] = i;
        }
    }

    int find(int a){
        while(parent[a] != a){
            parent[a] = find(parent[a]);
            a = parent[a];
        }
        return parent[a];
    }

    bool connected(int a, int b){
        return find(a) == find(b);
    }

    void connect(int a, int b){
        int pa = find(a);
        int pb = find(b);
        if(pa != pb){
            parent[pa] = pb;
        }
    }
};
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        vector<vector<int>> edges;
        for(int i = 0; i < points.size(); ++i){
            for(int j = i+1; j < points.size(); ++j){
                edges.push_back({i,j,abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])});
            }
        }

        sort(edges.begin(),edges.end(),[](const vector<int>& a, const vector<int>& b){return a[2] < b[2];});
        UF uf(points.size());
        int res = 0;
        for(const vector<int>& i : edges){
            int from = i[0];
            int to  = i[1];
            int cost = i[2];
            if(uf.connected(from,to)) continue;
            res += cost;
            uf.connect(from,to);
        }
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
// [[0,0],[2,2],[3,10],[5,2],[7,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[3,12],[-2,5],[-4,1]]\n
// @lcpr case=end

 */

