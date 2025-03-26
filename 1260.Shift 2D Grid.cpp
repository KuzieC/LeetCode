/*
 * @lc app=leetcode id=1260 lang=cpp
 * @lcpr version=30104
 *
 * [1260] Shift 2D Grid
 *
 * https://leetcode.com/problems/shift-2d-grid/description/
 *
 * algorithms
 * Easy (67.58%)
 * Likes:    1755
 * Dislikes: 344
 * Total Accepted:    114.5K
 * Total Submissions: 169.5K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
 *
 * Given a 2D grid of size m x n and an integer k. You need to shift the grid k
 * times.
 * 
 * In one shift operation:
 * 
 * 
 * Element at grid[i][j] moves to grid[i][j + 1].
 * Element at grid[i][n - 1] moves to grid[i + 1][0].
 * Element at grid[m - 1][n - 1] moves to grid[0][0].
 * 
 * 
 * Return the 2D grid after applying shift operation k times.
 * 
 * 
 * Example 1:
 * 
 * Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
 * Output: [[9,1,2],[3,4,5],[6,7,8]]
 * 
 * 
 * Example 2:
 * 
 * Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
 * Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
 * 
 * 
 * Example 3:
 * 
 * Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
 * Output: [[1,2,3],[4,5,6],[7,8,9]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m <= 50
 * 1 <= n <= 50
 * -1000 <= grid[i][j] <= 1000
 * 0 <= k <= 100
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    int x;
    int y;
    vector<vector<int>> serialize(vector<int>& input){
        vector<vector<int>> res(x,vector<int>(y,0));
        for(int i = 0; i < x; i++){
            for(int j = 0; j < y; j++){
                res[i][j] = input[i * y + j];
            }
        }
        return res;
    }
    vector<int> deserialize(vector<vector<int>>& input){
        vector<int> res(this->x*this->y,0);
        for(int i = 0; i < this->x; i++){
            for(int j = 0; j < this->y; j++){
                res[i * y + j] = input[i][j];
            }
        }
        return res;
    }
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        this->x = grid.size();
        this->y = grid[0].size();
        auto temp = deserialize(grid);

        k = k % temp.size();
        reverse(temp.begin(),temp.end());
        reverse(temp.begin(),temp.begin() + k);
        reverse(temp.begin() + k,temp.end());

        return serialize(temp);
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n1\n
// @lcpr case=end

// @lcpr case=start
// [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]\n4\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n9\n
// @lcpr case=end

 */

