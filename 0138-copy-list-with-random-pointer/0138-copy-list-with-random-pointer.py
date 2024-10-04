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
        oldToNew ={None:None}
        dummy=head
        while dummy:
            oldToNew[dummy]=Node(dummy.val)
            dummy=dummy.next
        dummy=head
        while dummy:
            oldToNew[dummy].next=oldToNew[dummy.next]
            oldToNew[dummy].random=oldToNew[dummy.random]
            dummy=dummy.next
        return oldToNew[head]