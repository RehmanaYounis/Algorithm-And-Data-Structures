# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        ptr=dummy
        carry=0
        cursum=0
        while l1 or l2 or carry:
            d1=l1.val if l1 else 0
            d2=l2.val if l2 else 0
            cursum=carry+d1+d2
            carry=cursum//10
            cursum=cursum%10
            print(carry, cursum)
            if l1 : l1=l1.next 
            if l2: l2=l2.next 
            node=ListNode(cursum)
            ptr.next=node
            ptr=ptr.next
        return dummy.next