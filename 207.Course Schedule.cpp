/*
 * @lc app=leetcode id=207 lang=cpp
 * @lcpr version=20004
 *
 * [207] Course Schedule
 *
 * https://leetcode.com/problems/course-schedule/description/
 *
 * algorithms
 * Medium (48.11%)
 * Likes:    16700
 * Dislikes: 770
 * Total Accepted:    1.9M
 * Total Submissions: 3.9M
 * Testcase Example:  '2\n[[1,0]]'
 *
 * There are a total of numCourses courses you have to take, labeled from 0 to
 * numCourses - 1. You are given an array prerequisites where prerequisites[i]
 * = [ai, bi] indicates that you must take course bi first if you want to take
 * course ai.
 * 
 * 
 * For example, the pair [0, 1], indicates that to take course 0 you have to
 * first take course 1.
 * 
 * 
 * Return true if you can finish all courses. Otherwise, return false.
 * 
 * 
 * Example 1:
 * 
 * Input: numCourses = 2, prerequisites = [[1,0]]
 * Output: true
 * Explanation: There are a total of 2 courses to take. 
 * To take course 1 you should have finished course 0. So it is possible.
 * 
 * 
 * Example 2:
 * 
 * Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
 * Output: false
 * Explanation: There are a total of 2 courses to take. 
 * To take course 1 you should have finished course 0, and to take course 0 you
 * should also have finished course 1. So it is impossible.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= numCourses <= 2000
 * 0 <= prerequisites.length <= 5000
 * prerequisites[i].length == 2
 * 0 <= ai, bi < numCourses
 * All the pairs prerequisites[i] are unique.
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
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> table(numCourses);
        for(auto& pre : prerequisites){
            table[pre[1]].push_back(pre[0]);
      
        }

        vector<int> memo(numCourses,0);
        vector<int> s(numCourses,0);

        for(int i = 0; i < numCourses;i++){
            if(dfs(table,memo,i,s) == false) return false;
        }
        return true;
    }

    bool dfs(vector<vector<int>>& table, vector<int>& memo, int start,vector<int>& visited){
        if(memo[start] == 1)return true;
        if(memo[start] == -1) return false;
        cout<<start<<endl;
        for(auto i : table[start]){
            if(visited[i] == 1) {
                memo[start] = -1;
                return false;
            }
            visited[i] = 1;
            if(dfs(table,memo,i,visited) == false) {
                memo[start] = -1;
                return false;
            }
            visited[i] = 0;
        }

        memo[start] = 1;
        return true;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 2\n[[1,0]]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[[1,0],[0,1]]\n
// @lcpr case=end

 */

