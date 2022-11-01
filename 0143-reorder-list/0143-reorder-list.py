# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy=ListNode(0,head)
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        ptr2=slow.next
        slow.next=None
        prev=None
        cur=ptr2
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        ptr1=head
        ptr2 = prev
        
        # print(ptr1)
        # print(ptr2)
        while ptr1 and ptr2:
            temp1=ptr1.next
            temp2=ptr2.next
            ptr1.next=ptr2
            ptr2.next=temp1
            ptr1=temp1
            ptr2=temp2
        return dummy.next