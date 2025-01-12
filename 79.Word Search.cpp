/*
 * @lc app=leetcode id=79 lang=cpp
 * @lcpr version=20004
 *
 * [79] Word Search
 *
 * https://leetcode.com/problems/word-search/description/
 *
 * algorithms
 * Medium (44.25%)
 * Likes:    16324
 * Dislikes: 692
 * Total Accepted:    1.9M
 * Total Submissions: 4.3M
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * Given an m x n grid of characters board and a string word, return true if
 * word exists in the grid.
 * 
 * The word can be constructed from letters of sequentially adjacent cells,
 * where adjacent cells are horizontally or vertically neighboring. The same
 * letter cell may not be used more than once.
 * 
 * 
 * Example 1:
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCCED"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "SEE"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCB"
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == board.length
 * n = board[i].length
 * 1 <= m, n <= 6
 * 1 <= word.length <= 15
 * board and word consists of only lowercase and uppercase English letters.
 * 
 * 
 * 
 * Follow up: Could you use search pruning to make your solution faster with a
 * larger board?
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
class Solution {
public:
    bool finde = false;
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size(), col = board[0].size();
        vector<pair<int,int>> directons{{-1,0},{1,0},{0,1},{0,-1}};
        vector<vector<int>> visited(row,vector<int>(col,0));
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col;j++){
                if(board[i][j] == word[0]){
                    dfs(i,j,visited,board,0,word);
                    if(finde) return true;
                }
            }
        }
        return finde;
    }


    void dfs(int i, int j, vector<vector<int>>& visited,vector<vector<char>>& board,int ind,string word){
        if( i < 0 || i > board.size()-1 || j < 0 || j > board[0].size()-1) return;
        if(finde) return;

        if(visited[i][j] == 1) return;
        if(ind == word.size()-1 && board[i][j] == word[ind]){
            finde = true;
            return;
        }
        if(word[ind] == board[i][j]){
            visited[i][j] = 1;
            dfs(i+1,j,visited,board,ind+1,word);
            dfs(i,j+1,visited,board,ind+1,word);
            dfs(i,j-1,visited,board,ind+1,word);
            dfs(i-1,j,visited,board,ind+1,word);
            visited[i][j] = 0;
        }
        return;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
// @lcpr case=end

// @lcpr case=start
// [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
// @lcpr case=end

// @lcpr case=start
// [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
// @lcpr case=end

 */

