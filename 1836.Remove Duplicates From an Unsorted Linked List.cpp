/*
 * @lc app=leetcode id=1836 lang=cpp
 * @lcpr version=20004
 *
 * [1836] Remove Duplicates From an Unsorted Linked List
 *
 * https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/
 *
 * algorithms
 * Medium (75.06%)
 * Likes:    400
 * Dislikes: 12
 * Total Accepted:    37K
 * Total Submissions: 49.3K
 * Testcase Example:  '[1,2,3,2]'
 *
 * Given the head of a linked list, find all the values that appear more than
 * once in the list and delete the nodes that have any of those values.
 * 
 * Return the linked list after the deletions.
 * 
 * 
 * Example 1:
 * 
 * Input: head = [1,2,3,2]
 * Output: [1,3]
 * Explanation: 2 appears twice in the linked list, so all 2's should be
 * deleted. After deleting all 2's, we are left with [1,3].
 * 
 * 
 * Example 2:
 * 
 * Input: head = [2,1,1,2]
 * Output: []
 * Explanation: 2 and 1 both appear twice. All the elements should be
 * deleted.
 * 
 * 
 * Example 3:
 * 
 * Input: head = [3,2,2,1,3,2,4]
 * Output: [1,4]
 * Explanation: 3 appears twice and 2 appears three times. After deleting all
 * 3's and 2's, we are left with [1,4].
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the list is in the range [1, 10^5]
 * 1 <= Node.val <= 10^5
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
    ListNode* deleteDuplicatesUnsorted(ListNode* head) {
        unordered_map<int,int> s;
        auto temp = head;
        while(temp!= nullptr){
            s[temp->val]++;
            temp = temp->next;
        }
        ListNode* d = new ListNode();
        auto dummy = d;
        while(head != nullptr){
            if(s[head->val] == 1){
                dummy->next = head;
                dummy = dummy->next;
            }
            head = head->next;
        }
        dummy->next = nullptr;
        return d->next;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,2]\n
// @lcpr case=end

// @lcpr case=start
// [2,1,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,2,2,1,3,2,4]\n
// @lcpr case=end

 */

