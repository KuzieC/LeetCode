/*
 * @lc app=leetcode id=2 lang=cpp
 * @lcpr version=20004
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (44.97%)
 * Likes:    32502
 * Dislikes: 6517
 * Total Accepted:    5.3M
 * Total Submissions: 11.8M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order, and each of their nodes
 * contains a single digit. Add the two numbers and return the sum as a linked
 * list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * 
 * Example 1:
 * 
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 * 
 * 
 * Example 2:
 * 
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 * 
 * 
 * Example 3:
 * 
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in each linked list is in the range [1, 100].
 * 0 <= Node.val <= 9
 * It is guaranteed that the list represents a number that does not have
 * leading zeros.
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
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
//  struct ListNode {
//       int val;
//       ListNode *next;
//       ListNode() : val(0), next(nullptr) {}
//       ListNode(int x) : val(x), next(nullptr) {}
//       ListNode(int x, ListNode *next) : val(x), next(next) {}
//  };
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* L1, ListNode* L2) {
        
        int carry = 0;
        int sum = 0;
        ListNode* dummy = new ListNode();
        auto curr = dummy;
        while(L1 != nullptr && L2 != nullptr){
            sum = L1->val + L2->val + carry;
            L1 = L1->next;
            L2 = L2->next;
            if(sum > 9){
                carry = 1;
                sum = sum % 10;
                
            }
            else{
                carry = 0;
            }
            curr->next = new ListNode(sum);
            curr = curr->next;
        }
        while(L1 != nullptr){
            sum = L1->val + carry;
            L1=L1->next;
            if(sum > 9){
                carry = 1;
                sum = sum % 10;
            }
            else{
                carry = 0;
            }
            curr->next = new ListNode(sum);
            curr = curr->next;
        }
        while(L2 != nullptr){
            sum = L2->val + carry;
            L2=L2->next;
            if(sum > 9){
                carry = 1;
                sum = sum % 10;
            }
            else{
                carry = 0;
            }
            curr->next = new ListNode(sum);
            curr = curr->next;
        }
        if(carry != 0){
            curr->next = new ListNode(1);
            curr = curr->next;
        }
        curr->next = nullptr;
        return dummy->next;

    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,4,3]\n[5,6,4]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n[0]\n
// @lcpr case=end

// @lcpr case=start
// [9,9,9,9,9,9,9]\n[9,9,9,9]\n
// @lcpr case=end

 */

