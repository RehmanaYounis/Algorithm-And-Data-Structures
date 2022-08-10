# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hmap={}
#         cur=head
#         while cur:
#             if cur in hmap: return True
#             hmap[cur]='visited'
#             cur=cur.next
#         return False
            