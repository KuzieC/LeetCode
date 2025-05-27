/*
 * @lc app=leetcode id=365 lang=cpp
 * @lcpr version=30201
 *
 * [365] Water and Jug Problem
 *
 * https://leetcode.com/problems/water-and-jug-problem/description/
 *
 * algorithms
 * Medium (42.96%)
 * Likes:    1588
 * Dislikes: 1499
 * Total Accepted:    123.6K
 * Total Submissions: 287.6K
 * Testcase Example:  '3\n5\n4'
 *
 * You are given two jugs with capacities x liters and y liters. You have an
 * infinite water supply. Return whether the total amount of water in both jugs
 * may reach target using the following operations:
 * 
 * 
 * Fill either jug completely with water.
 * Completely empty either jug.
 * Pour water from one jug into another until the receiving jug is full, or the
 * transferring jug is empty.
 * 
 * 
 * 
 * Example 1: 
 * 
 * 
 * Input:   x = 3, y = 5, target = 4 
 * 
 * Output:   true 
 * 
 * Explanation:
 * 
 * Follow these steps to reach a total of 4 liters:
 * 
 * 
 * Fill the 5-liter jug (0, 5).
 * Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2).
 * Empty the 3-liter jug (0, 2).
 * Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0).
 * Fill the 5-liter jug again (2, 5).
 * Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is
 * full. This leaves 4 liters in the 5-liter jug (3, 4).
 * Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0,
 * 4).
 * 
 * 
 * Reference: The Die Hard example.
 * 
 * 
 * Example 2: 
 * 
 * 
 * Input:   x = 2, y = 6, target = 5 
 * 
 * Output:   false 
 * 
 * 
 * Example 3: 
 * 
 * 
 * Input:   x = 1, y = 2, target = 3 
 * 
 * Output:   true 
 * 
 * Explanation: Fill both jugs. The total amount of water in both jugs is equal
 * to 3 now.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= x, y, target <= 10^3
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
    bool canMeasureWater(int x, int y, int target) {
        int currx = 0, curry = 0;
        queue<pair<int,int>> q;
        q.push({currx,curry});
        unordered_set<int> visited;
        visited.insert(currx*10000+curry);

        while(!q.empty()){
            auto[a,b] = q.front();q.pop();
            if(a + b == target) return true;
            vector<pair<int,int>> steps;
            steps.push_back({x,b});
            steps.push_back({a,y});
            steps.push_back({0,b});
            steps.push_back({a,0});
            steps.push_back({a - min(a,y-b), b + min(a,y-b)});
            steps.push_back({a + min(b,x-a), b - min(b,x-a)});

            for(const auto& [a,b] : steps){
                if(visited.find(a*10000+b) != visited.end()) continue;
                q.push({a,b});
                visited.insert(a*10000+b);
            }
        }
        return false;


    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// 3\n5\n4\n
// @lcpr case=end

// @lcpr case=start
// 2\n6\n5\n
// @lcpr case=end

// @lcpr case=start
// 1\n2\n3\n
// @lcpr case=end

 */

