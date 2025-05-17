/*
 * @lc app=leetcode id=1926 lang=cpp
 * @lcpr version=30201
 *
 * [1926] Nearest Exit from Entrance in Maze
 *
 * https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/
 *
 * algorithms
 * Medium (47.45%)
 * Likes:    2476
 * Dislikes: 117
 * Total Accepted:    222.4K
 * Total Submissions: 468.6K
 * Testcase Example:  '[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]\n[1,2]'
 *
 * You are given an m x n matrix maze (0-indexed) with empty cells (represented
 * as '.') and walls (represented as '+'). You are also given the entrance of
 * the maze, where entrance = [entrancerow, entrancecol] denotes the row and
 * column of the cell you are initially standing at.
 * 
 * In one step, you can move one cell up, down, left, or right. You cannot step
 * into a cell with a wall, and you cannot step outside the maze. Your goal is
 * to find the nearest exit from the entrance. An exit is defined as an empty
 * cell that is at the border of the maze. The entrance does not count as an
 * exit.
 * 
 * Return the number of steps in the shortest path from the entrance to the
 * nearest exit, or -1 if no such path exists.
 * 
 * 
 * Example 1:
 * 
 * Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
 * entrance = [1,2]
 * Output: 1
 * Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
 * Initially, you are at the entrance cell [1,2].
 * - You can reach [1,0] by moving 2 steps left.
 * - You can reach [0,2] by moving 1 step up.
 * It is impossible to reach [2,3] from the entrance.
 * Thus, the nearest exit is [0,2], which is 1 step away.
 * 
 * 
 * Example 2:
 * 
 * Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
 * Output: 2
 * Explanation: There is 1 exit in this maze at [1,2].
 * [1,0] does not count as an exit since it is the entrance cell.
 * Initially, you are at the entrance cell [1,0].
 * - You can reach [1,2] by moving 2 steps right.
 * Thus, the nearest exit is [1,2], which is 2 steps away.
 * 
 * 
 * Example 3:
 * 
 * Input: maze = [[".","+"]], entrance = [0,0]
 * Output: -1
 * Explanation: There are no exits in this maze.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * maze.length == m
 * maze[i].length == n
 * 1 <= m, n <= 100
 * maze[i][j] is either '.' or '+'.
 * entrance.length == 2
 * 0 <= entrancerow < m
 * 0 <= entrancecol < n
 * entrance will always be an empty cell.
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
    array<array<int,2>,4> dirs = {{{1,0},{-1,0},{0,1},{0,-1}}};
    bool isExit(vector<vector<char>>& maze, int row, int col){
        if(row >= 0 && row < maze.size() && col >= 0 && col < maze[0].size()){
            if(maze[row][col] == '.') return (row == 0 || row == maze.size()-1 || col == 0 || col == maze[0].size()-1);
        }
        return false;
    }

    bool isValid(vector<vector<char>>& maze, int row, int col){
        if(row >= 0 && row < maze.size() && col >= 0 && col < maze[0].size()){
            return true;
        }
        return false;
    }
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        deque<pair<int,int>> dq;
        int res = 0;
        dq.push_back({entrance[0],entrance[1]});
        maze[entrance[0]][entrance[1]] = '+';
        while(!dq.empty()){
            int siz = dq.size();
            for(int i = 0; i < siz; ++i){
                auto curr = dq.front(); dq.pop_front();
                for(auto dir: dirs){
                    if(isValid(maze,curr.first + dir[0],curr.second+dir[1]) && maze[curr.first + dir[0]][curr.second+dir[1]] == '.'){
                        if(isExit(maze,curr.first + dir[0],curr.second+dir[1])) return res+1;
                        dq.push_back({curr.first + dir[0],curr.second+dir[1]});
                        maze[curr.first + dir[0]][curr.second+dir[1]] = '+';
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
// [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]\n[1,2]\n
// @lcpr case=end

// @lcpr case=start
// [["+","+","+"],[".",".","."],["+","+","+"]]\n[1,0]\n
// @lcpr case=end

// @lcpr case=start
// [[".","+"]]\n[0,0]\n
// @lcpr case=end

 */

