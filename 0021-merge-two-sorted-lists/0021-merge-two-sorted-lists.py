# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        node=dummy=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            node=node.next
        node.next=list1 or list2
        return dummy.next
        