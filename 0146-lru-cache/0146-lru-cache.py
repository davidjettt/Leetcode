class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node
        
        # Left = LRU, Right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        # self.head = None
        # self.tail = None
        # self.length = 0

    # Insert at right aka tail
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev
        
        node.next = nxt
        nxt.prev = node


    # Remove from list
    def remove(self, node):
        # prev, nxt = node.prev, node.next
        # prev.next, nxt.prev = nxt, prev 

        prev_node = node.prev
        nxt_node = node.next

        prev_node.next = nxt_node
        nxt_node.prev = prev_node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''

get: takes in a key and returns the value of that key and if key doesn't exist return -1

put: takes in a key and value and we want to update that in the cache.
    if that key-value doesn't exist then add it to cache
    if number of keys exceeds capacity, remove the least recently used key

cap = 3
  3 <-> 4 -> 2

'''