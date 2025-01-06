/*
 * @lc app=leetcode id=967 lang=cpp
 * @lcpr version=20004
 *
 * [967] Numbers With Same Consecutive Differences
 *
 * https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
 *
 * algorithms
 * Medium (58.43%)
 * Likes:    2835
 * Dislikes: 198
 * Total Accepted:    140.6K
 * Total Submissions: 240.6K
 * Testcase Example:  '3\n7'
 *
 * Given two integers n and k, return an array of all the integers of length n
 * where the difference between every two consecutive digits is k. You may
 * return the answer in any order.
 * 
 * Note that the integers should not have leading zeros. Integers as 02 and 043
 * are not allowed.
 * 
 * 
 * Example 1:
 * 
 * Input: n = 3, k = 7
 * Output: [181,292,707,818,929]
 * Explanation: Note that 070 is not a valid number, because it has leading
 * zeroes.
 * 
 * 
 * Example 2:
 * 
 * Input: n = 2, k = 1
 * Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= n <= 9
 * 0 <= k <= 9
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
    vector<int> res;
    vector<int> numsSameConsecDiff(int n, int k) {
        traverse(n,k,NULL,0);
        return res;
    }

    void traverse(int n, int k, int curr, int dig){
        if(dig == n){
            res.push_back(curr);
            return;
        }
        if(dig == 0){
            for(int i = 1; i <= 9; i++){
                curr = i;
                traverse(n,k,curr,dig+1);  
            }
        }
        else{
            for(int i = 0; i <= 9; i++){
                if(abs((curr % 10) - i) == k){
                    curr = curr * 10 + i; 
                    traverse(n,k,curr,dig+1);
                    curr = curr / 10;
                }
            }
        }
        return;
    }


};
// @lc code=end



/*
// @lcpr case=start
// 3\n7\n
// @lcpr case=end

// @lcpr case=start
// 2\n1\n
// @lcpr case=end

 */

