# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        
        # while cur:
        #     nxt = cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=nxt
        # return prev
        def listRev(cur, prev):
            if cur is None:
                return prev
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            return listRev(cur, prev)
        return listRev(cur, prev)