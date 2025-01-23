/*
 * @lc app=leetcode id=1474 lang=cpp
 * @lcpr version=20004
 *
 * [1474] Delete N Nodes After M Nodes of a Linked List
 *
 * https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/
 *
 * algorithms
 * Easy (73.44%)
 * Likes:    412
 * Dislikes: 15
 * Total Accepted:    34.7K
 * Total Submissions: 47.3K
 * Testcase Example:  '[1,2,3,4,5,6,7,8,9,10,11,12,13]\n2\n3'
 *
 * You are given the head of a linked list and two integers m and n.
 * 
 * Traverse the linked list and remove some nodes in the following way:
 * 
 * 
 * Start with the head as the current node.
 * Keep the first m nodes starting with the current node.
 * Remove the next n nodes
 * Keep repeating steps 2 and 3 until you reach the end of the list.
 * 
 * 
 * Return the head of the modified list after removing the mentioned nodes.
 * 
 * 
 * Example 1:
 * 
 * Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
 * Output: [1,2,6,7,11,12]
 * Explanation: Keep the first (m = 2) nodes starting from the head of the
 * linked List  (1 ->2) show in black nodes.
 * Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
 * Continue with the same procedure until reaching the tail of the Linked List.
 * Head of the linked list after removing nodes is returned.
 * 
 * 
 * Example 2:
 * 
 * Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
 * Output: [1,5,9]
 * Explanation: Head of linked list after removing nodes is returned.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the list is in the range [1, 10^4].
 * 1 <= Node.val <= 10^6
 * 1 <= m, n <= 1000
 * 
 * 
 * 
 * Follow up: Could you solve this problem by modifying the list in-place?
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
class Solution {
public:
    ListNode* deleteNodes(ListNode* head, int m, int n) {
        ListNode* curr = head;
        while(curr!= nullptr && curr->next != nullptr){
            for(int i = 0; i < m-1; i++){
                if(curr->next!=nullptr) curr = curr->next;
            }
            auto temp = curr;
            for(int i = 0; i < n+1; i++){
                if(curr->next != nullptr) curr = curr->next;
                else{
                    curr = nullptr;
                    break;
                }
            }
            temp->next = curr;
        }
        return head;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10,11,12,13]\n2\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10,11]\n1\n3\n
// @lcpr case=end

 */

