# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        count=0
        while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
        second=slow.next
        prev=None
        slow.next=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        
        first=head
        second=prev
        while second:
            temp1 = first.next
            temp2 = second.next
            # print(temp1, temp2)
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
        