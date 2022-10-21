# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        list1=head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        list2=slow.next
        slow.next=None
        
        prev=None
        while list2:
            nxt=list2.next
            list2.next=prev
            prev=list2
            list2=nxt
        list2=prev
        
        while list1 and list2:
            temp1=list1.next
            temp2=list2.next
            list1.next=list2
            list2.next=temp1
            list1=temp1
            list2=temp2
        return head
            