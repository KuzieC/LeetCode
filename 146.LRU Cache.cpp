/*
 * @lc app=leetcode id=146 lang=cpp
 * @lcpr version=20004
 *
 * [146] LRU Cache
 *
 * https://leetcode.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (43.98%)
 * Likes:    21305
 * Dislikes: 1102
 * Total Accepted:    1.9M
 * Total Submissions: 4.3M
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * Design a data structure that follows the constraints of a Least Recently
 * Used (LRU) cache.
 * 
 * Implement the LRUCache class:
 * 
 * 
 * LRUCache(int capacity) Initialize the LRU cache with positive size
 * capacity.
 * int get(int key) Return the value of the key if the key exists, otherwise
 * return -1.
 * void put(int key, int value) Update the value of the key if the key exists.
 * Otherwise, add the key-value pair to the cache. If the number of keys
 * exceeds the capacity from this operation, evict the least recently used
 * key.
 * 
 * 
 * The functions get and put must each run in O(1) average time complexity.
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
 * [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
 * Output
 * [null, null, null, 1, null, -1, null, -1, 3, 4]
 * 
 * Explanation
 * LRUCache lRUCache = new LRUCache(2);
 * lRUCache.put(1, 1); // cache is {1=1}
 * lRUCache.put(2, 2); // cache is {1=1, 2=2}
 * lRUCache.get(1);    // return 1
 * lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
 * lRUCache.get(2);    // returns -1 (not found)
 * lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
 * lRUCache.get(1);    // return -1 (not found)
 * lRUCache.get(3);    // return 3
 * lRUCache.get(4);    // return 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= capacity <= 3000
 * 0 <= key <= 10^4
 * 0 <= value <= 10^5
 * At most 2 * 10^5 calls will be made to get and put.
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
class Node  {
public:
    int val;
    int key;
    Node* prev;
    Node* next;
    Node(int val, int key): val(val), key(key) {
        prev = nullptr;
        next = nullptr;
    }
};
class LinkList {
public:
    Node* head;
    Node* tail;
    int cap;
    int siz;
    LinkList(int s) : cap(s), siz(0) {
        head = new Node(-1,-1);
        tail = new Node(-1,-1);
        head->next = tail;
        tail->prev = head;
    }

    Node* insert(int key,int val){
        Node* newNode = new Node(val,key);
        auto temp = tail->prev;
        temp->next = newNode;
        newNode->prev = temp;
        newNode->next = tail;
        tail->prev = newNode;
        siz++;
        return newNode;
    }

    void remove(Node* node){
        siz--;
        node->prev->next = node->next;
        node->next->prev = node->prev;
        node->next = nullptr;
        node->prev = nullptr;
        delete node;
    }

};
class LRUCache {
public:
    unordered_map<int,Node*> mp;
    int siz;
    LinkList* link;
    LRUCache(int capacity): siz(capacity) {
        link = new LinkList(capacity);

    }
    
    int get(int key) {
        if (mp.find(key) == mp.end()){
            return -1;
        }
        int val = mp[key]->val;
        link->remove(mp[key]);
        auto newNode = link->insert(key,val);
        mp[key] = newNode;
        return val;
    }
    
    void put(int key, int value) {
        if (mp.find(key) != mp.end()){
            link->remove(mp[key]);
        }
        auto newNode = link->insert(key,value);
        mp[key] = newNode;
        if (link->siz > siz){
            link->remove(link->head->next);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end



