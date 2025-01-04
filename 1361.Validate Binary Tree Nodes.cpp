/*
 * @lc app=leetcode id=1361 lang=cpp
 * @lcpr version=20004
 *
 * [1361] Validate Binary Tree Nodes
 *
 * https://leetcode.com/problems/validate-binary-tree-nodes/description/
 *
 * algorithms
 * Medium (43.80%)
 * Likes:    2164
 * Dislikes: 513
 * Total Accepted:    121.4K
 * Total Submissions: 277.1K
 * Testcase Example:  '4\n[1,-1,3,-1]\n[2,-1,-1,-1]'
 *
 * You have n binary tree nodes numbered from 0 to n - 1 where node i has two
 * children leftChild[i] and rightChild[i], return true if and only if all the
 * given nodes form exactly one valid binary tree.
 * 
 * If node i has no left child then leftChild[i] will equal -1, similarly for
 * the right child.
 * 
 * Note that the nodes have no values and that we only use the node numbers in
 * this problem.
 * 
 * 
 * Example 1:
 * 
 * Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
 * Output: false
 * 
 * 
 * Example 3:
 * 
 * Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == leftChild.length == rightChild.length
 * 1 <= n <= 10^4
 * -1 <= leftChild[i], rightChild[i] <= n - 1
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
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        
    }
};
// @lc code=end



/*
// @lcpr case=start
// 4\n[1,-1,3,-1]\n[2,-1,-1,-1]\n
// @lcpr case=end

// @lcpr case=start
// 4\n[1,-1,3,-1]\n[2,3,-1,-1]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[1,0]\n[-1,-1]\n
// @lcpr case=end

 */

