/*
 * @lc app=leetcode id=200 lang=cpp
 * @lcpr version=20004
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (61.09%)
 * Likes:    23331
 * Dislikes: 545
 * Total Accepted:    3.1M
 * Total Submissions: 5.1M
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
 vector<vector<char>> grid;

    int dfs(int row,int col){
        if(row < 0 || row >= this->grid.size() || col < 0 || col >= this->grid[0].size() || this->grid[row][col] == '0'){
            return 0;
        }
        //cout<<row<<"@"<<col<<endl;
        this->grid[row][col] = '0';
        dfs(row+1,col); 
        dfs(row-1,col);
        dfs(row,col+1);
        dfs(row,col-1);
        return 1;
    }
    int numIslands(vector<vector<char>>& grid) {
        int col = grid[0].size();
        int row = grid.size();
        UF uni(row*col);
        for(int i = 0; i < row; i ++){
            for(int j = 0; j < col; j++){
                if(grid[i][j] == '1'){
                    if(i+1 < row && grid[i+1][j] == '1'){
                        uni.connect(i*col+j,(i+1)*col+j);
                    }
                    if(j + 1 < col && grid[i][j+1] == '1'){
                        uni.connect(i*col+j,i*col+j+1);
                    }
                }
                else{
                    uni.count--;
                }
            }
        }
        return uni.get();

    }
};
// @lc code=end



/*
// @lcpr case=start
// [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
// @lcpr case=end

// @lcpr case=start
// [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
// @lcpr case=end

 */

