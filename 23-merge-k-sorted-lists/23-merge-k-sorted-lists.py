# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        # while len(lists) > 1:
        #     mergedLists = []
        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i + 1] if (i + 1) < len(lists) else None
        #         mergedLists.append(self.mergeList(l1, l2))
        #     lists = mergedLists
        # return lists[0]

class Solution(object):
    def mergeKLists(self, lists):
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergedLists=[]
            for i in range(0, len(lists), 2):
                l1=lists[i]
                l2=lists[i+1] if i+1 <len(lists) else None
                mergedLists.append(self.mergeList(l1,l2))
            lists=mergedLists
        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy=ListNode()
        cur=dummy
        while l1 and l2:
            if l1.val< l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        if l1:
            cur.next=l1
        if l2:
            cur.next=l2
        return dummy.next