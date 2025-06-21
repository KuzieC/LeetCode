/*
 * @lc app=leetcode id=241 lang=cpp
 * @lcpr version=30201
 *
 * [241] Different Ways to Add Parentheses
 *
 * https://leetcode.com/problems/different-ways-to-add-parentheses/description/
 *
 * algorithms
 * Medium (72.35%)
 * Likes:    6194
 * Dislikes: 385
 * Total Accepted:    348.5K
 * Total Submissions: 481.6K
 * Testcase Example:  '"2-1-1"'
 *
 * Given a string expression of numbers and operators, return all possible
 * results from computing all the different possible ways to group numbers and
 * operators. You may return the answer in any order.
 * 
 * The test cases are generated such that the output values fit in a 32-bit
 * integer and the number of different results does not exceed 10^4.
 * 
 * 
 * Example 1:
 * 
 * Input: expression = "2-1-1"
 * Output: [0,2]
 * Explanation:
 * ((2-1)-1) = 0 
 * (2-(1-1)) = 2
 * 
 * 
 * Example 2:
 * 
 * Input: expression = "2*3-4*5"
 * Output: [-34,-14,-10,-10,10]
 * Explanation:
 * (2*(3-(4*5))) = -34 
 * ((2*3)-(4*5)) = -14 
 * ((2*(3-4))*5) = -10 
 * (2*((3-4)*5)) = -10 
 * (((2*3)-4)*5) = 10
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= expression.length <= 20
 * expression consists of digits and the operator '+', '-', and '*'.
 * All the integer values in the input expression are in the range [0, 99].
 * The integer values in the input expression do not have a leading '-' or '+'
 * denoting the sign.
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
    vector<int> diffWaysToCompute(string expression) {
        unordered_set<char> s({'+','-','*'});
        vector<int> res;

        for(size_t i = 0; i < expression.size(); ++i){
            if(s.count(expression[i])){
                auto left = diffWaysToCompute(expression.substr(0,i));
                auto right = diffWaysToCompute(expression.substr(i+1));

                for(int l : left){
                    for(int r : right){
                        if(expression[i] == '+'){
                            res.push_back(l+r);
                        }
                        else if(expression[i] == '-'){
                            res.push_back(l-r);
                        }
                        else if (expression[i] == '*'){
                            res.push_back(l*r);
                        }
                    }
                }
            }
        }
        if(res.empty()){
            res.push_back(stoi(expression));
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
// "2-1-1"\n
// @lcpr case=end

// @lcpr case=start
// "2*3-4*5"\n
// @lcpr case=end

 */

