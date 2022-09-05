# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        
        slow=head
        if not slow.next:
            return head
        fast=head.next
        
        dummy=ListNode(0)
        dummy=slow
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        temp=slow.next
        
        slow.next=None
        
        prev=None
        cur=temp
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
       
        first=dummy
        second=prev
        print(second.val)
        while first and second:
            temp1=first.next
            temp2=second.next
            first.next = second
            second.next=temp1
            first = temp1
            second=temp2
        return dummy
        
        
        