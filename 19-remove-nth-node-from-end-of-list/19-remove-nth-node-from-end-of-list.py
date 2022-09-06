# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
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
        