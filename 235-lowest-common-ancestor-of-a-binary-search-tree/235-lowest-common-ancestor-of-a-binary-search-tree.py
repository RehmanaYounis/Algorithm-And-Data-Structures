# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:return
        def LCA (root, p,q):
            if not root: return
            if (root.val == p.val or root.val== q.val) or (root.val>p.val and root.val<q.val):
                return root
            elif root.val<p.val and root.val<q.val:
                return LCA(root.right, p,q)
            elif root.val>p.val and root.val>q.val:
                return LCA(root.left, p,q)
            else:
                return root
        return LCA(root, p,q)


            
    
    
    
    
    
#     cur = root
#         while cur:
#             if p.val < cur.val and q.val < cur.val:
#                 cur=cur.left
#             elif p.val > cur.val and q.val > cur.val:
#                 cur=cur.right
#             else:
#                 return cur
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cur = root
#         while cur:
#             if p.val < cur.val and q.val < cur.val:
#                 cur=cur.left
#             elif p.val> cur.val and q.val >cur.val:
#                 cur=cur.right
#             else:
#                 return cur