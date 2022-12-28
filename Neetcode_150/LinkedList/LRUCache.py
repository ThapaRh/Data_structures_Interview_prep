"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

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
#Time complexity : O(1)\mathcal{O}(1)O(1) both for put and get.

#Space complexity : O(capacity)\mathcal{O}(capacity)O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.

class Node:
    def __init__(self, key, value):
        #creating a doubly linkedList Node to store kesy and values
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dict={} #this is the cache which allows get data in O(1)
        self.left=Node(0,0)#stores the leftmost pointer left.next will be least recently used 
        self.right=Node(0,0)#this one will store the right pointer
        self.right.prev=self.left
        self.left.next=self.right
        

    def remove(self,valuePointer): #erase the value from linkedlist
        previous=valuePointer.prev
        nxt=valuePointer.next
        previous.next=nxt
        nxt.prev=previous
        
    
    def insert(self,valuePointer):
        previous=self.right.prev
        previous.next=valuePointer
        self.right.prev=valuePointer
        valuePointer.next=self.right
        valuePointer.prev=previous



    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])#removes from the specified location doubly ll
            self.insert(self.dict[key])#inserts to the rightmost ll
            return self.dict[key].value
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])#remove from the linkedList
            del self.dict[key] #deletes the dictionary with that key
        newLL=Node(key,value) #create new node with that new value
        self.dict[key]=newLL #add it to the dictionary
        self.insert(newLL) #create connections in ll and put it on the right
        if len(self.dict)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.dict[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

