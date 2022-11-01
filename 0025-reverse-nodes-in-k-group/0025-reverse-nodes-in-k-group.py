# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy=ListNode(0, head)
        grpPrev=dummy
        while True:
            kth=self.getKthElements(grpPrev, k)
            if not kth:
                break 
            grpNxt=kth.next
            cur=grpPrev.next
            prev=grpNxt
            while cur != grpNxt:
                
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            temp=grpPrev.next
            grpPrev.next=kth
            grpPrev=temp
        return dummy.next
    def getKthElements(self, grpPrev, k):
        cur=grpPrev
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur