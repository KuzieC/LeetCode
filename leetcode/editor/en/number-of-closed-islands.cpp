/*
 * @lc app=leetcode id=1254 lang=cpp
 * @lcpr version=30200
 *
 * [1254] Number of Closed Islands
 *
 * https://leetcode.com/problems/number-of-closed-islands/description/
 *
 * algorithms
 * Medium (66.69%)
 * Likes:    4648
 * Dislikes: 181
 * Total Accepted:    252K
 * Total Submissions: 377.8K
 * Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
 *
 * Given a 2D grid consists of 0s (land) and 1s (water).  An island is a
 * maximal 4-directionally connected group of 0s and a closed island is an
 * island totally (all left, top, right, bottom) surrounded by 1s.
 * 
 * Return the number of closed islands.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * Input: grid =
 * [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
 * Output: 2
 * Explanation: 
 * Islands in gray are closed because they are completely surrounded by water
 * (group of 1s).
 * 
 * Example 2:
 * 
 * 
 * 
 * Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
 * Output: 1
 * 
 * 
 * Example 3:
 * 
 * Input: grid = [[1,1,1,1,1,1,1],
 * [1,0,0,0,0,0,1],
 * [1,0,1,1,1,0,1],
 * [1,0,1,0,1,0,1],
 * [1,0,1,1,1,0,1],
 * [1,0,0,0,0,0,1],
 * ⁠              [1,1,1,1,1,1,1]]
 * Output: 2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= grid.length, grid[0].length <= 100
 * 0 <= grid[i][j] <=1
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
    bool flood(vector<vector<int>>& grid, int x, int y){
        if(x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size()){
            return false;
        }

        if(grid[x][y] == 1) return true;
        else{
            grid[x][y] = 1;
            bool a = flood(grid,x+1,y);
            bool b = flood(grid,x-1,y);
            bool c = flood(grid,x,y+1);
            bool d = flood(grid,x,y-1);
            return  a && b && c && d;
        }

    }
    int closedIsland(vector<vector<int>>& grid) {
        int res = 0;
        for(int x = 0; x < grid.size(); ++x){
            for(int y = 0; y < grid[0].size(); ++y){
                if(grid[x][y] == 1) continue;
                if(flood(grid,x,y)) res++;
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
// [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1,1,1,1,1,1],\n[1,0,0,0,0,0,1],\n[1,0,1,1,1,0,1],\n[1,0,1,0,1,0,1],\n[1,0,1,1,1,0,1],\n[1,0,0,0,0,0,1],\n[1,1,1,1,1,1,1]]\n
// @lcpr case=end

 */

