# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        grpPrev=dummy
        while True:
            kth=self.getKth(grpPrev, k)
            if not kth:
                break
            nxtGrp=kth.next
            cur=grpPrev.next
            prev=nxtGrp
            while cur != nxtGrp:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            temp=grpPrev.next
            grpPrev.next=kth
            grpPrev=temp
        return dummy.next
    def getKth(self, cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur