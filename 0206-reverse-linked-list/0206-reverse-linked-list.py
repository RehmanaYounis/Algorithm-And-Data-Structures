# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        prev=None
        while head:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cur=head
#         prev=None
#         while cur:
#             temp=cur.next
#             cur.next=prev
#             prev=cur
#             cur=temp
#         return prev