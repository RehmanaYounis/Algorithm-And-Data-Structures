class Node:
    def __init__(self, key=0,val=0):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
        
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity=capacity
        self.hashMap={}
        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left
        
    def insert(self, node):
        prev=self.right.prev
        prev.next= node
        node.prev=prev
        node.next=self.right
        self.right.prev=node
    
    
    
    def remove(self, node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev

        
    
        
    def get(self, key):
        res=-1
        if key in self.hashMap:
            node=self.hashMap[key]
            self.remove(node)
            self.insert(node)
            self.hashMap[key]=node
            res = self.hashMap[key].val
        return res        

    def put(self, key, value):
        if key in self.hashMap:
            node=self.hashMap[key]
            self.remove(node)
        self.hashMap[key]=Node(key,value)
        self.insert(self.hashMap[key])
        if len(self.hashMap)>self.capacity:
            LeftNode=self.left.next
            self.remove(LeftNode)
            del self.hashMap[LeftNode.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)