# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1=list1
        ptr2=list2
        dummy=ListNode()
        head=dummy
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                head.next=ptr1
                ptr1=ptr1.next
            else:
                head.next=ptr2
                ptr2=ptr2.next
            head=head.next
        if ptr1:
            head.next=ptr1
        elif ptr2:
            head.next=ptr2
        return dummy.next