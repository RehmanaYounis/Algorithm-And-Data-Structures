# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        slow=dummy
        fast=head
        
        while n>0:
            fast=fast.next
            n-=1
        
        while fast:
            fast=fast.next
            slow=slow.next
            
        slow.next=slow.next.next 
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy=ListNode(0, head)
#         slow=dummy
#         fast=head
#         k=n
#         while k>0:
#             fast=fast.next
#             k-=1
#         while fast:
#             slow=slow.next
#             fast=fast.next
#         slow.next=slow.next.next
#         return dummy.next