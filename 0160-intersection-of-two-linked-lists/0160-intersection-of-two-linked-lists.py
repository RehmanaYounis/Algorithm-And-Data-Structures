# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1, list2 = headA, headB
        while list1 != list2:
            if not list1:
                list1=headB
            if not list2:
                list2=headA
            if list1 == list2:
                return list1
            list1=list1.next
            list2=list2.next
        return list1