"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        listMap={None:None}
        cur=head
        while cur:
            listMap[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            listMap[cur].next=listMap[cur.next]
            listMap[cur].random=listMap[cur.random]
            cur=cur.next
        return listMap[head]
        