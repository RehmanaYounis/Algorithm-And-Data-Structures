# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1 and not head.next: return None
        cur=head
        dummy=ListNode(0, head)
        left=dummy
        while n:
            cur=cur.next
            n-=1
        while cur:
            left=left.next
            cur=cur.next
        left.next=left.next.next
        return dummy.next
            