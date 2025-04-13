/*
 * @lc app=leetcode id=460 lang=cpp
 * @lcpr version=20004
 *
 * [460] LFU Cache
 *
 * https://leetcode.com/problems/lfu-cache/description/
 *
 * algorithms
 * Hard (45.48%)
 * Likes:    5835
 * Dislikes: 337
 * Total Accepted:    281K
 * Total Submissions: 617.9K
 * Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
 *
 * Design and implement a data structure for a Least Frequently Used (LFU)
 * cache.
 * 
 * Implement the LFUCache class:
 * 
 * 
 * LFUCache(int capacity) Initializes the object with the capacity of the data
 * structure.
 * int get(int key) Gets the value of the key if the key exists in the cache.
 * Otherwise, returns -1.
 * void put(int key, int value) Update the value of the key if present, or
 * inserts the key if not already present. When the cache reaches its capacity,
 * it should invalidate and remove the least frequently used key before
 * inserting a new item. For this problem, when there is a tie (i.e., two or
 * more keys with the same frequency), the least recently used key would be
 * invalidated.
 * 
 * 
 * To determine the least frequently used key, a use counter is maintained for
 * each key in the cache. The key with the smallest use counter is the least
 * frequently used key.
 * 
 * When a key is first inserted into the cache, its use counter is set to 1
 * (due to the put operation). The use counter for a key in the cache is
 * incremented either a get or put operation is called on it.
 * 
 * The functions get and put must each run in O(1) average time complexity.
 * 
 * 
 * Example 1:
 * 
 * Input
 * ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
 * "get"]
 * [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
 * Output
 * [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
 * 
 * Explanation
 * // cnt(x) = the use counter for key x
 * // cache=[] will show the last used order for tiebreakers (leftmost element
 * is  most recent)
 * LFUCache lfu = new LFUCache(2);
 * lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
 * lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
 * lfu.get(1);      // return 1
 * ⁠                // cache=[1,2], cnt(2)=1, cnt(1)=2
 * lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest,
 * invalidate 2.
 * // cache=[3,1], cnt(3)=1, cnt(1)=2
 * lfu.get(2);      // return -1 (not found)
 * lfu.get(3);      // return 3
 * ⁠                // cache=[3,1], cnt(3)=2, cnt(1)=2
 * lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate
 * 1.
 * ⁠                // cache=[4,3], cnt(4)=1, cnt(3)=2
 * lfu.get(1);      // return -1 (not found)
 * lfu.get(3);      // return 3
 * ⁠                // cache=[3,4], cnt(4)=1, cnt(3)=3
 * lfu.get(4);      // return 4
 * ⁠                // cache=[4,3], cnt(4)=2, cnt(3)=3
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= capacity <= 10^4
 * 0 <= key <= 10^5
 * 0 <= value <= 10^9
 * At most 2 * 10^5 calls will be made to get and put.
 * 
 * 
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
#include <memory>
// @lcpr-template-end
// @lc code=start
class Node {
public:
    int key;
    int val;
    int freq;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;

    Node(int k, int v) : key(k), val(v), freq(1), next(nullptr) {}
};

class LinkList {
public:
    LinkList() {
        head = std::make_shared<Node>(-1, -1);
        tail = std::make_shared<Node>(-1, -1);
        head->next = tail;
        tail->prev = head;
    }

    void insertToEnd(int key, int val) {
        auto newNode = std::make_shared<Node>(key, val);
        auto lastNode = tail->prev.lock();
        lastNode->next = newNode;
        newNode->prev = lastNode;
        newNode->next = tail;
        tail->prev = newNode;
    }

    void insertToEnd(const std::shared_ptr<Node>& node) {
        auto lastNode = tail->prev.lock();
        lastNode->next = node;
        node->prev = lastNode;
        node->next = tail;
        tail->prev = node;
    }

    void remove(std::shared_ptr<Node>& node) {
        auto prevNode = node->prev.lock();
        auto nextNode = node->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
        node->next = nullptr;
    }

    shared_ptr<Node> removeLFU() {
        auto firstNode = head->next;
        head->next = firstNode->next;
        firstNode->next->prev = head;
        firstNode->next = nullptr;
        return firstNode;
    }

    bool isEmpty() {
        return head->next == tail;
    }

private:
    std::shared_ptr<Node> head;
    std::shared_ptr<Node> tail;
};

class LFUCache {
public:
    LFUCache(int capacity) : size(0), minFreq(1), cap(capacity) {
        freqList[minFreq] = std::make_unique<LinkList>();
    }

    void put(int key, int value) {
        if (cap <= 0) return;
        if (mp.find(key) != mp.end()) {
            get(key);
            mp[key]->val = value;
            return;  
        }
        if (size == cap) {
            removeLFU();
            size--;
        }
        auto newNode = std::make_shared<Node>(key, value);
        insertNewNode(newNode);
        mp[key] = newNode;
        size++;
    }

    int get(int key) {
        if (mp.find(key) == mp.end()) return -1;
        auto node = mp[key];
        removeNode(node);
        node->freq++;
        insertNewNode(node);

        return node->val;
    }

private:
    int size;
    int minFreq;
    int cap;
    std::unordered_map<int, std::shared_ptr<Node>> mp;
    std::unordered_map<int, std::unique_ptr<LinkList>> freqList;

    void removeLFU() {
        auto node = freqList[minFreq]->removeLFU();
        mp.erase(node->key);
        if (freqList[minFreq]->isEmpty()) {
            minFreq++;
        }
    }

    void removeNode(std::shared_ptr<Node>& node) {
        int freq = node->freq;
        freqList[freq]->remove(node);
        if (freqList[freq]->isEmpty()) {
            if (minFreq == freq) {
                minFreq++;
            }
        }
    }

    void insertNewNode(std::shared_ptr<Node>& node) {
        if (freqList.find(node->freq) == freqList.end()) {
            freqList[node->freq] = std::make_unique<LinkList>();
        }
        freqList[node->freq]->insertToEnd(node);
        minFreq = std::min(minFreq, node->freq);
    }
};
/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

// int main() {
//     LFUCache lfu(10);

//     lfu.put(10, 13);
//     lfu.put(3, 17);
//     lfu.put(6, 11);
//     lfu.put(10, 5);
//     lfu.put(9, 10);
//     std::cout << lfu.get(13) << std::endl; // -1
//     lfu.put(2, 19);
//     std::cout << lfu.get(2) << std::endl; // 19
//     std::cout << lfu.get(3) << std::endl; // 17
//     lfu.put(5, 25);
//     std::cout << lfu.get(8) << std::endl; // -1
//     lfu.put(9, 22);
//     lfu.put(5, 5);
//     lfu.put(1, 30);
//     std::cout << lfu.get(11) << std::endl; // -1
//     lfu.put(9, 12);
//     std::cout << lfu.get(7) << std::endl; // -1
//     std::cout << lfu.get(5) << std::endl; // 5
//     std::cout << lfu.get(8) << std::endl; // -1
//     std::cout << lfu.get(9) << std::endl; // 12
//     lfu.put(4, 30);
//     lfu.put(9, 3);
//     std::cout << lfu.get(9) << std::endl; // 3
//     std::cout << lfu.get(10) << std::endl; // 5
//     std::cout << lfu.get(10) << std::endl; // 5
//     lfu.put(6, 14);
//     lfu.put(3, 1);
//     std::cout << lfu.get(3) << std::endl; // 1
//     lfu.put(10, 11);
//     std::cout << lfu.get(8) << std::endl; // -1
//     lfu.put(2, 14);
//     std::cout << lfu.get(1) << std::endl; // 30
//     std::cout << lfu.get(5) << std::endl; // 5
//     std::cout << lfu.get(4) << std::endl; // 30
//     lfu.put(11, 4);
//     lfu.put(12, 24);
//     lfu.put(5, 18);
//     std::cout << lfu.get(13) << std::endl; // -1
//     lfu.put(7, 23);
//     std::cout << lfu.get(8) << std::endl; // -1
//     std::cout << lfu.get(12) << std::endl; // 24
//     lfu.put(3, 27);
//     lfu.put(2, 12);
//     std::cout << lfu.get(5) << std::endl; // 18
//     lfu.put(2, 9);
//     lfu.put(13, 4);
//     lfu.put(8, 18);
//     lfu.put(1, 7);
//     std::cout << lfu.get(6) << std::endl; // 14
//     lfu.put(9, 29);
//     lfu.put(8, 21);
//     std::cout << lfu.get(5) << std::endl; // 18
//     lfu.put(6, 30);
//     lfu.put(1, 12);
//     std::cout << lfu.get(10) << std::endl; // 11
//     lfu.put(4, 15);
//     lfu.put(7, 22);
//     lfu.put(11, 26);
//     lfu.put(8, 17);
//     lfu.put(9, 29);
//     std::cout << lfu.get(5) << std::endl; // 18
//     lfu.put(3, 4);
//     lfu.put(11, 30);
//     std::cout << lfu.get(12) << std::endl; // -1
//     lfu.put(4, 29);
//     std::cout << lfu.get(3) << std::endl; // 4
//     std::cout << lfu.get(9) << std::endl; // 29
//     std::cout << lfu.get(6) << std::endl; // 30
//     lfu.put(3, 4);
//     std::cout << lfu.get(1) << std::endl; // 12
//     std::cout << lfu.get(10) << std::endl; // 11
//     lfu.put(3, 29);
//     lfu.put(10, 28);
//     lfu.put(1, 20);
//     lfu.put(11, 13);
//     std::cout << lfu.get(3) << std::endl; // 29
//     lfu.put(3, 12);
//     lfu.put(3, 8);
//     lfu.put(10, 9);
//     lfu.put(3, 26);
//     std::cout << lfu.get(8) << std::endl; // 17
//     std::cout << lfu.get(7) << std::endl; // -1
//     std::cout << lfu.get(5) << std::endl; // 18
//     lfu.put(13, 17);
//     lfu.put(2, 27);
//     lfu.put(11, 15);
//     std::cout << lfu.get(12) << std::endl; // -1
//     lfu.put(9, 19);
//     lfu.put(2, 15);
//     lfu.put(3, 16);
//     std::cout << lfu.get(1) << std::endl; // 20
//     lfu.put(12, 17);
//     lfu.put(9, 1);
//     lfu.put(6, 19);
//     std::cout << lfu.get(4) << std::endl; // 29
//     std::cout << lfu.get(5) << std::endl; // 18
//     std::cout << lfu.get(5) << std::endl; // 18
//     lfu.put(8, 1);
//     lfu.put(11, 7);
//     lfu.put(5, 2);
//     lfu.put(9, 28);
//     std::cout << lfu.get(1) << std::endl; // 20
//     lfu.put(2, 2);
//     lfu.put(7, 4);
//     lfu.put(4, 22);
//     lfu.put(7, 24);
//     lfu.put(9, 26);
//     lfu.put(13, 28);
//     lfu.put(11, 26);
//     return 0;
// }


