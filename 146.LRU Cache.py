#
# @lc app=leetcode id=146 lang=python3
# @lcpr version=20004
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.09%)
# Likes:    21383
# Dislikes: 1106
# Total Accepted:    1.9M
# Total Submissions: 4.4M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# 
# Example 1:
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
      if self.cache.get(key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        return node.value
      return -1        

    def put(self, key: int, value: int) -> None:
      if self.cache.get(key):
        self.cache[key].value = value
        self.get(key)
      else:
        if len(self.cache) == self.capacity:
          node = self.head.next
          self.head.next = node.next
          node.next.prev = self.head
          del self.cache[node.key]
          del node
        node = Node(key,value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



