# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists)==0:
            return 
        elif len(lists)==1:
            return lists[0]
        
        while len(lists)>1:
            res=[]
            for k in range(0, len(lists), 2):
                h1=lists[k]
                h2=lists[k+1] if (k+1) < len(lists) else None
                res.append(self.Merge(h1,h2))
            lists=res

        return lists[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def Merge(self, head1, head2 ):
            l1 = head1
            l2= head2
            dummy=ListNode(0)
            temp = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    dummy.next=l1
                    l1=l1.next
                else:
                    dummy.next=l2
                    l2=l2.next
                dummy=dummy.next
            
            if l1:
                dummy.next=l1
            if l2:
                dummy.next=l2
            return temp.next
        
        