class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next = None
        self.prev=None

class LRUCache(object):

    def __init__(self, capacity):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next, self.right.prev=self.right,self.left
        
    
    def get(self, key):
        res=-1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return res
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        
        
    def remove(self,node):
        # going to remove a node from the link and the cache
        prev,nxt=node.prev, node.next
        prev.next,nxt.prev=nxt,prev
    
    
    def insert(self, node):
        prev,nxt= self.right.prev,self.right
        node.prev, prev.next,node.next,nxt.prev=prev,node,nxt,node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)