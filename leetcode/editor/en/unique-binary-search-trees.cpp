/*
 * @lc app=leetcode id=96 lang=cpp
 * @lcpr version=30104
 *
 * [96] Unique Binary Search Trees
 *
 * https://leetcode.com/problems/unique-binary-search-trees/description/
 *
 * algorithms
 * Medium (62.24%)
 * Likes:    10634
 * Dislikes: 427
 * Total Accepted:    748.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '3'
 *
 * Given an integer n, return the number of structurally unique BST's (binary
 * search trees) which has exactly n nodes of unique values from 1 to n.
 * 
 * 
 * Example 1:
 * 
 * Input: n = 3
 * Output: 5
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
 * 1 <= n <= 19
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
    vector<vector<int>> memo;

    int numTrees(int n) {
        memo.resize(n+1,vector<int>(n+1,0));
        return helper(1,n);
    }

    int helper(int lo, int hi){
        if(lo >= hi) return 1;
        int res = 0;
        if(memo[lo][hi] != 0) return memo[lo][hi];
        for(int mid = lo; mid <= hi; mid++){
            int left = helper(lo,mid-1);
            int right = helper(mid+1,hi);
            res += left * right;
        }
        memo[lo][hi] = res;
        return memo[lo][hi];
    }
};
// @lc code=end

int main() {
    Solution solution;
    // your test code here
}



/*
// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

