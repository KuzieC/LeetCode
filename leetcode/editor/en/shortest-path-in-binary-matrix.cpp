/*
 * @lc app=leetcode id=1091 lang=cpp
 * @lcpr version=30201
 *
 * [1091] Shortest Path in Binary Matrix
 *
 * https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
 *
 * algorithms
 * Medium (49.54%)
 * Likes:    6941
 * Dislikes: 262
 * Total Accepted:    666K
 * Total Submissions: 1.3M
 * Testcase Example:  '[[0,1],[1,0]]'
 *
 * Given an n x n binary matrix grid, return the length of the shortest clear
 * path in the matrix. If there is no clear path, return -1.
 * 
 * A clear path in a binary matrix is a path from the top-left cell (i.e., (0,
 * 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
 * 
 * 
 * All the visited cells of the path are 0.
 * All the adjacent cells of the path are 8-directionally connected (i.e., they
 * are different and they share an edge or a corner).
 * 
 * 
 * The length of a clear path is the number of visited cells of this path.
 * 
 * 
 * Example 1:
 * 
 * Input: grid = [[0,1],[1,0]]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
 * Output: 4
 * 
 * 
 * Example 3:
 * 
 * Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
 * Output: -1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == grid.length
 * n == grid[i].length
 * 1 <= n <= 100
 * grid[i][j] is 0 or 1
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

    array<array<int,2>,8> dirs = {{{1,0},{1,1},{0,1},{-1,1},{1,-1},{-1,0},{-1,-1},{0,-1}}};
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int res = 1;
        queue<pair<int,int>> q;
        if(grid[0][0] == 0) {
            q.push({0,0});
            grid[0][0] = 1;
        }
        while(!q.empty()){
            int siz = q.size();
            for(int i = 0; i < siz; ++i){
                auto curr = q.front(); q.pop();
                if(curr.first == grid.size()-1&& curr.second == grid[0].size() -1 ) return res;
                for(auto dir: dirs){
                    if(dir[0] + curr.first >= 0 && dir[0] + curr.first < grid.size() &&
                    dir[1] + curr.second >= 0 && dir[1] + curr.second < grid[0].size() && grid[dir[0] + curr.first][dir[1]+curr.second] == 0){
                        if(dir[0] + curr.first == grid.size() - 1 && dir[1] + curr.second == grid[0].size() - 1){
                            return res+1;
                        }
                        q.push({dir[0] + curr.first,dir[1] + curr.second});
                        grid[dir[0] + curr.first][dir[1] + curr.second] = 1;
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
// [[0,1],[1,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0,0],[1,1,0],[1,1,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,0,0],[1,1,0],[1,1,0]]\n
// @lcpr case=end

 */

