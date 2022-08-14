# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grpPrev=dummy
        while True:
            kth=self.getKthElements(grpPrev, k)
            if not kth:
                break
            grpNxt=kth.next
            prev = grpNxt
            cur = grpPrev.next
            while cur != grpNxt:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            tmp=grpPrev.next
            grpPrev.next=kth
            grpPrev=tmp
        return dummy.next
        
   
        
        
    def getKthElements(self, cur, k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur
        