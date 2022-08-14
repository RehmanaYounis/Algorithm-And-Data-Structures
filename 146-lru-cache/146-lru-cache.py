class Node:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key = key
        self.val=val
        self.next = nxt
        self.prev=prev
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left
        self.cache={}
    def get(self, key: int) -> int:
        res=-1
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add(node)
            res=node.val
        return res
        

    def put(self, key: int, value: int) -> None:
        node=Node(key,value)
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(node)
            self.cache[key]=node
            return
        
        if len(self.cache)==self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
            
        self.add(node)
        self.cache[key]=node     
  

      
#         if len(self.cache) == self.capacity:
#             toDel=self.left.next
#             self.remove(toDel)
#             del self.cache[toDel.key]
#         self.add(node)
#         self.cache[key]=node
        


    def add(self, node):
        prev = self.right.prev
        nxt=self.right
        prev.next=node
        nxt.prev = node
        node.next=nxt
        node.prev=prev
        
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)