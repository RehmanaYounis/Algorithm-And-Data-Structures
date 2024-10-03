# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        list1, list2= headA, headB
        while list1 != list2:
            if not list1:
                list1=headB
            else:
                list1=list1.next
            if not list2:
                list2=headA
            else:
                list2=list2.next
        return list1
        
        