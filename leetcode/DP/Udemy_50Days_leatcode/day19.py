"""
   Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict() 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        self.cache.move_to_end(key) #最近使われたものとして末尾へ
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache: #すでに存在する場合、末尾へ移動
            self.cache.move_to_end(key)
        self.cache[key] = value #値を更新or追加
        
        #容量を超えたら⇒一番古いキーを削除
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)