# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hmap={}
        cur=head
        while cur:
            if cur in hmap: return True
            hmap[cur]='visited'
            cur=cur.next
        return False
            