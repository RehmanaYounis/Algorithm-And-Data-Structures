# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        while len(lists) > 1:
            MergedLists=[]
            for i in range(0, len(lists),2):
                h1=lists[i]
                h2 =lists[i+1] if (i+1)<len(lists) else None
                MergedLists.append(self.Merge(h1,h2))
            lists=MergedLists
        return lists[0]
        
    def Merge(self, list1, list2):
        node= dummy = ListNode()
        while list1 and list2:
            if list1.val <list2.val:
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            node=node.next
        node.next = list1 or list2
        return dummy.next