# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        left=dummy
        count=0
        right=head
        while count<n:
            right=right.next
            count+=1
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next