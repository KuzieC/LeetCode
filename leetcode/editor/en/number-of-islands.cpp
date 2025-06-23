/*
 * @lc app=leetcode id=200 lang=cpp
 * @lcpr version=30201
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (62.35%)
 * Likes:    23893
 * Dislikes: 567
 * Total Accepted:    3.5M
 * Total Submissions: 5.6M
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given an m x n 2D binary grid grid which represents a map of '1's (land) and
 * '0's (water), return the number of islands.
 * 
 * An island is surrounded by water and is formed by connecting adjacent lands
 * horizontally or vertically. You may assume all four edges of the grid are
 * all surrounded by water.
 * 
 * 
 * Example 1:
 * 
 * Input: grid = [
 * ⁠ ["1","1","1","1","0"],
 * ⁠ ["1","1","0","1","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","0","0","0"]
 * ]
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * Input: grid = [
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","1","0","0"],
 * ⁠ ["0","0","0","1","1"]
 * ]
 * Output: 3
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 300
 * grid[i][j] is '0' or '1'.
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
    const vector<pair<int,int>> dirs = {{1,0},{0,1},{-1,0},{0,-1}};
    bool isValid(vector<vector<char>>& grid,int x, int y){
        if(x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size()) return false;
        return true;
    }
    void dfs(vector<vector<char>>& grid,size_t row, size_t col){
        grid[row][col] = '0';
        for(auto& [x,y] : dirs){
            if(isValid(grid,row+x,col+y) && grid[row+x][col+y] == '1'){
                dfs(grid,row+x,col+y);
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;

        for(size_t row = 0; row < grid.size(); row++){
            for(size_t col = 0; col < grid[0].size(); col++){
                if(grid[row][col] == '1'){
                    res++;
                    dfs(grid,row,col);
                }
            }
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
// [\n["1","1","1","1","0"],\n["1","1","0","1","0"],\n["1","1","0","0","0"],\n["0","0","0","0","0"]\n]\n
// @lcpr case=end

// @lcpr case=start
// [\n["1","1","0","0","0"],\n["1","1","0","0","0"],\n["0","0","1","0","0"],\n["0","0","0","1","1"]\n]\n
// @lcpr case=end

 */

