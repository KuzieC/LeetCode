/*
 * @lc app=leetcode id=526 lang=cpp
 * @lcpr version=20004
 *
 * [526] Beautiful Arrangement
 *
 * https://leetcode.com/problems/beautiful-arrangement/description/
 *
 * algorithms
 * Medium (64.40%)
 * Likes:    3277
 * Dislikes: 373
 * Total Accepted:    187.7K
 * Total Submissions: 291.5K
 * Testcase Example:  '2'
 *
 * Suppose you have n integers labeled 1 through n. A permutation of those n
 * integers perm (1-indexed) is considered a beautiful arrangement if for every
 * i (1 <= i <= n), either of the following is true:
 * 
 * 
 * perm[i] is divisible by i.
 * i is divisible by perm[i].
 * 
 * 
 * Given an integer n, return the number of the beautiful arrangements that you
 * can construct.
 * 
 * 
 * Example 1:
 * 
 * Input: n = 2
 * Output: 2
 * Explanation: 
 * The first beautiful arrangement is [1,2]:
 * ⁠   - perm[1] = 1 is divisible by i = 1
 * ⁠   - perm[2] = 2 is divisible by i = 2
 * The second beautiful arrangement is [2,1]:
 * ⁠   - perm[1] = 2 is divisible by i = 1
 * ⁠   - i = 2 is divisible by perm[2] = 1
 * 
 * 
 * Example 2:
 * 
 * Input: n = 1
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 15
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
    vector<int> used;
    int res;
    int countArrangement(int n) {
        res = 0;
        used.resize(n+1,0);
        bf(n,1);
        return res;
    }

    void bf(int n, int ind){
        if(ind > n){
            res++;
            return;
        }

        for(int i = 1; i <= n; i++){
            if(used[i] == 1) continue;
            
            if(i % ind == 0 || ind % i == 0){
                used[i] = 1;
                bf(n,ind+1);
                used[i] = 0;
            }
        }
    }
};
// @lc code=end



/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

