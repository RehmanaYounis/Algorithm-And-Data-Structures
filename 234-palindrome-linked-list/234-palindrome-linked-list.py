# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        cur=slow
        prev= None
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        p1=head
        p2=prev
        
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True