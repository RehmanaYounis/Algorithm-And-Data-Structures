"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap={None:None}
        cur=head
        while cur:
            val=cur.val
            copyMap[cur] = Node(val)
            cur=cur.next
        
        cur=head
        while cur:
            copyMap[cur].next= copyMap[cur.next]
            copyMap[cur].random = copyMap[cur.random]
            cur=cur.next
        return copyMap[head]
        
        