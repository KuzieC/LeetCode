/*
 * @lc app=leetcode id=1700 lang=cpp
 * @lcpr version=30200
 *
 * [1700] Number of Students Unable to Eat Lunch
 *
 * https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
 *
 * algorithms
 * Easy (78.62%)
 * Likes:    2520
 * Dislikes: 268
 * Total Accepted:    296.2K
 * Total Submissions: 376.8K
 * Testcase Example:  '[1,1,0,0]\n[0,1,0,1]'
 *
 * The school cafeteria offers circular and square sandwiches at lunch break,
 * referred to by numbers 0 and 1 respectively. All students stand in a queue.
 * Each student either prefers square or circular sandwiches.
 * 
 * The number of sandwiches in the cafeteria is equal to the number of
 * students. The sandwiches are placed in a stack. At each step:
 * 
 * 
 * If the student at the front of the queue prefers the sandwich on the top of
 * the stack, they will take it and leave the queue.
 * Otherwise, they will leave it and go to the queue's end.
 * 
 * 
 * This continues until none of the queue students want to take the top
 * sandwich and are thus unable to eat.
 * 
 * You are given two integer arrays students and sandwiches where sandwiches[i]
 * is the type of the i^​​​​​​th sandwich in the stack (i = 0 is the top of the
 * stack) and students[j] is the preference of the j^​​​​​​th student in the
 * initial queue (j = 0 is the front of the queue). Return the number of
 * students that are unable to eat.
 * 
 * 
 * Example 1:
 * 
 * Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
 * Output: 0 
 * Explanation:
 * - Front student leaves the top sandwich and returns to the end of the line
 * making students = [1,0,0,1].
 * - Front student leaves the top sandwich and returns to the end of the line
 * making students = [0,0,1,1].
 * - Front student takes the top sandwich and leaves the line making students =
 * [0,1,1] and sandwiches = [1,0,1].
 * - Front student leaves the top sandwich and returns to the end of the line
 * making students = [1,1,0].
 * - Front student takes the top sandwich and leaves the line making students =
 * [1,0] and sandwiches = [0,1].
 * - Front student leaves the top sandwich and returns to the end of the line
 * making students = [0,1].
 * - Front student takes the top sandwich and leaves the line making students =
 * [1] and sandwiches = [1].
 * - Front student takes the top sandwich and leaves the line making students =
 * [] and sandwiches = [].
 * Hence all students are able to eat.
 * 
 * 
 * Example 2:
 * 
 * Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
 * Output: 3
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= students.length, sandwiches.length <= 100
 * students.length == sandwiches.length
 * sandwiches[i] is 0 or 1.
 * students[i] is 0 or 1.
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
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        unordered_map<int,int> mp;
        for(const auto& i : students){
            mp[i]++;
        }
        for(const auto& i : sandwiches){
            if(mp[i] > 0){
                mp[i]--;
            }
            else{
                return mp[1-i];
            }
        }
        return 0;
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// [1,1,0,0]\n[0,1,0,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,0,0,1]\n[1,0,0,0,1,1]\n
// @lcpr case=end

 */

