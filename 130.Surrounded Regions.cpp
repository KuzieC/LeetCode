/*
 * @lc app=leetcode id=130 lang=cpp
 * @lcpr version=20004
 *
 * [130] Surrounded Regions
 *
 * https://leetcode.com/problems/surrounded-regions/description/
 *
 * algorithms
 * Medium (41.53%)
 * Likes:    8949
 * Dislikes: 1986
 * Total Accepted:    849.1K
 * Total Submissions: 2M
 * Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
 *
 * You are given an m x n matrix board containing letters 'X' and 'O', capture
 * regions that are surrounded:
 * 
 * 
 * Connect: A cell is connected to adjacent cells horizontally or
 * vertically.
 * Region: To form a region connect every 'O' cell.
 * Surround: The region is surrounded with 'X' cells if you can connect the
 * region with 'X' cells and none of the region cells are on the edge of the
 * board.
 * 
 * 
 * To capture a surrounded region, replace all 'O's with 'X's in-place within
 * the original board. You do not need to return anything.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: board =
 * [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
 * 
 * Output:
 * [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
 * 
 * Explanation:
 * 
 * In the above diagram, the bottom region is not captured because it is on the
 * edge of the board and cannot be surrounded.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: board = [["X"]]
 * 
 * Output: [["X"]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == board.length
 * n == board[i].length
 * 1 <= m, n <= 200
 * board[i][j] is 'X' or 'O'.
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
    vector<vector<int>> visited;
    void dfs(vector<vector<char>>& board, int x , int y){
        int m = board.size();
        int n = board[0].size();
        if(x < 0 || x >= m || y < 0 || y >= n){
            return;
        }
        if(visited[x][y] == 1){
            return;
        }
        visited[x][y] = 1;
        if(board[x][y] == 'O'){
            board[x][y] = 'A';
            dfs(board, x, y - 1);
            dfs(board, x, y + 1);
            dfs(board, x - 1, y);
            dfs(board, x + 1, y);
        }
    
        return;
    }
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        visited.resize(m, vector<int>(n, 0));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(i == 0 || i == m - 1 || j == 0 || j == n - 1){
                    if(board[i][j] == 'O'){
                        dfs(board, i, j);
                    }
                }
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                if(board[i][j] == 'A'){
                    board[i][j] = 'O';
                }
            }
        }
    }
};
// @lc code=end



/*
// @lcpr case=start
// [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
// @lcpr case=end

// @lcpr case=start
// [["X"]]\n
// @lcpr case=end

 */

