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
// @lcpr-template-end
// @lc code=start
// class LFUCache {
// public:
//     int cap, minifre;
//     unordered_map<int,int> keyval;
//     unordered_map<int,int> keyfre;
//     unordered_map<int,list<int>> freqkey;
//     unordered_map<int,list<int>::iterator>keyIte;
//     LFUCache(int capacity) {
//         cap = capacity;
//         minifre = 1;
//     }
    
//     int get(int key) {
//         if(keyval.find(key) == keyval.end()){
//             return -1;
//         }
//         int tempfreq = keyfre[key];
//         int tempval = keyval[key];
//         freqkey[tempfreq].erase(keyIte[key]);
//         freqkey[tempfreq+1].push_back(key);
//         keyIte[key] = prev(freqkey[tempfreq+1].end());
//         if(freqkey[tempfreq].empty()){
//             freqkey.erase(tempfreq);
//             if(minifre == tempfreq){
//                 minifre++;
//             }
//         }
//         keyfre[key] = tempfreq+1;
//         //cout<<"now the oldest is "<<*(freqkey[minifre].begin())<<endl;

//         return tempval;
//     }
//     void removelfu(){
//         int key = *(freqkey[minifre].begin());
//         //cout<<"removing "<<key<<endl;;
//         freqkey[minifre].erase(freqkey[minifre].begin());
//         if(freqkey[minifre].empty()){
//             freqkey.erase(minifre);
//         }
//         keyIte.erase(key);
//         keyval.erase(key);
//         keyfre.erase(key);
//     }
//     void put(int key, int value) {

//         if(keyval.find(key) == keyval.end()){
//             //cout<<"putting "<<key<<" new"<<endl;
//             if(keyval.size() == cap){
//                 //cout<<"reaching"<<endl;
//                 removelfu();
//             }
//             keyval[key] = value;
//             keyfre[key] = 1;
//             minifre = 1;
//             freqkey[1].push_back(key);
//             keyIte[key]=prev(freqkey[1].end());
//             return;
//         }
//         //cout<<"putting "<<key<<" old"<<endl;
//         keyval[key] = value;
//         int tempfreq = keyfre[key];
//         keyfre[key] = tempfreq+1;
//         freqkey[tempfreq].erase(keyIte[key]);
//         freqkey[tempfreq+1].push_back(key);
//         keyIte[key] = prev(freqkey[tempfreq+1].end());
//         if(freqkey[tempfreq].empty()){
//             freqkey.erase(tempfreq);
//             if(minifre == tempfreq) minifre++;
//         }
//     }
// };

template<typename Key, typename Value>
class Node {
private:
    Key key;
    Value val;
    int freq;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;
public:
    Node(Key k, Value v) : key(k), val(v), freq(1), next(nullptr) {}
    Key getKey() { return key; }
    Value getVal() { return val; }
    int getFreq() { return freq; }
    void setFreq(int f) { freq = f; }
    void setVal(Value v) { val = v; }
    std::shared_ptr<Node> getNext() { return next; }
    void setNext(std::shared_ptr<Node> n) { next = n; }
    std::weak_ptr<Node> getPrev() { return prev; }
    void setPrev(std::weak_ptr<Node> p) { prev = p; }
};
template<typename Key, typename Value>
class LinkList {
public:
    LinkList() {
        head = std::make_shared<Node<Key, Value>>(-1, -1);
        tail = std::make_shared<Node<Key, Value>>(-1, -1);
        head->setNext(tail);
        tail->setPrev(head);
    }

    void insertToEnd(int key, int val) {
        auto newNode = std::make_shared<Node<Key, Value>>(key, val);
        auto lastNode = tail->getPrev().lock();
        lastNode->setNext(newNode);
        newNode->setPrev(lastNode);
        newNode->setNext(tail);
        tail->setPrev(newNode);
    }

    void insertToEnd(const std::shared_ptr<Node<Key, Value>>& node) {
        auto lastNode = tail->getPrev().lock();
        lastNode->setNext(node);
        node->setPrev(lastNode);
        node->setNext(tail);
        tail->setPrev(node);
    }

    void remove(std::shared_ptr<Node<Key, Value>> node) {
        auto prevNode = node->getPrev().lock();
        auto nextNode = node->getNext();
        prevNode->setNext(nextNode);
        nextNode->setPrev(node->getPrev());
        node->setNext(nullptr);
    }

    void removeHead() {
        auto firstNode = head->getNext();
        head->setNext(firstNode->getNext());
        firstNode->getNext()->setPrev(head);
        firstNode->setNext(nullptr);
    }

    bool isEmpty() {
        return head->getNext() == tail;
    }
private:
    std::shared_ptr<Node<Key, Value>> head;
    std::shared_ptr<Node<Key, Value>> tail;

};
template<typename Key, typename Value>
class LFUCache {
public:
    LFUCache(int capacity) : size(0), minFreq(0), cap(capacity) {
        freqList[minFreq] = std::make_unique<LinkList<Key, Value>>();
    }

    void put(Key key, Value value) {
        if(cap <= 0) return;
        if(mp.find(key) != mp.end()) {
            removeNode(mp[key]);
        }
        if(size == cap) {
            removeLFU();
            size--;
        }
        auto newNode = std::make_shared<Node<Key, Value>>(key, value);
        mp[key] = newNode;
        insertNewNode(newNode);
        size++;
        minFreq = 1;
    }

    Value get(Key key) {
        if(mp.find(key) == mp.end()) return Value();
        auto node = mp[key];
        removeNode(node);
        node->setFreq(node->getFreq() + 1);
        insertNewNode(node);
        return node->getVal();
    }

private:
    int size;
    int minFreq;
    int cap;
    std::unordered_map<Key, std::shared_ptr<Node<Key, Value>>> mp;
    std::unordered_map<int, std::unique_ptr<LinkList<Key, Value>>> freqList;

    void removeLFU() {
        auto node = freqList[minFreq]->getHead();
        mp.erase(node->getKey());
        freqList[minFreq]->removeHead();
        if(freqList[minFreq]->isEmpty()) {
            freqList.erase(minFreq);
            minFreq++;
        }
    }

    void removeNode(std::shared_ptr<Node<Key, Value>> node) {
        auto freq = node->getFreq();
        freqList[freq]->remove(node);
        mp.erase(node->getKey());
        if(freqList[freq]->isEmpty()) {
            freqList.erase(freq);
            if(minFreq == freq) minFreq++;
        }
    }

    void insertNewNode(std::shared_ptr<Node<Key, Value>> node) {
        if(freqList.find(node->getFreq()) == freqList.end()) {
            freqList[node->getFreq()] = std::make_unique<LinkList<Key, Value>>();
        }
        freqList[node->getFreq()]->insertToEnd(node);
    }

    
};
/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end



